"""
Arquivo: factories.py
Caminho: apps/selecao/tests/factories.py
Factories para o app Selecao
Data: 27 de março de 2026
"""

import factory
from django.utils import timezone
from datetime import timedelta

from apps.interessados.tests.factories import InteressadoFactory as BaseInteressadoFactory
from apps.eventos.models import Evento, Status, Criterio, EventoCriterio
from ..models import StatusInscricao, Inscricao, Classificacao, InscricaoCriterioAtendido
from apps.interessados.models import gerar_hash_cpf

class InteressadoFactory(BaseInteressadoFactory):
    """Factory de Interessado com CPF sequencial único."""
    cpf = factory.Sequence(lambda n: f'{n:011d}')
    cpf_hash = factory.Sequence(lambda n: gerar_hash_cpf(f'{n:011d}'))


class StatusInscricaoFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = StatusInscricao
        django_get_or_create = ('nome',)

    nome = factory.Sequence(lambda n: f'StatusInscricao {n}')
    cor = factory.Faker('hex_color')
    ordem = factory.Faker('random_int', min=0, max=10)


class StatusFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Status
        django_get_or_create = ('nome',)

    nome = factory.Sequence(lambda n: f'EventoStatus {n}')
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

    nome = factory.Faker('word')
    descricao = factory.Faker('text')
    status = factory.SubFactory(StatusFactory, nome='INSCRICOES_ABERTAS')
    total_vagas = factory.Faker('random_int', min=5, max=20)
    data_inicio_inscricao = factory.LazyFunction(lambda: timezone.now() - timedelta(days=7))
    data_fim_inscricao = factory.LazyFunction(lambda: timezone.now() + timedelta(days=7))
    data_inicio_evento = factory.LazyFunction(lambda: timezone.now().date() + timedelta(days=10))
    data_fim_evento = factory.LazyFunction(lambda: timezone.now().date() + timedelta(days=20))


class EventoCriterioFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = EventoCriterio

    evento = factory.SubFactory(EventoFactory)
    criterio = factory.SubFactory(CriterioFactory)
    prioridade = factory.Sequence(lambda n: n)
    ativo = True


class InscricaoFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Inscricao

    interessado = factory.SubFactory(InteressadoFactory)
    evento = factory.SubFactory(EventoFactory)
    status = factory.LazyAttribute(lambda o: StatusInscricaoFactory(nome='Pendente'))
    data_inscricao = factory.LazyFunction(timezone.now)


class ClassificacaoFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Classificacao

    inscricao = factory.SubFactory(InscricaoFactory)
    pontuacao_total = factory.Faker('random_int', min=0, max=100)
    posicao = None
    classificado = False
    lista_espera = False
    processado_em = factory.LazyFunction(timezone.now)


class InscricaoCriterioAtendidoFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = InscricaoCriterioAtendido

    inscricao = factory.SubFactory(InscricaoFactory)
    criterio = factory.SubFactory(CriterioFactory)
    pontos_atribuidos = factory.Faker('random_int', min=1, max=20)
    validado = False


