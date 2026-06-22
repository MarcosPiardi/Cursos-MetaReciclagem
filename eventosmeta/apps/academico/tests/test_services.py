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
from apps.academico.models import Avaliacao, StatusMatricula
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


# ============================================================
# TESTES DE MATRÍCULA
# 22/06/2026 - Adicionados testes para matricular_classificado,
#              matricular_lote, matricular_alunos e alterar_status_inscricao
# ============================================================

@pytest.mark.django_db
class TestMatricularClassificado:
    """Testes para matricular_classificado()"""

    def setup_method(self):
        from apps.eventos.tests.factories import EventoFactory, StatusFactory
        from apps.selecao.tests.factories import InscricaoFactory, ClassificacaoFactory, StatusInscricaoFactory

        self.status_ativa = StatusMatriculaFactory(nome='Ativa')
        self.status_evento = StatusFactory()
        self.status_inscricao = StatusInscricaoFactory(nome='Confirmada')
        self.turma = TurmaFactory(capacidade=5)
        self.inscricao = InscricaoFactory(
            evento=self.turma.evento,
            status=self.status_inscricao,
        )
        self.classificacao = ClassificacaoFactory(
            inscricao=self.inscricao,
            classificado=True,
            posicao=1,
            pontuacao_total=100.0,
        )

    def test_matricular_classificado_com_sucesso(self):
        """Deve criar matrícula para classificado com turma disponível"""
        matricula = MatriculaService.matricular_classificado(self.classificacao, self.turma)

        assert matricula.interessado == self.classificacao.inscricao.interessado
        assert matricula.turma == self.turma
        assert matricula.status.nome == 'Ativa'
        assert matricula.inscricao == self.classificacao.inscricao
        assert 'Matriculado automaticamente' in matricula.observacoes

    def test_matricular_classificado_nao_classificado(self):
        """Deve lançar ValidationError se candidato não está classificado"""
        self.classificacao.classificado = False
        self.classificacao.save()

        with pytest.raises(ValidationError, match='não está classificado'):
            MatriculaService.matricular_classificado(self.classificacao, self.turma)

    def test_matricular_classificado_turma_lotada(self):
        """Deve lançar ValidationError se turma não tem vagas"""
        turma_cheia = TurmaFactory(capacidade=1)
        MatriculaFactory(turma=turma_cheia, status=self.status_ativa)

        with pytest.raises(ValidationError, match='não possui vagas'):
            MatriculaService.matricular_classificado(self.classificacao, turma_cheia)

    def test_matricular_classificado_ja_matriculado(self):
        """Deve lançar ValidationError se candidato já está matriculado"""
        MatriculaService.matricular_classificado(self.classificacao, self.turma)

        with pytest.raises(ValidationError, match='já está matriculado'):
            MatriculaService.matricular_classificado(self.classificacao, self.turma)

    def test_matricular_classificado_sem_status_ativa(self):
        """Deve lançar exception se StatusMatricula 'Ativa' não existe"""
        self.status_ativa.delete()

        with pytest.raises(StatusMatricula.DoesNotExist):
            MatriculaService.matricular_classificado(self.classificacao, self.turma)

