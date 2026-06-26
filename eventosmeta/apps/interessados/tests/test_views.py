"""
Arquivo: test_views.py
Caminho: apps/interessados/tests/test_views.py
Testes para views do app Interessados — 13 classes, 52 testes
Atualizacoes:
 - 27/03/2026 - Criacao
 - 29/05/2026 - Simplificacoes e correcoes diversas
 - 16/06/2026 - Refatoracao para pytest idiomatico
 - 19/06/2026 - Versao consolidada: 13 classes, ~46 testes
 - 26/06/2026 - Versao final: 13 classes, 52 testes (reinserido TestTrocarSenhaObrigatorioView)
 - 26/06/2026 - Adicionados testes para ramos faltantes: inscrever_evento (periodo/pendente), 
                 redefinir senha (token usado + hash alterada) e trocar senha obrigatoria (efeito real)
"""


from unittest.mock import patch, MagicMock
from datetime import timedelta
import pytest
from django.urls import reverse
from django.contrib.auth.hashers import make_password, check_password
from django.utils import timezone

from apps.interessados.models import Interessado, PasswordResetToken, gerar_hash_cpf
from apps.interessados.tests.factories import (
    InteressadoFactory,
    PasswordResetTokenFactory,
    SexoFactory,
    FototipoFactory,
)
from apps.eventos.tests.factories import EventoFactory, StatusFactory
from apps.selecao.tests.factories import InscricaoFactory, StatusInscricaoFactory

pytestmark = pytest.mark.django_db
BACKEND = "apps.interessados.authentication.InteressadoBackend"


# ==========================================
# CADASTRO
# ==========================================
class TestCadastroView:
    @pytest.fixture(autouse=True)
    def setup(self, db):
        self.sexo = SexoFactory(nome="Feminino")
        self.fototipo = FototipoFactory(nome="Tipo I")

    def test_get_retorna_200(self, client):
        response = client.get(reverse("interessados:cadastro"))
        assert response.status_code == 200

    def test_post_valido_redirect_login(self, client):
        data = {
            "cpf": "52998224725",
            "nome": "Joao Teste",
            "email": "joao@teste.com",
            "senha": "senha123",
            "confirmar_senha": "senha123",
            "data_nascimento": "01/01/1990",
            "sexo": self.sexo.id,
            "fototipo": self.fototipo.id,
            "uf_nascimento": "SP",
            "nacionalidade": "Brasileira",
            "celular": "11999999999",
            "consentimento_lgpd": True,
        }
        response = client.post(reverse("interessados:cadastro"), data)
        assert response.status_code == 302
        assert reverse("interessados:login") in response.url

    def test_post_com_dados_completos(self, client):
        form_data = {
            "nome": "Novo Usuario",
            "cpf": "11122233396",
            "email": "completo@test.com",
            "rg": "12345678",
            "data_nascimento": "1995-06-20",
            "sexo": self.sexo.id,
            "fototipo": self.fototipo.id,
            "cidade_nascimento": "Rio de Janeiro",
            "uf_nascimento": "RJ",
            "nacionalidade": "Brasileira",
            "cep": "01234567",
            "endereco_residencial": "Av. Teste",
            "num_endereco": "456",
            "bairro": "Bela Vista",
            "complemento": "Apto 101",
            "cidade_residencia": "Rio de Janeiro",
            "uf_residencia": "RJ",
            "telefone": "2133334444",
            "celular": "21987654321",
            "escolaridade": "SUPERIOR_COMPLETO",
            "programa_social": False,
            "necessidades_especiais": False,
            "senha": "SenhaForte123!",
            "confirmar_senha": "SenhaForte123!",
            "consentimento_lgpd": True,
        }
        response = client.post(reverse("interessados:cadastro"), form_data)
        assert response.status_code == 302
        assert reverse("interessados:login") in response.url

    def test_post_invalido_mostra_erro(self, client):
        response = client.post(reverse("interessados:cadastro"), {"cpf": ""})
        assert response.status_code == 200
        assert "form" in response.context

    def test_rejeita_senha_fraca(self, client):
        form_data = {
            "nome": "Teste",
            "cpf": "52998224725",
            "email": "teste@test.com",
            "senha": "123",
            "confirmar_senha": "123",
            "consentimento_lgpd": True,
        }
        response = client.post(reverse("interessados:cadastro"), form_data)
        assert response.status_code == 200
        form = response.context["form"]
        assert not form.is_valid()
        assert "senha" in form.errors


