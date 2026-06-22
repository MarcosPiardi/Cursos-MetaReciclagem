"""
Arquivo: test_reports.py
Caminho: apps/selecao/tests/test_reports.py
Finalidade: Testes para o modulo de relatorios (formatação, PDF e Excel) do app selecao
Atualizacoes:
 - 28/05/2026 - Criacao de testes para formatacao (CPF, telefone)
 - 08/06/2026 - Refatoracao para pytest (unittest → pytest)
 - 19/06/2026 - Adicionados testes para geracao de PDF (staff/mural) e Excel (staff/mural)
Escopo:
- Formatacao: CPF, CPF mascarado e telefone
- Geracao PDF staff: status code, content type, filename, conteudo nao vazio
- Geracao PDF mural: status code, content type, filename
- Geracao Excel staff: status code, content type, filename
- Geracao Excel mural: status code, content type, filename
- Ordem classificacao e ordem nome
"""

import pytest
from apps.selecao.reports import RelatorioAprovadosService

pytestmark = pytest.mark.django_db

# ============================================================
# TESTES DE FORMATACAO (METODOS ESTATICOS PUROS)
# ============================================================

class TestRelatorioAprovadosService:
    """Testes herdados do arquivo original"""

    def test_formatar_cpf_valido(self):
        resultado = RelatorioAprovadosService.formatar_cpf('12345678900')
        assert resultado == '123.456.789-00'

    def test_formatar_cpf_none(self):
        resultado = RelatorioAprovadosService.formatar_cpf(None)
        assert resultado == '\u2014'

    def test_formatar_cpf_vazio(self):
        resultado = RelatorioAprovadosService.formatar_cpf('')
        assert resultado == '\u2014'

    def test_formatar_cpf_ja_formatado(self):
        resultado = RelatorioAprovadosService.formatar_cpf('123.456.789-00')
        assert resultado == '123.456.789-00'

    def test_formatar_cpf_menos_de_11(self):
        resultado = RelatorioAprovadosService.formatar_cpf('1234567890')
        assert resultado == '1234567890'

    def test_formatar_cpf_mascarado_valido(self):
        resultado = RelatorioAprovadosService.formatar_cpf_mascarado('12345678901')
        assert resultado == '123.4**.***-**'

    def test_formatar_cpf_mascarado_none(self):
        resultado = RelatorioAprovadosService.formatar_cpf_mascarado(None)
        assert resultado == '\u2014'

    def test_formatar_cpf_mascarado_vazio(self):
        resultado = RelatorioAprovadosService.formatar_cpf_mascarado('')
        assert resultado == '\u2014'

    def test_formatar_telefone_celular(self):
        resultado = RelatorioAprovadosService.formatar_telefone('31999999999')
        assert resultado == '(31) 99999-9999'

    def test_formatar_telefone_fixo(self):
        resultado = RelatorioAprovadosService.formatar_telefone('3133333333')
        assert resultado == '(31) 3333-3333'

    def test_formatar_telefone_none(self):
        resultado = RelatorioAprovadosService.formatar_telefone(None)
        assert resultado == '\u2014'

    def test_formatar_telefone_vazio(self):
        resultado = RelatorioAprovadosService.formatar_telefone('')
        assert resultado == '\u2014'

    def test_formatar_telefone_ja_formatado(self):
        resultado = RelatorioAprovadosService.formatar_telefone('(31) 99999-9999')
        assert resultado == '(31) 99999-9999'

# ============================================================
# FIXTURE: evento com 3 classificacoes
# ============================================================

@pytest.fixture
def evento_com_classificacoes():
    """
    Cria um evento com 3 inscricoes classificadas.
    Usa factories existentes dos 3 apps.
    """
    from apps.eventos.tests.factories import EventoFactory, StatusFactory
    from apps.selecao.tests.factories import InscricaoFactory, ClassificacaoFactory, StatusInscricaoFactory
    from django.utils import timezone

    status_evento = StatusFactory()
    status_inscricao = StatusInscricaoFactory(nome="Pendente")
    evento = EventoFactory(status=status_evento, nome="Evento Teste Relatorio")

    classificacoes = []
    for i in range(3):
        inscricao = InscricaoFactory(evento=evento, status=status_inscricao)
        classificacao = ClassificacaoFactory(
            inscricao=inscricao,
            posicao=i + 1,
            pontuacao_total=float(100.0 - (i * 10)),
            classificado=(i < 2),
            lista_espera=(i >= 2),
            processado_em=timezone.now(),
        )
        classificacoes.append(classificacao)

    from apps.selecao.models import Classificacao
    qs = Classificacao.objects.filter(
        inscricao__evento=evento
    ).order_by("posicao")

    return {"evento": evento, "classificacoes": qs}

# ============================================================
# TESTES DE GERACAO PDF STAFF
# ============================================================

