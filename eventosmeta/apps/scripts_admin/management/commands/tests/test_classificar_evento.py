"""
Arquivo: test_classificar_evento.py
Caminho: apps/selecao/tests/test_classificar_evento.py
Finalidade: Testes automatizados do management command classificar_evento
Esse feito diretamente pelo Claude, com base na análise do código do comando e dos modelos envolvidos.
Data: 02/06/2026 - v1.0 - Criação dos testes (todos os 8 cenários).
"""

import hashlib
from datetime import date, timedelta
from io import StringIO

import factory
from django.core.management import call_command
from django.test import TestCase
from django.utils import timezone
from factory.django import DjangoModelFactory
from factory import LazyFunction, Sequence

from apps.eventos.models import Evento, EventoCriterio, Criterio, Status
from apps.interessados.models import Interessado, Fototipo, Sexo
from apps.selecao.models import Inscricao, Classificacao, InscricaoCriterioAtendido, StatusInscricao


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
    data_nascimento = date(1990, 1, 1)  # 35 anos — adulto padrão
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

class ClassificarEventoEventoNaoEncontradoTest(TestCase):
    """Evento com ID inexistente."""

    def test_evento_inexistente_exibe_erro(self):
        out = _rodar_comando(evento_id=99999)
        self.assertIn("não encontrado", out)


class ClassificarEventoSemInscricoesTest(TestCase):
    """Evento sem inscrições confirmadas."""

    def setUp(self):
        self.evento = EventoFactory()

    def test_sem_inscricoes_confirmadas_exibe_aviso(self):
        out = _rodar_comando(self.evento.id)
        self.assertIn("Nenhuma inscrição", out)

    def test_sem_inscricoes_nao_cria_classificacao(self):
        _rodar_comando(self.evento.id)
        self.assertEqual(Classificacao.objects.count(), 0)


class ClassificarEventoSemCriteriosTest(TestCase):
    """Evento com inscrição confirmada, mas sem critérios ativos."""

    def setUp(self):
        self.evento = EventoFactory()
        InscricaoFactory(evento=self.evento)

    def test_sem_criterios_exibe_aviso(self):
        out = _rodar_comando(self.evento.id)
        self.assertIn("Nenhum critério", out)


