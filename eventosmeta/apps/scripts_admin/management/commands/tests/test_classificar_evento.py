"""
Arquivo: test_classificar_evento.py
Caminho: apps/scripts_admin/management/commands/tests/test_classificar_evento.py
Finalidade: Testes automatizados do management command classificar_evento
Atualizações:
 - 02/06/2026 - v1.0 - Criação dos testes
 - 16/06/2026 - v2.0 - Refatoração para pytest idiomático
"""

import hashlib
from datetime import date, timedelta
from io import StringIO

import factory
import pytest
from django.core.management import call_command
from django.utils import timezone
from factory.django import DjangoModelFactory
from factory import LazyFunction, Sequence

from apps.eventos.models import Evento, EventoCriterio, Criterio, Status
from apps.interessados.models import Interessado, Fototipo
from apps.selecao.models import Inscricao, Classificacao, InscricaoCriterioAtendido, StatusInscricao

pytestmark = pytest.mark.django_db


# =============================================================================
# FACTORIES
# =============================================================================

class StatusFactory(DjangoModelFactory):
    class Meta:
        model = Status
        django_get_or_create = ('nome',)
    nome = "Ativo"
    cor = "#28a745"
    ordem = 1


class StatusInscricaoFactory(DjangoModelFactory):
    class Meta:
        model = StatusInscricao
        django_get_or_create = ('nome',)
    nome = "Confirmada"
    cor = "#007bff"
    ordem = 3


class EventoFactory(DjangoModelFactory):
    class Meta:
        model = Evento
    nome = "Evento Teste"
    descricao = "Descricao"
    total_vagas = 5
    data_inicio_inscricao = LazyFunction(lambda: timezone.now() - timedelta(days=10))
    data_fim_inscricao = LazyFunction(lambda: timezone.now() - timedelta(days=1))
    data_inicio_evento = LazyFunction(lambda: (timezone.now() + timedelta(days=1)).date())
    data_fim_evento = LazyFunction(lambda: (timezone.now() + timedelta(days=10)).date())
    status = factory.SubFactory(StatusFactory)


class CriterioFactory(DjangoModelFactory):
    class Meta:
        model = Criterio
        django_get_or_create = ('codigo',)
    tipo_criterio = "PONTUACAO"
    codigo = Sequence(lambda n: f"CRIT{n:02d}")
    nome = "Criterio Teste"
    descricao = "Descricao"
    pontos = 10
    categoria = "GERAL"
    ativo = True


class EventoCriterioFactory(DjangoModelFactory):
    class Meta:
        model = EventoCriterio
    evento = factory.SubFactory(EventoFactory)
    criterio = factory.SubFactory(CriterioFactory)
    prioridade = 1
    ativo = True


class FototipoFactory(DjangoModelFactory):
    class Meta:
        model = Fototipo
        django_get_or_create = ('nome',)
    nome = "Branca"
    descricao = ""


class InteressadoFactory(DjangoModelFactory):
    class Meta:
        model = Interessado
    cpf = Sequence(lambda n: f"{n:011d}")
    cpf_hash = factory.LazyAttribute(
        lambda o: hashlib.sha256(o.cpf.encode()).hexdigest()
    )
    nome = Sequence(lambda n: f"Interessado {n}")
    senha = "pbkdf2_sha256$dummy"
    data_nascimento = date(1990, 1, 1)
    email = Sequence(lambda n: f"interessado{n}@teste.com")
    escolaridade = ""
    num_nis = ""
    pcd_fisica = False
    pcd_visual = False
    pcd_auditiva = False
    pcd_intelectual = False
    pcd_psicossocial = False
    pcd_multiplas = False


class InscricaoFactory(DjangoModelFactory):
    class Meta:
        model = Inscricao
    interessado = factory.SubFactory(InteressadoFactory)
    evento = factory.SubFactory(EventoFactory)
    status = factory.SubFactory(StatusInscricaoFactory)