class TestGerarRelatorioStaff:
    def test_retorna_http_response(self, evento_com_classificacoes):
        response = RelatorioAprovadosService.gerar_relatorio_staff(
            evento=evento_com_classificacoes["evento"],
            classificacoes=evento_com_classificacoes["classificacoes"],
            ordem="classificacao"
        )
        assert response.status_code == 200

    def test_content_type_pdf(self, evento_com_classificacoes):
        response = RelatorioAprovadosService.gerar_relatorio_staff(
            evento=evento_com_classificacoes["evento"],
            classificacoes=evento_com_classificacoes["classificacoes"],
            ordem="classificacao"
        )
        assert response["Content-Type"] == "application/pdf"

    def test_content_disposition_inline(self, evento_com_classificacoes):
        response = RelatorioAprovadosService.gerar_relatorio_staff(
            evento=evento_com_classificacoes["evento"],
            classificacoes=evento_com_classificacoes["classificacoes"],
            ordem="classificacao"
        )
        assert "inline" in response["Content-Disposition"]
        assert ".pdf" in response["Content-Disposition"]

    def test_conteudo_nao_vazio(self, evento_com_classificacoes):
        response = RelatorioAprovadosService.gerar_relatorio_staff(
            evento=evento_com_classificacoes["evento"],
            classificacoes=evento_com_classificacoes["classificacoes"],
            ordem="classificacao"
        )
        assert len(response.content) > 0

    def test_filename_contem_staff(self, evento_com_classificacoes):
        response = RelatorioAprovadosService.gerar_relatorio_staff(
            evento=evento_com_classificacoes["evento"],
            classificacoes=evento_com_classificacoes["classificacoes"],
            ordem="classificacao"
        )
        assert "staff" in response["Content-Disposition"]

    def test_ordem_nome_altera_filename(self, evento_com_classificacoes):
        response = RelatorioAprovadosService.gerar_relatorio_staff(
            evento=evento_com_classificacoes["evento"],
            classificacoes=evento_com_classificacoes["classificacoes"],
            ordem="nome"
        )
        assert "nome" in response["Content-Disposition"]

# ============================================================
# TESTES DE GERACAO PDF MURAL
# ============================================================

class TestGerarRelatorioMural:
    def test_retorna_http_response(self, evento_com_classificacoes):
        response = RelatorioAprovadosService.gerar_relatorio_mural(
            evento=evento_com_classificacoes["evento"],
            classificacoes=evento_com_classificacoes["classificacoes"],
            ordem="classificacao"
        )
        assert response.status_code == 200

    def test_content_type_pdf(self, evento_com_classificacoes):
        response = RelatorioAprovadosService.gerar_relatorio_mural(
            evento=evento_com_classificacoes["evento"],
            classificacoes=evento_com_classificacoes["classificacoes"],
            ordem="classificacao"
        )
        assert response["Content-Type"] == "application/pdf"

    def test_content_disposition_inline(self, evento_com_classificacoes):
        response = RelatorioAprovadosService.gerar_relatorio_mural(
            evento=evento_com_classificacoes["evento"],
            classificacoes=evento_com_classificacoes["classificacoes"],
            ordem="classificacao"
        )
        assert "inline" in response["Content-Disposition"]
        assert ".pdf" in response["Content-Disposition"]

    def test_filename_contem_mural(self, evento_com_classificacoes):
        response = RelatorioAprovadosService.gerar_relatorio_mural(
            evento=evento_com_classificacoes["evento"],
            classificacoes=evento_com_classificacoes["classificacoes"],
            ordem="classificacao"
        )
        assert "mural" in response["Content-Disposition"]

# ============================================================
# TESTES DE GERACAO EXCEL STAFF
# ============================================================

class TestGerarExcelStaff:
    def test_retorna_http_response(self, evento_com_classificacoes):
        response = RelatorioAprovadosService.gerar_excel_staff(
            evento=evento_com_classificacoes["evento"],
            classificacoes=evento_com_classificacoes["classificacoes"],
            ordem="classificacao"
        )
        assert response.status_code == 200

    def test_content_type_excel(self, evento_com_classificacoes):
        response = RelatorioAprovadosService.gerar_excel_staff(
            evento=evento_com_classificacoes["evento"],
            classificacoes=evento_com_classificacoes["classificacoes"],
            ordem="classificacao"
        )
        assert "spreadsheetml" in response["Content-Type"]

    def test_content_disposition_attachment(self, evento_com_classificacoes):
        response = RelatorioAprovadosService.gerar_excel_staff(
            evento=evento_com_classificacoes["evento"],
            classificacoes=evento_com_classificacoes["classificacoes"],
            ordem="classificacao"
        )
        assert "attachment" in response["Content-Disposition"]
        assert ".xlsx" in response["Content-Disposition"]

    def test_filename_contem_staff(self, evento_com_classificacoes):
        response = RelatorioAprovadosService.gerar_excel_staff(
            evento=evento_com_classificacoes["evento"],
            classificacoes=evento_com_classificacoes["classificacoes"],
            ordem="classificacao"
        )
        assert "staff" in response["Content-Disposition"]

    def test_conteudo_nao_vazio(self, evento_com_classificacoes):
        response = RelatorioAprovadosService.gerar_excel_staff(
            evento=evento_com_classificacoes["evento"],
            classificacoes=evento_com_classificacoes["classificacoes"],
            ordem="classificacao"
        )
        assert len(response.content) > 0

# ============================================================
# TESTES DE GERACAO EXCEL MURAL
# ============================================================

class TestGerarExcelMural:
    def test_retorna_http_response(self, evento_com_classificacoes):
        response = RelatorioAprovadosService.gerar_excel_mural(
            evento=evento_com_classificacoes["evento"],
            classificacoes=evento_com_classificacoes["classificacoes"],
            ordem="classificacao"
        )
        assert response.status_code == 200

    def test_content_type_excel(self, evento_com_classificacoes):
        response = RelatorioAprovadosService.gerar_excel_mural(
            evento=evento_com_classificacoes["evento"],
            classificacoes=evento_com_classificacoes["classificacoes"],
            ordem="classificacao"
        )
        assert "spreadsheetml" in response["Content-Type"]

    def test_filename_contem_mural(self, evento_com_classificacoes):
        response = RelatorioAprovadosService.gerar_excel_mural(
            evento=evento_com_classificacoes["evento"],
            classificacoes=evento_com_classificacoes["classificacoes"],
            ordem="classificacao"
        )
        assert "mural" in response["Content-Disposition"]




