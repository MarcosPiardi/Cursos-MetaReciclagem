"""
Arquivo: test_models.py
Caminho: apps/academico/tests/test_models.py
Atualizações
28/05/2026 - Criação do arquivo 
"""


from django.test import TestCase
from django.db import IntegrityError
from django.utils import timezone
from apps.academico.models import StatusMatricula, Matricula
from .factories import StatusMatriculaFactory, MatriculaFactory, InteressadoFactory, TurmaFactory


class TestStatusMatriculaModel(TestCase):
    """Testes do model StatusMatricula"""

    def test_status_criado_corretamente(self):
        status = StatusMatriculaFactory(nome='Ativo', cor='#00FF00', ordem=1)
        self.assertEqual(status.nome, 'Ativo')
        self.assertEqual(status.cor, '#00FF00')
        self.assertEqual(status.ordem, 1)

    def test_status_nome_unique_no_banco(self):
        """Testa a constraint real, nao o comportamento da factory"""
        StatusMatricula.objects.create(nome='Ativo', cor='#000', ordem=1)
        with self.assertRaises(IntegrityError):
            StatusMatricula.objects.create(nome='Ativo', cor='#FFF', ordem=2)


class TestMatriculaModel(TestCase):
    """Testes do model Matricula"""

    def test_matricula_criada_corretamente(self):
        matricula = MatriculaFactory()
        self.assertIsNotNone(matricula.numero_matricula)
        self.assertIsNotNone(matricula.turma)
        self.assertIsNotNone(matricula.interessado)
        self.assertIsNotNone(matricula.status)
        self.assertIsNotNone(matricula.data_matricula)
        self.assertLessEqual(matricula.data_matricula, timezone.now())

    def test_matricula_unique_together_turma_interessado(self):
        """
        unique_together = ['turma', 'interessado']
        Mesma turma + mesmo interessado = violacao
        """
        turma = TurmaFactory()
        interessado = InteressadoFactory()
        MatriculaFactory(turma=turma, interessado=interessado)
        with self.assertRaises(IntegrityError):
            MatriculaFactory(turma=turma, interessado=interessado)


            
            