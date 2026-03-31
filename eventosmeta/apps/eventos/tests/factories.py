import factory
from django.utils import timezone
from datetime import timedelta
from apps.eventos.models import Evento, Turma, Status

class StatusFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Status
        django_get_or_create = ('nome',)

    nome = factory.Sequence(lambda n: f'Status {n}')
    cor = factory.Faker('hex_color')
    ordem = factory.Faker('random_int', min=0, max=10)

class EventoFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Evento

    nome = factory.Faker('word')
    descricao = factory.Faker('text')
    status = factory.SubFactory(StatusFactory, nome='ATIVA')
    total_vagas = factory.Faker('random_int', min=10, max=50)
    data_inicio_inscricao = factory.LazyFunction(lambda: timezone.now() - timedelta(days=7))
    data_fim_inscricao = factory.LazyFunction(lambda: timezone.now() + timedelta(days=7))
    data_inicio_evento = factory.LazyFunction(lambda: timezone.now().date() + timedelta(days=10))
    data_fim_evento = factory.LazyFunction(lambda: timezone.now().date() + timedelta(days=20))

class TurmaFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Turma

    evento = factory.SubFactory(EventoFactory)
    nome = factory.Sequence(lambda n: f'Turma {n}')
    turno = factory.Faker('random_element', elements=['MATUTINO', 'VESPERTINO', 'NOTURNO', 'INTEGRAL'])
    capacidade = factory.Faker('random_int', min=10, max=50)
    local = factory.Faker('address')
    data_inicio = factory.LazyFunction(lambda: timezone.now().date() + timedelta(days=10))
    data_fim = factory.LazyFunction(lambda: timezone.now().date() + timedelta(days=90))


    