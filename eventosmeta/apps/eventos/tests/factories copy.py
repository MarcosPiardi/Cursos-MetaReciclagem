"""
Arquivo: factories.py
Caminho: apps/eventos/tests/factories.py
Finalidade: Fornecer dados de teste para os modelos do app eventos usando Factory Boy
Atualizações:
 - 15/05/2026 - Criação do arquivo com factories para os modelos do app eventos, utilizando Factory
 - 26/05/2026 - Adicionando factory
 - 03/06/2026 - Ajustando factories para refletir as relações entre os modelos e garantir a criação de dados consistentes para os testes.
"""

import factory
from factory import Faker, SubFactory, Sequence, LazyAttribute, LazyFunction
from datetime import timedelta
from django.utils import timezone
from apps.eventos.models import Status, Criterio, Evento, EventoCriterio, Turma, Horario

class StatusFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Status
        django_get_or_create = ('nome',)

    nome = Sequence(lambda n: f'Status {n}')
    cor = Faker('hex_color')
    ordem = Faker('random_int', min=1, max=100)

class CriterioFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Criterio

    tipo_criterio = Faker('word')
    codigo = Sequence(lambda n: f'CRIT-{n:03d}')
    nome = Faker('sentence', nb_words=3)
    descricao = Faker('text')
    pontos = Faker('random_int', min=1, max=10)
    categoria = Faker('word')
    ativo = True

class EventoFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Evento

    nome = Faker('catch_phrase')
    descricao = Faker('paragraph')
    status = SubFactory(StatusFactory)
    total_vagas = Faker('random_int', min=10, max=100)
    data_inicio_inscricao = LazyFunction(timezone.now)
    data_fim_inscricao = LazyAttribute(lambda o: o.data_inicio_inscricao + timedelta(days=5))
    data_inicio_evento = LazyAttribute(lambda o: o.data_fim_inscricao + timedelta(days=1))
    data_fim_evento = LazyAttribute(lambda o: o.data_inicio_evento + timedelta(days=2))

class EventoCriterioFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = EventoCriterio

    evento = SubFactory(EventoFactory)
    criterio = SubFactory(CriterioFactory)
    prioridade = Faker('random_int', min=1, max=5)
    ativo = True


class TurmaFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Turma

    evento = SubFactory(EventoFactory)
    nome = Faker('word')
    turno = Faker('random_element', elements=['M', 'T', 'N'])
    capacidade = Faker('random_int', min=20, max=50)
    local = Faker('address')
    data_inicio = LazyFunction(timezone.now)
    data_fim = LazyAttribute(lambda o: o.data_inicio + timedelta(days=30))

class HorarioFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Horario

    turma = SubFactory(TurmaFactory)
    dia_semana = Faker('random_int', min=1, max=7)
    hora_inicio = Faker('time')
    hora_fim = Faker('time')

