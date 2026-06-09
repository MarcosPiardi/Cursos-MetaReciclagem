"""
Arquivo: test_services.py
Caminho: apps/academico/tests/test_services.py
Descrição: Testes para MatriculaService (disponibilidade, avaliação, relatório)
Atualizações
 - 28/05/2026 - Criação do arquivo 
 - 09/06/2026 - Adicionados testes para limites de nota e frequência em avaliar_aluno()
 - 09/06/2026 - Corrigido setup_method do relatório para incluir status necessários pelo service
"""

import pytest
from django.core.exceptions import ValidationError

from apps.academico.services import MatriculaService
from apps.academico.models import Avaliacao
from .factories import MatriculaFactory, TurmaFactory, StatusMatriculaFactory

@pytest.mark.django_db
class TestVerificacaoDisponibilidade:
    """Testes para verificar_disponibilidade_turma()"""

    def setup_method(self):
        self.status_ativa = StatusMatriculaFactory(nome='Ativa')

    def test_verificar_disponibilidade_turma_com_vagas(self):
        """Turma com 5 vagas e 0 matriculados deve retornar (True, 5)"""
        turma = TurmaFactory(capacidade=5)
        disponivel, vagas = MatriculaService.verificar_disponibilidade_turma(turma)
        assert disponivel is True
        assert vagas == 5

    def test_verificar_disponibilidade_turma_lotada(self):
        """Turma com 1 vaga e 1 matriculado deve retornar (False, 0)"""
        turma = TurmaFactory(capacidade=1)
        MatriculaFactory(turma=turma, status=self.status_ativa)
        disponivel, vagas = MatriculaService.verificar_disponibilidade_turma(turma)
        assert disponivel is False
        assert vagas == 0

    def test_verificar_disponibilidade_turma_parcial(self):
        """Turma com 5 vagas e 2 matriculados deve retornar (True, 3)"""
        turma = TurmaFactory(capacidade=5)
        MatriculaFactory.create_batch(2, turma=turma, status=self.status_ativa)
        disponivel, vagas = MatriculaService.verificar_disponibilidade_turma(turma)
        assert disponivel is True
        assert vagas == 3

    def test_verificar_disponibilidade_turma_exatamente_cheia(self):
        """Turma com 3 vagas e 3 matriculados deve retornar (False, 0)"""
        turma = TurmaFactory(capacidade=3)
        MatriculaFactory.create_batch(3, turma=turma, status=self.status_ativa)
        disponivel, vagas = MatriculaService.verificar_disponibilidade_turma(turma)
        assert disponivel is False
        assert vagas == 0


@pytest.mark.django_db
class TestAvaliacaoAluno:
    """Testes para avaliar_aluno()"""

    def setup_method(self):
        self.status_ativa = StatusMatriculaFactory(nome='Ativa')
        self.status_concluida = StatusMatriculaFactory(nome='Concluída')
        self.status_cancelada = StatusMatriculaFactory(nome='Cancelada')
        self.matricula = MatriculaFactory(status=self.status_ativa)

    def test_avaliar_aluno_aprovado(self):
        """Nota 8.5 e freq 90% deve resultar em aprovado=True"""
        av = MatriculaService.avaliar_aluno(self.matricula, 8.5, 90.0)
        assert av.aprovado is True
        assert av.nota_final == 8.5
        assert av.frequencia == 90.0

    def test_avaliar_aluno_reprovado_por_nota(self):
        """Nota 5.0 e freq 70% deve resultar em aprovado=False"""
        av = MatriculaService.avaliar_aluno(self.matricula, 5.0, 70.0)
        assert av.aprovado is False

    def test_avaliar_aluno_reprovado_por_frequencia(self):
        """Nota 8.0 e freq 50% deve resultar em aprovado=False"""
        av = MatriculaService.avaliar_aluno(self.matricula, 8.0, 50.0)
        assert av.aprovado is False

    def test_avaliar_aluno_nota_invalida(self):
        """Nota 11.0 deve lançar ValidationError"""
        with pytest.raises(ValidationError):
            MatriculaService.avaliar_aluno(self.matricula, 11.0, 80.0)

    def test_avaliar_aluno_frequencia_invalida(self):
        """Frequência 150% deve lançar ValidationError"""
        with pytest.raises(ValidationError):
            MatriculaService.avaliar_aluno(self.matricula, 8.0, 150.0)

    def test_avaliar_aluno_nota_limite_minimo_aprovado(self):
        """Nota 7.0 e freq 75% deve resultar em aprovado=True (limites mínimos)"""
        av = MatriculaService.avaliar_aluno(self.matricula, 7.0, 75.0)
        assert av.aprovado is True

    def test_avaliar_aluno_nota_limite_maximo(self):
        """Nota 10.0 deve ser aceita"""
        av = MatriculaService.avaliar_aluno(self.matricula, 10.0, 100.0)
        assert av.nota_final == 10.0
        assert av.aprovado is True

    def test_avaliar_aluno_frequencia_limite_minimo(self):
        """Frequência 75% deve ser aceita (limite mínimo)"""
        av = MatriculaService.avaliar_aluno(self.matricula, 7.0, 75.0)
        assert av.frequencia == 75.0
        assert av.aprovado is True

    def test_avaliar_aluno_frequencia_limite_maximo(self):
        """Frequência 100% deve ser aceita"""
        av = MatriculaService.avaliar_aluno(self.matricula, 7.0, 100.0)
        assert av.frequencia == 100.0
        assert av.aprovado is True

    def test_avaliar_aluno_atualiza_status_matricula(self):
        """Avaliação aprovada deve atualizar status para 'Concluída'"""
        MatriculaService.avaliar_aluno(self.matricula, 8.0, 80.0)
        self.matricula.refresh_from_db()
        assert self.matricula.status.nome == 'Concluída'

    def test_avaliar_aluno_cria_ou_atualiza(self):
        """Chamar avaliar_aluno duas vezes deve atualizar, não duplicar"""
        MatriculaService.avaliar_aluno(self.matricula, 5.0, 50.0)
        MatriculaService.avaliar_aluno(self.matricula, 9.0, 90.0)
        assert Avaliacao.objects.filter(matricula=self.matricula).count() == 1
        av = Avaliacao.objects.get(matricula=self.matricula)
        assert av.nota_final == 9.0
        assert av.frequencia == 90.0


