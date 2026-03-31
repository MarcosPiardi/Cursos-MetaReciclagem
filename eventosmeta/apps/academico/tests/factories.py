import factory
from decimal import Decimal
from django.utils import timezone

from apps.academico.models import StatusMatricula, Matricula, Avaliacao
from apps.eventos.tests.factories import TurmaFactory
from apps.interessados.tests.factories import InteressadoFactory
from apps.selecao.tests.factories import InscricaoFactory


class StatusMatriculaFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = StatusMatricula
        django_get_or_create = ('nome',)

    nome = factory.Sequence(lambda n: f'StatusMatricula {n}')
    cor = factory.Faker('hex_color')
    ordem = factory.Faker('random_int', min=0, max=10)


class MatriculaFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Matricula

    numero_matricula = factory.Sequence(lambda n: f'{timezone.now().year}{n:04d}')
    turma = factory.SubFactory(TurmaFactory)
    interessado = factory.SubFactory(InteressadoFactory)
    inscricao = factory.SubFactory(
        InscricaoFactory,
        interessado=factory.SelfAttribute('..interessado'),
        evento=factory.SelfAttribute('..turma.evento')
    )
    status = factory.SubFactory(StatusMatriculaFactory, nome='Ativa')
    observacoes = factory.Faker('text')


class AvaliacaoFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Avaliacao

    matricula = factory.SubFactory(MatriculaFactory)
    nota_final = factory.Faker('pydecimal', left_digits=1, right_digits=2, min_value=Decimal('0.00'), max_value=Decimal('10.00'))
    frequencia = factory.Faker('pydecimal', left_digits=2, right_digits=2, min_value=Decimal('0.00'), max_value=Decimal('100.00'))
    aprovado = factory.LazyAttribute(lambda o: o.nota_final >= Decimal('7.00') and o.frequencia >= Decimal('75.00'))
    observacoes = factory.Faker('text')
    certificado_emitido = False
    data_emissao_certificado = None
    avaliado_em = factory.LazyFunction(timezone.now)

    