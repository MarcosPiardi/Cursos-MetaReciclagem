"""
Arquivo: test_services.py
Caminho: apps/dashboard/tests/test_services.py
Finalidade: Testes para os serviços de dashboard.

Atualizações:
 - 10/06/2026 - Criação do arquivo - Implementação inicial dos testes de serviços de dashboard
 - 11/06/2026 - Refatorado com setUp() completo, factories corretas, assertions específicas
              - Corrigido: usar Avaliacao criada automaticamente pelo signal, não criar manualmente
 - 16/06/2026 - Refatorado de unittest.TestCase para pytest
 """

import pytest
from django.utils import timezone
from datetime import date, timedelta
from apps.interessados.tests.factories import InteressadoFactory
from apps.eventos.tests.factories import EventoFactory, StatusFactory, TurmaFactory
from apps.dashboard.services import (
    DashboardInteressadosService,
    DashboardEventosService,
    DashboardAcademicoService,
    DashboardProcessoSeletivoService,
)

pytestmark = pytest.mark.django_db

# =============================================================================
# DASHBOARD INTERESSADOS
# =============================================================================

class TestDashboardInteressadosService:
    """Testes para DashboardInteressadosService"""

    @pytest.fixture(autouse=True)
    def setup(self, db):
        from apps.interessados.models import Sexo, Fototipo

        self.sexo_m = Sexo.objects.create(nome='Masculino')
        self.sexo_f = Sexo.objects.create(nome='Feminino')
        self.fototipo_1 = Fototipo.objects.create(nome='Tipo I')
        self.fototipo_2 = Fototipo.objects.create(nome='Tipo II')

        self.interessado_1 = InteressadoFactory.create(
            sexo=self.sexo_m,
            fototipo=self.fototipo_1,
            escolaridade='SUPERIOR_COMPLETO',
            programa_social=True,
            necessidades_especiais=False,
            data_nascimento=date(1990, 5, 15),
        )

        self.interessado_2 = InteressadoFactory.create(
            sexo=self.sexo_f,
            fototipo=self.fototipo_2,
            escolaridade='MEDIO_COMPLETO',
            programa_social=False,
            necessidades_especiais=True,
            pcd_fisica=True,
            data_nascimento=date(1995, 8, 20),
        )

    def test_calcular_metricas_gerais(self):
        metricas = DashboardInteressadosService.calcular_metricas_gerais()
        assert isinstance(metricas, dict)
        assert metricas['total_interessados'] == 2
        assert 'interessados_matriculados' in metricas
        assert 'interessados_sem_matricula' in metricas

    def test_calcular_distribuicao_sexo(self):
        distribuicao = DashboardInteressadosService.calcular_distribuicao_sexo()
        assert isinstance(distribuicao, list)
        assert len(distribuicao) > 0
        if distribuicao:
            assert 'sexo__nome' in distribuicao[0]
            assert 'total' in distribuicao[0]
            assert 'percentual' in distribuicao[0]

    def test_calcular_distribuicao_fototipo(self):
        distribuicao = DashboardInteressadosService.calcular_distribuicao_fototipo()
        assert isinstance(distribuicao, list)
        assert len(distribuicao) > 0
        if distribuicao:
            assert 'fototipo__nome' in distribuicao[0]
            assert 'total' in distribuicao[0]
            assert 'percentual' in distribuicao[0]

    def test_calcular_distribuicao_escolaridade(self):
        distribuicao = DashboardInteressadosService.calcular_distribuicao_escolaridade()
        assert isinstance(distribuicao, list)
        assert len(distribuicao) > 0
        if distribuicao:
            assert 'escolaridade' in distribuicao[0]
            assert 'escolaridade_label' in distribuicao[0]
            assert 'total' in distribuicao[0]

    def test_calcular_distribuicao_programas_sociais(self):
        distribuicao = DashboardInteressadosService.calcular_distribuicao_programas_sociais()
        assert isinstance(distribuicao, list)
        assert len(distribuicao) == 2
        assert 'participa' in distribuicao[0]
        assert 'total' in distribuicao[0]
        assert 'percentual' in distribuicao[0]

    def test_calcular_distribuicao_deficiencias(self):
        distribuicao = DashboardInteressadosService.calcular_distribuicao_deficiencias()
        assert isinstance(distribuicao, list)
        assert len(distribuicao) == 2
        assert 'tipo' in distribuicao[0]
        assert 'total' in distribuicao[0]
        assert 'percentual' in distribuicao[0]

    def test_calcular_tipos_deficiencia(self):
        tipos = DashboardInteressadosService.calcular_tipos_deficiencia()
        assert isinstance(tipos, list)
        if tipos:
            assert 'tipo_deficiencia' in tipos[0]
            assert 'total' in tipos[0]

    def test_calcular_faixas_etarias(self):
        faixas = DashboardInteressadosService.calcular_faixas_etarias()
        assert isinstance(faixas, list)
        if faixas:
            assert 'faixa' in faixas[0]
            assert 'total' in faixas[0]
            assert 'percentual' in faixas[0]

    def test_obter_contexto_completo(self):
        contexto = DashboardInteressadosService.obter_contexto_completo()
        assert isinstance(contexto, dict)
        assert 'total_interessados' in contexto
        assert 'distribuicao_sexo' in contexto
        assert 'distribuicao_fototipo' in contexto
        assert 'distribuicao_escolaridade' in contexto
        assert 'distribuicao_programas' in contexto
        assert 'distribuicao_deficiencia' in contexto
        assert 'tipos_deficiencia' in contexto
        assert 'faixas_etarias' in contexto

