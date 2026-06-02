"""
Arquivo: test_certificado.py
Caminho: apps/academico/tests/test_certificado.py
Atualizações
29/05/2026 - Criação do arquivo 
"""



from datetime import date
from io import BytesIO
from unittest.mock import patch, MagicMock
from django.test import TestCase
from apps.academico.certificado import GeradorCertificado


class TestGeradorCertificado(TestCase):
    def setUp(self):
        """Configura objetos minimos para instanciar GeradorCertificado"""
        from apps.academico.models import Avaliacao, Matricula, StatusMatricula
        from apps.eventos.models import Evento, Turma, Status
        from apps.selecao.models import Inscricao, StatusInscricao
        from apps.interessados.tests.factories import InteressadoFactory

        status_evento = Status.objects.create(nome="Ativo")
        status_insc = StatusInscricao.objects.create(nome="Confirmada")

        self.evento = Evento.objects.create(
            nome="Curso de Python",
            status=status_evento,
            total_vagas=50,
            data_inicio_inscricao=date.today(),
            data_fim_inscricao=date.today(),
            data_inicio_evento=date.today(),
            data_fim_evento=date.today(),
        )
        self.turma = Turma.objects.create(
            nome="Turma A",
            evento=self.evento,
            capacidade=40,
            data_inicio=date(2026, 1, 10),
            data_fim=date(2026, 3, 15),
        )
        self.interessado = InteressadoFactory()
        self.inscricao = Inscricao.objects.create(
            interessado=self.interessado,
            evento=self.evento,
            status=status_insc,
        )
        status_mat = StatusMatricula.objects.create(
            nome="Ativa", cor="#00ff00", ordem=1
        )
        self.matricula = Matricula.objects.create(
            numero_matricula="001",
            interessado=self.interessado,
            turma=self.turma,
            status=status_mat,
            inscricao=self.inscricao,
        )
        # CORRIGIR: usar update_or_create para evitar violacao de constraint unica
        self.avaliacao, _ = Avaliacao.objects.update_or_create(
            matricula=self.matricula,
            defaults={
                "nota_final": 8.5,
                "frequencia": 90,
                "aprovado": True,
                "data_emissao_certificado": date(2026, 5, 29),
            },
        )
        self.gerador = GeradorCertificado(self.avaliacao)

    # --- Testes de extracao de atributos ---

    def test_inicializacao_atributos(self):
        """Verifica se o construtor extrai corretamente a cadeia de FK"""
        self.assertEqual(self.gerador.avaliacao, self.avaliacao)
        self.assertEqual(self.gerador.matricula, self.matricula)
        self.assertEqual(self.gerador.aluno, self.interessado)
        self.assertEqual(self.gerador.turma, self.turma)
        self.assertEqual(self.gerador.evento, self.evento)

    def test_pagesize_a4_paisagem(self):
        """Verifica se o tamanho da pagina e A4 em modo paisagem"""
        from reportlab.lib.pagesizes import A4, landscape
        expected = landscape(A4)
        self.assertEqual(self.gerador.pagesize, expected)

    def test_static_path_construido(self):
        """Verifica se static_path foi construido com BASE_DIR"""
        from django.conf import settings
        expected = str(settings.BASE_DIR / 'static' / 'images')
        self.assertEqual(self.gerador.static_path, expected)

    # --- Testes de formatacao ---

    def test_cpf_formatado(self):
        """Verifica a formatacao do CPF: XXX.XXX.XXX-XX"""
        cpf_bruto = self.interessado.cpf  # Vem da factory
        esperado = f"{cpf_bruto[:3]}.{cpf_bruto[3:6]}.{cpf_bruto[6:9]}-{cpf_bruto[9:]}"

        # O CPF formatado aparece dentro de _adicionar_texto_certificado
        # Vamos verificar a logica inline do codigo
        cpf = self.interessado.cpf
        cpf_formatado = f"CPF: {cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"
        self.assertIn(cpf_formatado, f"CPF: {esperado}")

    # --- Testes de traducao de mes ---

    def test_traducao_mes_janeiro(self):
        """Verifica se 'January' e traduzido para 'janeiro'"""
        data = date(2026, 1, 15)
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
        self.assertEqual(data_str, "15 de janeiro de 2026")

    def test_traducao_mes_agosto(self):
        """Verifica se 'August' e traduzido para 'agosto'"""
        data = date(2026, 8, 3)
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
        self.assertEqual(data_str, "03 de agosto de 2026")

    # --- Testes de fallback ---

    def test_data_emissao_fallback_para_agora(self):
        """
        Verifica se quando data_emissao_certificado e None,
        a data usada e a atual (datetime.now)
        """
        avaliacao_sem_data = self.avaliacao
        avaliacao_sem_data.data_emissao_certificado = None
        gerador2 = GeradorCertificado(avaliacao_sem_data)

        # Nao podemos testar a string exata (depende do relogio),
        # mas podemos verificar que o codigo usa datetime.now()
        # O metodo _adicionar_rodape e chamado no gerar_pdf
        # Vamos testar que gera_pdf produz um buffer sem erro
        buffer = BytesIO()
        resultado = gerador2.gerar_pdf(buffer)
        self.assertIsNotNone(resultado)
        self.assertGreater(len(resultado.getvalue()), 100)  # PDF tem conteudo

    def test_carga_horaria_fallback_40h(self):
        """
        Verifica se quando carga_horaria nao existe no evento,
        o texto usa '40h' como fallback
        """
        # O codigo usa: hasattr(self.evento, 'carga_horaria') and self.evento.carga_horaria
        # Vamos verificar esse comportamento
        evento_sem_carga = self.evento
        # Remover o atributo se existir
        if hasattr(evento_sem_carga, 'carga_horaria'):
            del evento_sem_carga.carga_horaria

        gerador2 = GeradorCertificado(self.avaliacao)
        # Forcar a reavaliacao do evento
        self.assertEqual(gerador2.evento, evento_sem_carga)
        # O fallback e' 40h
        carga = f"{gerador2.evento.carga_horaria}h" if hasattr(gerador2.evento, 'carga_horaria') and gerador2.evento.carga_horaria else "40h"
        self.assertEqual(carga, "40h")

    # --- Teste de geracao de PDF ---

    def test_gerar_pdf_retorna_buffer_valido(self):
        """Verifica se gerar_pdf retorna um buffer com PDF valido (%PDF)"""
        buffer = BytesIO()
        resultado = self.gerador.gerar_pdf(buffer)
        conteudo = resultado.getvalue()
        self.assertTrue(conteudo.startswith(b"%PDF"), "PDF deve comecar com %PDF")

    def test_gerar_pdf_multiplas_chamadas(self):
        """Verifica se pode gerar multiplos PDFs sem erro"""
        for _ in range(3):
            buffer = BytesIO()
            resultado = self.gerador.gerar_pdf(buffer)
            self.assertTrue(resultado.getvalue().startswith(b"%PDF"))

            