# =============================================================================
# HELPERS
# =============================================================================

def _idade_para_nascimento(idade):
    """Retorna uma data de nascimento que resulta exatamente na idade informada."""
    hoje = date.today()
    return hoje.replace(year=hoje.year - idade)


def _rodar_comando(evento_id):
    """Executa o comando e retorna o stdout como string."""
    out = StringIO()
    call_command('classificar_evento', f'--evento_id={evento_id}', stdout=out)
    return out.getvalue()


# =============================================================================
# TESTES
# =============================================================================

class TestClassificarEventoEventoNaoEncontrado:
    """Evento com ID inexistente."""

    def test_evento_inexistente_exibe_erro(self):
        out = _rodar_comando(evento_id=99999)
        assert "não encontrado" in out


class TestClassificarEventoSemInscricoes:
    """Evento sem inscrições confirmadas."""

    @pytest.fixture(autouse=True)
    def _setup(self):
        self.evento = EventoFactory()

    def test_sem_inscricoes_confirmadas_exibe_aviso(self):
        out = _rodar_comando(self.evento.id)
        assert "Nenhuma inscrição" in out

    def test_sem_inscricoes_nao_cria_classificacao(self):
        _rodar_comando(self.evento.id)
        assert Classificacao.objects.count() == 0


class TestClassificarEventoSemCriterios:
    """Evento com inscrição confirmada, mas sem critérios ativos."""

    @pytest.fixture(autouse=True)
    def _setup(self):
        self.evento = EventoFactory()
        InscricaoFactory(evento=self.evento)

    def test_sem_criterios_exibe_aviso(self):
        out = _rodar_comando(self.evento.id)
        assert "Nenhum critério" in out