# =============================================================================
# DASHBOARD EVENTOS
# =============================================================================

class TestDashboardEventosService:
    """Testes para DashboardEventosService"""

    @pytest.fixture(autouse=True)
    def setup(self, db):
        self.status = StatusFactory.create(nome='Ativo')
        self.evento = EventoFactory.create(status=self.status)
        self.turma = TurmaFactory.create(evento=self.evento)

    def test_calcular_metricas_gerais(self):
        metricas = DashboardEventosService.calcular_metricas_gerais()
        assert isinstance(metricas, dict)
        assert 'total_eventos' in metricas
        assert 'total_turmas' in metricas
        assert 'eventos_inscricoes_abertas' in metricas

    def test_calcular_turmas_por_status(self):
        status = DashboardEventosService.calcular_turmas_por_status()
        assert isinstance(status, dict)
        assert 'turmas_futuras' in status
        assert 'turmas_em_andamento' in status
        assert 'turmas_encerradas' in status

    def test_calcular_eventos_por_status(self):
        eventos = DashboardEventosService.calcular_eventos_por_status()
        assert isinstance(eventos, list)
        if eventos:
            assert 'status__nome' in eventos[0]
            assert 'total' in eventos[0]

    def test_calcular_top_eventos_inscricoes(self):
        top = DashboardEventosService.calcular_top_eventos_inscricoes()
        assert isinstance(top, list)

    def test_obter_contexto_completo(self):
        contexto = DashboardEventosService.obter_contexto_completo()
        assert isinstance(contexto, dict)
        assert 'total_eventos' in contexto
        assert 'total_turmas' in contexto
        assert 'eventos_por_status' in contexto
        assert 'top_eventos_inscricoes' in contexto

# =============================================================================
# DASHBOARD ACADEMICO
# =============================================================================

