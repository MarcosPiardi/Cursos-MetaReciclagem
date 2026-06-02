"""
Arquivo: test_urls.py
Caminho: apps/interessados/tests/test_urls.py
Testes de resolucao de URLs do app Interessados
Data: 29/05/2026 - Criação do arquivo
"""


from django.test import SimpleTestCase
from django.urls import reverse, resolve

from apps.interessados import views
from apps.interessados import views_exclusao


PREFIXO = '/inscricao/'


class TestUrlsResolvem(SimpleTestCase):

    def test_cadastro_url(self):
        url = reverse('interessados:cadastro')
        self.assertEqual(resolve(url).func, views.cadastro_view)

    def test_login_url(self):
        url = reverse('interessados:login')
        self.assertEqual(resolve(url).func, views.login_view)

    def test_logout_url(self):
        url = reverse('interessados:logout')
        self.assertEqual(resolve(url).func, views.logout_view)

    def test_meus_dados_url(self):
        url = reverse('interessados:meus_dados')
        self.assertEqual(resolve(url).func, views.meus_dados_view)

    def test_dashboard_url(self):
        url = reverse('interessados:dashboard')
        self.assertEqual(resolve(url).func, views.dashboard_view)

    def test_detalhes_url(self):
        url = reverse('interessados:detalhes', args=[1])
        self.assertEqual(resolve(url).func, views.detalhes_view)

    def test_inscrever_evento_url(self):
        url = reverse('interessados:inscrever_evento', args=[1])
        self.assertEqual(resolve(url).func, views.inscrever_evento_view)

    def test_senha_recuperar_url(self):
        url = reverse('interessados:senha_recuperar')
        self.assertEqual(resolve(url).func, views.senha_recuperar_view)

    def test_senha_recuperar_enviado_url(self):
        url = reverse('interessados:senha_recuperar_enviado')
        self.assertEqual(resolve(url).func, views.senha_recuperar_enviado_view)

    def test_senha_redefinir_url(self):
        url = reverse('interessados:senha_redefinir', args=['abc123'])
        self.assertEqual(resolve(url).func, views.senha_redefinir_view)

    def test_senha_redefinir_concluido_url(self):
        url = reverse('interessados:senha_redefinir_concluido')
        self.assertEqual(resolve(url).func, views.senha_redefinir_concluido_view)

    def test_senha_sem_email_url(self):
        url = reverse('interessados:senha_sem_email')
        self.assertEqual(resolve(url).func, views.senha_sem_email_view)

    def test_solicitar_exclusao_url(self):
        url = reverse('interessados:solicitar_exclusao')
        self.assertEqual(resolve(url).func, views_exclusao.solicitar_exclusao_view)

    def test_exclusao_solicitada_url(self):
        url = reverse('interessados:exclusao_solicitada')
        self.assertEqual(resolve(url).func, views_exclusao.exclusao_solicitada_view)


PREFIXO = '/inscricao/'


class TestUrlsPath(SimpleTestCase):

    def test_cadastro_path(self):
        self.assertEqual(reverse('interessados:cadastro'), PREFIXO + 'cadastro/')

    def test_login_path(self):
        self.assertEqual(reverse('interessados:login'), PREFIXO + 'login/')

    def test_logout_path(self):
        self.assertEqual(reverse('interessados:logout'), PREFIXO + 'logout/')

    def test_meus_dados_path(self):
        self.assertEqual(reverse('interessados:meus_dados'), PREFIXO + 'meus-dados/')

    def test_dashboard_path(self):
        self.assertEqual(reverse('interessados:dashboard'), PREFIXO + 'dashboard/')

    def test_detalhes_path(self):
        self.assertEqual(
            reverse('interessados:detalhes', args=[42]),
            PREFIXO + 'inscricao/42/detalhes/',
        )

    def test_inscrever_evento_path(self):
        self.assertEqual(
            reverse('interessados:inscrever_evento', args=[7]),
            PREFIXO + 'inscrever/7/',
        )

    def test_senha_recuperar_path(self):
        self.assertEqual(reverse('interessados:senha_recuperar'), PREFIXO + 'senha/recuperar/')

    def test_senha_recuperar_enviado_path(self):
        self.assertEqual(
            reverse('interessados:senha_recuperar_enviado'),
            PREFIXO + 'senha/recuperar/enviado/',
        )

    def test_senha_redefinir_path(self):
        self.assertEqual(
            reverse('interessados:senha_redefinir', args=['TOKEN']),
            PREFIXO + 'senha/redefinir/TOKEN/',
        )

    def test_senha_redefinir_concluido_path(self):
        self.assertEqual(
            reverse('interessados:senha_redefinir_concluido'),
            PREFIXO + 'senha/redefinir/concluido/',
        )

    def test_senha_sem_email_path(self):
        self.assertEqual(
            reverse('interessados:senha_sem_email'),
            PREFIXO + 'senha/sem-email/',
        )

    def test_solicitar_exclusao_path(self):
        self.assertEqual(
            reverse('interessados:solicitar_exclusao'),
            PREFIXO + 'exclusao/solicitar/',
        )

    def test_exclusao_solicitada_path(self):
        self.assertEqual(
            reverse('interessados:exclusao_solicitada'),
            PREFIXO + 'exclusao/solicitada/',
        )
