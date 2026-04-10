"""
Arquivo: test_models.py
Caminho: apps/selecao/tests/test_models.py
27/03/2026 - Testes de modelos para o app Selecao
08/04/2026 - Testes de modelos para o app Seleção com validações e desempate
"""

from django.test import TestCase
from django.db.utils import IntegrityError
from django.core.exceptions import ValidationError

from apps.selecao.models import StatusInscricao, Inscricao, Classificacao
from apps.selecao.tests.factories import (
    StatusInscricaoFactory,
    InscricaoFactory,
    ClassificacaoFactory
)
from apps.eventos.tests.factories import EventoFactory
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

    # ==========================================
    # NOVOS TESTES DE VALIDAÇÃO
    # ==========================================

    def test_pontuacao_total_validacao_range(self):
        """A pontuação total não deve ser menor que 0 ou maior que 100."""
        classificacao = ClassificacaoFactory(inscricao=self.inscricao)
        
        # Teste menor que zero
        classificacao.pontuacao_total = -1
        with self.assertRaises(ValidationError):
            classificacao.full_clean()
            
        # Teste maior que 100
        classificacao.pontuacao_total = 101
        with self.assertRaises(ValidationError):
            classificacao.full_clean()

    def test_flags_classificacao_mutuamente_exclusivas(self):
        """Um candidato não pode estar classificado e na lista de espera ao mesmo tempo."""
        classificacao = ClassificacaoFactory(
            inscricao=self.inscricao,
            classificado=True,
            lista_espera=True
        )
        
        with self.assertRaises(ValidationError):
            classificacao.full_clean()

    def test_desempate_por_data_inscricao(self):
        """Verifica se a ordenação pelo banco respeita a data de inscrição."""
        # Funciona como uma fila de banco: quem chega primeiro, tem prioridade
        interessado2 = InteressadoFactory()
        inscricao2 = InscricaoFactory(interessado=interessado2)
        
        classificacao1 = ClassificacaoFactory(
            inscricao=self.inscricao,
            pontuacao_total=50
        )
        classificacao2 = ClassificacaoFactory(
            inscricao=inscricao2,
            pontuacao_total=50
        )
        
        # Força datas diferentes para simular ordem de chegada
        self.inscricao.data_inscricao = '2026-01-01 10:00:00'
        self.inscricao.save()
        inscricao2.data_inscricao = '2026-01-01 11:00:00'
        inscricao2.save()
        
        # Ordena por pontuação (decrescente) e data de inscrição (crescente)
        queryset = Classificacao.objects.all().order_by('-pontuacao_total', 'inscricao__data_inscricao')
        
        self.assertEqual(queryset.first(), classificacao1)
        self.assertEqual(queryset.last(), classificacao2)

