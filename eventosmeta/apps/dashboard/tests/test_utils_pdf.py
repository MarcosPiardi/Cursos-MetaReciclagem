"""
Arquivo: test_utils_pdf.py
Caminho: apps/dashboard/tests/test_utils_pdf.py
Atualizações
29/05/2026 - Criação do arquivo 
"""

from io import BytesIO
from unittest.mock import patch, MagicMock
from django.test import SimpleTestCase
from apps.dashboard.utils_pdf import (
    criar_grafico_pizza,
    criar_grafico_barras,
    gerar_pdf_interessados,
    gerar_pdf_eventos,
    gerar_pdf_academico,
    gerar_pdf_processo_seletivo,
)


class TestCriarGraficoPizza(SimpleTestCase):
    def test_dados_validos_retorna_buffer(self):
        labels = ["Masculino", "Feminino"]
        values = [30, 70]
        resultado = criar_grafico_pizza(labels, values, "Teste")
        self.assertIsNotNone(resultado)
        conteudo = resultado.getvalue()
        self.assertGreater(len(conteudo), 100)

    def test_todos_valores_zero_retorna_none(self):
        labels = ["Masculino", "Feminino"]
        values = [0, 0]
        resultado = criar_grafico_pizza(labels, values, "Teste")
        self.assertIsNone(resultado)

    def test_lista_vazia_retorna_none(self):
        resultado = criar_grafico_pizza([], [], "Teste")
        self.assertIsNone(resultado)

    def test_um_item_valido_retorna_buffer(self):
        labels = ["Unico"]
        values = [100]
        resultado = criar_grafico_pizza(labels, values, "Teste")
        self.assertIsNotNone(resultado)


class TestCriarGraficoBarras(SimpleTestCase):
    def test_dados_validos_retorna_buffer(self):
        labels = ["Faixa 1", "Faixa 2", "Faixa 3"]
        values = [10, 25, 15]
        resultado = criar_grafico_barras(labels, values, "Teste")
        self.assertIsNotNone(resultado)
        conteudo = resultado.getvalue()
        self.assertGreater(len(conteudo), 100)


class TestGerarPdfInteressados(SimpleTestCase):
    def test_context_minimo_retorna_buffer(self):
        context = {
            "total_interessados": 100,
            "interessados_matriculados": 60,
            "interessados_sem_matricula": 40,
            "distribuicao_sexo": [],
            "distribuicao_fototipo": [],
            "distribuicao_escolaridade": [],
            "distribuicao_programas": [],
            "distribuicao_deficiencia": [],
            "tipos_deficiencia": [],
            "faixas_etarias": [],
        }
        buffer = gerar_pdf_interessados(context)
        self.assertIsNotNone(buffer)
        conteudo = buffer.getvalue()
        self.assertTrue(conteudo.startswith(b"%PDF"), "Deve comecar com %PDF")


class TestGerarPdfEventos(SimpleTestCase):
    def test_context_minimo_retorna_buffer(self):
        context = {
            "total_eventos": 10,
            "eventos_inscricoes_abertas": 3,
            "total_turmas": 20,
            "turmas_futuras": 5,
            "turmas_em_andamento": 8,
            "turmas_encerradas": 7,
            "eventos_por_status": [],
            "top_eventos_inscricoes": [],
        }
        buffer = gerar_pdf_eventos(context)
        self.assertIsNotNone(buffer)
        conteudo = buffer.getvalue()
        self.assertTrue(conteudo.startswith(b"%PDF"))


class TestGerarPdfAcademico(SimpleTestCase):
    def test_context_minimo_retorna_buffer(self):
        context = {
            "total_avaliacoes": 50,
            "total_aprovados": 40,
            "total_reprovados": 10,
            "taxa_aprovacao": 80.0,
            "media_notas": 7.5,
            "media_frequencia": 85.0,
            "certificados_emitidos": 30,
            "top_cursos_aprovados": [],
        }
        buffer = gerar_pdf_academico(context)
        self.assertIsNotNone(buffer)
        conteudo = buffer.getvalue()
        self.assertTrue(conteudo.startswith(b"%PDF"))


class TestGerarPdfProcessoSeletivo(SimpleTestCase):
    def test_context_minimo_retorna_buffer(self):
        context = {
            "total_inscricoes": 200,
            "inscricoes_recentes": 45,
            "total_classificacoes": 150,
            "classificados": 100,
            "lista_espera": 50,
            "taxa_classificacao": 66.7,
            "top_eventos_inscricoes": [],
        }
        buffer = gerar_pdf_processo_seletivo(context)
        self.assertIsNotNone(buffer)
        conteudo = buffer.getvalue()
        self.assertTrue(conteudo.startswith(b"%PDF"))