class TestClassificarEventoPontuacao:
    """Testa o cálculo de pontuação para cada critério."""

    @pytest.fixture(autouse=True)
    def _setup(self):
        self.evento = EventoFactory(total_vagas=10)

    def _criar_criterio_e_inscricao(self, codigo, pontos, interessado_kwargs):
        criterio = CriterioFactory(codigo=codigo, pontos=pontos, tipo_criterio="PONTUACAO")
        EventoCriterioFactory(evento=self.evento, criterio=criterio)
        interessado = InteressadoFactory(**interessado_kwargs)
        return InscricaoFactory(evento=self.evento, interessado=interessado)

    def test_criterio_pcd_atribuido(self):
        inscricao = self._criar_criterio_e_inscricao('PCD', 10, {'pcd_fisica': True})
        _rodar_comando(self.evento.id)
        classificacao = Classificacao.objects.get(inscricao=inscricao)
        assert classificacao.pontuacao_total == 10

    def test_criterio_pcd_nao_atribuido_quando_sem_deficiencia(self):
        inscricao = self._criar_criterio_e_inscricao('PCD', 10, {})
        _rodar_comando(self.evento.id)
        classificacao = Classificacao.objects.get(inscricao=inscricao)
        assert classificacao.pontuacao_total == 0

    def test_criterio_nis_atribuido(self):
        inscricao = self._criar_criterio_e_inscricao('NIS', 15, {'num_nis': '12345678901'})
        _rodar_comando(self.evento.id)
        classificacao = Classificacao.objects.get(inscricao=inscricao)
        assert classificacao.pontuacao_total == 15

    def test_criterio_nis_nao_atribuido_sem_nis(self):
        inscricao = self._criar_criterio_e_inscricao('NIS', 15, {'num_nis': ''})
        _rodar_comando(self.evento.id)
        classificacao = Classificacao.objects.get(inscricao=inscricao)
        assert classificacao.pontuacao_total == 0

    def test_criterio_jovem_atribuido_16_anos(self):
        inscricao = self._criar_criterio_e_inscricao(
            'JOVEM', 5, {'data_nascimento': _idade_para_nascimento(16)}
        )
        _rodar_comando(self.evento.id)
        classificacao = Classificacao.objects.get(inscricao=inscricao)
        assert classificacao.pontuacao_total == 5

    def test_criterio_jovem_atribuido_24_anos(self):
        inscricao = self._criar_criterio_e_inscricao(
            'JOVEM', 5, {'data_nascimento': _idade_para_nascimento(24)}
        )
        _rodar_comando(self.evento.id)
        classificacao = Classificacao.objects.get(inscricao=inscricao)
        assert classificacao.pontuacao_total == 5

    def test_criterio_jovem_nao_atribuido_para_adulto(self):
        inscricao = self._criar_criterio_e_inscricao(
            'JOVEM', 5, {'data_nascimento': _idade_para_nascimento(35)}
        )
        _rodar_comando(self.evento.id)
        classificacao = Classificacao.objects.get(inscricao=inscricao)
        assert classificacao.pontuacao_total == 0

    def test_criterio_idoso_atribuido_50_anos(self):
        inscricao = self._criar_criterio_e_inscricao(
            'IDOSO', 8, {'data_nascimento': _idade_para_nascimento(50)}
        )
        _rodar_comando(self.evento.id)
        classificacao = Classificacao.objects.get(inscricao=inscricao)
        assert classificacao.pontuacao_total == 8

    def test_criterio_idoso_nao_atribuido_para_49_anos(self):
        inscricao = self._criar_criterio_e_inscricao(
            'IDOSO', 8, {'data_nascimento': _idade_para_nascimento(49)}
        )
        _rodar_comando(self.evento.id)
        classificacao = Classificacao.objects.get(inscricao=inscricao)
        assert classificacao.pontuacao_total == 0

    def test_criterio_cota_racial_preta(self):
        fototipo = FototipoFactory(nome='Preta')
        inscricao = self._criar_criterio_e_inscricao(
            'COTA_RACIAL', 10, {'fototipo': fototipo}
        )
        _rodar_comando(self.evento.id)
        classificacao = Classificacao.objects.get(inscricao=inscricao)
        assert classificacao.pontuacao_total == 10

    def test_criterio_cota_racial_parda(self):
        fototipo = FototipoFactory(nome='Parda')
        inscricao = self._criar_criterio_e_inscricao(
            'COTA_RACIAL', 10, {'fototipo': fototipo}
        )
        _rodar_comando(self.evento.id)
        classificacao = Classificacao.objects.get(inscricao=inscricao)
        assert classificacao.pontuacao_total == 10

    def test_criterio_cota_racial_indigena(self):
        fototipo = FototipoFactory(nome='Indígena')
        inscricao = self._criar_criterio_e_inscricao(
            'COTA_RACIAL', 10, {'fototipo': fototipo}
        )
        _rodar_comando(self.evento.id)
        classificacao = Classificacao.objects.get(inscricao=inscricao)
        assert classificacao.pontuacao_total == 10

    def test_criterio_cota_racial_nao_atribuido_para_branca(self):
        fototipo = FototipoFactory(nome='Branca')
        inscricao = self._criar_criterio_e_inscricao(
            'COTA_RACIAL', 10, {'fototipo': fototipo}
        )
        _rodar_comando(self.evento.id)
        classificacao = Classificacao.objects.get(inscricao=inscricao)
        assert classificacao.pontuacao_total == 0

    def test_criterio_cota_racial_sem_fototipo(self):
        inscricao = self._criar_criterio_e_inscricao(
            'COTA_RACIAL', 10, {'fototipo': None}
        )
        _rodar_comando(self.evento.id)
        classificacao = Classificacao.objects.get(inscricao=inscricao)
        assert classificacao.pontuacao_total == 0

    def test_criterio_escolaridade_fundamental_incompleto(self):
        inscricao = self._criar_criterio_e_inscricao(
            'ESC_FUND_INC', 5, {'escolaridade': 'FUNDAMENTAL_INCOMPLETO'}
        )
        _rodar_comando(self.evento.id)
        classificacao = Classificacao.objects.get(inscricao=inscricao)
        assert classificacao.pontuacao_total == 5

    def test_criterio_escolaridade_medio_completo(self):
        inscricao = self._criar_criterio_e_inscricao(
            'ESC_MEDIO_COMP', 3, {'escolaridade': 'MEDIO_COMPLETO'}
        )
        _rodar_comando(self.evento.id)
        classificacao = Classificacao.objects.get(inscricao=inscricao)
        assert classificacao.pontuacao_total == 3

    def test_multiplos_criterios_somam_pontos(self):
        crit_pcd = CriterioFactory(codigo='PCD', pontos=10, tipo_criterio='PONTUACAO')
        crit_nis = CriterioFactory(codigo='NIS', pontos=15, tipo_criterio='PONTUACAO')
        EventoCriterioFactory(evento=self.evento, criterio=crit_pcd)
        EventoCriterioFactory(evento=self.evento, criterio=crit_nis)
        interessado = InteressadoFactory(pcd_fisica=True, num_nis='12345678901')
        inscricao = InscricaoFactory(evento=self.evento, interessado=interessado)
        _rodar_comando(self.evento.id)
        classificacao = Classificacao.objects.get(inscricao=inscricao)
        assert classificacao.pontuacao_total == 25


