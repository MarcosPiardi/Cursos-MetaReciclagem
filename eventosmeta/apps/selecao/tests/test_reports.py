"""
Arquivo: test_reports.py
Caminho: apps/selecao/tests/test_reports.py
Atualizações: 
- 28/05/2026 - Criando testes para geração de relatórios de classificação.
"""

from django.test import TestCase
from apps.selecao.reports import RelatorioAprovadosService


class TestRelatorioAprovadosService(TestCase):
    def test_formatar_cpf_valido(self):
        resultado = RelatorioAprovadosService.formatar_cpf('12345678900')
        self.assertEqual(resultado, '123.456.789-00')

    def test_formatar_cpf_none(self):
        resultado = RelatorioAprovadosService.formatar_cpf(None)
        self.assertEqual(resultado, '\u2014')

    def test_formatar_cpf_vazio(self):
        resultado = RelatorioAprovadosService.formatar_cpf('')
        self.assertEqual(resultado, '\u2014')

    def test_formatar_cpf_ja_formatado(self):
        resultado = RelatorioAprovadosService.formatar_cpf('123.456.789-00')
        self.assertEqual(resultado, '123.456.789-00')

    def test_formatar_cpf_menos_de_11(self):
        resultado = RelatorioAprovadosService.formatar_cpf('1234567890')
        self.assertEqual(resultado, '1234567890')

    def test_formatar_cpf_mascarado_valido(self):
        resultado = RelatorioAprovadosService.formatar_cpf_mascarado('12345678901')
        self.assertEqual(resultado, '123.4**.***-**')

    def test_formatar_cpf_mascarado_none(self):
        resultado = RelatorioAprovadosService.formatar_cpf_mascarado(None)
        self.assertEqual(resultado, '\u2014')

    def test_formatar_cpf_mascarado_vazio(self):
        resultado = RelatorioAprovadosService.formatar_cpf_mascarado('')
        self.assertEqual(resultado, '\u2014')

    def test_formatar_telefone_celular(self):
        resultado = RelatorioAprovadosService.formatar_telefone('31999999999')
        self.assertEqual(resultado, '(31) 99999-9999')

    def test_formatar_telefone_fixo(self):
        resultado = RelatorioAprovadosService.formatar_telefone('3133333333')
        self.assertEqual(resultado, '(31) 3333-3333')

    def test_formatar_telefone_none(self):
        resultado = RelatorioAprovadosService.formatar_telefone(None)
        self.assertEqual(resultado, '\u2014')

    def test_formatar_telefone_vazio(self):
        resultado = RelatorioAprovadosService.formatar_telefone('')
        self.assertEqual(resultado, '\u2014')

    def test_formatar_telefone_ja_formatado(self):
        resultado = RelatorioAprovadosService.formatar_telefone('(31) 99999-9999')
        self.assertEqual(resultado, '(31) 99999-9999')



