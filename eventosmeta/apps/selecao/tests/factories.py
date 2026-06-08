"""
Arquivo: factories.py
caminho: apps/selecao/tests/factories.py
Finalidade: Definir factories para testes do app seleção.

Histórico de Alterações:
- 15/05/2026 - Inclusão de cabeçalho 
"""

import factory
import hashlib
from django.utils import timezone
from datetime import timedelta

from apps.interessados.tests.factories import InteressadoFactory as BaseInteressadoFactory
from apps.eventos.models import Evento, Status, Criterio, EventoCriterio
from apps.eventos.tests.factories import EventoFactory, StatusFactory, CriterioFactory
from ..models import StatusInscricao, Inscricao, Classificacao, InscricaoCriterioAtendido


def gerar_hash_cpf(cpf):
    """Gera um hash para o CPF."""
    return hashlib.md5(cpf.encode()).hexdigest()


class InteressadoFactory(BaseInteressadoFactory):
    cpf = factory.Sequence(lambda n: f'{n:011d}')
    cpf_hash = factory.Sequence(lambda n: gerar_hash_cpf(f'{n:011d}'))
    email = factory.Sequence(lambda n: f'interessado{n}@teste.com')  # EMAIL SEQUENCIAL


class StatusInscricaoFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = StatusInscricao
        django_get_or_create = ('nome',)

    nome = factory.Sequence(lambda n: f'StatusInscricao {n}')
    cor = factory.Faker('hex_color')
    ordem = factory.Faker('random_int', min=0, max=10)


class InscricaoFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Inscricao

    interessado = factory.SubFactory(InteressadoFactory)
    evento = factory.SubFactory(EventoFactory)
    status = factory.SubFactory(StatusInscricaoFactory, nome='Pendente')
    data_inscricao = factory.LazyFunction(timezone.now)


class ClassificacaoFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Classificacao

    inscricao = factory.SubFactory(InscricaoFactory)
    pontuacao_total = factory.Faker('random_int', min=0, max=100)
    posicao = 1
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

    