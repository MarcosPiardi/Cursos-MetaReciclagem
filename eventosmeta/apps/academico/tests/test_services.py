"""
Arquivo: test_services.py
Caminho: apps/academico/tests/test_services.py
Atualizações
28/05/2026 - Criação do arquivo 
"""


from django.test import TestCase
from django.core.exceptions import ValidationError
from apps.academico.services import MatriculaService
from .factories import (
    MatriculaFactory,
    TurmaFactory,
    StatusMatriculaFactory,
    InteressadoFactory,
)


class TestMatriculaService(TestCase):
    def setUp(self):
        self.status_ativa = StatusMatriculaFactory(nome="Ativa")
        self.status_concluida = StatusMatriculaFactory(nome="Concluída")
        self.status_cancelada = StatusMatriculaFactory(nome="Cancelada")

        self.turma_com_vagas = TurmaFactory(capacidade=5)
        self.turma_sem_vagas = TurmaFactory(capacidade=1)

    # --- Disponibilidade ---

    def test_verificar_disponibilidade_turma_com_vagas(self):
        disponivel, vagas = MatriculaService.verificar_disponibilidade_turma(
            self.turma_com_vagas
        )
        self.assertTrue(disponivel)
        self.assertEqual(vagas, 5)

    def test_verificar_disponibilidade_turma_lotada(self):
        MatriculaFactory(turma=self.turma_sem_vagas, status=self.status_ativa)
        disponivel, vagas = MatriculaService.verificar_disponibilidade_turma(
            self.turma_sem_vagas
        )
        self.assertFalse(disponivel)
        self.assertEqual(vagas, 0)

    # --- Avaliacao ---

    def test_avaliar_aluno_aprovado(self):
        matricula = MatriculaFactory(status=self.status_ativa)
        avaliacao = MatriculaService.avaliar_aluno(
            matricula=matricula,
            nota_final=8.5,
            frequencia=90.0,
            observacoes="Bom desempenho",
        )
        self.assertEqual(avaliacao.nota_final, 8.5)
        self.assertEqual(avaliacao.frequencia, 90.0)
        self.assertTrue(avaliacao.aprovado)

    def test_avaliar_aluno_reprovado_por_nota(self):
        matricula = MatriculaFactory(status=self.status_ativa)
        avaliacao = MatriculaService.avaliar_aluno(
            matricula=matricula,
            nota_final=5.0,
            frequencia=70.0,
        )
        self.assertFalse(avaliacao.aprovado)

    def test_avaliar_aluno_reprovado_por_frequencia(self):
        matricula = MatriculaFactory(status=self.status_ativa)
        avaliacao = MatriculaService.avaliar_aluno(
            matricula=matricula,
            nota_final=8.0,
            frequencia=50.0,
        )
        self.assertFalse(avaliacao.aprovado)

    def test_avaliar_aluno_nota_invalida(self):
        matricula = MatriculaFactory()
        with self.assertRaises(ValidationError):
            MatriculaService.avaliar_aluno(matricula, 11.0, 90.0)

    def test_avaliar_aluno_frequencia_invalida(self):
        matricula = MatriculaFactory()
        with self.assertRaises(ValidationError):
            MatriculaService.avaliar_aluno(matricula, 8.0, 150.0)

    # --- Relatorio ---

    def test_gerar_relatorio_turma(self):
        interessado1 = InteressadoFactory()
        interessado2 = InteressadoFactory()

        matricula1 = MatriculaFactory(
            turma=self.turma_com_vagas, interessado=interessado1
        )
        matricula2 = MatriculaFactory(
            turma=self.turma_com_vagas, interessado=interessado2
        )

        MatriculaService.avaliar_aluno(matricula1, 8.5, 90.0)
        MatriculaService.avaliar_aluno(matricula2, 6.0, 75.0)

        relatorio = MatriculaService.gerar_relatorio_turma(
            self.turma_com_vagas
        )

        self.assertEqual(relatorio["total_matriculas"], 2)
        self.assertEqual(relatorio["total_avaliacoes"], 2)
        self.assertEqual(relatorio["aprovados"], 1)
        self.assertEqual(relatorio["reprovados"], 1)
        self.assertIn("media_nota", relatorio)
        self.assertIn("taxa_aprovacao", relatorio)