class TestClassificarEventoCriterioOrdenacao:
    """Critérios do tipo ORDENACAO não devem somar pontos."""

    def test_criterio_ordenacao_nao_soma_pontos(self):
        evento = EventoFactory(total_vagas=10)
        criterio = CriterioFactory(codigo='ORD01', tipo_criterio='ORDENACAO', pontos=0)
        EventoCriterioFactory(evento=evento, criterio=criterio)
        InscricaoFactory(evento=evento)
        _rodar_comando(evento.id)
        classificacao = Classificacao.objects.get(inscricao__evento=evento)
        assert classificacao.pontuacao_total == 0


class TestClassificarEventoPosicao:
    """Testa a atribuição de posições e flags classificado/lista_espera."""

    @pytest.fixture(autouse=True)
    def _setup(self):
        self.evento = EventoFactory(total_vagas=2)
        criterio = CriterioFactory(codigo='PCD', pontos=10, tipo_criterio='PONTUACAO')
        EventoCriterioFactory(evento=self.evento, criterio=criterio)

    def test_primeiro_colocado_esta_classificado(self):
        interessado = InteressadoFactory(pcd_fisica=True)
        inscricao = InscricaoFactory(evento=self.evento, interessado=interessado)
        InscricaoFactory(evento=self.evento)
        InscricaoFactory(evento=self.evento)
        _rodar_comando(self.evento.id)
        classificacao = Classificacao.objects.get(inscricao=inscricao)
        assert classificacao.posicao == 1
        assert classificacao.classificado
        assert not classificacao.lista_espera

    def test_fora_das_vagas_esta_em_lista_espera(self):
        for _ in range(3):
            InscricaoFactory(evento=self.evento)
        _rodar_comando(self.evento.id)
        ultima = Classificacao.objects.get(posicao=3)
        assert not ultima.classificado
        assert ultima.lista_espera

    def test_total_de_classificacoes_igual_ao_total_de_inscricoes(self):
        for _ in range(4):
            InscricaoFactory(evento=self.evento)
        _rodar_comando(self.evento.id)
        assert Classificacao.objects.count() == 4

    def test_posicoes_sao_unicas(self):
        for _ in range(3):
            InscricaoFactory(evento=self.evento)
        _rodar_comando(self.evento.id)
        posicoes = list(Classificacao.objects.values_list('posicao', flat=True))
        assert len(posicoes) == len(set(posicoes))