@pytest.mark.django_db
class TestMatricularLote:
    """Testes para matricular_lote()"""

    def setup_method(self):
        from apps.eventos.tests.factories import StatusFactory
        from apps.selecao.tests.factories import InscricaoFactory, ClassificacaoFactory, StatusInscricaoFactory

        self.status_ativa = StatusMatriculaFactory(nome='Ativa')
        self.status_inscricao = StatusInscricaoFactory(nome='Confirmada')
        self.turma = TurmaFactory(capacidade=10)

        # Criar 3 classificações
        self.classificacoes = []
        for i in range(3):
            inscricao = InscricaoFactory(
                evento=self.turma.evento,
                status=self.status_inscricao,
            )
            classificacao = ClassificacaoFactory(
                inscricao=inscricao,
                classificado=True,
                posicao=i + 1,
                pontuacao_total=float(100 - i * 10),
            )
            self.classificacoes.append(classificacao)

    def test_matricular_lote_todos_sucesso(self):
        """Deve matricular todos os 3 classificados"""
        from apps.selecao.models import Classificacao
        qs = Classificacao.objects.filter(id__in=[c.id for c in self.classificacoes])

        resultado = MatriculaService.matricular_lote(qs, self.turma)

        assert len(resultado['sucesso']) == 3
        assert len(resultado['erros']) == 0

    def test_matricular_lote_um_erro(self):
        """Deve matricular 2 e reportar 1 erro"""
        from apps.selecao.models import Classificacao

        # Tornar um não classificado
        self.classificacoes[1].classificado = False
        self.classificacoes[1].save()

        qs = Classificacao.objects.filter(id__in=[c.id for c in self.classificacoes])

        resultado = MatriculaService.matricular_lote(qs, self.turma)

        assert len(resultado['sucesso']) == 2
        assert len(resultado['erros']) == 1
        assert 'não está classificado' in resultado['erros'][0]['erro']

    def test_matricular_lote_todos_erro(self):
        """Deve reportar erro para todos se turma está lotada"""
        from apps.selecao.models import Classificacao

        turma_cheia = TurmaFactory(capacidade=1)
        MatriculaFactory(turma=turma_cheia, status=self.status_ativa)

        qs = Classificacao.objects.filter(id__in=[c.id for c in self.classificacoes])

        resultado = MatriculaService.matricular_lote(qs, turma_cheia)

        assert len(resultado['sucesso']) == 0
        assert len(resultado['erros']) == 3

@pytest.mark.django_db
class TestMatricularAlunos:
    """Testes para matricular_alunos()"""

    def setup_method(self):
        from apps.eventos.tests.factories import EventoFactory, StatusFactory
        from apps.selecao.tests.factories import InscricaoFactory, StatusInscricaoFactory

        self.status_matricula_ativa = StatusMatriculaFactory(nome='Ativa')
        self.status_inscricao_confirmado = StatusInscricaoFactory(nome='Confirmado')
        self.status_inscricao_pendente = StatusInscricaoFactory(nome='Pendente')
        self.evento = EventoFactory()

    def test_matricular_alunos_com_sucesso(self):
        """Deve matricular aluno e criar matrícula"""
        from apps.selecao.tests.factories import InscricaoFactory

        TurmaFactory(evento=self.evento, capacidade=30)
        inscricao = InscricaoFactory(
            evento=self.evento,
            status=self.status_inscricao_pendente,
        )

        resultado = MatriculaService.matricular_alunos(
            inscricoes_ids=[inscricao.id]
        )

        assert resultado['sucesso'] is True
        assert resultado['total_sucesso'] == 1
        assert resultado['total_ja_matriculados'] == 0
        assert len(resultado['erros']) == 0

        # Verificar que matrícula foi criada
        from apps.academico.models import Matricula
        assert Matricula.objects.filter(interessado=inscricao.interessado).exists()

        # Verificar que status foi atualizado
        inscricao.refresh_from_db()
        assert inscricao.status.nome == 'Confirmado'

    def test_matricular_alunos_sem_turma(self):
        """Deve reportar erro se evento não tem turmas"""
        from apps.selecao.tests.factories import InscricaoFactory

        inscricao = InscricaoFactory(
            evento=self.evento,
            status=self.status_inscricao_pendente,
        )

        resultado = MatriculaService.matricular_alunos(
            inscricoes_ids=[inscricao.id]
        )

        assert resultado['total_sucesso'] == 0
        assert len(resultado['erros']) > 0
        assert 'não possui turmas' in resultado['erros'][0]

    def test_matricular_alunos_ja_matriculado(self):
        """Deve pular aluno já matriculado"""
        from apps.selecao.tests.factories import InscricaoFactory
        from apps.academico.models import Matricula

        turma = TurmaFactory(evento=self.evento, capacidade=30)
        inscricao = InscricaoFactory(
            evento=self.evento,
            status=self.status_inscricao_pendente,
        )

        # Criar matrícula manualmente (MatriculaFactory geraria inscricao divergente)
        Matricula.objects.create(
            turma=turma,
            interessado=inscricao.interessado,
            inscricao=inscricao,
            status=self.status_matricula_ativa,
        )

        resultado = MatriculaService.matricular_alunos(
            inscricoes_ids=[inscricao.id]
        )

        assert resultado['total_sucesso'] == 0
        assert resultado['total_ja_matriculados'] == 1

    def test_matricular_alunos_sem_status_ativa(self):
        """Deve lançar ValueError se StatusMatricula 'Ativa' não existe"""
        from apps.selecao.tests.factories import InscricaoFactory

        self.status_matricula_ativa.delete()
        inscricao = InscricaoFactory(
            evento=self.evento,
            status=self.status_inscricao_pendente,
        )

        with pytest.raises(ValueError, match="Status 'Ativa' não encontrado"):
            MatriculaService.matricular_alunos(
                inscricoes_ids=[inscricao.id]
            )

    def test_matricular_alunos_multiplos(self):
        """Deve matricular múltiplos alunos"""
        from apps.selecao.tests.factories import InscricaoFactory

        TurmaFactory(evento=self.evento, capacidade=50)

        inscricoes = []
        for i in range(3):
            inscricao = InscricaoFactory(
                evento=self.evento,
                status=self.status_inscricao_pendente,
            )
            inscricoes.append(inscricao)

        ids = [insc.id for insc in inscricoes]

        resultado = MatriculaService.matricular_alunos(
            inscricoes_ids=ids
        )

        assert resultado['total_sucesso'] == 3
        assert resultado['total_ja_matriculados'] == 0