class ClassificarEventoPontuacaoTest(TestCase):
    """Testa o cálculo de pontuação para cada critério."""

    def setUp(self):
        self.evento = EventoFactory(total_vagas=10)

    def _criar_criterio_e_inscricao(self, codigo, pontos, interessado_kwargs):
        criterio = CriterioFactory(codigo=codigo, pontos=pontos, tipo_criterio="PONTUACAO")
        EventoCriterioFactory(evento=self.evento, criterio=criterio)
        interessado = InteressadoFactory(**interessado_kwargs)
        return InscricaoFactory(evento=self.evento, interessado=interessado)

    def test_criterio_pcd_atribuido(self):
        inscricao = self._criar_criterio_e_inscricao(
            codigo='PCD', pontos=10,
            interessado_kwargs={'pcd_fisica': True}
        )
        _rodar_comando(self.evento.id)
        classificacao = Classificacao.objects.get(inscricao=inscricao)
        self.assertEqual(classificacao.pontuacao_total, 10)

    def test_criterio_pcd_nao_atribuido_quando_sem_deficiencia(self):
        inscricao = self._criar_criterio_e_inscricao(
            codigo='PCD', pontos=10,
            interessado_kwargs={}  # sem nenhum pcd_*
        )
        _rodar_comando(self.evento.id)
        classificacao = Classificacao.objects.get(inscricao=inscricao)
        self.assertEqual(classificacao.pontuacao_total, 0)

    def test_criterio_nis_atribuido(self):
        inscricao = self._criar_criterio_e_inscricao(
            codigo='NIS', pontos=15,
            interessado_kwargs={'num_nis': '12345678901'}
        )
        _rodar_comando(self.evento.id)
        classificacao = Classificacao.objects.get(inscricao=inscricao)
        self.assertEqual(classificacao.pontuacao_total, 15)

    def test_criterio_nis_nao_atribuido_sem_nis(self):
        inscricao = self._criar_criterio_e_inscricao(
            codigo='NIS', pontos=15,
            interessado_kwargs={'num_nis': ''}
        )
        _rodar_comando(self.evento.id)
        classificacao = Classificacao.objects.get(inscricao=inscricao)
        self.assertEqual(classificacao.pontuacao_total, 0)

    def test_criterio_jovem_atribuido_16_anos(self):
        inscricao = self._criar_criterio_e_inscricao(
            codigo='JOVEM', pontos=5,
            interessado_kwargs={'data_nascimento': _idade_para_nascimento(16)}
        )
        _rodar_comando(self.evento.id)
        classificacao = Classificacao.objects.get(inscricao=inscricao)
        self.assertEqual(classificacao.pontuacao_total, 5)

    def test_criterio_jovem_atribuido_24_anos(self):
        inscricao = self._criar_criterio_e_inscricao(
            codigo='JOVEM', pontos=5,
            interessado_kwargs={'data_nascimento': _idade_para_nascimento(24)}
        )
        _rodar_comando(self.evento.id)
        classificacao = Classificacao.objects.get(inscricao=inscricao)
        self.assertEqual(classificacao.pontuacao_total, 5)

    def test_criterio_jovem_nao_atribuido_para_adulto(self):
        inscricao = self._criar_criterio_e_inscricao(
            codigo='JOVEM', pontos=5,
            interessado_kwargs={'data_nascimento': _idade_para_nascimento(35)}
        )
        _rodar_comando(self.evento.id)
        classificacao = Classificacao.objects.get(inscricao=inscricao)
        self.assertEqual(classificacao.pontuacao_total, 0)

    def test_criterio_idoso_atribuido_50_anos(self):
        inscricao = self._criar_criterio_e_inscricao(
            codigo='IDOSO', pontos=8,
            interessado_kwargs={'data_nascimento': _idade_para_nascimento(50)}
        )
        _rodar_comando(self.evento.id)
        classificacao = Classificacao.objects.get(inscricao=inscricao)
        self.assertEqual(classificacao.pontuacao_total, 8)

    def test_criterio_idoso_nao_atribuido_para_49_anos(self):
        inscricao = self._criar_criterio_e_inscricao(
            codigo='IDOSO', pontos=8,
            interessado_kwargs={'data_nascimento': _idade_para_nascimento(49)}
        )
        _rodar_comando(self.evento.id)
        classificacao = Classificacao.objects.get(inscricao=inscricao)
        self.assertEqual(classificacao.pontuacao_total, 0)

    def test_criterio_cota_racial_preta(self):
        fototipo = FototipoFactory(nome='Preta')
        inscricao = self._criar_criterio_e_inscricao(
            codigo='COTA_RACIAL', pontos=10,
            interessado_kwargs={'fototipo': fototipo}
        )
        _rodar_comando(self.evento.id)
        classificacao = Classificacao.objects.get(inscricao=inscricao)
        self.assertEqual(classificacao.pontuacao_total, 10)

    def test_criterio_cota_racial_parda(self):
        fototipo = FototipoFactory(nome='Parda')
        inscricao = self._criar_criterio_e_inscricao(
            codigo='COTA_RACIAL', pontos=10,
            interessado_kwargs={'fototipo': fototipo}
        )
        _rodar_comando(self.evento.id)
        classificacao = Classificacao.objects.get(inscricao=inscricao)
        self.assertEqual(classificacao.pontuacao_total, 10)

    def test_criterio_cota_racial_indigena(self):
        fototipo = FototipoFactory(nome='Indígena')
        inscricao = self._criar_criterio_e_inscricao(
            codigo='COTA_RACIAL', pontos=10,
            interessado_kwargs={'fototipo': fototipo}
        )
        _rodar_comando(self.evento.id)
        classificacao = Classificacao.objects.get(inscricao=inscricao)
        self.assertEqual(classificacao.pontuacao_total, 10)

    def test_criterio_cota_racial_nao_atribuido_para_branca(self):
        fototipo = FototipoFactory(nome='Branca')
        inscricao = self._criar_criterio_e_inscricao(
            codigo='COTA_RACIAL', pontos=10,
            interessado_kwargs={'fototipo': fototipo}
        )
        _rodar_comando(self.evento.id)
        classificacao = Classificacao.objects.get(inscricao=inscricao)
        self.assertEqual(classificacao.pontuacao_total, 0)

    def test_criterio_cota_racial_sem_fototipo(self):
        inscricao = self._criar_criterio_e_inscricao(
            codigo='COTA_RACIAL', pontos=10,
            interessado_kwargs={'fototipo': None}
        )
        _rodar_comando(self.evento.id)
        classificacao = Classificacao.objects.get(inscricao=inscricao)
        self.assertEqual(classificacao.pontuacao_total, 0)

    def test_criterio_escolaridade_fundamental_incompleto(self):
        inscricao = self._criar_criterio_e_inscricao(
            codigo='ESC_FUND_INC', pontos=5,
            interessado_kwargs={'escolaridade': 'FUNDAMENTAL_INCOMPLETO'}
        )
        _rodar_comando(self.evento.id)
        classificacao = Classificacao.objects.get(inscricao=inscricao)
        self.assertEqual(classificacao.pontuacao_total, 5)

    def test_criterio_escolaridade_medio_completo(self):
        inscricao = self._criar_criterio_e_inscricao(
            codigo='ESC_MEDIO_COMP', pontos=3,
            interessado_kwargs={'escolaridade': 'MEDIO_COMPLETO'}
        )
        _rodar_comando(self.evento.id)
        classificacao = Classificacao.objects.get(inscricao=inscricao)
        self.assertEqual(classificacao.pontuacao_total, 3)

    def test_multiplos_criterios_somam_pontos(self):
        crit_pcd = CriterioFactory(codigo='PCD', pontos=10, tipo_criterio='PONTUACAO')
        crit_nis = CriterioFactory(codigo='NIS', pontos=15, tipo_criterio='PONTUACAO')
        EventoCriterioFactory(evento=self.evento, criterio=crit_pcd)
        EventoCriterioFactory(evento=self.evento, criterio=crit_nis)
        interessado = InteressadoFactory(pcd_fisica=True, num_nis='12345678901')
        inscricao = InscricaoFactory(evento=self.evento, interessado=interessado)
        _rodar_comando(self.evento.id)
        classificacao = Classificacao.objects.get(inscricao=inscricao)
        self.assertEqual(classificacao.pontuacao_total, 25)


