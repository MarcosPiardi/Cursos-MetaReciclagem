"""
Arquivo: test_models_evento_expanded.py
caminho: apps/eventos/tests/test_models_evento_expanded.py
Finalidade: Testes expandidos dos modelos do app eventos.
Atualizações:
 - 03/06/2026 - Criação do arquivo com testes mais abrangentes para o modelo Evento, incluindo validação de datas, relacionamentos e casos de borda.
"""


import pytest
from django.utils import timezone
from datetime import timedelta
from django.core.exceptions import ValidationError
from django.db.models import ProtectedError
import factory
from factory.django import DjangoModelFactory
from factory import LazyFunction, Faker
from apps.eventos.models import Status, Evento, Criterio, EventoCriterio, Turma, Horario

class StatusFactory(DjangoModelFactory):
    class Meta:
        model = Status
    nome = factory.Sequence(lambda n: f'Status {n}')
    cor = '#FFFFFF'
    ordem = 1

class EventoFactory(DjangoModelFactory):
    class Meta:
        model = Evento
    nome = factory.Sequence(lambda n: f'Evento {n}')
    status = factory.SubFactory(StatusFactory)
    total_vagas = 100
    data_inicio_inscricao = timezone.now()
    data_fim_inscricao = timezone.now() + timedelta(days=10)
    data_inicio_evento = timezone.now() + timedelta(days=11)
    data_fim_evento = timezone.now() + timedelta(days=20)

class TurmaFactory(DjangoModelFactory):
    class Meta:
        model = Turma
    nome = "Turma A"
    turno = "MATUTINO"
    capacidade = 20
    local = "Sala A"
    data_inicio = LazyFunction(lambda: timezone.now().date())
    data_fim = LazyFunction(lambda: (timezone.now() + timedelta(days=30)).date())
    evento = factory.SubFactory(EventoFactory)

class HorarioFactory(DjangoModelFactory):
    class Meta:
        model = Horario
    turma = factory.SubFactory(TurmaFactory)
    dia_semana = 1
    hora_inicio = '08:00'
    hora_fim = '10:00'

@pytest.mark.django_db
class TestEventoCreation:
    def test_criar_evento(self):
        e = EventoFactory()
        assert e.pk is not None
    def test_str_evento(self):
        e = EventoFactory(nome='Teste')
        assert str(e) == 'Teste'
    def test_defaults_evento(self):
        e = EventoFactory(total_vagas=100)
        assert e.total_vagas == 100
    def test_status_evento(self):
        e = EventoFactory()
        assert isinstance(e.status, Status)
    def test_multiplos_eventos(self):
        e1 = EventoFactory()
        e2 = EventoFactory()
        e3 = EventoFactory()
        assert Evento.objects.count() == 3

@pytest.mark.django_db
class TestEventoValidacaoDatas:
    def test_fim_inscricao_antes_inicio(self):
        with pytest.raises(ValidationError):
            e = EventoFactory(data_fim_inscricao=timezone.now() - timedelta(days=1))
            e.full_clean()
    def test_fim_evento_antes_inicio(self):
        with pytest.raises(ValidationError):
            e = EventoFactory(data_fim_evento=timezone.now())
            e.full_clean()
    def test_datas_validas(self):
        e = EventoFactory()
        e.full_clean()
    def test_datas_iguais(self):
        now = timezone.now()
        e = EventoFactory(data_inicio_evento=now, data_fim_evento=now)
        e.full_clean()

@pytest.mark.django_db
class TestEventoValidacaoVagas:
    def test_vagas_negativas(self):
        with pytest.raises(ValidationError):
            e = EventoFactory(total_vagas=-1)
            e.full_clean()
    def test_vagas_altas(self):
        e = EventoFactory(total_vagas=999999)
        e.full_clean()

@pytest.mark.django_db
class TestEventoRelacionamentos:
    def test_has_status(self):
        e = EventoFactory()
        assert e.status is not None
    def test_status_has_eventos(self):
        s = StatusFactory()
        EventoFactory(status=s)
        assert s.evento_set.count() == 1
    def test_protect_status(self):
        s = StatusFactory()
        EventoFactory(status=s)
        with pytest.raises(ProtectedError):
            s.delete()

@pytest.mark.django_db
class TestTurmaHorario:
    def test_turma_horario_relation(self):
        h = HorarioFactory()
        assert h.turma.horarios.count() == 1






