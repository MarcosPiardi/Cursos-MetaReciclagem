"""
Arquivo: test_reports.py
Caminho: apps/selecao/tests/test_reports.py
Atualizações: 
 - 28/05/2026 - Criando testes para geração de relatórios de classificação.
 - 08/06/2026 - Refatoração para pytest (unittest → pytest)
"""

import pytest
from apps.selecao.reports import RelatorioAprovadosService

@pytest.mark.django_db
class TestRelatorioAprovadosService:
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