class ClassificarEventoCriterioOrdenacaoTest(TestCase):
    """Critérios do tipo ORDENACAO não devem somar pontos."""

    def test_criterio_ordenacao_nao_soma_pontos(self):
        evento = EventoFactory(total_vagas=10)
        criterio = CriterioFactory(codigo='ORD01', tipo_criterio='ORDENACAO', pontos=0)
        EventoCriterioFactory(evento=evento, criterio=criterio)
        inscricao = InscricaoFactory(evento=evento)
        _rodar_comando(evento.id)
        classificacao = Classificacao.objects.get(inscricao=inscricao)
        self.assertEqual(classificacao.pontuacao_total, 0)


class ClassificarEventoPosicaoTest(TestCase):
    """Testa a atribuição de posições e flags classificado/lista_espera."""

    def setUp(self):
        self.evento = EventoFactory(total_vagas=2)
        criterio = CriterioFactory(codigo='PCD', pontos=10, tipo_criterio='PONTUACAO')
        EventoCriterioFactory(evento=self.evento, criterio=criterio)

    def test_primeiro_colocado_esta_classificado(self):
        # Interessado com PCD (10 pts) deve ser o 1º
        interessado = InteressadoFactory(pcd_fisica=True)
        inscricao = InscricaoFactory(evento=self.evento, interessado=interessado)
        InscricaoFactory(evento=self.evento)  # 2º (0 pts)
        InscricaoFactory(evento=self.evento)  # 3º (0 pts)
        _rodar_comando(self.evento.id)
        classificacao = Classificacao.objects.get(inscricao=inscricao)
        self.assertEqual(classificacao.posicao, 1)
        self.assertTrue(classificacao.classificado)
        self.assertFalse(classificacao.lista_espera)

    def test_fora_das_vagas_esta_em_lista_espera(self):
        # 2 vagas, 3 inscritos sem pontuação — o último fica em espera
        inscricoes = [InscricaoFactory(evento=self.evento) for _ in range(3)]
        _rodar_comando(self.evento.id)
        ultima = Classificacao.objects.get(posicao=3)
        self.assertFalse(ultima.classificado)
        self.assertTrue(ultima.lista_espera)

    def test_total_de_classificacoes_igual_ao_total_de_inscricoes(self):
        for _ in range(4):
            InscricaoFactory(evento=self.evento)
        _rodar_comando(self.evento.id)
        self.assertEqual(Classificacao.objects.count(), 4)

    def test_posicoes_sao_unicas(self):
        for _ in range(3):
            InscricaoFactory(evento=self.evento)
        _rodar_comando(self.evento.id)
        posicoes = list(Classificacao.objects.values_list('posicao', flat=True))
        self.assertEqual(len(posicoes), len(set(posicoes)))


