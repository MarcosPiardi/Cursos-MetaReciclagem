"""
Arquivo: test_views.py
Caminho: apps/accounts/tests/test_views.py
Testes para as views do app Accounts.
Atualizacoes:
 - 28/05/2026 - Criacao inicial dos testes
 - 16/06/2026 - Refatorado para pytest puro
 - 25/06/2026 - Adicionados testes para trocar_senha_obrigatorio_view
                e testes extras para login_staff
 - 25/06/2026 - Corrigido: URL correta e '/staff/senha/trocar-obrigatorio/'
 - 22/07/2026 - Corrigido URLs e redirects para incluir prefixo /eventosmeta/
"""
import pytest
from django.test import Client
from django.contrib.auth import get_user_model
from django.urls import reverse

# =============================================================================
# Testes para login_staff
# =============================================================================
@pytest.mark.django_db
class TestLoginStaffView:
    """Testes para a view login_staff."""
    def test_login_staff_get(self):
        """Pagina de login deve ser acessivel via GET."""
        response = Client().get(reverse('accounts:login_staff'))
        assert response.status_code == 200

    def test_login_staff_valido(self):
        """Credenciais validas de staff devem logar e redirecionar."""
        User = get_user_model()
        User.objects.create_user(
            username='stafftest', password='password123',
            cpf='11111111111', is_staff=True, is_active=True
        )
        client = Client()
        response = client.post(reverse('accounts:login_staff'), {
            'username': 'stafftest',
            'password': 'password123'
        })
        assert response.status_code == 302
        assert '_auth_user_id' in client.session

    def test_login_staff_invalido(self):
        """Credenciais invalidas devem falhar."""
        User = get_user_model()
        User.objects.create_user(
            username='stafftest', password='password123',
            cpf='11111111111', is_staff=True, is_active=True
        )
        client = Client()
        response = client.post(reverse('accounts:login_staff'), {
            'username': 'stafftest',
            'password': 'wrongpassword'
        })
        assert response.status_code == 200
        assert '_auth_user_id' not in client.session

    def test_login_staff_nao_staff(self):
        """Usuario nao-staff nao deve conseguir logar."""
        User = get_user_model()
        User.objects.create_user(
            username='user_normal', password='password123',
            cpf='22222222222', is_staff=False, is_active=True
        )
        client = Client()
        response = client.post(reverse('accounts:login_staff'), {
            'username': 'user_normal',
            'password': 'password123'
        })
        assert response.status_code == 200
        assert '_auth_user_id' not in client.session

    def test_login_staff_inativo_falha(self):
        """Usuario inativo nao deve conseguir logar."""
        User = get_user_model()
        User.objects.create_user(
            username='inactive', password='password123',
            cpf='33333333333', is_staff=True, is_active=False
        )
        client = Client()
        response = client.post(reverse('accounts:login_staff'), {
            'username': 'inactive',
            'password': 'password123'
        })
        assert response.status_code == 200
        assert '_auth_user_id' not in client.session

    def test_staff_acessa_admin_apos_login(self):
        """Staff logado deve acessar o admin."""
        User = get_user_model()
        usuario = User.objects.create_user(
            username='stafftest', password='password123',
            cpf='11111111111', is_staff=True, is_active=True
        )
        client = Client()
        client.force_login(usuario)
        response = client.get(reverse('admin:index'))
        assert response.status_code == 200

    def test_nao_staff_redirecionado_do_admin(self):
        """Nao-staff deve ser redirecionado ao tentar acessar admin."""
        User = get_user_model()
        usuario = User.objects.create_user(
            username='normal', password='password123',
            cpf='22222222222', is_staff=False, is_active=True
        )
        client = Client()
        client.force_login(usuario)
        response = client.get(reverse('admin:index'))
        assert response.status_code == 302

    def test_login_staff_form_tem_csrf(self):
        """O formulario de login deve conter csrf token."""
        response = Client().get(reverse('accounts:login_staff'))
        assert response.status_code == 200
        assert 'csrfmiddlewaretoken' in response.content.decode()

    def test_usuario_ja_logado_staff_redireciona(self):
        """Staff ja logado deve ser redirecionado para admin."""
        User = get_user_model()
        usuario = User.objects.create_user(
            username='staff', password='123', cpf='11111111111',
            is_staff=True, is_active=True
        )
        client = Client()
        client.force_login(usuario)
        response = client.get(reverse('accounts:login_staff'))
        assert response.status_code == 302
        # 22/07/2026 - Corrigido: prefixo /eventosmeta/ incluido
        assert response.url == '/eventosmeta/admin/'

    def test_usuario_ja_logado_nao_staff_nao_redireciona(self):
        """Nao-staff ja logado nao deve ser redirecionado (mostra form)."""
        User = get_user_model()
        usuario = User.objects.create_user(
            username='normal', password='123', cpf='22222222222',
            is_staff=False, is_active=True
        )
        client = Client()
        client.force_login(usuario)
        response = client.get(reverse('accounts:login_staff'))
        assert response.status_code == 200

    def test_context_tem_url_recuperar_senha(self):
        """O contexto deve conter url_recuperar_senha."""
        response = Client().get(reverse('accounts:login_staff'))
        assert response.context.get('url_recuperar_senha') == 'staff_senha_recuperar'

