"""
ARQUIVO: apps/cursoseoutros/services.py
AÇÃO: CRIAR arquivo completo
MUDANÇA: Serviço de classificação de candidatos com algoritmo de pontuação
DATA/HORA: 2025-10-29 15:15:00
"""

from datetime import date
from decimal import Decimal
from django.db.models import Count, Q
from django.utils import timezone
from .models import (
    Evento, Inscricao, Classificacao, InscricaoCriterioAtendido,
    EventoCriterio, TipoCriterio
)


class ClassificadorService:
    """
    Serviço responsável pela classificação de inscritos em eventos/cursos.
    
    Algoritmo:
    1. Para cada inscrição, calcula pontos em cada critério do evento
    2. Aplica peso do critério (0-10)
    3. Soma todos os pontos = score total
    4. Ordena por score (maior primeiro), desempate por data de inscrição
    5. Atribui posição (1º, 2º, 3º...)
    """
    
    @staticmethod
    def calcular_idade(data_nascimento):
        """
        Calcula idade a partir da data de nascimento.
        
        Args:
            data_nascimento (date): Data de nascimento
            
        Returns:
            int: Idade em anos completos
        """
        if not data_nascimento:
            return 0
        
        hoje = date.today()
        idade = hoje.year - data_nascimento.year
        
        # Ajusta se ainda não fez aniversário este ano
        if (hoje.month, hoje.day) < (data_nascimento.month, data_nascimento.day):
            idade -= 1
        
        return idade
    
    @staticmethod
    def calcular_pontos_ordem_inscricao(inscricao, total_inscricoes):
        """
        Calcula pontos por ordem de inscrição.
        Primeiro inscrito = 100 pontos, último = 0 pontos (escala linear).
        
        Args:
            inscricao (Inscricao): Inscrição sendo avaliada
            total_inscricoes (int): Total de inscrições no evento
            
        Returns:
            Decimal: Pontos obtidos (0-100)
        """
        if total_inscricoes <= 1:
            return Decimal('100.00')
        
        # Conta quantos foram inscritos antes
        inscricoes_anteriores = Inscricao.objects.filter(
            evento=inscricao.evento,
            data_inscricao__lt=inscricao.data_inscricao
        ).count()
        
        # Calcula pontos (100 para primeiro, 0 para último)
        pontos = Decimal('100.00') - (
            Decimal(inscricoes_anteriores) / Decimal(total_inscricoes - 1) * Decimal('100.00')
        )
        
        return round(pontos, 2)
    
    @staticmethod
    def calcular_pontos_idade_crescente(inscricao):
        """
        Calcula pontos priorizando mais jovens.
        Idade 0 = 100 pontos, Idade 100+ = 0 pontos (escala linear).
        
        Args:
            inscricao (Inscricao): Inscrição sendo avaliada
            
        Returns:
            Decimal: Pontos obtidos (0-100)
        """
        idade = ClassificadorService.calcular_idade(
            inscricao.interessado.data_nascimento
        )
        
        # Quanto menor a idade, mais pontos
        pontos = max(Decimal('0.00'), Decimal('100.00') - Decimal(idade))
        return round(pontos, 2)
    
    @staticmethod
    def calcular_pontos_idade_decrescente(inscricao):
        """
        Calcula pontos priorizando mais velhos.
        Idade 100+ = 100 pontos, Idade 0 = 0 pontos (escala linear).
        
        Args:
            inscricao (Inscricao): Inscrição sendo avaliada
            
        Returns:
            Decimal: Pontos obtidos (0-100)
        """
        idade = ClassificadorService.calcular_idade(
            inscricao.interessado.data_nascimento
        )
        
        # Quanto maior a idade, mais pontos (limitado a 100)
        pontos = min(Decimal('100.00'), Decimal(idade))
        return round(pontos, 2)
    
    @staticmethod
    def calcular_pontos_faixa_etaria(inscricao, evento_criterio):
        """
        Calcula pontos por faixa etária específica.
        Dentro da faixa = 100 pontos, fora = pontos proporcionais à distância.
        
        Args:
            inscricao (Inscricao): Inscrição sendo avaliada
            evento_criterio (EventoCriterio): Configuração do critério
            
        Returns:
            Decimal: Pontos obtidos (0-100)
        """
        idade = ClassificadorService.calcular_idade(
            inscricao.interessado.data_nascimento
        )
        
        idade_min = evento_criterio.idade_minima or 0
        idade_max = evento_criterio.idade_maxima or 999
        
        if idade_min <= idade <= idade_max:
            # Dentro da faixa prioritária
            return Decimal('100.00')
        else:
            # Fora da faixa - pontos decrescem com a distância
            distancia = min(abs(idade - idade_min), abs(idade - idade_max))
            pontos = max(Decimal('0.00'), Decimal('100.00') - (Decimal(distancia) * Decimal('5.00')))
            return round(pontos, 2)
    
    @staticmethod
    def calcular_pontos_programa_social(inscricao):
        """
        Calcula pontos por programa social (NIS).
        Tem NIS preenchido = 100 pontos, não tem = 0 pontos.
        
        Args:
            inscricao (Inscricao): Inscrição sendo avaliada
            
        Returns:
            Decimal: Pontos obtidos (0 ou 100)
        """
        interessado = inscricao.interessado
        
        if interessado.programa_social and interessado.num_nis:
            return Decimal('100.00')
        
        return Decimal('0.00')
    
    @staticmethod
    def calcular_pontos_necessidade_especial(inscricao):
        """
        Calcula pontos por necessidades especiais (PCD).
        Tem alguma necessidade = 100 pontos, não tem = 0 pontos.
        
        Args:
            inscricao (Inscricao): Inscrição sendo avaliada
            
        Returns:
            Decimal: Pontos obtidos (0 ou 100)
        """
        interessado = inscricao.interessado
        
        if interessado.necessidades_especiais:
            # Verifica se marcou alguma necessidade específica
            if any([
                interessado.fisica,
                interessado.visual,
                interessado.auditiva,
                interessado.intelectual,
                interessado.psicossocial,
                interessado.multiplas
            ]):
                return Decimal('100.00')
        
        return Decimal('0.00')
    
    @staticmethod
    def calcular_pontos_fototipo(inscricao, evento_criterio):
        """
        Calcula pontos por fototipo/cor (cotas raciais).
        Fototipo na lista prioritária = 100 pontos, outros = 0 pontos.
        
        Args:
            inscricao (Inscricao): Inscrição sendo avaliada
            evento_criterio (EventoCriterio): Configuração do critério
            
        Returns:
            Decimal: Pontos obtidos (0 ou 100)
        """
        interessado = inscricao.interessado
        
        if not interessado.fototipo:
            return Decimal('0.00')
        
        # Busca fototipos prioritários configurados
        # Nota: Este relacionamento precisa ser implementado no model EventoCriterio
        # Por enquanto, retorna 50 pontos (neutro) se não houver configuração
        
        # TODO: Implementar relacionamento ManyToMany entre EventoCriterio e Fototipo
        # fototipos_prioritarios = evento_criterio.fototipos_prioritarios.all()
        # if interessado.fototipo in fototipos_prioritarios:
        #     return Decimal('100.00')
        
        return Decimal('50.00')  # Temporário até implementar relacionamento
    
    @staticmethod
    def calcular_pontos_customizado(inscricao, criterio):
        """
        Calcula pontos para critério customizado.
        Deve ser validado manualmente pelo operador via InscricaoCriterioAtendido.
        
        Args:
            inscricao (Inscricao): Inscrição sendo avaliada
            criterio (Criterio): Critério customizado
            
        Returns:
            Decimal: Pontos obtidos (0-100 ou valor validado manualmente)
        """
        # Busca se há validação manual
        try:
            validacao = InscricaoCriterioAtendido.objects.get(
                inscricao=inscricao,
                criterio=criterio,
                validado=True
            )
            return validacao.pontos_obtidos
        except InscricaoCriterioAtendido.DoesNotExist:
            # Não validado = 0 pontos
            return Decimal('0.00')
    
    @classmethod
    def calcular_pontos_criterio(cls, inscricao, evento_criterio):
        """
        Calcula pontos para um critério específico.
        
        Args:
            inscricao (Inscricao): Inscrição sendo avaliada
            evento_criterio (EventoCriterio): Configuração do critério no evento
            
        Returns:
            Decimal: Pontos obtidos (0-100)
        """
        criterio = evento_criterio.criterio
        tipo = criterio.tipo_criterio
        
        # Calcula pontos base (0-100) conforme tipo do critério
        if tipo == TipoCriterio.ORDEM:
            total_inscricoes = inscricao.evento.inscricoes.count()
            pontos_base = cls.calcular_pontos_ordem_inscricao(inscricao, total_inscricoes)
        
        elif tipo == TipoCriterio.IDADE_CRESCENTE:
            pontos_base = cls.calcular_pontos_idade_crescente(inscricao)
        
        elif tipo == TipoCriterio.IDADE_DECRESCENTE:
            pontos_base = cls.calcular_pontos_idade_decrescente(inscricao)
        
        elif tipo == TipoCriterio.FAIXA_ETARIA:
            pontos_base = cls.calcular_pontos_faixa_etaria(inscricao, evento_criterio)
        
        elif tipo == TipoCriterio.NIS:
            pontos_base = cls.calcular_pontos_programa_social(inscricao)
        
        elif tipo == TipoCriterio.PCD:
            pontos_base = cls.calcular_pontos_necessidade_especial(inscricao)
        
        elif tipo == TipoCriterio.FOTOTIPO:
            pontos_base = cls.calcular_pontos_fototipo(inscricao, evento_criterio)
        
        elif tipo == TipoCriterio.CUSTOMIZADO:
            pontos_base = cls.calcular_pontos_customizado(inscricao, criterio)
        
        else:
            pontos_base = Decimal('0.00')
        
        return pontos_base
    
    @classmethod
    def calcular_score_inscricao(cls, inscricao):
        """
        Calcula o score total de uma inscrição baseado em todos os critérios do evento.
        
        Score = Σ (pontos_base × peso_criterio / 10)
        
        Args:
            inscricao (Inscricao): Inscrição a ser avaliada
            
        Returns:
            Decimal: Score total calculado
        """
        evento = inscricao.evento
        score_total = Decimal('0.00')
        
        # Busca critérios do evento ordenados
        evento_criterios = evento.evento_criterios.select_related('criterio').filter(
            criterio__ativo=True
        ).order_by('ordem')
        
        for evento_criterio in evento_criterios:
            # Calcula pontos base do critério (0-100)
            pontos_base = cls.calcular_pontos_criterio(inscricao, evento_criterio)
            
            # Aplica o peso do critério (0-10)
            # Exemplo: pontos_base=80, peso=8 → 80 × 8 / 10 = 64 pontos
            pontos_ponderados = (pontos_base * Decimal(evento_criterio.peso)) / Decimal('10.00')
            
            score_total += pontos_ponderados
            
            # Registra/atualiza critério atendido
            InscricaoCriterioAtendido.objects.update_or_create(
                inscricao=inscricao,
                criterio=evento_criterio.criterio,
                defaults={
                    'pontos_obtidos': pontos_ponderados,
                    # Critérios não customizados são automaticamente validados
                    'validado': evento_criterio.criterio.tipo_criterio != TipoCriterio.CUSTOMIZADO
                }
            )
        
        return round(score_total, 2)
    
    @classmethod
    def classificar_evento(cls, evento):
        """
        Classifica todas as inscrições de um evento.
        
        Processo:
        1. Calcula score de cada inscrição
        2. Ordena por score (maior primeiro)
        3. Desempate por data de inscrição (mais antigo primeiro)
        4. Atribui posição sequencial
        5. Atualiza status (APROVADO ou FILA_ESPERA)
        
        Args:
            evento (Evento): Evento a ser classificado
            
        Returns:
            QuerySet: Inscrições classificadas ordenadas
        """
        # Busca todas as inscrições do evento
        inscricoes = evento.inscricoes.select_related('interessado').all()
        
        # Calcula score de cada inscrição
        for inscricao in inscricoes:
            score = cls.calcular_score_inscricao(inscricao)
            
            # Cria ou atualiza classificação
            Classificacao.objects.update_or_create(
                inscricao=inscricao,
                defaults={
                    'score_total': score,
                    'data_classificacao': timezone.now()
                }
            )
        
        # Ordena por score (maior primeiro), desempate por data (mais antigo primeiro)
        inscricoes_classificadas = inscricoes.order_by(
            '-classificacao__score_total',
            'data_inscricao'
        )
        
        # Atribui posição e atualiza status
        for posicao, inscricao in enumerate(inscricoes_classificadas, start=1):
            classificacao = inscricao.classificacao
            classificacao.posicao = posicao
            classificacao.save()
            
            # Atualiza status da inscrição
            if posicao <= evento.vagas:
                inscricao.status = 'APROVADO'
            else:
                inscricao.status = 'FILA_ESPERA'
            
            inscricao.save()
        
        return inscricoes_classificadas
    
    @classmethod
    def gerar_relatorio_classificacao(cls, evento):
        """
        Gera relatório completo da classificação de um evento.
        
        Args:
            evento (Evento): Evento a ser classificado
            
        Returns:
            dict: Relatório com informações detalhadas
        """
        # Executa classificação
        inscricoes_classificadas = cls.classificar_evento(evento)
        
        # Monta relatório
        relatorio = {
            'evento': {
                'id': evento.id,
                'nome': evento.descricao,
                'status': evento.status.status,
                'modalidade': evento.get_modalidade_display(),
            },
            'vagas': {
                'total': evento.vagas,
                'minimas': evento.vagas_minimas,
                'disponiveis': evento.vagas_disponiveis(),
            },
            'inscricoes': {
                'total': inscricoes_classificadas.count(),
                'aprovados': inscricoes_classificadas.filter(
                    classificacao__posicao__lte=evento.vagas
                ).count(),
                'fila_espera': inscricoes_classificadas.filter(
                    classificacao__posicao__gt=evento.vagas
                ).count(),
            },
            'criterios': [],
            'classificados': []
        }
        
        # Informações dos critérios aplicados
        for evento_criterio in evento.evento_criterios.select_related('criterio').all():
            relatorio['criterios'].append({
                'nome': evento_criterio.criterio.descricao_criterio,
                'tipo': evento_criterio.criterio.get_tipo_criterio_display(),
                'peso': evento_criterio.peso,
                'ordem': evento_criterio.ordem,
                'tipo_reserva': evento_criterio.get_tipo_reserva_display(),
                'vagas_reservadas': evento_criterio.vagas_reservadas,
            })
        
        # Lista detalhada de classificados
        for inscricao in inscricoes_classificadas:
            classificacao = inscricao.classificacao
            
            # Detalhamento dos critérios atendidos
            criterios_atendidos = []
            for criterio_atendido in inscricao.criterios_atendidos.select_related('criterio').all():
                criterios_atendidos.append({
                    'criterio': criterio_atendido.criterio.descricao_criterio,
                    'pontos': float(criterio_atendido.pontos_obtidos),
                    'validado': criterio_atendido.validado,
                })
            
            relatorio['classificados'].append({
                'posicao': classificacao.posicao,
                'nome': inscricao.interessado.nome,
                'cpf': inscricao.interessado.cpf,
                'score_total': float(classificacao.score_total),
                'data_inscricao': inscricao.data_inscricao.strftime('%d/%m/%Y %H:%M'),
                'situacao': 'APROVADO' if classificacao.posicao <= evento.vagas else 'FILA DE ESPERA',
                'criterios_atendidos': criterios_atendidos,
            })
        
        return relatorio
    
    @classmethod
    def exportar_classificacao_csv(cls, evento):
        """
        Gera dados de classificação no formato para exportação CSV.
        
        Args:
            evento (Evento): Evento a ser exportado
            
        Returns:
            list: Lista de dicionários com dados para CSV
        """
        relatorio = cls.gerar_relatorio_classificacao(evento)
        
        dados_csv = []
        for classificado in relatorio['classificados']:
            dados_csv.append({
                'Posição': classificado['posicao'],
                'Nome': classificado['nome'],
                'CPF': classificado['cpf'],
                'Score': classificado['score_total'],
                'Data Inscrição': classificado['data_inscricao'],
                'Situação': classificado['situacao'],
            })
        
        return dados_csv