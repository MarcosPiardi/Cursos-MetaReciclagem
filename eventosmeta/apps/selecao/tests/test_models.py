"""
Arquivo: test_models.py
Caminho: apps/selecao/tests/test_models.py
Testes de modelos para o app Selecao
Data: 27 de março de 2026
"""

from django.test import TestCase
from django.db.utils import IntegrityError

from ..models import StatusInscricao, Inscricao, Classificacao
from .factories import (
    StatusInscricaoFactory,
    InscricaoFactory,
    ClassificacaoFactory,
    EventoFactory
)
from apps.interessados.tests.factories import InteressadoFactory


class TestStatusInscricaoModel(TestCase):
    """Testes para o modelo StatusInscricao."""

    def test_create_status_inscricao(self):
        """Deve criar um StatusInscricao com sucesso."""
        status = StatusInscricaoFactory(nome='Pendente', cor='#FF0000')
        self.assertIsNotNone(status.pk)
        self.assertEqual(status.nome, 'Pendente')
        self.assertEqual(status.cor, '#FF0000')

    def test_status_inscricao_str(self):
        """O método __str__ deve retornar o nome do status."""
        status = StatusInscricaoFactory(nome='Aprovado')
        self.assertEqual(str(status), 'Aprovado')

    def test_status_inscricao_unique_name(self):
        """Não deve permitir dois status com o mesmo nome."""
        StatusInscricaoFactory(nome='Unico')
        with self.assertRaises(IntegrityError):
            StatusInscricao.objects.create(nome='Unico', cor='#FF0000')


class TestInscricaoModel(TestCase):
    """Testes para o modelo Inscricao."""

    def setUp(self):
        self.interessado = InteressadoFactory()
        self.evento = EventoFactory()
        self.status_pendente = StatusInscricaoFactory(nome='Pendente')

    def test_create_inscricao(self):
        """Deve criar uma Inscricao com sucesso."""
        inscricao = InscricaoFactory(
            interessado=self.interessado,
            evento=self.evento,
            status=self.status_pendente
        )
        self.assertIsNotNone(inscricao.pk)
        self.assertEqual(inscricao.interessado, self.interessado)
        self.assertEqual(inscricao.evento, self.evento)

    def test_inscricao_str(self):
        """O método __str__ deve retornar formato legível."""
        inscricao = InscricaoFactory(
            interessado=self.interessado,
            evento=self.evento,
            status=self.status_pendente
        )
        self.assertIn(self.interessado.nome, str(inscricao))
        self.assertIn(self.evento.nome, str(inscricao))

    def test_inscricao_unique_together(self):
        """Não deve permitir duas inscrições do mesmo interessado no mesmo evento."""
        InscricaoFactory(
            interessado=self.interessado,
            evento=self.evento,
            status=self.status_pendente
        )
        with self.assertRaises(IntegrityError):
            InscricaoFactory(
                interessado=self.interessado,
                evento=self.evento,
                status=self.status_pendente
            )

    def test_inscricao_relacionamentos(self):
        """Deve verificar os relacionamentos corretos."""
        inscricao = InscricaoFactory(
            interessado=self.interessado,
            evento=self.evento,
            status=self.status_pendente
        )
        self.assertEqual(inscricao.interessado.nome, self.interessado.nome)
        self.assertEqual(inscricao.evento.nome, self.evento.nome)
        self.assertEqual(inscricao.status.nome, self.status_pendente.nome)


class TestClassificacaoModel(TestCase):
    """Testes para o modelo Classificacao."""

    def setUp(self):
        self.inscricao = InscricaoFactory()

    def test_create_classificacao(self):
        """Deve criar uma Classificacao com sucesso."""
        classificacao = ClassificacaoFactory(
            inscricao=self.inscricao,
            pontuacao_total=50,
            posicao=1,
            classificado=True
        )
        self.assertIsNotNone(classificacao.pk)
        self.assertEqual(classificacao.inscricao, self.inscricao)
        self.assertEqual(classificacao.pontuacao_total, 50)
        self.assertEqual(classificacao.posicao, 1)
        self.assertTrue(classificacao.classificado)
        self.assertFalse(classificacao.lista_espera)

    def test_classificacao_str(self):
        """O método __str__ deve retornar formato legível."""
        classificacao = ClassificacaoFactory(
            inscricao=self.inscricao,
            pontuacao_total=75,
            posicao=3
        )
        resultado_str = str(classificacao)
        self.assertIn('3º', resultado_str)
        self.assertIn(self.inscricao.interessado.nome, resultado_str)

    def test_classificacao_posicao_null_default(self):
        """A posição deve ser nula por padrão."""
        classificacao = ClassificacaoFactory(
            inscricao=self.inscricao,
            pontuacao_total=60,
            posicao=None
        )
        self.assertIsNone(classificacao.posicao)
        self.assertFalse(classificacao.classificado)
        self.assertFalse(classificacao.lista_espera)

    def test_classificacao_unique_inscricao(self):
        """Cada inscrição deve ter apenas uma classificacao."""
        ClassificacaoFactory(inscricao=self.inscricao)
        with self.assertRaises(IntegrityError):
            ClassificacaoFactory(inscricao=self.inscricao)


            