from django.test import TestCase
from django.utils import timezone
from datetime import timedelta

from apps.selecao.models import Inscricao, Classificacao
from .factories import InscricaoFactory, ClassificacaoFactory


class TestInscricaoModel(TestCase):
    """Testes para o modelo Inscricao."""

    def test_criar_inscricao_basica(self):
        """Verifica a criação básica de uma Inscricao."""
        inscricao = InscricaoFactory()
        self.assertIsNotNone(inscricao)
        self.assertIsNotNone(inscricao.evento)
        self.assertIsNotNone(inscricao.interessado)
        self.assertIsNotNone(inscricao.data_inscricao)

    def test_inscricao_com_evento_e_interessado(self):
        """Verifica se a Inscricao é criada com Evento e Interessado."""
        inscricao = InscricaoFactory()
        self.assertEqual(inscricao.evento.id, inscricao.evento.id)
        self.assertEqual(inscricao.interessado.id, inscricao.interessado.id)

    def test_inscricao_data_automatica(self):
        """Verifica se a data de inscrição é preenchida automaticamente."""
        inscricao = InscricaoFactory()
        self.assertIsNotNone(inscricao.data_inscricao)
        self.assertLess(abs((timezone.now() - inscricao.data_inscricao).total_seconds()), 5)


class TestClassificacaoModel(TestCase):
    """Testes para o modelo Classificacao."""

    def test_criar_classificacao_basica(self):
        """Verifica a criação básica de uma Classificacao."""
        classificacao = ClassificacaoFactory()
        self.assertIsNotNone(classificacao)
        self.assertIsNotNone(classificacao.inscricao)
        self.assertIsNotNone(classificacao.posicao)
        self.assertGreater(classificacao.posicao, 0)

    def test_classificacao_pontuacao_valida(self):
        """Verifica se a pontuação está entre 0 e 100."""
        classificacao = ClassificacaoFactory(pontuacao_total=75)
        self.assertEqual(classificacao.pontuacao_total, 75)
        self.assertGreaterEqual(classificacao.pontuacao_total, 0)
        self.assertLessEqual(classificacao.pontuacao_total, 100)

    def test_classificacao_status_flags(self):
        """Verifica as flags de classificado e lista_espera."""
        classificacao = ClassificacaoFactory()
        self.assertIsNotNone(classificacao.classificado)
        self.assertIsNotNone(classificacao.lista_espera)

        