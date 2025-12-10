"""
Arquivo: services.py
Caminho: apps/selecao/services.py
Alteração: Corrigido erro fototipo.upper() para fototipo.nome e ampliado status válidos
Data: 10/12/2025
"""

"""
Arquivo: services.py
Caminho: apps/selecao/services.py
Responsável por: Lógica de classificação e pontuação
Alteração: Adicionado suporte a critérios de ORDENACAO com prioridade
Data: 09/12/2025
"""

from django.db import transaction
from django.utils import timezone
from .models import Inscricao, Classificacao, InscricaoCriterioAtendido, StatusInscricao
from apps.eventos.models import Evento, EventoCriterio
from decimal import Decimal
import logging

logger = logging.getLogger(__name__)


class ClassificadorService:
    """
    Service responsável por classificar inscrições com base em critérios
    """
    
    @staticmethod
    def calcular_pontuacao_inscricao(inscricao):
        """
        Calcula pontuação total de uma inscrição baseado nos critérios atendidos
        
        Args:
            inscricao: Objeto Inscricao
            
        Returns:
            Decimal: Pontuação total
        """
        criterios_atendidos = InscricaoCriterioAtendido.objects.filter(
            inscricao=inscricao
        )
        
        total = sum(
            criterio.pontos_atribuidos 
            for criterio in criterios_atendidos
        )
        
        return Decimal(str(total))
    
    @staticmethod
    def verificar_criterios_automaticos(inscricao):
        """
        Verifica automaticamente quais critérios o interessado atende
        
        Args:
            inscricao: Objeto Inscricao
            
        Returns:
            list: Lista de criterios atendidos
        """
        interessado = inscricao.interessado
        evento = inscricao.evento
        criterios_evento = EventoCriterio.objects.filter(evento=evento, ativo=True)
        
        criterios_atendidos = []
        
        for evento_criterio in criterios_evento:
            criterio = evento_criterio.criterio
            
            if criterio.tipo_criterio == 'ORDENACAO':
                continue
            
            atende = False
            pontos = criterio.pontos or 0
            
            if criterio.codigo == 'PCD':
                if interessado.tem_deficiencia:
                    atende = True
            
            elif criterio.codigo == 'PROGRAMA_SOCIAL' or criterio.codigo == 'NIS':
                if interessado.programa_social and interessado.num_nis:
                    atende = True
            
            elif criterio.codigo.startswith('JOVEM') or criterio.codigo.startswith('IDOSO') or criterio.categoria == 'FAIXA_ETARIA':
                if interessado.data_nascimento:
                    hoje = timezone.now().date()
                    idade = hoje.year - interessado.data_nascimento.year
                    
                    if (hoje.month, hoje.day) < (interessado.data_nascimento.month, interessado.data_nascimento.day):
                        idade -= 1
                    
                    if '16' in criterio.nome and '24' in criterio.nome:
                        if 16 <= idade <= 24:
                            atende = True
                    elif '50' in criterio.nome or 'Idoso' in criterio.nome:
                        if idade >= 50:
                            atende = True
                    elif '60' in criterio.nome:
                        if idade >= 60:
                            atende = True
            
            elif criterio.categoria == 'ESCOLARIDADE':
                if interessado.escolaridade:
                    niveis_ordem = [
                        'FUNDAMENTAL_INCOMPLETO',
                        'FUNDAMENTAL_COMPLETO',
                        'MEDIO_INCOMPLETO',
                        'MEDIO_COMPLETO',
                        'SUPERIOR_INCOMPLETO',
                        'SUPERIOR_COMPLETO',
                        'POS_GRADUACAO'
                    ]
                    
                    nivel_minimo = None
                    if 'Fundamental Completo' in criterio.nome:
                        nivel_minimo = 'FUNDAMENTAL_COMPLETO'
                    elif 'Médio Completo' in criterio.nome or 'Medio Completo' in criterio.nome:
                        nivel_minimo = 'MEDIO_COMPLETO'
                    elif 'Superior' in criterio.nome:
                        nivel_minimo = 'SUPERIOR_COMPLETO'
                    
                    if nivel_minimo and interessado.escolaridade in niveis_ordem:
                        idx_interessado = niveis_ordem.index(interessado.escolaridade)
                        idx_minimo = niveis_ordem.index(nivel_minimo)
                        
                        if idx_interessado >= idx_minimo:
                            atende = True
            
            elif criterio.codigo == 'RENDA_FAMILIAR':
                atende = False
            
            elif criterio.categoria == 'COTA_RACIAL':
                if interessado.fototipo:
                    racas_cotistas = ['Preta', 'Parda', 'Indígena', 'Preto', 'Pardo', 'Indigena']
                    if interessado.fototipo.nome in racas_cotistas:
                        atende = True
            
            if atende:
                criterios_atendidos.append({
                    'criterio': criterio,
                    'pontos': pontos,
                    'validado': True
                })
        
        return criterios_atendidos
    
    @staticmethod
    @transaction.atomic
    def processar_inscricao(inscricao):
        """
        Processa uma inscrição: verifica critérios e calcula pontuação
        
        Args:
            inscricao: Objeto Inscricao
        """
        criterios_atendidos = ClassificadorService.verificar_criterios_automaticos(inscricao)
        
        for item in criterios_atendidos:
            InscricaoCriterioAtendido.objects.update_or_create(
                inscricao=inscricao,
                criterio=item['criterio'],
                defaults={
                    'pontos_atribuidos': item['pontos'],
                    'validado': item['validado']
                }
            )
        
        pontuacao_total = ClassificadorService.calcular_pontuacao_inscricao(inscricao)
        
        Classificacao.objects.update_or_create(
            inscricao=inscricao,
            defaults={
                'pontuacao_total': pontuacao_total,
                'processado_em': timezone.now()
            }
        )
        
        logger.info(f"Inscrição {inscricao.id} processada. Pontuação: {pontuacao_total}")
    
    @staticmethod
    @transaction.atomic
    def classificar_evento(evento):
        """
        Classifica todas as inscrições de um evento
        
        LÓGICA:
        - Critérios são aplicados conforme prioridade definida no evento
        - Pode ser: ORDENACAO primeiro, PONTUACAO primeiro, ou misturado
        
        Args:
            evento: Objeto Evento
        """
        status_validos = StatusInscricao.objects.filter(
            nome__in=['Aprovada', 'Pendente', 'APROVADA', 'PENDENTE', 'Confirmada', 'CONFIRMADA']
        )
        
        inscricoes = Inscricao.objects.filter(
            evento=evento,
            status__in=status_validos
        ).select_related('interessado')
        
        for inscricao in inscricoes:
            ClassificadorService.processar_inscricao(inscricao)
        
        criterios_evento = EventoCriterio.objects.filter(
            evento=evento,
            ativo=True
        ).select_related('criterio').order_by('prioridade')
        
        order_fields = []
        
        for evento_criterio in criterios_evento:
            criterio = evento_criterio.criterio
            
            if criterio.tipo_criterio == 'PONTUACAO':
                if '-pontuacao_total' not in order_fields:
                    order_fields.append('-pontuacao_total')
            
            elif criterio.tipo_criterio == 'ORDENACAO':
                codigo = criterio.codigo
                
                if codigo == 'ORDEM_INSCRICAO':
                    order_fields.append('inscricao__data_inscricao')
                
                elif codigo == 'IDADE_CRESCENTE':
                    order_fields.append('-inscricao__interessado__data_nascimento')
                
                elif codigo == 'IDADE_DECRESCENTE':
                    order_fields.append('inscricao__interessado__data_nascimento')
        
        if not order_fields:
            order_fields = ['-pontuacao_total', 'inscricao__data_inscricao']
        
        if 'inscricao__data_inscricao' not in order_fields and '-inscricao__data_inscricao' not in order_fields:
            order_fields.append('inscricao__data_inscricao')
        
        classificacoes = Classificacao.objects.filter(
            inscricao__evento=evento
        ).select_related('inscricao__interessado').order_by(*order_fields)
        
        total_vagas = evento.total_vagas
        posicao = 1
        
        for classificacao in classificacoes:
            classificacao.posicao = posicao
            classificacao.classificado = (posicao <= total_vagas)
            classificacao.lista_espera = (posicao > total_vagas)
            classificacao.atualizado_em = timezone.now()
            classificacao.save()
            
            posicao += 1
        
        logger.info(
            f"Evento {evento.nome} classificado com critérios: {order_fields}. "
            f"Total: {classificacoes.count()} inscrições"
        )
        
        return classificacoes