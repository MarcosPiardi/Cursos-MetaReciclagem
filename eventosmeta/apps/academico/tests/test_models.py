from django.test import TestCase
from django.db import IntegrityError
from django.utils import timezone
from apps.academico.models import StatusMatricula, Matricula
from .factories import StatusMatriculaFactory, MatriculaFactory, InteressadoFactory, TurmaFactory

class TestStatusMatricula(TestCase):
    def test_status_criado_corretamente(self):
        status = StatusMatriculaFactory(nome='Ativo', cor='#00FF00', ordem=1)
        self.assertEqual(status.nome, 'Ativo')
        self.assertEqual(status.cor, '#00FF00')
        self.assertEqual(status.ordem, 1)

    def test_status_get_or_create_evita_duplicata(self):
        StatusMatriculaFactory(nome='Ativo')
        StatusMatriculaFactory(nome='Ativo')
        self.assertEqual(StatusMatricula.objects.filter(nome='Ativo').count(), 1)

class TestMatricula(TestCase):
    def test_matricula_criada_corretamente(self):
        matricula = MatriculaFactory()
        self.assertIsNotNone(matricula.numero_matricula)
        self.assertIsNotNone(matricula.turma)
        self.assertIsNotNone(matricula.interessado)
        self.assertIsNotNone(matricula.status)
        self.assertIsNotNone(matricula.data_matricula)

    def test_matricula_data_preenchida(self):
        matricula = MatriculaFactory()
        self.assertIsNotNone(matricula.data_matricula)
        self.assertLessEqual(matricula.data_matricula, timezone.now())

    def test_matricula_status_ativo_default(self):
        matricula = MatriculaFactory()
        self.assertEqual(matricula.status.nome, 'Ativa')

    def test_matricula_unique_together_turma_interessado(self):
        turma = TurmaFactory()
        interessado = InteressadoFactory()
        MatriculaFactory(turma=turma, interessado=interessado)
        with self.assertRaises(IntegrityError):
            MatriculaFactory(turma=turma, interessado=interessado)

            