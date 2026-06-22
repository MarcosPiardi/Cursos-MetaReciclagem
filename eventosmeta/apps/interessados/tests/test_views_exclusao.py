"""
Arquivo: test_views_exclusao.py
Caminho: apps/interessados/tests/test_views_exclusao.py
Testes para views de exclusao de dados (LGPD) - views_exclusao.py
Atualizações:
 - 29/05/2026 - Criacao do arquivo
 - 18/06/2026 - Refatorado para pytest
"""

import pytest
from django.urls import reverse

from apps.interessados.models import SolicitacaoExclusao
from .factories import InteressadoFactory

BACKEND = "apps.interessados.authentication.InteressadoBackend"
pytestmark = pytest.mark.django_db

class TestSolicitarExclusaoView:
    """Testes para solicitar_exclusao_view"""

    @pytest.fixture(autouse=True)
    def setup(self, db):
        self.interessado = InteressadoFactory.create(is_active=True)
        self.url = reverse("interessados:solicitar_exclusao")
        self.login_url = reverse("interessados:login")
        self.dashboard_url = reverse("interessados:dashboard")
        self.client = __import__("django").test.Client()

    # --- ACESSO SEM LOGIN ---

    def test_sem_login_redirect_para_login(self):
        response = self.client.get(self.url)
        assert response.status_code == 302
        assert self.login_url + "?next=" + self.url in response.url

    def test_post_sem_login_redirect_para_login(self):
        response = self.client.post(self.url, {"confirmacao": "CONFIRMAR"})
        assert response.status_code == 302
        assert self.login_url + "?next=" + self.url in response.url

    # --- INTERESSADO INATIVO ---

    def test_interessado_inativo_logout_e_redirect(self):
        self.interessado.is_active = False
        self.interessado.save()
        self.client.force_login(self.interessado, backend=BACKEND)
        response = self.client.get(self.url)
        assert response.status_code == 302
        assert self.login_url + "?next=" + self.url in response.url

    # --- GET SEM SOLICITACAO PENDENTE ---

    def test_get_sem_pendente_retorna_200(self):
        self.client.force_login(self.interessado, backend=BACKEND)
        response = self.client.get(self.url)
        assert response.status_code == 200
        assert "interessados/exclusao/solicitar.html" in [
            t.name for t in response.templates
        ]

    # --- GET COM SOLICITACAO PENDENTE ---

    def test_get_com_pendente_redirect_dashboard(self):
        SolicitacaoExclusao.objects.create(
            interessado=self.interessado,
            nome_solicitante=self.interessado.nome,
            email_solicitante=self.interessado.email or "",
            status="PENDENTE",
        )
        self.client.force_login(self.interessado, backend=BACKEND)
        response = self.client.get(self.url)
        assert response.status_code == 302
        assert self.dashboard_url in response.url

    # --- POST COM CONFIRMACAO VALIDA ---

    def test_post_confirmacao_valida_cria_solicitacao(self):
        self.client.force_login(self.interessado, backend=BACKEND)
        response = self.client.post(
            self.url,
            {"confirmacao": "CONFIRMAR", "motivo": "Quero excluir meus dados"},
        )
        assert response.status_code == 302
        assert reverse("interessados:exclusao_solicitada") in response.url

        solicitacao = SolicitacaoExclusao.objects.get(
            interessado=self.interessado
        )
        assert solicitacao.status == "PENDENTE"
        assert solicitacao.motivo == "Quero excluir meus dados"
        assert solicitacao.nome_solicitante == self.interessado.nome

    def test_post_confirmacao_valida_sem_motivo(self):
        self.client.force_login(self.interessado, backend=BACKEND)
        response = self.client.post(self.url, {"confirmacao": "CONFIRMAR"})
        assert response.status_code == 302
        assert reverse("interessados:exclusao_solicitada") in response.url
        assert SolicitacaoExclusao.objects.filter(
            interessado=self.interessado
        ).exists()

    # --- POST COM CONFIRMACAO INVALIDA ---

    def test_post_confirmacao_invalida_mostra_erro(self):
        self.client.force_login(self.interessado, backend=BACKEND)
        response = self.client.post(
            self.url,
            {"confirmacao": "NAO_CONFIRMO", "motivo": "Teste"},
        )
        assert response.status_code == 200
        assert "interessados/exclusao/solicitar.html" in [
            t.name for t in response.templates
        ]
        assert "erro" in response.context
        assert response.context["erro"] is not None
        assert not SolicitacaoExclusao.objects.filter(
            interessado=self.interessado
        ).exists()

    def test_post_confirmacao_vazia_mostra_erro(self):
        self.client.force_login(self.interessado, backend=BACKEND)
        response = self.client.post(
            self.url,
            {"confirmacao": "", "motivo": "Teste"},
        )
        assert response.status_code == 200
        assert "erro" in response.context
        assert response.context["erro"] is not None
        assert not SolicitacaoExclusao.objects.filter(
            interessado=self.interessado
        ).exists()

    # --- POST COM SOLICITACAO PENDENTE ---

    def test_post_com_pendente_nao_cria_nova(self):
        SolicitacaoExclusao.objects.create(
            interessado=self.interessado,
            nome_solicitante=self.interessado.nome,
            email_solicitante=self.interessado.email or "",
            status="PENDENTE",
        )
        self.client.force_login(self.interessado, backend=BACKEND)
        response = self.client.post(self.url, {"confirmacao": "CONFIRMAR"})
        assert response.status_code == 302
        assert self.dashboard_url in response.url
        assert (
            SolicitacaoExclusao.objects.filter(
                interessado=self.interessado
            ).count()
            == 1
        )

class TestExclusaoSolicitadaView:
    """Testes para exclusao_solicitada_view"""

    @pytest.fixture(autouse=True)
    def setup(self, db):
        self.interessado = InteressadoFactory.create(is_active=True)
        self.url = reverse("interessados:exclusao_solicitada")
        self.login_url = reverse("interessados:login")
        self.client = __import__("django").test.Client()

    def test_sem_login_redirect_para_login(self):
        response = self.client.get(self.url)
        assert response.status_code == 302
        assert self.login_url + "?next=" + self.url in response.url

    def test_get_com_login_retorna_200(self):
        self.client.force_login(self.interessado, backend=BACKEND)
        response = self.client.get(self.url)
        assert response.status_code == 200
        assert "interessados/exclusao/solicitada.html" in [
            t.name for t in response.templates
        ]