class TestClassificarEventoDesempatePorIdade:
    """Testa desempate por idade (JOVEM = mais novo, IDOSO = mais velho)."""

    def test_desempate_jovem_prioriza_mais_novo(self):
        evento = EventoFactory(total_vagas=1)
        criterio = CriterioFactory(codigo='JOVEM', pontos=5, tipo_criterio='PONTUACAO')
        EventoCriterioFactory(evento=evento, criterio=criterio)
        mais_novo = InteressadoFactory(data_nascimento=_idade_para_nascimento(17))
        mais_velho = InteressadoFactory(data_nascimento=_idade_para_nascimento(22))
        insc_novo = InscricaoFactory(evento=evento, interessado=mais_novo)
        insc_velho = InscricaoFactory(evento=evento, interessado=mais_velho)
        _rodar_comando(evento.id)
        assert Classificacao.objects.get(inscricao=insc_novo).posicao == 1
        assert Classificacao.objects.get(inscricao=insc_velho).posicao == 2

    def test_desempate_idoso_prioriza_mais_velho(self):
        evento = EventoFactory(total_vagas=1)
        criterio = CriterioFactory(codigo='IDOSO', pontos=8, tipo_criterio='PONTUACAO')
        EventoCriterioFactory(evento=evento, criterio=criterio)
        mais_velho = InteressadoFactory(data_nascimento=_idade_para_nascimento(70))
        mais_novo = InteressadoFactory(data_nascimento=_idade_para_nascimento(51))
        insc_velho = InscricaoFactory(evento=evento, interessado=mais_velho)
        insc_novo = InscricaoFactory(evento=evento, interessado=mais_novo)
        _rodar_comando(evento.id)
        assert Classificacao.objects.get(inscricao=insc_velho).posicao == 1
        assert Classificacao.objects.get(inscricao=insc_novo).posicao == 2


class TestClassificarEventoIdempotencia:
    """Rodar o comando duas vezes não deve duplicar registros."""

    def test_segunda_execucao_nao_duplica_classificacao(self):
        evento = EventoFactory(total_vagas=5)
        criterio = CriterioFactory(codigo='PCD', pontos=10, tipo_criterio='PONTUACAO')
        EventoCriterioFactory(evento=evento, criterio=criterio)
        InscricaoFactory(evento=evento)
        _rodar_comando(evento.id)
        _rodar_comando(evento.id)
        assert Classificacao.objects.count() == 1

    def test_segunda_execucao_nao_duplica_criterios_atendidos(self):
        evento = EventoFactory(total_vagas=5)
        criterio = CriterioFactory(codigo='PCD', pontos=10, tipo_criterio='PONTUACAO')
        EventoCriterioFactory(evento=evento, criterio=criterio)
        interessado = InteressadoFactory(pcd_fisica=True)
        InscricaoFactory(evento=evento, interessado=interessado)
        _rodar_comando(evento.id)
        _rodar_comando(evento.id)
        assert InscricaoCriterioAtendido.objects.count() == 1


class TestClassificarEventoStatusInscricao:
    """Apenas inscrições CONFIRMADA/APROVADA devem ser processadas."""

    def test_inscricao_pendente_e_ignorada(self):
        evento = EventoFactory(total_vagas=5)
        criterio = CriterioFactory(codigo='PCD', pontos=10, tipo_criterio='PONTUACAO')
        EventoCriterioFactory(evento=evento, criterio=criterio)
        status_pendente = StatusInscricaoFactory(nome='Pendente')
        InscricaoFactory(evento=evento, status=status_pendente)
        _rodar_comando(evento.id)
        assert Classificacao.objects.count() == 0

    def test_inscricao_confirmada_e_processada(self):
        evento = EventoFactory(total_vagas=5)
        criterio = CriterioFactory(codigo='PCD', pontos=10, tipo_criterio='PONTUACAO')
        EventoCriterioFactory(evento=evento, criterio=criterio)
        InscricaoFactory(evento=evento)
        _rodar_comando(evento.id)
        assert Classificacao.objects.count() == 1



