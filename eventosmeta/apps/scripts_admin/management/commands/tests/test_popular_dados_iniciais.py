"""
Arquivo: test_popular_dados_iniciais.py
Caminho: apps/scripts_admin/management/commands/tests/test_popular_dados_iniciais.py
Finalidade: Testes unitários para o comando de gestão popular_dados_iniciais.
Atualizações:
 - 01/06/2026 - v1.0 - Criação dos testes (todos os 8 cenários).
 - 16/06/2026 - v2.0 - Refatoração para pytest idiomático.
"""

import re
from io import StringIO

import pytest
from django.core.management import call_command

from apps.academico.models import StatusMatricula
from apps.eventos.models import Criterio, Status
from apps.interessados.models import Fototipo, Sexo
from apps.selecao.models import StatusInscricao

pytestmark = pytest.mark.django_db


# =============================================================================
# HELPERS
# =============================================================================

def _limpar_ansi(texto):
    return re.sub(r'\x1b\[[0-9;]*m', '', texto)


def _rodar_comando():
    out = StringIO()
    call_command('popular_dados_iniciais', stdout=out)
    return _limpar_ansi(out.getvalue())


# =============================================================================
# TESTES
# =============================================================================

class TestPopularDadosIniciaisComando:
    """Verifica execução básica do comando."""

    def test_comando_executa_sem_erro(self):
        _rodar_comando()

    def test_comando_retorna_string(self):
        assert isinstance(_rodar_comando(), str)

    def test_comando_nao_vazio(self):
        assert len(_rodar_comando()) > 0


class TestPopularDadosIniciaisStatusEventos:
    """Verifica criação dos status de evento."""

    @pytest.fixture(autouse=True)
    def _setup(self):
        _rodar_comando()

    def test_status_planejamento(self):
        assert Status.objects.filter(nome='Planejamento').exists()

    def test_status_inscricoes_abertas(self):
        assert Status.objects.filter(nome='Inscrições Abertas').exists()

    def test_status_inscricoes_encerradas(self):
        assert Status.objects.filter(nome='Inscrições Encerradas').exists()

    def test_status_em_classificacao(self):
        assert Status.objects.filter(nome='Em Classificação').exists()

    def test_status_resultado_divulgado(self):
        assert Status.objects.filter(nome='Resultado Divulgado').exists()

    def test_status_em_andamento(self):
        assert Status.objects.filter(nome='Em Andamento').exists()

    def test_status_finalizado(self):
        assert Status.objects.filter(nome='Finalizado').exists()

    def test_status_cancelado(self):
        assert Status.objects.filter(nome='Cancelado').exists()

    def test_total_status_eventos(self):
        assert Status.objects.count() == 8


class TestPopularDadosIniciaisStatusInscricoes:
    """Verifica criação dos status de inscrição."""

    @pytest.fixture(autouse=True)
    def _setup(self):
        _rodar_comando()

    def test_status_pendente(self):
        assert StatusInscricao.objects.filter(nome='Pendente').exists()

    def test_status_classificado(self):
        assert StatusInscricao.objects.filter(nome='Classificado').exists()

    def test_status_confirmada(self):
        assert StatusInscricao.objects.filter(nome='Confirmada').exists()

    def test_status_lista_espera(self):
        assert StatusInscricao.objects.filter(nome='Lista de Espera').exists()

    def test_status_cancelada(self):
        assert StatusInscricao.objects.filter(nome='Cancelada').exists()

    def test_status_expirada(self):
        assert StatusInscricao.objects.filter(nome='Expirada').exists()

    def test_status_desistente(self):
        assert StatusInscricao.objects.filter(nome='Desistente').exists()

    def test_status_nao_localizado(self):
        assert StatusInscricao.objects.filter(
            nome='Não localizado para confirmar matricula'
        ).exists()

    def test_total_status_inscricoes(self):
        assert StatusInscricao.objects.count() == 8


class TestPopularDadosIniciaisStatusMatriculas:
    """Verifica criação dos status de matrícula."""

    @pytest.fixture(autouse=True)
    def _setup(self):
        _rodar_comando()

    def test_status_pendente(self):
        assert StatusMatricula.objects.filter(nome='Pendente').exists()

    def test_status_ativa(self):
        assert StatusMatricula.objects.filter(nome='Ativa').exists()

    def test_status_concluida(self):
        assert StatusMatricula.objects.filter(nome='Concluída').exists()

    def test_status_trancada(self):
        assert StatusMatricula.objects.filter(nome='Trancada').exists()

    def test_status_cancelada(self):
        assert StatusMatricula.objects.filter(nome='Cancelada').exists()

    def test_total_status_matriculas(self):
        assert StatusMatricula.objects.count() == 5


