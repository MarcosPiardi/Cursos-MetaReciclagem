"""
Arquivo: test_admin.py
Caminho: apps/accounts/tests/test_admin.py
Finalidade: Testes para as admin.py do app accounts
Atualizações:
 - 28/05/2026 - Criação do arquivo
 - 17/06/2026 - Refatorado de unittest.TestCase para pytest
 - 13/07/2026 - REMOVIDO: Testes de CustomAdminSite (descontinuado)
              - Mantidos: Testes de UsuarioAdmin
"""

import pytest
from django.test import Client
from django.urls import reverse
from django.contrib.messages import get_messages

from apps.accounts.models import Usuario

pytestmark = pytest.mark.django_db

class TestUsuarioAdminList:
    def setup_method(self):
        self.client = Client()
        self.staff_user = Usuario.objects.create_user(
            username='staff',
            email='staff@example.com',
            password='staffpass',
            cpf='11111111111',
            is_staff=True,
            is_superuser=True,
        )
        self.user1 = Usuario.objects.create_user(
            username='user1', email='user1@ex.com',
            password='pass1', cpf='11111111112',
        )
        self.user2 = Usuario.objects.create_user(
            username='user2', email='user2@ex.com',
            password='pass2', cpf='11111111113',
        )

    def test_usuario_admin_list_status_200(self):
        self.client.force_login(self.staff_user)
        response = self.client.get(reverse('admin:accounts_usuario_changelist'))
        assert response.status_code == 200

    def test_usuario_admin_list_sem_login_redirect(self):
        response = self.client.get(reverse('admin:accounts_usuario_changelist'))
        assert response.status_code == 302

    def test_usuario_admin_list_pesquisa_por_username(self):
        self.client.force_login(self.staff_user)
        url = reverse('admin:accounts_usuario_changelist') + '?q=user1'
        response = self.client.get(url)
        content = response.content.decode()
        assert response.status_code == 200
        assert 'user1' in content
        assert 'user2' not in content

class TestUsuarioAdminAdd:
    def setup_method(self):
        self.client = Client()
        self.staff_user = Usuario.objects.create_user(
            username='staff',
            email='staff@example.com',
            password='staffpass',
            cpf='11111111111',
            is_staff=True,
            is_superuser=True,
        )

    def test_usuario_admin_add_status_200(self):
        self.client.force_login(self.staff_user)
        response = self.client.get(reverse('admin:accounts_usuario_add'))
        assert response.status_code == 200

    def test_usuario_admin_add_usuario(self):
        self.client.force_login(self.staff_user)
        initial_count = Usuario.objects.count()
        data = {
            'username': 'novo_usuario',
            'email': 'novo@example.com',
            'cpf': '11111111114',
            'password1': 'teste1234',
            'password2': 'teste1234',
        }
        response = self.client.post(
            reverse('admin:accounts_usuario_add'), data
        )
        assert response.status_code == 302
        assert Usuario.objects.count() == initial_count + 1

class TestUsuarioAdminActionGerarSenhaProvisoria:
    def setup_method(self):
        self.client = Client()
        self.staff_user = Usuario.objects.create_user(
            username='staff',
            email='staff@example.com',
            password='staffpass',
            cpf='11111111111',
            is_staff=True,
            is_superuser=True,
        )
        self.usuario_alvo = Usuario.objects.create_user(
            username='alvo',
            email='alvo@example.com',
            password='senha_antiga',
            cpf='11111111115',
            is_staff=True,
            is_active=True,
        )

    def test_gerar_senha_provisoria_seleciona_1(self):
        self.client.force_login(self.staff_user)
        data = {
            'action': 'gerar_senha_provisoria',
            '_selected_action': [self.usuario_alvo.id],
        }
        response = self.client.post(
            reverse('admin:accounts_usuario_changelist'), data
        )
        assert response.status_code == 302
        self.usuario_alvo.refresh_from_db()
        assert self.usuario_alvo.must_change_password
        assert not self.usuario_alvo.check_password('senha_antiga')

    def test_gerar_senha_provisoria_seleciona_2_falha(self):
        self.client.force_login(self.staff_user)
        outro = Usuario.objects.create_user(
            username='outro', email='outro@ex.com',
            password='outropass', cpf='11111111116',
        )
        data = {
            'action': 'gerar_senha_provisoria',
            '_selected_action': [self.usuario_alvo.id, outro.id],
        }
        response = self.client.post(
            reverse('admin:accounts_usuario_changelist'), data
        )
        assert response.status_code == 302
        messages = list(get_messages(response.wsgi_request))
        warning_messages = [
            str(m) for m in messages if m.level_tag == 'warning'
        ]
        assert len(warning_messages) > 0
        assert 'exatamente 1' in warning_messages[0].lower()



        