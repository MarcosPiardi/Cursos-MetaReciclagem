"""
Arquivo: test_views.py
Caminho: apps/academico/tests/test_views.py
Atualizações
28/05/2026 - Criação do arquivo 
"""

from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse
from unittest.mock import patch
import io
import zipfile

from .factories import MatriculaFactory, InteressadoFactory


class BaseCertificadoTest(TestCase):
    """Base class for certificate view tests."""

    def setUp(self):
        super().setUp()
        self.client = Client()
        self.User = get_user_model()

        self.staff_user = self.User.objects.create_user(
            username="staffuser",
            email="staff@example.com",
            password="password123",
            cpf="11111111111",
            is_staff=True,
        )

        # Mock GeradorCertificado
        self.patcher = patch("apps.academico.views.GeradorCertificado")
        self.MockGeradorCertificado = self.patcher.start()
        self.mock_instance = self.MockGeradorCertificado.return_value
        self.mock_instance.gerar_pdf.side_effect = (
            lambda buffer: buffer.write(b"Mock PDF Content")
        )

    def tearDown(self):
        self.patcher.stop()
        super().tearDown()

    def _criar_avaliacao(self, aprovado=False):
        """Helper: cria matricula + avaliacao com o status de aprovacao desejado"""
        matricula = MatriculaFactory()
        avaliacao = matricula.avaliacao
        if aprovado:
            avaliacao.aprovado = True
            avaliacao.save()
        return avaliacao

    def _login(self):
        self.client.force_login(self.staff_user)

    def _avaliacao_inexistente(self):
        return 9999


class TestDownloadCertificadoIndividual(BaseCertificadoTest):
    """Tests for download_certificado_individual view."""

    def test_sem_autenticacao_redireciona(self):
        avaliacao = self._criar_avaliacao()
        response = self.client.get(
            reverse("academico:download_certificado", args=[avaliacao.pk])
        )
        self.assertEqual(response.status_code, 302)
        self.assertIn("/admin/login/", response.url)

    def test_aluno_aprovado_gera_pdf(self):
        avaliacao = self._criar_avaliacao(aprovado=True)
        self._login()

        response = self.client.get(
            reverse("academico:download_certificado", args=[avaliacao.pk])
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response["Content-Type"], "application/pdf")
        self.assertIn("attachment", response["Content-Disposition"])
        self.MockGeradorCertificado.assert_called_once_with(avaliacao)
        self.mock_instance.gerar_pdf.assert_called_once()

    def test_aluno_reprovado_retorna_400(self):
        avaliacao = self._criar_avaliacao(aprovado=False)
        self._login()

        response = self.client.get(
            reverse("academico:download_certificado", args=[avaliacao.pk])
        )

        self.assertEqual(response.status_code, 400)
        self.assertIn(b"Certificado", response.content)
        self.MockGeradorCertificado.assert_not_called()

    def test_avaliacao_inexistente_retorna_404(self):
        self._login()
        response = self.client.get(
            reverse("academico:download_certificado", args=[self._avaliacao_inexistente()])
        )
        self.assertEqual(response.status_code, 404)


class TestPreviewCertificado(BaseCertificadoTest):
    """Tests for preview_certificado view."""

    def test_sem_autenticacao_redireciona(self):
        avaliacao = self._criar_avaliacao()
        response = self.client.get(
            reverse("academico:preview_certificado", args=[avaliacao.pk])
        )
        self.assertEqual(response.status_code, 302)
        self.assertIn("/admin/login/", response.url)

    def test_aluno_aprovado_inline(self):
        avaliacao = self._criar_avaliacao(aprovado=True)
        self._login()

        response = self.client.get(
            reverse("academico:preview_certificado", args=[avaliacao.pk])
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response["Content-Type"], "application/pdf")
        self.assertIn("inline", response["Content-Disposition"])
        self.MockGeradorCertificado.assert_called_once_with(avaliacao)
        self.mock_instance.gerar_pdf.assert_called_once()

    def test_aluno_reprovado_retorna_400(self):
        avaliacao = self._criar_avaliacao(aprovado=False)
        self._login()

        response = self.client.get(
            reverse("academico:preview_certificado", args=[avaliacao.pk])
        )

        self.assertEqual(response.status_code, 400)
        self.assertIn(b"Certificado", response.content)


class TestDownloadCertificadosLote(BaseCertificadoTest):
    """Tests for download_certificados_lote view."""

    def test_sem_ids_retorna_400(self):
        self._login()
        response = self.client.get(
            reverse("academico:download_certificados_lote")
        )
        self.assertEqual(response.status_code, 400)
        self.assertIn(b"Nenhuma avalia", response.content)

    def test_ids_invalidos_retorna_400(self):
        self._login()
        response = self.client.get(
            reverse("academico:download_certificados_lote") + "?ids=abc,123"
        )
        self.assertEqual(response.status_code, 400)
        self.assertIn(b"Nenhum aluno aprovado", response.content)

    def test_apenas_aprovados_no_zip(self):
        avaliacao_aprovada = self._criar_avaliacao(aprovado=True)
        avaliacao_reprovada = self._criar_avaliacao(aprovado=False)

        self._login()
        response = self.client.get(
            reverse("academico:download_certificados_lote")
            + f"?ids={avaliacao_aprovada.pk},{avaliacao_reprovada.pk}"
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response["Content-Type"], "application/zip")
        self.assertIn("attachment", response["Content-Disposition"])

        zip_buffer = io.BytesIO(response.content)
        with zipfile.ZipFile(zip_buffer, "r") as zf:
            self.assertEqual(len(zf.namelist()), 1)

    def test_zip_com_multiplos_certificados(self):
        avaliacao1 = self._criar_avaliacao(aprovado=True)
        avaliacao2 = self._criar_avaliacao(aprovado=True)

        self._login()
        response = self.client.get(
            reverse("academico:download_certificados_lote")
            + f"?ids={avaliacao1.pk},{avaliacao2.pk}"
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response["Content-Type"], "application/zip")
        self.assertIn("attachment", response["Content-Disposition"])

        zip_buffer = io.BytesIO(response.content)
        with zipfile.ZipFile(zip_buffer, "r") as zf:
            self.assertEqual(len(zf.namelist()), 2)



