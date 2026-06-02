"""
Arquivo: test_models.py
caminho: apps/eventos/tests/test_models.py
Finalidade: Testar os modelos do app eventos.
Atualizações:
Data:   15/05/2026 - Corrigir de onde está chamando inscricaofactory, classificacaofactory e Inclusão de cabeçalho  
        26/05/2026 - adicionando factory boy para criar objetos de teste
"""

import factory
from factory.django import DjangoModelFactory
from factory import LazyFunction
from django.utils import timezone
from datetime import timedelta
from django.core.exceptions import ValidationError
from django.test import TestCase
from apps.eventos.models import Status, Evento, Criterio, Turma, Horario

class StatusFactory(DjangoModelFactory):
    class Meta:
        model = Status
    nome = "Ativo"
    cor = "#ffffff"
    ordem = 1

class EventoFactory(DjangoModelFactory):
    class Meta:
        model = Evento
    nome = "Evento Teste"
    descricao = "Descricao"
    total_vagas = 100
    data_inicio_inscricao = LazyFunction(lambda: timezone.now() - timedelta(days=10))
    data_fim_inscricao = LazyFunction(lambda: timezone.now() - timedelta(days=5))
    data_inicio_evento = LazyFunction(lambda: timezone.now() + timedelta(days=1))
    data_fim_evento = LazyFunction(lambda: timezone.now() + timedelta(days=10))
    status = factory.SubFactory(StatusFactory)

class CriterioFactory(DjangoModelFactory):
    class Meta:
        model = Criterio
    tipo_criterio = "PONTUACAO"
    codigo = "CRIT01"
    nome = "Criterio Teste"
    descricao = "Descricao"
    pontos = 10
    categoria = "GERAL"
    ativo = True

class TurmaFactory(DjangoModelFactory):
    class Meta:
        model = Turma
    nome = "Turma A"
    turno = "MATUTINO"
    capacidade = 30
    local = "SALA A"
    data_inicio = "2025-03-01"
    data_fim = "2025-05-30"
    evento = factory.SubFactory(EventoFactory)

class HorarioFactory(DjangoModelFactory):
    class Meta:
        model = Horario
    turma = factory.SubFactory(TurmaFactory)
    dia_semana = 2
    hora_inicio = "08:00"
    hora_fim = "12:00"

class StatusModelTest(TestCase):
    def test_create_status(self):
        status = StatusFactory()
        self.assertIsNotNone(status.pk)
        self.assertEqual(status.nome, "Ativo")
        self.assertEqual(status.cor, "#ffffff")
        self.assertEqual(status.ordem, 1)
    def test_status_str(self):
        status = StatusFactory()
        self.assertEqual(str(status), status.nome)
    def test_status_ordem_unique(self):
        StatusFactory(ordem=1)
        with self.assertRaises(Exception):
            StatusFactory(ordem=1)
    def test_status_cor_valid_hex(self):
        status = StatusFactory(cor="#123abc")
        status.full_clean()
        self.assertTrue(True)

class EventoModelTest(TestCase):
    def test_create_evento(self):
        evento = EventoFactory()
        self.assertIsNotNone(evento.pk)
    def test_evento_str(self):
        evento = EventoFactory()
        self.assertEqual(str(evento), evento.nome)
    def test_evento_foreign_key_status(self):
        evento = EventoFactory()
        self.assertIsNotNone(evento.status)
        self.assertIsInstance(evento.status, Status)
    def test_evento_total_vagas_positive(self):
        with self.assertRaises(ValidationError):
            evento = EventoFactory(total_vagas=-1)
            evento.full_clean()
    def test_evento_data_inicio_inscricao_before_fim(self):
        with self.assertRaises(ValidationError):
            evento = EventoFactory(
                data_inicio_inscricao=timezone.now(),
                data_fim_inscricao=timezone.now() - timedelta(days=1)
            )
            evento.full_clean()
    def test_evento_data_inicio_evento_before_fim(self):
        with self.assertRaises(ValidationError):
            evento = EventoFactory(
                data_inicio_evento=timezone.now() + timedelta(days=10),
                data_fim_evento=timezone.now() + timedelta(days=5)
            )
            evento.full_clean()
    def test_evento_datas_evento_validas(self):
        evento = EventoFactory(
            data_inicio_evento=timezone.now() + timedelta(days=1),
            data_fim_evento=timezone.now() + timedelta(days=10)
        )
        self.assertIsNotNone(evento.pk)

class CriterioModelTest(TestCase):
    def test_create_criterio(self):
        criterio = CriterioFactory()
        self.assertIsNotNone(criterio.pk)
    def test_criterio_str(self):
        criterio = CriterioFactory()
        self.assertIn(criterio.nome, str(criterio))
    def test_criterio_codigo_unique(self):
        CriterioFactory(codigo="CRIT01")
        with self.assertRaises(Exception):
            CriterioFactory(codigo="CRIT01")
    def test_criterio_pontos_non_negative(self):
        with self.assertRaises(ValidationError):
            criterio = CriterioFactory(pontos=-5)
            criterio.full_clean()
    def test_criterio_categoria_choices(self):
        with self.assertRaises(ValidationError):
            criterio = CriterioFactory(categoria="INVALIDA")
            criterio.full_clean()

class TurmaModelTest(TestCase):
    def test_create_turma(self):
        turma = TurmaFactory()
        self.assertIsNotNone(turma.pk)
    def test_turma_str(self):
        turma = TurmaFactory()
        self.assertIn(turma.nome, str(turma))  # __str__ retorna "Evento - Turma"
    def test_turma_foreign_key_evento(self):
        turma = TurmaFactory()
        self.assertIsNotNone(turma.evento)
        self.assertIsInstance(turma.evento, Evento)
    def test_turma_capacidade_positive(self):
        with self.assertRaises(ValidationError):
            turma = TurmaFactory(capacidade=-10)
            turma.full_clean()

class HorarioModelTest(TestCase):
    def test_create_horario(self):
        horario = HorarioFactory()
        self.assertIsNotNone(horario.pk)
    def test_horario_foreign_key_turma(self):
        horario = HorarioFactory()
        self.assertIsNotNone(horario.turma)
        self.assertIsInstance(horario.turma, Turma)