@pytest.mark.django_db
class TestRelatorioTurma:
    """Testes para gerar_relatorio_turma()"""

    def setup_method(self):
        # CORREÇÃO: Garante a presença de todos os status que o service exige internamente
        self.status_ativa = StatusMatriculaFactory(nome='Ativa')
        self.status_concluida = StatusMatriculaFactory(nome='Concluída')
        self.status_cancelada = StatusMatriculaFactory(nome='Cancelada')
        self.turma = TurmaFactory()

    def test_gerar_relatorio_turma(self):
        """Relatório com 2 matriculados e 2 avaliados (1 aprovado, 1 reprovado)"""
        m1 = MatriculaFactory(turma=self.turma, status=self.status_ativa)
        m2 = MatriculaFactory(turma=self.turma, status=self.status_ativa)
        MatriculaService.avaliar_aluno(m1, 8.0, 80.0)
        MatriculaService.avaliar_aluno(m2, 5.0, 50.0)
        
        rel = MatriculaService.gerar_relatorio_turma(self.turma)
        
        assert rel['total_matriculas'] == 2
        assert rel['total_avaliacoes'] == 2
        assert rel['aprovados'] == 1
        assert rel['reprovados'] == 1
        assert rel['media_nota'] == 6.5
        assert rel['taxa_aprovacao'] == 50.0

    def test_gerar_relatorio_turma_vazia(self):
        """Relatório de turma sem matriculados"""
        rel = MatriculaService.gerar_relatorio_turma(self.turma)
        
        assert rel['total_matriculas'] == 0
        assert rel['total_avaliacoes'] == 0
        assert rel['aprovados'] == 0
        assert rel['reprovados'] == 0
        assert rel['media_nota'] == 0
        assert rel['taxa_aprovacao'] == 0

    def test_gerar_relatorio_turma_parcialmente_avaliada(self):
        """Relatório com 2 matriculados mas apenas 1 avaliado"""
        m1 = MatriculaFactory(turma=self.turma, status=self.status_ativa)
        MatriculaFactory(turma=self.turma, status=self.status_ativa)
        MatriculaService.avaliar_aluno(m1, 8.0, 80.0)
        
        rel = MatriculaService.gerar_relatorio_turma(self.turma)
        
        assert rel['total_matriculas'] == 2
        assert rel['total_avaliacoes'] == 1
        assert rel['pendentes'] == 1

    def test_gerar_relatorio_turma_valida_valores(self):
        """Valida cálculo de média e taxa de aprovação"""
        m1 = MatriculaFactory(turma=self.turma, status=self.status_ativa)
        m2 = MatriculaFactory(turma=self.turma, status=self.status_ativa)
        MatriculaService.avaliar_aluno(m1, 10.0, 100.0)
        MatriculaService.avaliar_aluno(m2, 0.0, 0.0)
        
        rel = MatriculaService.gerar_relatorio_turma(self.turma)
        
        assert rel['media_nota'] == 5.0
        assert rel['taxa_aprovacao'] == 50.0