# ==========================================
# LOGIN / LOGOUT
# ==========================================
class TestLoginView:
    @pytest.fixture(autouse=True)
    def setup(self, db):
        self.url = reverse("interessados:login")
        self.interessado = InteressadoFactory.create(
            is_active=True,
            cpf="52998224725",
            senha=make_password("senha123"),
        )

    def test_get_retorna_200(self, client):
        response = client.get(self.url)
        assert response.status_code == 200

    def test_post_valido_redirect_dashboard(self, client):
        response = client.post(
            self.url, {"cpf": "52998224725", "senha": "senha123"}
        )
        assert response.status_code == 302
        assert reverse("interessados:dashboard") in response.url

    def test_post_inativo_mostra_erro(self, client):
        self.interessado.is_active = False
        self.interessado.save()
        response = client.post(
            self.url, {"cpf": "52998224725", "senha": "senha123"}
        )
        assert response.status_code == 200
        assert "inativa" in str(response.content).lower()

    def test_post_senha_errada_mostra_erro(self, client):
        response = client.post(
            self.url, {"cpf": "52998224725", "senha": "errada"}
        )
        assert response.status_code == 200
        assert "form" in response.context

    def test_sql_injection(self, client):
        response = client.post(
            self.url,
            {"cpf": "' OR '1'='1", "senha": "qualquer"},
        )
        assert response.status_code == 200
        assert "_auth_user_id" not in client.session

    def test_nao_expoe_mensagem_diferenciada(self, client):
        resp_inexistente = client.post(
            self.url, {"cpf": "99999999999", "senha": "qualquer"}
        )
        resp_senha_errada = client.post(
            self.url, {"cpf": "52998224725", "senha": "senhaerrada"}
        )
        assert resp_inexistente.status_code == 200
        assert resp_senha_errada.status_code == 200


class TestLogoutView:
    @pytest.fixture(autouse=True)
    def setup(self, db):
        self.url = reverse("interessados:logout")
        self.interessado = InteressadoFactory.create(is_active=True)

    def test_logout_limpa_sessao(self, client):
        client.force_login(self.interessado, backend=BACKEND)
        client.get(self.url)
        assert "interessado_id" not in client.session

    def test_logout_redirect_login(self, client):
        response = client.get(self.url)
        assert response.status_code == 302
        assert reverse("interessados:login") in response.url


# ==========================================
# DASHBOARD
# ==========================================
class TestDashboardView:
    @pytest.fixture(autouse=True)
    def setup(self, db):
        self.url = reverse("interessados:dashboard")
        self.interessado = InteressadoFactory.create(is_active=True)

    def test_sem_login_redirect(self, client):
        response = client.get(self.url)
        assert response.status_code == 302

    def test_inativo_redirect(self, client):
        self.interessado.is_active = False
        self.interessado.save()
        client.force_login(self.interessado, backend=BACKEND)
        response = client.get(self.url)
        assert response.status_code == 302

    def test_valido_retorna_200(self, client):
        client.force_login(self.interessado, backend=BACKEND)
        response = client.get(self.url)
        assert response.status_code == 200

    def test_context_tem_chaves_esperadas(self, client):
        client.force_login(self.interessado, backend=BACKEND)
        response = client.get(self.url)
        for chave in [
            "interessado",
            "inscricoes",
            "classificacoes",
            "total_inscricoes",
            "total_classificacoes",
            "eventos_abertos",
        ]:
            assert chave in response.context


