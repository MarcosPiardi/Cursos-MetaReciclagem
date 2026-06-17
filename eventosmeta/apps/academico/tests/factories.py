"""
Arquivo: factories.py
Caminho: apps/academico/tests/factories.py
Finalidade: Factories para criacao de objetos de teste relacionados ao app academico
Atualizacoes:
 - 29/05/2026 - Criacao do arquivo
 - 09/06/2026 - Adicionada AvaliacaoFactory e MatriculaFactory
 - 09/06/2006 - Corrigida MatriculaFactory para garantir consistencia
 - 17/06/2026 - Adicionado django_get_or_create em StatusMatriculaFactory
"""

import factory
from decimal import Decimal
from django.utils import timezone
from datetime import timedelta

from apps.academico.models import StatusMatricula, Matricula, Avaliacao
from apps.eventos.models import Turma
from apps.selecao.tests.factories import InscricaoFactory

class StatusMatriculaFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = StatusMatricula
        django_get_or_create = ("nome",)

    nome = factory.Sequence(lambda n: f"Status {n}")
    cor = "#007bff"
    ordem = factory.Sequence(lambda n: n)

class TurmaFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Turma

    nome = factory.Sequence(lambda n: f"Turma {n}")
    evento = factory.SubFactory("apps.eventos.tests.factories.EventoFactory")
    capacidade = 30
    data_inicio = factory.LazyFunction(lambda: timezone.now().date())
    data_fim = factory.LazyFunction(
        lambda: (timezone.now() + timedelta(days=30)).date()
    )

class MatriculaFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Matricula

    inscricao = factory.SubFactory(
        InscricaoFactory,
        evento=factory.SelfAttribute("..turma.evento"),
    )

    @factory.lazy_attribute
    def turma(self):
        return TurmaFactory()

    interessado = factory.SelfAttribute("inscricao.interessado")
    status = factory.SubFactory(StatusMatriculaFactory)
    observacoes = ""

class AvaliacaoFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Avaliacao

    matricula = factory.SubFactory(MatriculaFactory)
    nota_final = Decimal("8.5")
    frequencia = Decimal("90.0")
    aprovado = True
    observacoes = ""



    