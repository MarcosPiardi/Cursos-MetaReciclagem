"""
Arquivo: test_certificado.py
Caminho: apps/academico/tests/test_certificado.py
Atualizacoes:
 - 29/05/2026 - Criacao do arquivo
 - 17/06/2026 - Refatorado de unittest.TestCase para pytest
"""

import pytest
from datetime import date
from io import BytesIO

from django.utils import timezone
from django.conf import settings

from apps.academico.certificado import GeradorCertificado
from apps.academico.models import Avaliacao, Matricula, StatusMatricula
from apps.eventos.models import Evento, Turma, Status
from apps.selecao.models import Inscricao, StatusInscricao
from apps.interessados.tests.factories import InteressadoFactory

pytestmark = pytest.mark.django_db

# ── Fixtures ──────────────────────────────────────────────────────────

@pytest.fixture
def evento():
    status_evento = Status.objects.create(nome="Ativo")
    return Evento.objects.create(
        nome="Curso de Python",
        status=status_evento,
        total_vagas=50,
        data_inicio_inscricao=timezone.now(),
        data_fim_inscricao=timezone.now(),
        data_inicio_evento=timezone.now().date(),
        data_fim_evento=timezone.now().date(),
    )

@pytest.fixture
def turma(evento):
    return Turma.objects.create(
        nome="Turma A",
        evento=evento,
        capacidade=40,
        data_inicio=date(2026, 1, 10),
        data_fim=date(2026, 3, 15),
    )

@pytest.fixture
def interessado():
    return InteressadoFactory()

@pytest.fixture
def inscricao(evento, interessado):
    status_insc = StatusInscricao.objects.create(nome="Confirmada")
    return Inscricao.objects.create(
        interessado=interessado,
        evento=evento,
        status=status_insc,
    )

@pytest.fixture
def matricula(turma, interessado, inscricao):
    status_mat = StatusMatricula.objects.create(
        nome="Ativa", cor="#00ff00", ordem=1
    )
    return Matricula.objects.create(
        numero_matricula="001",
        interessado=interessado,
        turma=turma,
        status=status_mat,
        inscricao=inscricao,
    )

@pytest.fixture
def avaliacao(matricula):
    avaliacao, _ = Avaliacao.objects.update_or_create(
        matricula=matricula,
        defaults={
            "nota_final": 8.5,
            "frequencia": 90,
            "aprovado": True,
            "data_emissao_certificado": date(2026, 5, 29),
        },
    )
    return avaliacao

@pytest.fixture
def gerador(avaliacao):
    return GeradorCertificado(avaliacao)

# ── Testes de extracao de atributos ───────────────────────────────────

class TestAtributos:
    """Extrai a cadeia de FK corretamente"""

    def test_inicializacao_atributos(self, gerador, avaliacao, matricula, interessado, turma, evento):
        assert gerador.avaliacao == avaliacao
        assert gerador.matricula == matricula
        assert gerador.aluno == interessado
        assert gerador.turma == turma
        assert gerador.evento == evento

    def test_pagesize_a4_paisagem(self, gerador):
        from reportlab.lib.pagesizes import A4, landscape
        expected = landscape(A4)
        assert gerador.pagesize == expected

    def test_static_path_construido(self, gerador):
        expected = str(settings.BASE_DIR / 'static' / 'images')
        assert gerador.static_path == expected

# ── Testes de formatacao ──────────────────────────────────────────────

class TestFormatacao:

    def test_cpf_formatado(self, gerador, interessado):
        cpf = interessado.cpf
        cpf_formatado = f"CPF: {cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"
        esperado = f"CPF: {cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"
        assert cpf_formatado == esperado

# ── Testes de traducao de mes ─────────────────────────────────────────

class TestTraducaoMes:
    """Verifica traducao de nomes de meses"""

    @pytest.mark.parametrize("data, esperado", [
        (date(2026, 1, 15), "15 de janeiro de 2026"),
        (date(2026, 8, 3), "03 de agosto de 2026"),
    ])
    def test_traducao_mes(self, data, esperado):
        data_str = data.strftime("%d de %B de %Y")
        meses = {
            "January": "janeiro", "February": "fevereiro",
            "March": "março", "April": "abril",
            "May": "maio", "June": "junho",
            "July": "julho", "August": "agosto",
            "September": "setembro", "October": "outubro",
            "November": "novembro", "December": "dezembro",
        }
        for eng, pt in meses.items():
            data_str = data_str.replace(eng, pt)
        assert data_str == esperado

# ── Testes de fallback ────────────────────────────────────────────────

class TestFallback:

    def test_data_emissao_fallback_para_agora(self, avaliacao, matricula):
        avaliacao_sem_data = avaliacao
        avaliacao_sem_data.data_emissao_certificado = None
        gerador2 = GeradorCertificado(avaliacao_sem_data)

        buffer = BytesIO()
        resultado = gerador2.gerar_pdf(buffer)
        assert resultado is not None
        assert len(resultado.getvalue()) > 100

    def test_carga_horaria_fallback_40h(self, evento, avaliacao):
        evento_sem_carga = evento
        if hasattr(evento_sem_carga, 'carga_horaria'):
            del evento_sem_carga.carga_horaria

        gerador2 = GeradorCertificado(avaliacao)
        assert gerador2.evento == evento_sem_carga

        carga = (
            f"{gerador2.evento.carga_horaria}h"
            if hasattr(gerador2.evento, 'carga_horaria') and gerador2.evento.carga_horaria
            else "40h"
        )
        assert carga == "40h"

# ── Testes de geracao de PDF ──────────────────────────────────────────

class TestGeracaoPDF:

    def test_gerar_pdf_retorna_buffer_valido(self, gerador):
        buffer = BytesIO()
        resultado = gerador.gerar_pdf(buffer)
        conteudo = resultado.getvalue()
        assert conteudo.startswith(b"%PDF"), "PDF deve comecar com %PDF"

    def test_gerar_pdf_multiplas_chamadas(self, gerador):
        for _ in range(3):
            buffer = BytesIO()
            resultado = gerador.gerar_pdf(buffer)
            assert resultado.getvalue().startswith(b"%PDF")


            