class TestDashboardAcademicoService:
    """Testes para DashboardAcademicoService"""

    @pytest.fixture(autouse=True)
    def setup(self, db):
        from apps.academico.models import Matricula, StatusMatricula
        from apps.eventos.models import Evento, Status as EventoStatus
        from apps.selecao.models import Inscricao, StatusInscricao

        self.status_evento = EventoStatus.objects.create(nome='Ativo')
        self.evento = Evento.objects.create(
            nome='Curso Teste',
            status=self.status_evento,
            total_vagas=30,
            data_inicio_inscricao=timezone.now(),
            data_fim_inscricao=timezone.now() + timedelta(days=7),
            data_inicio_evento=timezone.now().date() + timedelta(days=8),
            data_fim_evento=timezone.now().date() + timedelta(days=15),
        )

        self.turma = TurmaFactory.create(evento=self.evento)
        self.interessado = InteressadoFactory.create()

        self.status_matricula = StatusMatricula.objects.create(nome='Ativa')
        self.status_inscricao = StatusInscricao.objects.create(nome='Confirmada')
        self.inscricao = Inscricao.objects.create(
            interessado=self.interessado,
            evento=self.evento,
            status=self.status_inscricao,
        )

        self.matricula = Matricula.objects.create(
            turma=self.turma,
            interessado=self.interessado,
            inscricao=self.inscricao,
            status=self.status_matricula,
        )

        # Avaliacao criada automaticamente pelo signal
        self.avaliacao = self.matricula.avaliacao
        self.avaliacao.nota_final = 8.5
        self.avaliacao.frequencia = 85.0
        self.avaliacao.aprovado = True
        self.avaliacao.certificado_emitido = True
        self.avaliacao.save()

    def test_calcular_metricas_avaliacoes(self):
        metricas = DashboardAcademicoService.calcular_metricas_avaliacoes()
        assert isinstance(metricas, dict)
        assert metricas['total_avaliacoes'] == 1
        assert metricas['total_aprovados'] == 1
        assert metricas['total_reprovados'] == 0
        assert 'media_notas' in metricas
        assert 'media_frequencia' in metricas
        assert 'certificados_emitidos' in metricas

    def test_calcular_taxa_aprovacao(self):
        taxa = DashboardAcademicoService.calcular_taxa_aprovacao()
        assert taxa == 100.0

    def test_calcular_top_cursos_aprovados(self):
        top = DashboardAcademicoService.calcular_top_cursos_aprovados()
        assert isinstance(top, list)

    def test_obter_contexto_completo(self):
        contexto = DashboardAcademicoService.obter_contexto_completo()
        assert isinstance(contexto, dict)
        assert 'total_avaliacoes' in contexto
        assert 'taxa_aprovacao' in contexto
        assert 'top_cursos_aprovados' in contexto

# =============================================================================
# DASHBOARD PROCESSO SELETIVO
# =============================================================================

class TestDashboardProcessoSeletivoService:
    """Testes para DashboardProcessoSeletivoService"""

    @pytest.fixture(autouse=True)
    def setup(self, db):
        from apps.selecao.models import Inscricao, Classificacao, StatusInscricao
        from apps.eventos.models import Evento, Status as EventoStatus

        self.status_evento = EventoStatus.objects.create(nome='Ativo')
        self.evento = Evento.objects.create(
            nome='Seleção 2026',
            status=self.status_evento,
            total_vagas=30,
            data_inicio_inscricao=timezone.now(),
            data_fim_inscricao=timezone.now() + timedelta(days=7),
            data_inicio_evento=timezone.now().date() + timedelta(days=8),
            data_fim_evento=timezone.now().date() + timedelta(days=15),
        )

        self.status_inscricao = StatusInscricao.objects.create(nome='Confirmada')
        self.interessado = InteressadoFactory.create()

        self.inscricao = Inscricao.objects.create(
            evento=self.evento,
            interessado=self.interessado,
            status=self.status_inscricao,
        )

        self.classificacao = Classificacao.objects.create(
            inscricao=self.inscricao,
            pontuacao_total=85.5,
            classificado=True,
        )

    def test_calcular_metricas_inscricoes(self):
        metricas = DashboardProcessoSeletivoService.calcular_metricas_inscricoes()
        assert isinstance(metricas, dict)
        assert 'total_inscricoes' in metricas
        assert 'inscricoes_recentes' in metricas

    def test_calcular_metricas_classificacoes(self):
        metricas = DashboardProcessoSeletivoService.calcular_metricas_classificacoes()
        assert isinstance(metricas, dict)
        assert metricas['total_classificacoes'] == 1
        assert metricas['classificados'] == 1
        assert 'taxa_classificacao' in metricas

    def test_calcular_top_eventos_inscricoes(self):
        top = DashboardProcessoSeletivoService.calcular_top_eventos_inscricoes()
        assert isinstance(top, list)

    def test_obter_contexto_completo(self):
        contexto = DashboardProcessoSeletivoService.obter_contexto_completo()
        assert isinstance(contexto, dict)
        assert 'total_inscricoes' in contexto
        assert 'total_classificacoes' in contexto
        assert 'top_eventos_inscricoes' in contexto



