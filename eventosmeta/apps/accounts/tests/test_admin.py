"""
Arquivo: test_admin.py
Caminho: apps/accounts/tests/test_admin.py
Finalidade: Testes para as admin.py do app accounts, garantindo que as funcionalidades de administração estejam funcionando corretamente.
Data: 28/05/2026
"""

from django.test import TestCase, Client
from django.urls import reverse
from apps.accounts.admin import admin_site
from apps.accounts.models import Usuario


class TestCustomAdminSite(TestCase):
    def setUp(self):
        self.client = Client()
        self.staff_user = Usuario.objects.create_user(
            username='staff',
            email='staff@example.com',
            password='staffpass',
            cpf='11111111111',
            is_staff=True,
            is_superuser=True,
        )

    def test_admin_index_status_200(self):
        self.client.force_login(self.staff_user)
        response = self.client.get(reverse('admin:index'))
        self.assertEqual(response.status_code, 200)

    def test_admin_index_sem_login_redirect(self):
        response = self.client.get(reverse('admin:index'))
        self.assertEqual(response.status_code, 302)

    def test_dashboard_status_200(self):
        self.client.force_login(self.staff_user)
        response = self.client.get(reverse('admin:dashboard'))
        self.assertEqual(response.status_code, 200)
        self.assertIn('total_eventos', response.context)
        self.assertIn('total_interessados', response.context)
        self.assertIn('total_inscricoes', response.context)
        self.assertIn('eventos_abertos', response.context)

    def test_dashboard_sem_login_redirect(self):
        response = self.client.get(reverse('admin:dashboard'))
        self.assertEqual(response.status_code, 302)


class TestUsuarioAdminList(TestCase):
    def setUp(self):
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
        self.assertEqual(response.status_code, 200)

    def test_usuario_admin_list_sem_login_redirect(self):
        response = self.client.get(reverse('admin:accounts_usuario_changelist'))
        self.assertEqual(response.status_code, 302)

    def test_usuario_admin_list_pesquisa_por_username(self):
        self.client.force_login(self.staff_user)
        url = reverse('admin:accounts_usuario_changelist') + '?q=user1'
        response = self.client.get(url)
        self.assertContains(response, 'user1')
        self.assertNotContains(response, 'user2')


class TestUsuarioAdminAdd(TestCase):
    def setUp(self):
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
        self.assertEqual(response.status_code, 200)

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
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Usuario.objects.count(), initial_count + 1)


class TestUsuarioAdminActionGerarSenhaProvisoria(TestCase):
    def setUp(self):
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
        self.assertEqual(response.status_code, 302)
        self.usuario_alvo.refresh_from_db()
        self.assertTrue(self.usuario_alvo.must_change_password)
        self.assertFalse(self.usuario_alvo.check_password('senha_antiga'))

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
        self.assertEqual(response.status_code, 302)
        from django.contrib.messages import get_messages
        messages = list(get_messages(response.wsgi_request))
        warning_messages = [
            str(m) for m in messages if m.level_tag == 'warning'
        ]
        self.assertTrue(len(warning_messages) > 0)
        self.assertIn('exatamente 1', warning_messages[0].lower())



        