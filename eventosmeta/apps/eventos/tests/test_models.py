"""
Arquivo: test_models.py
Caminho: apps/eventos/tests/test_models.py
Finalidade: Testar os modelos do app eventos.
Atualizações:
Data:   15/05/2026 - Corrigir de onde está chamando inscricaofactory, classificacaofactory
                    e Inclusão de cabeçalho
        26/05/2026 - Adicionando factory boy para criar objetos de teste
        16/06/2026 - Refatorado de unittest.TestCase para pytest
"""

import pytest
import factory
from factory.django import DjangoModelFactory
from factory import LazyFunction
from django.utils import timezone
from datetime import timedelta
from django.core.exceptions import ValidationError
from django.db import IntegrityError
from apps.eventos.models import Status, Evento, Criterio, Turma, Horario

pytestmark = pytest.mark.django_db

# 
# FACTORIES
# 

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

# 
# STATUS
# 

class TestStatusModel:

    def test_create_status(self):
        status = StatusFactory()
        assert status.pk is not None
        assert status.nome == "Ativo"
        assert status.cor == "#ffffff"
        assert status.ordem == 1

    def test_status_str(self):
        status = StatusFactory()
        assert str(status) == status.nome

    def test_status_ordem_unique(self):
        StatusFactory(ordem=1)
        with pytest.raises(IntegrityError):
            StatusFactory(ordem=1)

    def test_status_cor_valid_hex(self):
        status = StatusFactory(cor="#123abc")
        status.full_clean()

# 
# EVENTO
# 

class TestEventoModel:

    def test_create_evento(self):
        evento = EventoFactory()
        assert evento.pk is not None

    def test_evento_str(self):
        evento = EventoFactory()
        assert str(evento) == evento.nome

    def test_evento_foreign_key_status(self):
        evento = EventoFactory()
        assert evento.status is not None
        assert isinstance(evento.status, Status)

    def test_evento_total_vagas_positive(self):
        with pytest.raises(ValidationError):
            evento = EventoFactory(total_vagas=-1)
            evento.full_clean()

    def test_evento_data_inicio_inscricao_before_fim(self):
        with pytest.raises(ValidationError):
            evento = EventoFactory(
                data_inicio_inscricao=timezone.now(),
                data_fim_inscricao=timezone.now() - timedelta(days=1),
            )
            evento.full_clean()

    def test_evento_data_inicio_evento_before_fim(self):
        with pytest.raises(ValidationError):
            evento = EventoFactory(
                data_inicio_evento=timezone.now() + timedelta(days=10),
                data_fim_evento=timezone.now() + timedelta(days=5),
            )
            evento.full_clean()

    def test_evento_datas_evento_validas(self):
        evento = EventoFactory(
            data_inicio_evento=timezone.now() + timedelta(days=1),
            data_fim_evento=timezone.now() + timedelta(days=10),
        )
        assert evento.pk is not None

# 
# CRITERIO
# 

class TestCriterioModel:

    def test_create_criterio(self):
        criterio = CriterioFactory()
        assert criterio.pk is not None

    def test_criterio_str(self):
        criterio = CriterioFactory()
        assert criterio.nome in str(criterio)

    def test_criterio_codigo_unique(self):
        CriterioFactory(codigo="CRIT01")
        with pytest.raises(IntegrityError):
            CriterioFactory(codigo="CRIT01")

    def test_criterio_pontos_non_negative(self):
        with pytest.raises(ValidationError):
            criterio = CriterioFactory(pontos=-5)
            criterio.full_clean()

    def test_criterio_categoria_choices(self):
        with pytest.raises(ValidationError):
            criterio = CriterioFactory(categoria="INVALIDA")
            criterio.full_clean()

# 
# TURMA
# 

class TestTurmaModel:

    def test_create_turma(self):
        turma = TurmaFactory()
        assert turma.pk is not None

    def test_turma_str(self):
        turma = TurmaFactory()
        assert turma.nome in str(turma)

    def test_turma_foreign_key_evento(self):
        turma = TurmaFactory()
        assert turma.evento is not None
        assert isinstance(turma.evento, Evento)

    def test_turma_capacidade_positive(self):
        with pytest.raises(ValidationError):
            turma = TurmaFactory(capacidade=-10)
            turma.full_clean()

# 
# HORARIO
# 

class TestHorarioModel:

    def test_create_horario(self):
        horario = HorarioFactory()
        assert horario.pk is not None

    def test_horario_foreign_key_turma(self):
        horario = HorarioFactory()
        assert horario.turma is not None
        assert isinstance(horario.turma, Turma)