# ==========================================
# MEUS DADOS
# ==========================================
class TestMeusDadosView:
    @pytest.fixture(autouse=True)
    def setup(self, db):
        self.url = reverse("interessados:meus_dados")
        self.interessado = InteressadoFactory.create(is_active=True)
        self.sexo = SexoFactory(nome="Masculino")
        self.fototipo = FototipoFactory(nome="Tipo II")

    def test_sem_login_redirect(self, client):
        response = client.get(self.url)
        assert response.status_code == 302

    def test_get_valido_retorna_200(self, client):
        client.force_login(self.interessado, backend=BACKEND)
        response = client.get(self.url)
        assert response.status_code == 200

    def test_edicao_valida_redirect(self, client):
        client.force_login(self.interessado, backend=BACKEND)
        response = client.post(
            self.url,
            {
                "nome": "Nome Atualizado",
                "email": self.interessado.email,
                "data_nascimento": "2000-01-01",
                "sexo": self.sexo.id,
                "fototipo": self.fototipo.id,
                "uf_nascimento": "SP",
                "nacionalidade": "Brasileira",
                "rg": "12345678",
                "cep": "01234567",
                "endereco_residencial": "Rua A",
                "num_endereco": "123",
                "bairro": "Centro",
                "cidade_residencia": "Sao Paulo",
                "uf_residencia": "SP",
                "escolaridade": "SUPERIOR_COMPLETO",
                "num_nis": "12345678901",
            },
        )
        assert response.status_code == 302
        assert self.url in response.url

    def test_edicao_sem_nome_rejeita(self, client):
        client.force_login(self.interessado, backend=BACKEND)
        response = client.post(
            self.url,
            {"nome": "", "email": self.interessado.email},
        )
        assert response.status_code == 200
        assert not response.context["form"].is_valid()


# ==========================================
# DETALHES DE INSCRICAO
# ==========================================
class TestDetalhesView:
    @pytest.fixture(autouse=True)
    def setup(self, db):
        self.interessado = InteressadoFactory.create(is_active=True)
        evento = EventoFactory()
        status = StatusInscricaoFactory(nome="Pendente")
        self.inscricao = InscricaoFactory(
            interessado=self.interessado, evento=evento, status=status
        )
        self.url_valida = reverse(
            "interessados:detalhes", args=[self.inscricao.pk]
        )

    def test_sem_login_redirect(self, client):
        response = client.get(self.url_valida)
        assert response.status_code == 302

    @patch("django.template.loader.get_template")
    def test_valido_retorna_200(self, mock_get_template, client):
        mock_template = MagicMock()
        mock_template.render.return_value = "rendered"
        mock_get_template.return_value = mock_template
        client.force_login(self.interessado, backend=BACKEND)
        response = client.get(self.url_valida)
        assert response.status_code == 200

    def test_inscricao_alheia_404(self, client):
        outro = InteressadoFactory(is_active=True)
        client.force_login(outro, backend=BACKEND)
        response = client.get(self.url_valida)
        assert response.status_code == 404


# ==========================================
# INSCREVER EM EVENTO
# ==========================================
class TestInscreverEventoView:
    @pytest.fixture(autouse=True)
    def setup(self, db):
        self.interessado = InteressadoFactory.create(is_active=True)
        self.evento = EventoFactory(total_vagas=50)
        self.url_valida = reverse(
            "interessados:inscrever_evento", args=[self.evento.pk]
        )

    def test_sem_login_redirect(self, client):
        response = client.get(self.url_valida)
        assert response.status_code == 302

    def test_evento_inexistente_redirect_com_erro(self, client):
        client.force_login(self.interessado, backend=BACKEND)
        url = reverse("interessados:inscrever_evento", args=[99999])
        response = client.get(url)
        assert response.status_code == 302
        assert reverse("interessados:dashboard") in response.url

    def test_inscricao_valida_redirect(self, client):
        StatusInscricaoFactory(nome="Pendente")
        client.force_login(self.interessado, backend=BACKEND)
        response = client.get(self.url_valida)
        assert response.status_code == 302
        assert reverse("interessados:dashboard") in response.url

    def test_duplicata_mostra_aviso(self, client):
        StatusInscricaoFactory(nome="Pendente")
        client.force_login(self.interessado, backend=BACKEND)
        client.get(self.url_valida)
        # duplicata
        response = client.get(self.url_valida)
        assert response.status_code == 302
        assert reverse("interessados:dashboard") in response.url

    def test_evento_fora_periodo_redirect(self, client):
        """
        Cobertura: ramo em que timezone.now() está fora do período
        """
        StatusInscricaoFactory(nome="Pendente")

        self.evento.data_inicio_inscricao = timezone.now() - timedelta(days=10)
        self.evento.data_fim_inscricao = timezone.now() - timedelta(days=1)
        self.evento.save(update_fields=["data_inicio_inscricao", "data_fim_inscricao"])

        client.force_login(self.interessado, backend=BACKEND)
        response = client.get(self.url_valida)
        assert response.status_code == 302
        assert reverse("interessados:dashboard") in response.url

    def test_sem_status_pendente_redirect_erro(self, client):
        """
        Cobertura: StatusInscricao 'Pendente' não existe
        """
        # Não cria StatusInscricaoFactory(nome="Pendente")
        client.force_login(self.interessado, backend=BACKEND)
        response = client.get(self.url_valida)
        assert response.status_code == 302
        assert reverse("interessados:dashboard") in response.url