@pytest.mark.django_db
class TestAlterarStatusInscricao:
    """Testes para alterar_status_inscricao()"""

    def setup_method(self):
        from apps.selecao.tests.factories import InscricaoFactory, StatusInscricaoFactory

        self.status_pendente = StatusInscricaoFactory(nome='Pendente')
        self.status_confirmado = StatusInscricaoFactory(nome='Confirmado')
        self.status_cancelado = StatusInscricaoFactory(nome='Cancelado')

        self.inscricoes = []
        for i in range(3):
            inscricao = InscricaoFactory(status=self.status_pendente)
            self.inscricoes.append(inscricao)

    def test_alterar_status_todas(self):
        """Deve alterar status de todas as inscrições"""
        ids = [insc.id for insc in self.inscricoes]

        resultado = MatriculaService.alterar_status_inscricao(
            inscricoes_ids=ids,
            novo_status_nome='Confirmado'
        )

        assert resultado['sucesso'] is True
        assert resultado['total_atualizadas'] == 3
        assert len(resultado['erros']) == 0

        # Verificar no banco
        from apps.selecao.models import Inscricao
        for insc in self.inscricoes:
            insc.refresh_from_db()
            assert insc.status.nome == 'Confirmado'

    def test_alterar_status_uma(self):
        """Deve alterar status de uma inscrição específica"""
        resultado = MatriculaService.alterar_status_inscricao(
            inscricoes_ids=[self.inscricoes[0].id],
            novo_status_nome='Cancelado'
        )

        assert resultado['total_atualizadas'] == 1

        self.inscricoes[0].refresh_from_db()
        assert self.inscricoes[0].status.nome == 'Cancelado'

    def test_alterar_status_inexistente(self):
        """Deve lançar ValueError se status não existe"""
        with pytest.raises(ValueError, match="Status 'Inexistente' não encontrado"):
            MatriculaService.alterar_status_inscricao(
                inscricoes_ids=[1],
                novo_status_nome='Inexistente'
            )



