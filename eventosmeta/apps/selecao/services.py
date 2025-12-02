"""
Services do app SELEÇÃO
Responsável por: Lógica de classificação e pontuação
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
        # 
        # ALTERAÇÃO: Removido filtro validado=True
        # MOTIVO: Critérios automáticos devem ser computados imediatamente
        # 
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
        criterios_evento = EventoCriterio.objects.filter(evento=evento)
        
        criterios_atendidos = []
        
        for evento_criterio in criterios_evento:
            criterio = evento_criterio.criterio
            atende = False
            pontos = evento_criterio.pontos_customizados or criterio.pontos
            
            # 
            # CRITÉRIO: Pessoa com Deficiência (PCD)
            # 
            if criterio.tipo == 'PCD':
                if interessado.tem_deficiencia:
                    atende = True
            
            # 
            # CRITÉRIO: Beneficiário de Programa Social
            # LÓGICA: Verifica se participa de programa social E possui NIS
            # 
            elif criterio.tipo == 'PROGRAMA_SOCIAL':
                if interessado.programa_social and interessado.num_nis:
                    atende = True
            
            # 
            # CRITÉRIO: Faixa Etária
            # LÓGICA: Calcula idade e verifica se atende a faixa específica
            # 
            elif criterio.tipo == 'FAIXA_ETARIA':
                if interessado.data_nascimento:
                    hoje = timezone.now().date()
                    idade = hoje.year - interessado.data_nascimento.year
                    
                    # Ajusta se ainda não fez aniversário este ano
                    if (hoje.month, hoje.day) < (interessado.data_nascimento.month, interessado.data_nascimento.day):
                        idade -= 1
                    
                    # Verificar qual faixa etária é este critério
                    if '16' in criterio.nome and '24' in criterio.nome:
                        if 16 <= idade <= 24:
                            atende = True
                    elif '50' in criterio.nome:
                        if idade >= 50:
                            atende = True
            
            # 
            # CRITÉRIO: Escolaridade
            # LÓGICA: Verifica se o interessado possui o nível mínimo exigido
            # 
            elif criterio.tipo == 'ESCOLARIDADE':
                if interessado.escolaridade:
                    # Ordem hierárquica de níveis de escolaridade
                    niveis_ordem = [
                        'FUNDAMENTAL_INCOMPLETO',
                        'FUNDAMENTAL_COMPLETO',
                        'MEDIO_INCOMPLETO',
                        'MEDIO_COMPLETO',
                        'SUPERIOR_INCOMPLETO',
                        'SUPERIOR_COMPLETO',
                        'POS_GRADUACAO'
                    ]
                    
                    # Identificar qual nível mínimo o critério exige
                    nivel_minimo = None
                    if 'Fundamental Completo' in criterio.nome:
                        nivel_minimo = 'FUNDAMENTAL_COMPLETO'
                    elif 'Médio Completo' in criterio.nome or 'Medio Completo' in criterio.nome:
                        nivel_minimo = 'MEDIO_COMPLETO'
                    elif 'Superior' in criterio.nome:
                        nivel_minimo = 'SUPERIOR_COMPLETO'
                    
                    # Verificar se o interessado atende o nível mínimo
                    if nivel_minimo and interessado.escolaridade in niveis_ordem:
                        idx_interessado = niveis_ordem.index(interessado.escolaridade)
                        idx_minimo = niveis_ordem.index(nivel_minimo)
                        
                        # Atende se o nível do interessado é maior ou igual ao mínimo
                        if idx_interessado >= idx_minimo:
                            atende = True
            
            # 
            # CRITÉRIO: Renda Familiar
            # STATUS: DESABILITADO - Campo não existe no modelo Interessado
            # 
            elif criterio.tipo == 'RENDA_FAMILIAR':
                # Campo renda_familiar não implementado no modelo
                # Critério ignorado automaticamente
                atende = False
            
            # 
            # CRITÉRIO: Fototipo (Cotas Raciais)
            # LÓGICA: Pontua pretos, pardos e indígenas
            # 
            elif criterio.tipo == 'FOTOTIPO':
                if interessado.fototipo:
                    # Critérios de cotas raciais geralmente pontuam pretos, pardos e indígenas
                    if interessado.fototipo.nome in ['Preta', 'Parda', 'Indígena']:
                        atende = True
            
            # Se atende o critério, adiciona à lista
            if atende:
                criterios_atendidos.append({
                    'criterio': criterio,
                    'pontos': pontos,
                    'validado': True  # ← ALTERAÇÃO: Sempre True para critérios automáticos
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
        # 1. Verificar critérios automaticamente
        criterios_atendidos = ClassificadorService.verificar_criterios_automaticos(inscricao)
        
        # 2. Criar registros de critérios atendidos
        for item in criterios_atendidos:
            InscricaoCriterioAtendido.objects.update_or_create(
                inscricao=inscricao,
                criterio=item['criterio'],
                defaults={
                    'pontos_atribuidos': item['pontos'],
                    'validado': item['validado']
                }
            )
        
        # 3. Calcular pontuação total
        pontuacao_total = ClassificadorService.calcular_pontuacao_inscricao(inscricao)
        
        # 4. Criar ou atualizar classificação
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
        
        Args:
            evento: Objeto Evento
        """
        # 1. Buscar inscrições aprovadas/pendentes
        status_validos = StatusInscricao.objects.filter(
            nome__in=['Aprovada', 'Pendente']
        )
        
        inscricoes = Inscricao.objects.filter(
            evento=evento,
            status__in=status_validos
        ).select_related('interessado')
        
        # 2. Processar cada inscrição
        for inscricao in inscricoes:
            ClassificadorService.processar_inscricao(inscricao)
        
        # 3. Ordenar classificações
        classificacoes = Classificacao.objects.filter(
            inscricao__evento=evento
        ).select_related('inscricao__interessado').order_by(
            '-pontuacao_total',
            'inscricao__data_inscricao'  # Desempate por data
        )
        
        # 4. Atualizar posições e status (classificado/lista de espera)
        total_vagas = evento.total_vagas
        posicao = 1
        
        for classificacao in classificacoes:
            classificacao.posicao = posicao
            classificacao.classificado = (posicao <= total_vagas)
            classificacao.lista_espera = (posicao > total_vagas)
            classificacao.atualizado_em = timezone.now()
            classificacao.save()
            
            posicao += 1
        
        logger.info(f"Evento {evento.nome} classificado. Total: {classificacoes.count()} inscrições")
        
        return classificacoes
    
    