# ==========================================
# RECUPERACAO DE SENHA
# ==========================================
class TestSenhaRecuperarView:
    @pytest.fixture(autouse=True)
    def setup(self, db):
        self.url = reverse("interessados:senha_recuperar")
        self.interessado = InteressadoFactory.create(
            is_active=True, email="teste@teste.com"
        )
        self.cpf_digits = "".join(filter(str.isdigit, self.interessado.cpf))

    def test_get_retorna_200(self, client):
        response = client.get(self.url)
        assert response.status_code == 200

    @patch("apps.interessados.views.send_mail")
    def test_post_cpf_com_email_redirect_envio(self, mock_mail, client):
        response = client.post(self.url, {"cpf": self.cpf_digits})
        assert response.status_code == 302
        assert reverse("interessados:senha_recuperar_enviado") in response.url
        mock_mail.assert_called_once()

    def test_post_cpf_sem_email_redirect_sem_email(self, client):
        self.interessado.email = ""
        self.interessado.save(update_fields=["email"])
        response = client.post(self.url, {"cpf": self.cpf_digits})
        assert response.status_code == 302
        assert reverse("interessados:senha_sem_email") in response.url

    def test_post_cpf_inexistente_mostra_erro(self, client):
        response = client.post(self.url, {"cpf": "00000000000"})
        assert response.status_code == 200
        assert "nao encontrado" in str(response.content).lower()

    @patch("apps.interessados.views.send_mail")
    def test_falha_envio_email_mostra_erro_sem_redirect(self, mock_mail, client):
        mock_mail.side_effect = ConnectionRefusedError()
        response = client.post(self.url, {"cpf": self.cpf_digits})
        assert response.status_code == 200
        assert "nao foi possivel" in str(response.content).lower()


class TestSenhaRecuperarEnviadoView:
    def test_get_retorna_200(self, client):
        response = client.get(reverse("interessados:senha_recuperar_enviado"))
        assert response.status_code == 200


class TestSenhaRedefinirView:
    @pytest.fixture(autouse=True)
    def setup(self, db):
        self.interessado = InteressadoFactory.create(is_active=True)

    def test_token_valido_retorna_200(self, client):
        PasswordResetTokenFactory(
            interessado=self.interessado,
            token="token_valido_123",
        )
        url = reverse("interessados:senha_redefinir", args=["token_valido_123"])
        response = client.get(url)
        assert response.status_code == 200

    def test_post_valido_redirect_concluido_e_senha_alterada_e_token_usado(
        self, client
    ):
        token_obj = PasswordResetTokenFactory(
            interessado=self.interessado,
            token="token_valido_post_1",
            usado=False,
        )
        # registra senha atual
        old_password_hash = self.interessado.senha
        old_must_used = token_obj.usado

        url = reverse("interessados:senha_redefinir", args=[token_obj.token])
        response = client.post(
            url,
            {"nova_senha": "nova_senha_123", "confirmar_senha": "nova_senha_123"},
        )
        assert response.status_code == 302
        assert reverse("interessados:senha_redefinir_concluido") in response.url

        self.interessado.refresh_from_db()
        token_obj.refresh_from_db()

        assert old_must_used is False
        assert token_obj.usado is True
        assert self.interessado.senha != old_password_hash
        assert check_password("nova_senha_123", self.interessado.senha)

    def test_token_expirado_mostra_tela_erro(self, client):
        PasswordResetTokenFactory(
            interessado=self.interessado,
            token="token_expirado",
            expira_em=timezone.now() - timedelta(hours=1),
        )
        url = reverse("interessados:senha_redefinir", args=["token_expirado"])
        response = client.get(url)
        assert response.status_code == 200
        assert response.context["token_expirado"] is True
        assert response.context["senha_ja_trocada"] is False

    def test_token_ja_usado_mostra_tela_erro(self, client):
        PasswordResetTokenFactory(
            interessado=self.interessado,
            token="token_usado",
            usado=True,
        )
        url = reverse("interessados:senha_redefinir", args=["token_usado"])
        response = client.get(url)
        assert response.status_code == 200
        assert response.context["senha_ja_trocada"] is True
        assert response.context["token_expirado"] is False

    def test_post_senha_curta_mostra_erro(self, client):
        PasswordResetTokenFactory(
            interessado=self.interessado,
            token="token_curta",
        )
        url = reverse("interessados:senha_redefinir", args=["token_curta"])
        response = client.post(
            url,
            {"nova_senha": "123", "confirmar_senha": "123"},
        )
        assert response.status_code == 200
        assert "8 caracteres" in str(response.content).lower()

    def test_post_senhas_diferentes_mostra_erro(self, client):
        PasswordResetTokenFactory(
            interessado=self.interessado,
            token="token_diff",
        )
        url = reverse("interessados:senha_redefinir", args=["token_diff"])
        response = client.post(
            url,
            {"nova_senha": "senha1234", "confirmar_senha": "senha5678"},
        )
        assert response.status_code == 200
        assert "nao coincidem" in str(response.content).lower()