class ClassificarEventoDesempatePorIdadeTest(TestCase):
    """Testa desempate por idade (JOVEM = mais novo primeiro, IDOSO = mais velho primeiro)."""

    def test_desempate_jovem_prioriza_mais_novo(self):
        evento = EventoFactory(total_vagas=1)
        criterio = CriterioFactory(codigo='JOVEM', pontos=5, tipo_criterio='PONTUACAO')
        EventoCriterioFactory(evento=evento, criterio=criterio)

        # Ambos são jovens (mesma pontuação), o mais novo deve ficar em 1º
        mais_novo = InteressadoFactory(data_nascimento=_idade_para_nascimento(17))
        mais_velho = InteressadoFactory(data_nascimento=_idade_para_nascimento(22))
        insc_novo = InscricaoFactory(evento=evento, interessado=mais_novo)
        insc_velho = InscricaoFactory(evento=evento, interessado=mais_velho)
        _rodar_comando(evento.id)
        self.assertEqual(Classificacao.objects.get(inscricao=insc_novo).posicao, 1)
        self.assertEqual(Classificacao.objects.get(inscricao=insc_velho).posicao, 2)

    def test_desempate_idoso_prioriza_mais_velho(self):
        evento = EventoFactory(total_vagas=1)
        criterio = CriterioFactory(codigo='IDOSO', pontos=8, tipo_criterio='PONTUACAO')
        EventoCriterioFactory(evento=evento, criterio=criterio)

        mais_velho = InteressadoFactory(data_nascimento=_idade_para_nascimento(70))
        mais_novo = InteressadoFactory(data_nascimento=_idade_para_nascimento(51))
        insc_velho = InscricaoFactory(evento=evento, interessado=mais_velho)
        insc_novo = InscricaoFactory(evento=evento, interessado=mais_novo)
        _rodar_comando(evento.id)
        self.assertEqual(Classificacao.objects.get(inscricao=insc_velho).posicao, 1)
        self.assertEqual(Classificacao.objects.get(inscricao=insc_novo).posicao, 2)


class ClassificarEventoIdempotenciaTest(TestCase):
    """Rodar o comando duas vezes não deve duplicar registros."""

    def test_segunda_execucao_nao_duplica_classificacao(self):
        evento = EventoFactory(total_vagas=5)
        criterio = CriterioFactory(codigo='PCD', pontos=10, tipo_criterio='PONTUACAO')
        EventoCriterioFactory(evento=evento, criterio=criterio)
        InscricaoFactory(evento=evento)
        _rodar_comando(evento.id)
        _rodar_comando(evento.id)
        self.assertEqual(Classificacao.objects.count(), 1)

    def test_segunda_execucao_nao_duplica_criterios_atendidos(self):
        evento = EventoFactory(total_vagas=5)
        criterio = CriterioFactory(codigo='PCD', pontos=10, tipo_criterio='PONTUACAO')
        EventoCriterioFactory(evento=evento, criterio=criterio)
        interessado = InteressadoFactory(pcd_fisica=True)
        InscricaoFactory(evento=evento, interessado=interessado)
        _rodar_comando(evento.id)
        _rodar_comando(evento.id)
        self.assertEqual(InscricaoCriterioAtendido.objects.count(), 1)


class ClassificarEventoStatusInscricaoTest(TestCase):
    """Apenas inscrições CONFIRMADA/APROVADA devem ser processadas."""

    def test_inscricao_pendente_e_ignorada(self):
        evento = EventoFactory(total_vagas=5)
        criterio = CriterioFactory(codigo='PCD', pontos=10, tipo_criterio='PONTUACAO')
        EventoCriterioFactory(evento=evento, criterio=criterio)
        status_pendente = StatusInscricaoFactory(nome='Pendente')
        InscricaoFactory(evento=evento, status=status_pendente)
        _rodar_comando(evento.id)
        self.assertEqual(Classificacao.objects.count(), 0)

    def test_inscricao_confirmada_e_processada(self):
        evento = EventoFactory(total_vagas=5)
        criterio = CriterioFactory(codigo='PCD', pontos=10, tipo_criterio='PONTUACAO')
        EventoCriterioFactory(evento=evento, criterio=criterio)
        status_conf = StatusInscricaoFactory(nome='Confirmada')
        InscricaoFactory(evento=evento, status=status_conf)
        _rodar_comando(evento.id)
        self.assertEqual(Classificacao.objects.count(), 1)


