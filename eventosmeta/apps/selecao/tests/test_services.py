"""
Arquivo: test_services.py
Caminho: apps/selecao/tests/test_services.py
Testes de serviços para o app Selecao
Data: 27 de março de 2026
"""

from django.test import TestCase
from django.utils import timezone
from datetime import timedelta
from decimal import Decimal

from .factories import (
    InteressadoFactory,   # ← adicione aqui
    InscricaoFactory,
    StatusInscricaoFactory,
    ClassificacaoFactory,
    EventoFactory,
    EventoCriterioFactory,
    CriterioFactory
)



from apps.selecao.models import Inscricao, Classificacao
from apps.selecao.services import ClassificadorService


class TestClassificadorService(TestCase):
    """Testes para o serviço ClassificadorService."""

    def setUp(self):
        self.status_pendente = StatusInscricaoFactory(nome='Pendente')
        self.status_classificado = StatusInscricaoFactory(nome='Classificado')
        self.status_lista_espera = StatusInscricaoFactory(nome='Lista de Espera')
        
        self.evento = EventoFactory(total_vagas=5)
        self.criterio = CriterioFactory(nome='PCD', tipo_criterio='PONTUACAO', pontos=10)
        self.evento_criterio = EventoCriterioFactory(evento=self.evento, criterio=self.criterio)

    def test_calcular_pontuacao_inscricao_zero(self):
        """Deve retornar 0 pontos para inscrição sem critérios."""
        interessado = InteressadoFactory()
        inscricao = InscricaoFactory(interessado=interessado, evento=self.evento)
        
        pontuacao = ClassificadorService.calcular_pontuacao_inscricao(inscricao)
        self.assertEqual(pontuacao, Decimal('0'))

    def test_calcular_pontuacao_inscricao_com_criterios(self):
        """Deve calcular pontuação com critérios atendidos."""
        interessado = InteressadoFactory()
        inscricao = InscricaoFactory(interessado=interessado, evento=self.evento)
        
        # Simula critérios atendidos
        from apps.selecao.models import InscricaoCriterioAtendido
        InscricaoCriterioAtendido.objects.create(
            inscricao=inscricao,
            criterio=self.criterio,
            pontos_atribuidos=10
        )
        
        pontuacao = ClassificadorService.calcular_pontuacao_inscricao(inscricao)
        self.assertEqual(pontuacao, Decimal('10'))

    def test_processar_inscricao_cria_classificacao(self):
        """Deve processar inscrição e criar classificacao."""
        interessado = InteressadoFactory()
        inscricao = InscricaoFactory(interessado=interessado, evento=self.evento)
        
        ClassificadorService.processar_inscricao(inscricao)
        
        classificacao = Classificacao.objects.get(inscricao=inscricao)
        self.assertIsNotNone(classificacao)
        self.assertIsNone(classificacao.posicao)

    def test_classificar_evento_atribui_posicoes(self):
        """Deve classificar evento atribuindo posições corretas."""
        inscricoes = []
        for i in range(7):
            interessado = InteressadoFactory()
            inscricao = InscricaoFactory(
                interessado=interessado,
                evento=self.evento,
                status=self.status_pendente
            )
            inscricoes.append(inscricao)
        
        ClassificadorService.classificar_evento(self.evento)
        
        classificacoes = Classificacao.objects.filter(
            inscricao__evento=self.evento
        ).order_by('posicao')
        
        self.assertEqual(classificacoes.count(), 7)
        for i, classificacao in enumerate(classificacoes):
            self.assertEqual(classificacao.posicao, i + 1)

    def test_classificar_evento_classifica_dentro_vagas(self):
        """Inscrições dentro de vagas devem ser classificadas."""
        for i in range(5):
            interessado = InteressadoFactory()
            InscricaoFactory(
                interessado=interessado,
                evento=self.evento,
                status=self.status_pendente
            )
        
        ClassificadorService.classificar_evento(self.evento)
        
        classificacoes = Classificacao.objects.filter(
            inscricao__evento=self.evento,
            posicao__lte=self.evento.total_vagas
        )
        
        for classificacao in classificacoes:
            self.assertTrue(classificacao.classificado)
            self.assertFalse(classificacao.lista_espera)

    def test_classificar_evento_lista_espera(self):
        """Inscrições acima de vagas devem estar em lista de espera."""
        for i in range(8):
            interessado = InteressadoFactory()
            InscricaoFactory(
                interessado=interessado,
                evento=self.evento,
                status=self.status_pendente
            )
        
        ClassificadorService.classificar_evento(self.evento)
        
        classificacoes = Classificacao.objects.filter(
            inscricao__evento=self.evento,
            posicao__gt=self.evento.total_vagas
        )
        
        for classificacao in classificacoes:
            self.assertFalse(classificacao.classificado)
            self.assertTrue(classificacao.lista_espera)

    def test_classificar_evento_atualiza_status_inscricao(self):
        """Deve atualizar status das inscrições após classificação."""
        interessado = InteressadoFactory()
        inscricao = InscricaoFactory(
            interessado=interessado,
            evento=self.evento,
            status=self.status_pendente
        )
        
        ClassificadorService.classificar_evento(self.evento)
        
        inscricao.refresh_from_db()
        self.assertEqual(inscricao.status.nome, 'Classificado')

    def test_classificar_evento_com_criterios(self):
        """Deve classificar evento respeitando critérios ativos."""
        for i in range(3):
            interessado = InteressadoFactory()
            InscricaoFactory(
                interessado=interessado,
                evento=self.evento,
                status=self.status_pendente
            )
        
        resultado = ClassificadorService.classificar_evento(self.evento)
        self.assertTrue(resultado['sucesso'])
        self.assertEqual(resultado['total_processadas'], 3)


