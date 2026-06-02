"""
Arquivo: test_middleware.py
Caminho: apps/accounts/tests/test_middleware.py
Finalidade: Testar o middleware de autenticação.
"""

from django.test import TestCase, RequestFactory
from django.contrib.sessions.middleware import SessionMiddleware
from django.contrib.auth.middleware import AuthenticationMiddleware
from apps.accounts.middleware import TrocarSenhaObrigatorioMiddleware
from apps.accounts.models import Usuario
from apps.interessados.tests.factories import InteressadoFactory


def _aplicar_middleware(request, user=None):
    """Aplica SessionMiddleware + AuthenticationMiddleware + TrocarSenhaObrigatorioMiddleware"""
    # Session
    session_middleware = SessionMiddleware(lambda r: None)
    session_middleware.process_request(request)
    request.session.save()

    # Auth
    auth_middleware = AuthenticationMiddleware(lambda r: None)
    auth_middleware.process_request(request)

    # Force login se user foi passado
    if user:
        request.user = user

    # Nosso middleware
    middleware = TrocarSenhaObrigatorioMiddleware(lambda r: None)
    response = middleware(request)
    return response


class TestTrocarSenhaObrigatorioMiddleware(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.usuario_staff = Usuario.objects.create_user(
            username='staff', email='staff@ex.com', password='123',
            cpf='11111111111', is_staff=True, is_active=True,
            must_change_password=False
        )
        self.usuario_comum = Usuario.objects.create_user(
            username='comum', email='comum@ex.com', password='123',
            cpf='22222222222', is_staff=False, is_active=True,
            must_change_password=False
        )
        self.interessado = InteressadoFactory(
            is_active=True, must_change_password=False
        )

    def test_usuario_nao_autenticado_passa(self):
        request = self.factory.get('/admin/')
        response = _aplicar_middleware(request)
        self.assertIsNone(response)

    def test_usuario_sem_must_change_password_passa(self):
        request = self.factory.get('/admin/')
        response = _aplicar_middleware(request, user=self.usuario_comum)
        self.assertIsNone(response)

    def test_usuario_com_must_change_password_url_liberada_staff(self):
        self.usuario_staff.must_change_password = True
        self.usuario_staff.save()
        request = self.factory.get('/staff/logout/')
        response = _aplicar_middleware(request, user=self.usuario_staff)
        self.assertIsNone(response)

    def test_usuario_com_must_change_password_url_restrita_staff(self):
        self.usuario_staff.must_change_password = True
        self.usuario_staff.save()
        request = self.factory.get('/admin/')
        response = _aplicar_middleware(request, user=self.usuario_staff)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/staff/senha/trocar-obrigatorio/')

    def test_interessado_com_must_change_password_url_restrita(self):
        self.interessado.must_change_password = True
        self.interessado.save()
        request = self.factory.get('/inscricao/')
        response = _aplicar_middleware(request, user=self.interessado)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/inscricao/senha/trocar-obrigatorio/')

    def test_static_url_liberada_mesmo_com_must_change_password(self):
        self.usuario_staff.must_change_password = True
        self.usuario_staff.save()
        request = self.factory.get('/static/css/style.css')
        response = _aplicar_middleware(request, user=self.usuario_staff)
        self.assertIsNone(response)

    def test_media_url_liberada_mesmo_com_must_change_password(self):
        self.usuario_staff.must_change_password = True
        self.usuario_staff.save()
        request = self.factory.get('/media/fotos/foto.jpg')
        response = _aplicar_middleware(request, user=self.usuario_staff)
        self.assertIsNone(response)

    def test_url_admin_login_liberada(self):
        self.usuario_staff.must_change_password = True
        self.usuario_staff.save()
        request = self.factory.get('/admin/login/')
        response = _aplicar_middleware(request, user=self.usuario_staff)
        self.assertIsNone(response)

    def test_url_admin_logout_liberada(self):
        self.usuario_staff.must_change_password = True
        self.usuario_staff.save()
        request = self.factory.get('/admin/logout/')
        response = _aplicar_middleware(request, user=self.usuario_staff)
        self.assertIsNone(response)




