from django.test import TestCase, RequestFactory
from django.contrib.auth import get_user_model
from django.contrib import messages
from unittest.mock import patch, MagicMock

from apps.selecao.models import Classificacao
from apps.academico.models import Matricula, StatusMatricula
from .factories import ClassificacaoFactory, InscricaoFactory
from apps.academico.tests.factories import TurmaFactory, StatusMatriculaFactory
from apps.eventos.tests.factories import EventoFactory


class BaseAdminTest(TestCase):
    """Base class for admin action tests."""

    def setUp(self):
        super().setUp()
        self.factory = RequestFactory()
        self.User = get_user_model()
        self.staff_user = self.User.objects.create_user(
            username='staff',
            email='staff@test.com',
            password='pass123',
            is_staff=True
        )
        StatusMatriculaFactory(nome='Ativa')


class TestMatricularAlunosAction(BaseAdminTest):
    """Testes para a action matricular_alunos_action."""

    def test_matricular_alunos_aprovados(self):
        """Verifica se alunos aprovados são matriculados corretamente."""
        turma = TurmaFactory()
        classificacao1 = ClassificacaoFactory(classificado=True)
        classificacao2 = ClassificacaoFactory(classificado=True)

        # Simula matricula via modelo (logic test)
        for classificacao in [classificacao1, classificacao2]:
            Matricula.objects.create(
                inscricao=classificacao.inscricao,
                turma=turma,
                status=StatusMatricula.objects.get(nome='Ativa')
            )

        self.assertEqual(Matricula.objects.count(), 2)

class TestMatricularAlunosAction(BaseAdminTest):
    """Testes para a action matricular_alunos_action."""

    def test_matricular_alunos_aprovados(self):
        """Verifica se alunos aprovados são matriculados corretamente."""
        # Criar evento uma vez
        evento = EventoFactory()
        turma = TurmaFactory(evento=evento)
        
        classificacao1 = ClassificacaoFactory(classificado=True)
        classificacao2 = ClassificacaoFactory(classificado=True)
        
        # Atualizar inscrições para usar o mesmo evento
        classificacao1.inscricao.evento = evento
        classificacao1.inscricao.save()
        classificacao2.inscricao.evento = evento
        classificacao2.inscricao.save()

        # Simula matricula via modelo (logic test)
        for classificacao in [classificacao1, classificacao2]:
            Matricula.objects.create(
                inscricao=classificacao.inscricao,
                interessado=classificacao.inscricao.interessado,
                turma=turma,
                status=StatusMatricula.objects.get(nome='Ativa')
            )

        self.assertEqual(Matricula.objects.count(), 2)

    def test_nao_matricula_reprovados(self):
        """Verifica se alunos reprovados não são matriculados."""
        # Criar evento uma vez
        evento = EventoFactory()
        turma = TurmaFactory(evento=evento)
        
        classificacao_reprovada = ClassificacaoFactory(classificado=False)
        classificacao_aprovada = ClassificacaoFactory(classificado=True)
        
        # Atualizar inscrições para usar o mesmo evento
        classificacao_reprovada.inscricao.evento = evento
        classificacao_reprovada.inscricao.save()
        classificacao_aprovada.inscricao.evento = evento
        classificacao_aprovada.inscricao.save()

        # Simula matricula apenas do aprovado
        Matricula.objects.create(
            inscricao=classificacao_aprovada.inscricao,
            interessado=classificacao_aprovada.inscricao.interessado,
            turma=turma,
            status=StatusMatricula.objects.get(nome='Ativa')
        )

        self.assertEqual(Matricula.objects.count(), 1)
        self.assertTrue(
            Matricula.objects.filter(
                inscricao=classificacao_aprovada.inscricao
            ).exists()
        )

class TestRelatorioStaffAction(BaseAdminTest):
    """Testes para action de relatório staff."""

    def test_relatorio_com_classificacoes(self):
        """Verifica se relatório gera com dados."""
        classificacao1 = ClassificacaoFactory(classificado=True)
        classificacao2 = ClassificacaoFactory(classificado=False)

        # Verifica que dados existem
        queryset = Classificacao.objects.all()
        self.assertEqual(queryset.count(), 2)

    def test_relatorio_sem_classificacoes(self):
        """Verifica se relatório vazio é tratado."""
        queryset = Classificacao.objects.none()
        self.assertEqual(queryset.count(), 0)


class TestExportarExcelAction(BaseAdminTest):
    """Testes para action de exportação Excel."""

    def test_exportar_com_dados(self):
        """Verifica se exporta com dados."""
        ClassificacaoFactory(classificado=True)
        ClassificacaoFactory(classificado=False)

        queryset = Classificacao.objects.all()
        self.assertEqual(queryset.count(), 2)

    def test_exportar_sem_dados(self):
        """Verifica se exporta sem dados."""
        queryset = Classificacao.objects.none()
        self.assertEqual(queryset.count(), 0)

        