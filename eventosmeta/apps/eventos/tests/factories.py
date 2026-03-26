from factory import SubFactory
from ..models import Evento, Turma, Status, Criterio

class StatusFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Status

    nome = factory.Iterator(['ABERTO', 'FECHADO', 'EM_ANDAMENTO'])

class CriterioFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Criterio

    nome = factory.Faker('word')
    pontos = factory.RandomInt(5, 50)
    ativo = True
    tipo = factory.RandomChoice(['AUTOMATICO', 'MANUAL'])

class EventoFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Evento

    nome = factory.Faker('sentence', nb_words=4)
    descricao = factory.Faker('paragraph', nb_sentences=3)
    data_inicio = factory.LazyAttribute(lambda obj: timezone.now() + timezone.timedelta(days=1))
    data_fim = factory.LazyAttribute(lambda obj: timezone.now() + timezone.timedelta(days=7))
    vagas = factory.RandomInt(10, 100)
    status = SubFactory(StatusFactory)

class TurmaFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Turma

    evento = SubFactory(EventoFactory)
    capacidade = factory.RandomInt(20, 50)
    horario = factory.Faker('time')

    