# =============================================================================
# Testes para logout_staff
# =============================================================================
@pytest.mark.django_db
class TestLogoutStaffView:
    """Testes para a view logout_staff."""
    def test_logout_staff_post(self):
        """POST no logout deve deslogar e redirecionar."""
        User = get_user_model()
        usuario = User.objects.create_user(
            username='stafftest', password='password123',
            cpf='11111111111', is_staff=True, is_active=True
        )
        client = Client()
        client.force_login(usuario)
        assert '_auth_user_id' in client.session
        response = client.post(reverse('accounts:logout_staff'))
        assert response.status_code == 302
        assert '_auth_user_id' not in client.session

    def test_logout_staff_get(self):
        """GET no logout tambem deve deslogar."""
        User = get_user_model()
        usuario = User.objects.create_user(
            username='stafftest', password='password123',
            cpf='11111111111', is_staff=True, is_active=True
        )
        client = Client()
        client.force_login(usuario)
        assert '_auth_user_id' in client.session
        response = client.get(reverse('accounts:logout_staff'))
        assert response.status_code == 302
        assert '_auth_user_id' not in client.session

# =============================================================================
# Testes para trocar_senha_obrigatorio_view
# =============================================================================
# 22/07/2026 - Corrigido: adicionado prefixo /eventosmeta/
TROCAR_SENHA_URL = '/eventosmeta/staff/senha/trocar-obrigatorio/'

@pytest.mark.django_db
class TestTrocarSenhaObrigatorioView:
    """Testes para a view trocar_senha_obrigatorio_view."""
    def test_get_sem_login_redireciona(self):
        """Usuario nao logado deve ser redirecionado para login."""
        response = Client().get(TROCAR_SENHA_URL)
        assert response.status_code == 302
        assert '/staff/login/' in response.url

    def test_get_sem_must_change_password_redireciona(self):
        """Staff sem must_change_password deve ser redirecionado para admin."""
        User = get_user_model()
        usuario = User.objects.create_user(
            username='staff', password='123', cpf='11111111111',
            is_staff=True, is_active=True, must_change_password=False
        )
        client = Client()
        client.force_login(usuario)
        response = client.get(TROCAR_SENHA_URL)
        assert response.status_code == 302
        # 22/07/2026 - Corrigido: prefixo /eventosmeta/ incluido
        assert response.url == '/eventosmeta/admin/'

    def test_get_com_must_change_password_renderiza(self):
        """Staff com must_change_password=True deve ver o template."""
        User = get_user_model()
        usuario = User.objects.create_user(
            username='staff', password='123', cpf='11111111111',
            is_staff=True, is_active=True, must_change_password=True
        )
        client = Client()
        client.force_login(usuario)
        response = client.get(TROCAR_SENHA_URL)
        assert response.status_code == 200
        assert 'accounts/senha/adm_trocar_obrigatorio.html' in [
            t.name for t in response.templates
        ]

    def test_post_senha_curta_mostra_erro(self):
        """Senha com menos de 8 caracteres deve mostrar erro."""
        User = get_user_model()
        usuario = User.objects.create_user(
            username='staff', password='123', cpf='11111111111',
            is_staff=True, is_active=True, must_change_password=True
        )
        client = Client()
        client.force_login(usuario)
        response = client.post(TROCAR_SENHA_URL, {
            'nova_senha': '123',
            'confirmar_senha': '123'
        })
        assert response.status_code == 200
        assert response.context.get('erro') is not None
        assert '8 caracteres' in response.context['erro']

    def test_post_senhas_diferentes_mostra_erro(self):
        """Senhas que nao coincidem devem mostrar erro."""
        User = get_user_model()
        usuario = User.objects.create_user(
            username='staff', password='123', cpf='11111111111',
            is_staff=True, is_active=True, must_change_password=True
        )
        client = Client()
        client.force_login(usuario)
        response = client.post(TROCAR_SENHA_URL, {
            'nova_senha': 'senha1234',
            'confirmar_senha': 'senha5678'
        })
        assert response.status_code == 200
        assert response.context.get('erro') is not None
        assert 'não coincidem' in response.context['erro']

    def test_post_valido_altera_senha_e_redireciona(self):
        """POST valido deve alterar senha, limpar flag e redirect para admin."""
        User = get_user_model()
        usuario = User.objects.create_user(
            username='staff', password='senha_antiga', cpf='11111111111',
            is_staff=True, is_active=True, must_change_password=True
        )
        client = Client()
        client.force_login(usuario)
        response = client.post(TROCAR_SENHA_URL, {
            'nova_senha': 'nova_senha_123',
            'confirmar_senha': 'nova_senha_123'
        })
        usuario.refresh_from_db()
        assert usuario.must_change_password is False
        assert usuario.check_password('nova_senha_123') is True
        assert response.status_code == 302
        # 22/07/2026 - Corrigido: prefixo /eventosmeta/ incluido
        assert response.url == '/eventosmeta/admin/'

        