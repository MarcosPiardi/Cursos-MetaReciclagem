"""
Arquivo: test_views.py
Caminho: apps/academico/tests/test_views.py
Atualizacoes:
 - 28/05/2006 - Criacao do arquivo
 - 17/06/2026 - Refatorado de unittest.TestCase para pytest
"""

import io
import zipfile

import pytest
from django.test import Client
from django.contrib.auth import get_user_model
from django.urls import reverse
from unittest.mock import patch

from .factories import MatriculaFactory

pytestmark = pytest.mark.django_db

@pytest.fixture
def client():
    return Client()

@pytest.fixture
def staff_user(db):
    User = get_user_model()
    return User.objects.create_user(
        username="staffuser",
        email="staff@example.com",
        password="password123",
        cpf="11111111111",
        is_staff=True,
    )

@pytest.fixture
def mock_gerador():
    with patch("apps.academico.views.GeradorCertificado") as MockGerador:
        mock_instance = MockGerador.return_value
        mock_instance.gerar_pdf.side_effect = (
            lambda buffer: buffer.write(b"Mock PDF Content")
        )
        yield MockGerador, mock_instance

def criar_avaliacao(aprovado=False):
    matricula = MatriculaFactory()
    avaliacao = matricula.avaliacao
    if aprovado:
        avaliacao.aprovado = True
        avaliacao.save()
    return avaliacao

AVALIACAO_INEXISTENTE = 9999

class TestDownloadCertificadoIndividual:
    def test_sem_autenticacao_redireciona(self, client):
        avaliacao = criar_avaliacao()
        response = client.get(
            reverse("academico:download_certificado", args=[avaliacao.pk])
        )
        assert response.status_code == 302
        assert "/admin/login/" in response.url

    def test_aluno_aprovado_gera_pdf(self, client, staff_user, mock_gerador):
        MockGerador, mock_instance = mock_gerador
        avaliacao = criar_avaliacao(aprovado=True)
        client.force_login(staff_user)
        response = client.get(
            reverse("academico:download_certificado", args=[avaliacao.pk])
        )
        assert response.status_code == 200
        assert response["Content-Type"] == "application/pdf"
        assert "attachment" in response["Content-Disposition"]
        MockGerador.assert_called_once_with(avaliacao)
        mock_instance.gerar_pdf.assert_called_once()

    def test_aluno_reprovado_retorna_400(self, client, staff_user, mock_gerador):
        MockGerador, mock_instance = mock_gerador
        avaliacao = criar_avaliacao(aprovado=False)
        client.force_login(staff_user)
        response = client.get(
            reverse("academico:download_certificado", args=[avaliacao.pk])
        )
        assert response.status_code == 400
        assert b"Certificado" in response.content
        MockGerador.assert_not_called()

    def test_avaliacao_inexistente_retorna_404(self, client, staff_user):
        client.force_login(staff_user)
        response = client.get(
            reverse("academico:download_certificado", args=[AVALIACAO_INEXISTENTE])
        )
        assert response.status_code == 404

class TestPreviewCertificado:
    def test_sem_autenticacao_redireciona(self, client):
        avaliacao = criar_avaliacao()
        response = client.get(
            reverse("academico:preview_certificado", args=[avaliacao.pk])
        )
        assert response.status_code == 302
        assert "/admin/login/" in response.url

    def test_aluno_aprovado_inline(self, client, staff_user, mock_gerador):
        MockGerador, mock_instance = mock_gerador
        avaliacao = criar_avaliacao(aprovado=True)
        client.force_login(staff_user)
        response = client.get(
            reverse("academico:preview_certificado", args=[avaliacao.pk])
        )
        assert response.status_code == 200
        assert response["Content-Type"] == "application/pdf"
        assert "inline" in response["Content-Disposition"]
        MockGerador.assert_called_once_with(avaliacao)
        mock_instance.gerar_pdf.assert_called_once()

    def test_aluno_reprovado_retorna_400(self, client, staff_user, mock_gerador):
        MockGerador, mock_instance = mock_gerador
        avaliacao = criar_avaliacao(aprovado=False)
        client.force_login(staff_user)
        response = client.get(
            reverse("academico:preview_certificado", args=[avaliacao.pk])
        )
        assert response.status_code == 400
        assert b"Certificado" in response.content

class TestDownloadCertificadosLote:
    def test_sem_ids_retorna_400(self, client, staff_user):
        client.force_login(staff_user)
        response = client.get(reverse("academico:download_certificados_lote"))
        assert response.status_code == 400
        assert b"Nenhuma avalia" in response.content

    def test_ids_invalidos_retorna_400(self, client, staff_user):
        client.force_login(staff_user)
        response = client.get(
            reverse("academico:download_certificados_lote") + "?ids=abc,123"
        )
        assert response.status_code == 400
        assert b"Nenhum aluno aprovado" in response.content

    def test_apenas_aprovados_no_zip(self, client, staff_user):
        avaliacao_aprovada = criar_avaliacao(aprovado=True)
        avaliacao_reprovada = criar_avaliacao(aprovado=False)
        client.force_login(staff_user)
        response = client.get(
            reverse("academico:download_certificados_lote")
            + f"?ids={avaliacao_aprovada.pk},{avaliacao_reprovada.pk}"
        )
        assert response.status_code == 200
        assert response["Content-Type"] == "application/zip"
        assert "attachment" in response["Content-Disposition"]
        zip_buffer = io.BytesIO(response.content)
        with zipfile.ZipFile(zip_buffer, "r") as zf:
            assert len(zf.namelist()) == 1

    def test_zip_com_multiplos_certificados(self, client, staff_user):
        avaliacao1 = criar_avaliacao(aprovado=True)
        avaliacao2 = criar_avaliacao(aprovado=True)
        client.force_login(staff_user)
        response = client.get(
            reverse("academico:download_certificados_lote")
            + f"?ids={avaliacao1.pk},{avaliacao2.pk}"
        )
        assert response.status_code == 200
        assert response["Content-Type"] == "application/zip"
        assert "attachment" in response["Content-Disposition"]
        zip_buffer = io.BytesIO(response.content)
        with zipfile.ZipFile(zip_buffer, "r") as zf:
            assert len(zf.namelist()) == 2

            