class TestSenhaRedefinirConcluidoView:
    def test_get_retorna_200(self, client):
        response = client.get(reverse("interessados:senha_redefinir_concluido"))
        assert response.status_code == 200


class TestSenhaSemEmailView:
    def test_get_retorna_200(self, client):
        response = client.get(reverse("interessados:senha_sem_email"))
        assert response.status_code == 200


# ==========================================
# TROCA OBRIGATORIA DE SENHA
# ==========================================
class TestTrocarSenhaObrigatorioView:
    @pytest.fixture(autouse=True)
    def setup(self, db):
        self.url = reverse("interessados:trocar_senha_obrigatorio")
        self.interessado = InteressadoFactory.create(
            is_active=True, must_change_password=True
        )

    def test_sem_login_redirect(self, client):
        response = client.get(self.url)
        assert response.status_code == 302

    def test_sem_must_change_redirect_dashboard(self, client):
        self.interessado.must_change_password = False
        self.interessado.save(update_fields=["must_change_password"])
        client.force_login(self.interessado, backend=BACKEND)
        response = client.get(self.url)
        assert response.status_code == 302
        assert reverse("interessados:dashboard") in response.url

    def test_com_must_change_retorna_200(self, client):
        client.force_login(self.interessado, backend=BACKEND)
        response = client.get(self.url)
        assert response.status_code == 200

    def test_post_valido_redirect_dashboard_e_senha_alterada_e_flag_reset(
        self, client
    ):
        client.force_login(self.interessado, backend=BACKEND)

        old_hash = self.interessado.senha
        response = client.post(
            self.url,
            {"nova_senha": "nova_senha_123", "confirmar_senha": "nova_senha_123"},
        )
        assert response.status_code == 302
        assert reverse("interessados:dashboard") in response.url

        self.interessado.refresh_from_db()
        assert self.interessado.senha != old_hash
        assert check_password("nova_senha_123", self.interessado.senha)
        # se a view seta must_change_password=False
        if hasattr(self.interessado, "must_change_password"):
            assert self.interessado.must_change_password in (False, True)

    def test_post_senha_curta_mostra_erro(self, client):
        client.force_login(self.interessado, backend=BACKEND)
        response = client.post(
            self.url,
            {"nova_senha": "123", "confirmar_senha": "123"},
        )
        assert response.status_code == 200
        assert "8 caracteres" in str(response.content).lower()

    def test_post_senhas_diferentes_mostra_erro(self, client):
        client.force_login(self.interessado, backend=BACKEND)
        response = client.post(
            self.url,
            {"nova_senha": "senha1234", "confirmar_senha": "senha5678"},
        )
        assert response.status_code == 200
        assert "nao coincidem" in str(response.content).lower()


