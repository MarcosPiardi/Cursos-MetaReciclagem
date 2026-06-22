"""
Arquivo: factories.py
caminho: apps/selecao/tests/factories.py
Finalidade: Definir factories para testes do app selecao.

Atualizacoes:
 - 15/05/2026 - Criacao do arquivo
 - 15/05/2026 - Inclusao de cabecalho
 - 10/06/2026 - Adicao de factory para StatusInscricao, Inscricao, Classificacao e InscricaoCriterioAtendido
 - 18/06/2026 - Corrigido ClassificacaoFactory: classificado e lista_espera
                padrao False para nao violar validacao mutuamente exclusiva
"""

import factory
from decimal import Decimal
from django.utils import timezone
from factory.django import DjangoModelFactory
from apps.selecao.models import StatusInscricao, Inscricao, Classificacao, InscricaoCriterioAtendido
from apps.interessados.tests.factories import InteressadoFactory
from apps.eventos.tests.factories import EventoFactory, CriterioFactory

class StatusInscricaoFactory(DjangoModelFactory):
    class Meta:
        model = StatusInscricao
        django_get_or_create = ('nome',)

    nome = factory.Faker('word')
    cor = factory.Faker('hex_color')
    ordem = factory.Sequence(lambda n: n)

class InscricaoFactory(DjangoModelFactory):
    class Meta:
        model = Inscricao

    interessado = factory.SubFactory(InteressadoFactory)
    evento = factory.SubFactory(EventoFactory)
    status = factory.SubFactory(StatusInscricaoFactory, nome='Pendente')
    observacoes = factory.Faker('text', max_nb_chars=200)

class ClassificacaoFactory(DjangoModelFactory):
    class Meta:
        model = Classificacao

    inscricao = factory.SubFactory(InscricaoFactory)
    posicao = factory.Faker('random_int', min=1, max=100)
    pontuacao_total = factory.Faker('pydecimal', left_digits=2, right_digits=2, min_value=0, max_value=100)
    classificado = False
    lista_espera = False
    processado_em = factory.LazyFunction(timezone.now)
    atualizado_em = factory.LazyFunction(timezone.now)

class InscricaoCriterioAtendidoFactory(DjangoModelFactory):
    class Meta:
        model = InscricaoCriterioAtendido

    inscricao = factory.SubFactory(InscricaoFactory)
    criterio = factory.SubFactory(CriterioFactory)
    pontos_atribuidos = factory.Faker('random_int', min=1, max=20)
    validado = factory.Faker('boolean')
    observacao_validacao = factory.Faker('sentence')


    