from factory import SubFactory
from ..models import Inscricao, Classificacao, CriterioAtendido
from apps.interessados.tests.factories import InteressadoFactory
from apps.eventos.tests.factories import EventoFactory  # Cross-app

class InscricaoFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Inscricao

    interessado = SubFactory(InteressadoFactory)
    evento = SubFactory(EventoFactory)
    status = 'PENDENTE'
    data_inscricao = factory.LazyAttribute(lambda obj: timezone.now())

class ClassificacaoFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Classificacao

    inscricao = SubFactory(InscricaoFactory)
    pontuacao = factory.RandomInt(0, 100)
    status = 'CLASSIFICADO'
    data_classificacao = factory.LazyAttribute(lambda obj: timezone.now())

class CriterioAtendidoFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = CriterioAtendido

    inscricao = SubFactory(InscricaoFactory)
    criterio = factory.RandomInt(1, 10)  # Assumindo ID de criterio
    pontuacao_criterio = factory.RandomInt(0, 20)

    