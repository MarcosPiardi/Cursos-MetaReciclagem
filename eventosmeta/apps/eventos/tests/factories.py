"""
Arquivo: factories.py
Caminho: apps/eventos/tests/factories.py
Finalidade: Fornecer dados de teste para os modelos do app eventos usando Factory Boy
Atualizações:
 - 15/05/2026 - Criação do arquivo com factories para os modelos do app eventos, utilizando Factory
 - 26/05/2026 - Adicionando factory
 - 03/06/2026 - Ajustando factories para refletir as relações entre os modelos e garantir a criação de dados consistentes para os testes.
 - 09/06/2026 - Correção de choices e validações dos models, garantindo que as factories gerem dados válidos e coerentes com as regras de negócio definidas nos modelos.
 """


from datetime import time, timedelta

import factory
from django.utils import timezone

from apps.eventos.models import (
    Status,
    Criterio,
    Evento,
    EventoCriterio,
    Turma,
    Horario,
)


# ============================================================
# STATUS
# ============================================================

class StatusFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Status
        django_get_or_create = ("nome",)

    nome = factory.Sequence(lambda n: f"Status {n}")
    cor = factory.Faker("hex_color")
    ordem = factory.Sequence(lambda n: n + 1)


# ============================================================
# CRITERIO
# ============================================================

class CriterioFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Criterio

    tipo_criterio = factory.Iterator(
        [
            "PONTUACAO",
            "ORDENACAO",
        ]
    )

    codigo = factory.Sequence(
        lambda n: f"CRIT-{n:03d}"
    )

    nome = factory.Faker(
        "sentence",
        nb_words=3
    )

    descricao = factory.Faker("text")

    pontos = factory.Faker(
        "random_int",
        min=0,
        max=20
    )

    categoria = factory.Iterator(
        [
            "ORDENACAO",
            "CRONOLÓGICA",
            "IDADE",
            "VULNERABILIDADE",
            "FAIXA_ETARIA",
            "ESCOLARIDADE",
            "COTA_RACIAL",
        ]
    )

    ativo = True


# ============================================================
# EVENTO
# ============================================================

class EventoFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Evento

    nome = factory.Faker("catch_phrase")

    descricao = factory.Faker("paragraph")

    status = factory.SubFactory(StatusFactory)

    total_vagas = factory.Faker(
        "random_int",
        min=10,
        max=100
    )

    data_inicio_inscricao = factory.LazyFunction(
        timezone.now
    )

    data_fim_inscricao = factory.LazyAttribute(
        lambda o: o.data_inicio_inscricao + timedelta(days=5)
    )

    data_inicio_evento = factory.LazyAttribute(
        lambda o: o.data_fim_inscricao + timedelta(days=1)
    )

    data_fim_evento = factory.LazyAttribute(
        lambda o: o.data_inicio_evento + timedelta(days=2)
    )


# ============================================================
# EVENTO CRITERIO
# ============================================================

class EventoCriterioFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = EventoCriterio

    evento = factory.SubFactory(EventoFactory)

    criterio = factory.SubFactory(CriterioFactory)

    prioridade = factory.Faker(
        "random_int",
        min=1,
        max=5
    )

    ativo = True


# ============================================================
# TURMA
# ============================================================

class TurmaFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Turma

    evento = factory.SubFactory(EventoFactory)

    nome = factory.Sequence(
        lambda n: f"Turma {n}"
    )

    turno = factory.Iterator(
        [
            "MATUTINO",
            "VESPERTINO",
            "NOTURNO",
            "INTEGRAL",
        ]
    )

    capacidade = factory.Faker(
        "random_int",
        min=20,
        max=50
    )

    local = factory.Faker("street_address")

    data_inicio = factory.LazyFunction(
        lambda: timezone.now().date()
    )

    data_fim = factory.LazyAttribute(
        lambda o: o.data_inicio + timedelta(days=30)
    )


# ============================================================
# HORARIO
# ============================================================

class HorarioFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Horario

    turma = factory.SubFactory(TurmaFactory)

    dia_semana = factory.Iterator(
        [0, 1, 2, 3, 4, 5, 6]
    )

    hora_inicio = factory.LazyFunction(
        lambda: time(8, 0)
    )

    hora_fim = factory.LazyFunction(
        lambda: time(10, 0)
    )