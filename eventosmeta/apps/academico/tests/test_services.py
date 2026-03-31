from django.test import TestCase
from django.core.exceptions import ValidationError
from django.utils import timezone
from apps.academico.services import MatriculaService
from apps.academico.models import Matricula, StatusMatricula, Avaliacao
from apps.eventos.models import Turma
from apps.selecao.models import Classificacao, Inscricao, StatusInscricao
from .factories import (
    MatriculaFactory, 
    TurmaFactory, 
    StatusMatriculaFactory,
    InteressadoFactory,
    InscricaoFactory
)


class TestMatriculaService(TestCase):
    def setUp(self):
        # Criar status necessários
        self.status_ativa = StatusMatriculaFactory(nome='Ativa')
        self.status_concluida = StatusMatriculaFactory(nome='Concluída')
        self.status_cancelada = StatusMatriculaFactory(nome='Cancelada')
        
        # Criar turmas (sem matrículas no setUp para evitar CPF duplicado)
        self.turma_com_vagas = TurmaFactory(capacidade=5)
        self.turma_sem_vagas = TurmaFactory(capacidade=1)

    def test_verificar_disponibilidade_turma_com_vagas(self):
        disponivel, vagas_restantes = MatriculaService.verificar_disponibilidade_turma(self.turma_com_vagas)
        self.assertTrue(disponivel)
        self.assertEqual(vagas_restantes, 5)

    def test_verificar_disponibilidade_turma_sem_vagas(self):
        # Criar matrícula apenas quando necessário
        MatriculaFactory(turma=self.turma_sem_vagas, status=self.status_ativa)
        disponivel, vagas_restantes = MatriculaService.verificar_disponibilidade_turma(self.turma_sem_vagas)
        self.assertFalse(disponivel)
        self.assertEqual(vagas_restantes, 0)

    def test_avaliar_aluno_aprova_com_nota_alta(self):
        matricula = MatriculaFactory(status=self.status_ativa)
        avaliacao = MatriculaService.avaliar_aluno(
            matricula=matricula,
            nota_final=8.5,
            frequencia=90.0,
            observacoes='Bom desempenho'
        )
        self.assertIsNotNone(avaliacao)
        self.assertEqual(avaliacao.nota_final, 8.5)
        self.assertEqual(avaliacao.frequencia, 90.0)
        self.assertTrue(avaliacao.aprovado)

    def test_avaliar_aluno_reprova_com_nota_baixa(self):
        matricula = MatriculaFactory(status=self.status_ativa)
        avaliacao = MatriculaService.avaliar_aluno(
            matricula=matricula,
            nota_final=5.0,
            frequencia=70.0,
            observacoes='Desempenho insuficiente'
        )
        self.assertIsNotNone(avaliacao)
        self.assertEqual(avaliacao.nota_final, 5.0)
        self.assertEqual(avaliacao.frequencia, 70.0)
        self.assertFalse(avaliacao.aprovado)

    def test_avaliar_aluno_reprova_frequencia_baixa(self):
        matricula = MatriculaFactory(status=self.status_ativa)
        avaliacao = MatriculaService.avaliar_aluno(
            matricula=matricula,
            nota_final=8.0,
            frequencia=50.0
        )
        self.assertFalse(avaliacao.aprovado)

    def test_gerar_relatorio_turma(self):
        # Criar matrículas com interessados DIFERENTES
        # Força criação com CPFs explícitos para evitar conflito de sequência
        interessado1 = InteressadoFactory(cpf='10000000001')
        interessado2 = InteressadoFactory(cpf='10000000002')
    
        matricula1 = MatriculaFactory(turma=self.turma_com_vagas, interessado=interessado1)
        matricula2 = MatriculaFactory(turma=self.turma_com_vagas, interessado=interessado2)
    
        MatriculaService.avaliar_aluno(matricula1, 8.5, 90.0)
        MatriculaService.avaliar_aluno(matricula2, 6.0, 75.0)
    
        relatorio = MatriculaService.gerar_relatorio_turma(self.turma_com_vagas)
    
        self.assertEqual(relatorio['total_matriculas'], 2)
        self.assertEqual(relatorio['total_avaliacoes'], 2)
        self.assertEqual(relatorio['aprovados'], 1)     
        self.assertEqual(relatorio['reprovados'], 1)
        self.assertIn('media_nota', relatorio)
        self.assertIn('taxa_aprovacao', relatorio)


    def test_avaliar_aluno_nota_invalida(self):
        matricula = MatriculaFactory()
        with self.assertRaises(ValidationError):
            MatriculaService.avaliar_aluno(matricula, 11.0, 90.0)

    def test_avaliar_aluno_frequencia_invalida(self):
        matricula = MatriculaFactory()
        with self.assertRaises(ValidationError):
            MatriculaService.avaliar_aluno(matricula, 8.0, 150.0)

