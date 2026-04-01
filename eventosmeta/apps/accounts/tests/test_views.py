from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse


class AccountsViewsTest(TestCase):
    """Testes para as views do app Accounts (login e logout de staff)."""

    def setUp(self):
        self.client = Client()
        self.User = get_user_model()

        # Criar usuário staff
        self.staff_user = self.User.objects.create_user(
            username='stafftest',
            email='stafftest@example.com',
            password='password123',
            cpf='11111111111',
            is_staff=True,
            is_active=True
        )

        # Criar usuário não-staff
        self.non_staff_user = self.User.objects.create_user(
            username='user_normal',
            email='normal@example.com',
            password='password123',
            cpf='22222222222',
            is_staff=False,
            is_active=True
        )

    def test_login_staff_get(self):
        """Verifica se a página de login é acessível via GET."""
        response = self.client.get(reverse('accounts:login_staff'))
        self.assertEqual(response.status_code, 200)

    def test_login_staff_valido(self):
        """Verifica se credenciais válidas realizam login e redirecionam."""
        response = self.client.post(reverse('accounts:login_staff'), {
            'username': 'stafftest',
            'password': 'password123'
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue('_auth_user_id' in self.client.session)

    def test_login_staff_invalido(self):
        """Verifica se credenciais inválidas falham."""
        response = self.client.post(reverse('accounts:login_staff'), {
            'username': 'stafftest',
            'password': 'wrongpassword'
        })
        self.assertEqual(response.status_code, 200)
        self.assertFalse('_auth_user_id' in self.client.session)

    def test_login_staff_nao_staff(self):
        """Verifica se usuário não-staff não consegue fazer login."""
        response = self.client.post(reverse('accounts:login_staff'), {
            'username': 'user_normal',
            'password': 'password123'
        })
        self.assertEqual(response.status_code, 200)
        self.assertFalse('_auth_user_id' in self.client.session)

    def test_logout_staff(self):
        """Verifica se logout funciona corretamente."""
        self.client.force_login(self.staff_user)
        self.assertTrue('_auth_user_id' in self.client.session)

        response = self.client.post(reverse('accounts:logout_staff'))
        self.assertEqual(response.status_code, 302)
        self.assertFalse('_auth_user_id' in self.client.session)

        