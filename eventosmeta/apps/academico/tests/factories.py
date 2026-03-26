from factory import SubFactory
from ..models import Matricula, Avaliacao
from apps.selecao.tests.factories import InscricaoFactory  # Cross-app

class MatriculaFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Matricula

    inscricao = SubFactory(InscricaoFactory)
    status = 'MATRICULADO'
    numero_matricula = factory.Sequence(lambda n: f'MAT-{n:03d}')
    data_matricula = factory.LazyAttribute(lambda obj: timezone.now())

class AvaliacaoFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Avaliacao

    matricula = SubFactory(MatriculaFactory)
    nota = factory.RandomInt(0, 100)
    frequencia = factory.RandomInt(70, 100)  # % frequência
    aprovado = factory.LazyAttribute(lambda obj: obj.nota >= 70 and obj.frequencia >= 75)

    