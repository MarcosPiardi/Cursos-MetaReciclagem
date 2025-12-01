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
        criterios_atendidos = InscricaoCriterioAtendido.objects.filter(
            inscricao=inscricao,
            validado=True
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
            
            # CRITÉRIO: Morador de Manaus
            if criterio.tipo == 'MORADOR_MANAUS':
                if interessado.cidade_residencia and 'manaus' in interessado.cidade_residencia.lower():
                    atende = True
            
            # CRITÉRIO: Pessoa com Deficiência (PCD)
            elif criterio.tipo == 'PCD':
                if interessado.tem_deficiencia:
                    atende = True
            
            # CRITÉRIO: Beneficiário de Programa Social
            elif criterio.tipo == 'PROGRAMA_SOCIAL':
                if interessado.programa_social:
                    atende = True
            
            # CRITÉRIO: Faixa Etária (requer validação manual)
            elif criterio.tipo == 'FAIXA_ETARIA':
                # Será validado manualmente
                atende = False
            
            # CRITÉRIO: Escolaridade (requer validação manual)
            elif criterio.tipo == 'ESCOLARIDADE':
                # Será validado manualmente
                atende = False
            
            # CRITÉRIO: Renda Familiar (requer validação manual)
            elif criterio.tipo == 'RENDA_FAMILIAR':
                # Será validado manualmente
                atende = False
            
            # Se atende o critério, adiciona à lista
            if atende:
                criterios_atendidos.append({
                    'criterio': criterio,
                    'pontos': pontos,
                    'validado': not criterio.requer_validacao_manual
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
    
    