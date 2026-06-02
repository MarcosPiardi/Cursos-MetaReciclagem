"""
Arquivo: test_urls.py
Caminho: apps/portal/tests/test_urls.py
Testes de resolucao de URLs do app PORTAL
Data: 29/05/2026
"""

from django.test import SimpleTestCase
from django.urls import reverse, resolve

from apps.portal import views


class TestUrlsResolvem(SimpleTestCase):
    """Testa se cada named URL resolve para a view correta."""

    def test_index_url(self):
        url = reverse('portal:index')
        self.assertEqual(resolve(url).func, views.index)

    def test_login_url(self):
        url = reverse('portal:login')
        self.assertEqual(resolve(url).func, views.login_interessado)

    def test_logout_url(self):
        url = reverse('portal:logout')
        self.assertEqual(resolve(url).func, views.logout_interessado)

    def test_dashboard_url(self):
        url = reverse('portal:dashboard')
        self.assertEqual(resolve(url).func, views.dashboard)

    def test_consulta_publica_url(self):
        url = reverse('portal:consulta_publica')
        self.assertEqual(resolve(url).func, views.consulta_publica)

    def test_resultado_evento_url(self):
        url = reverse('portal:resultado_evento', args=[1])
        self.assertEqual(resolve(url).func, views.resultado_evento)

    def test_detalhes_evento_url(self):
        url = reverse('portal:detalhes_evento', args=[1])
        self.assertEqual(resolve(url).func, views.detalhes_evento)

    def test_contato_url(self):
        url = reverse('portal:contato')
        self.assertEqual(resolve(url).func, views.contato)

    def test_privacidade_url(self):
        url = reverse('portal:politica_privacidade')
        self.assertEqual(resolve(url).func, views.politica_privacidade)


class TestUrlsPath(SimpleTestCase):
    """Testa se cada named URL gera o path correto."""

    def test_index_path(self):
        self.assertEqual(reverse('portal:index'), '/')

    def test_login_path(self):
        self.assertEqual(reverse('portal:login'), '/login/')

    def test_logout_path(self):
        self.assertEqual(reverse('portal:logout'), '/logout/')

    def test_dashboard_path(self):
        self.assertEqual(reverse('portal:dashboard'), '/dashboard/')

    def test_consulta_publica_path(self):
        self.assertEqual(reverse('portal:consulta_publica'), '/consulta/')

    def test_resultado_evento_path(self):
        self.assertEqual(
            reverse('portal:resultado_evento', args=[42]),
            '/resultado/42/',
        )

    def test_detalhes_evento_path(self):
        self.assertEqual(
            reverse('portal:detalhes_evento', args=[7]),
            '/evento/7/',
        )

    def test_contato_path(self):
        self.assertEqual(reverse('portal:contato'), '/contato/')

    def test_privacidade_path(self):
        self.assertEqual(
            reverse('portal:politica_privacidade'),
            '/privacidade/',
        )


        