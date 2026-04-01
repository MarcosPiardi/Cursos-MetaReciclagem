import factory
from faker import Faker
from datetime import timedelta, time
from django.utils import timezone
from apps.eventos.models import Status, Criterio, Evento, EventoCriterio, Turma, Horario


class StatusFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Status
        django_get_or_create = ('nome',)

    nome = factory.Sequence(lambda n: f'Status {n}')
    cor = factory.Faker('hex_color')
    ordem = factory.Faker('random_int', min=0, max=10)


class CriterioFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Criterio

    tipo_criterio = 'PONTUACAO'
    codigo = factory.Sequence(lambda n: f'CRITERIO_{n}')
    nome = factory.Faker('word')
    descricao = factory.Faker('text')
    pontos = factory.Faker('random_int', min=5, max=20)
    categoria = 'GERAL'
    ativo = True


class EventoFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Evento

    nome = factory.Faker('sentence', nb_words=3, locale='pt_BR')
    descricao = factory.Faker('text', max_nb_chars=200, locale='pt_BR')
    status = factory.SubFactory(StatusFactory, nome='INSCRICOES_ABERTAS')
    total_vagas = factory.Faker('random_int', min=5, max=20)
    data_inicio_inscricao = factory.LazyFunction(lambda: timezone.now() - timedelta(days=7))
    data_fim_inscricao = factory.LazyFunction(lambda: timezone.now() + timedelta(days=7))
    data_inicio_evento = factory.LazyAttribute(lambda o: o.data_fim_inscricao + timedelta(days=10))
    data_fim_evento = factory.LazyAttribute(lambda o: o.data_inicio_evento + timedelta(days=20))


class EventoCriterioFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = EventoCriterio

    evento = factory.SubFactory(EventoFactory)
    criterio = factory.SubFactory(CriterioFactory)
    prioridade = factory.Sequence(lambda n: n)
    ativo = True


class TurmaFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Turma

    evento = factory.SubFactory(EventoFactory)
    nome = factory.Faker('sentence', nb_words=2, locale='pt_BR')
    turno = 'MATUTINO'
    capacidade = factory.Faker('random_int', min=10, max=30)
    local = factory.Faker('city', locale='pt_BR')
    data_inicio = factory.LazyFunction(timezone.now)
    data_fim = factory.LazyAttribute(lambda o: o.data_inicio + timedelta(days=30))

    
class HorarioFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Horario

    turma = factory.SubFactory(TurmaFactory)
    dia_semana = 1
    hora_inicio = factory.LazyFunction(lambda: time(8, 0, 0))
    hora_fim = factory.LazyFunction(lambda: time(12, 0, 0))