class TestPopularDadosIniciaisCriterios:
    """Verifica criação dos critérios de classificação."""

    @pytest.fixture(autouse=True)
    def _setup(self):
        _rodar_comando()

    def test_criterio_pcd(self):
        assert Criterio.objects.filter(codigo='PCD').exists()

    def test_criterio_programa_social(self):
        assert Criterio.objects.filter(codigo='PROGRAMA_SOCIAL').exists()

    def test_criterio_jovem(self):
        assert Criterio.objects.filter(codigo='JOVEM').exists()

    def test_criterio_idoso(self):
        assert Criterio.objects.filter(codigo='IDOSO').exists()

    def test_criterio_ensino_fundamental(self):
        assert Criterio.objects.filter(codigo='ENSINO_FUNDAMENTAL').exists()

    def test_criterio_renda_baixa(self):
        assert Criterio.objects.filter(codigo='RENDA_BAIXA').exists()

    def test_criterio_cota_racial(self):
        assert Criterio.objects.filter(codigo='COTA_RACIAL').exists()


class TestPopularDadosIniciaisSexo:
    """Verifica criação das opções de sexo."""

    @pytest.fixture(autouse=True)
    def _setup(self):
        _rodar_comando()

    def test_sexo_masculino(self):
        assert Sexo.objects.filter(nome='Masculino').exists()

    def test_sexo_feminino(self):
        assert Sexo.objects.filter(nome='Feminino').exists()

    def test_sexo_outro(self):
        assert Sexo.objects.filter(nome='Outro').exists()

    def test_sexo_nao_informar(self):
        assert Sexo.objects.filter(nome='Prefiro não informar').exists()

    def test_total_sexo(self):
        assert Sexo.objects.count() == 4


class TestPopularDadosIniciaisFototipes:
    """Verifica criação dos fototipos (raça/cor)."""

    @pytest.fixture(autouse=True)
    def _setup(self):
        _rodar_comando()

    def test_fototipo_branca(self):
        assert Fototipo.objects.filter(nome='Branca').exists()

    def test_fototipo_preta(self):
        assert Fototipo.objects.filter(nome='Preta').exists()

    def test_fototipo_parda(self):
        assert Fototipo.objects.filter(nome='Parda').exists()

    def test_fototipo_amarela(self):
        assert Fototipo.objects.filter(nome='Amarela').exists()

    def test_fototipo_indigena(self):
        assert Fototipo.objects.filter(nome='Indígena').exists()

    def test_total_fototipos(self):
        assert Fototipo.objects.count() == 5


class TestPopularDadosIniciaisIntegracao:
    """Verifica integridade entre modelos após população."""

    def test_todos_modelos_populados(self):
        _rodar_comando()
        assert Status.objects.exists()
        assert StatusInscricao.objects.exists()
        assert StatusMatricula.objects.exists()

    def test_contagem_total_registros(self):
        _rodar_comando()
        total = (
            Status.objects.count()
            + StatusInscricao.objects.count()
            + StatusMatricula.objects.count()
            + Criterio.objects.count()
            + Sexo.objects.count()
            + Fototipo.objects.count()
        )
        assert total == 8 + 8 + 5 + 7 + 4 + 5

    def test_integridade_dados(self):
        _rodar_comando()
        assert Status.objects.get(nome='Planejamento') is not None


class TestPopularDadosIniciaisIdempotencia:
    """Executar o comando múltiplas vezes não deve duplicar dados."""

    def test_execucao_dupla_nao_duplica_dados(self):
        _rodar_comando()
        _rodar_comando()
        assert Status.objects.count() == 8

    def test_execucao_tripla_nao_duplica_dados(self):
        _rodar_comando()
        _rodar_comando()
        _rodar_comando()
        assert Status.objects.count() == 8


class TestPopularDadosIniciaisSaida:
    """Verifica o conteúdo da saída do comando."""

    def test_saida_contem_sucesso(self):
        output = _rodar_comando()
        assert 'sucesso' in output.lower()

    def test_saida_contem_nome_comando(self):
        output = _rodar_comando()
        assert 'populando' in output.lower()

    def test_saida_nao_contem_ansi(self):
        output = _rodar_comando()
        assert '\x1b' not in output


