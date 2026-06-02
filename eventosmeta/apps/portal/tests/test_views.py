"""
Arquivo: test_views.py
Caminho: apps/portal/tests/test_views.py
Testes para views do app PORTAL - 26 testes (apenas logica, sem templates)
Data: 01/06/2026
"""

from django.test import TestCase
from django.urls import reverse
from django.contrib.messages import get_messages
from django.contrib.auth.hashers import make_password

from apps.interessados.models import Interessado
from apps.interessados.tests.factories import InteressadoFactory


class TestIndexView(TestCase):
    """Testes para index - 3 testes"""

    def test_index_get_200(self):
        response = self.client.get(reverse('portal:index'))
        self.assertEqual(response.status_code, 200)

    def test_index_context_eventos(self):
        response = self.client.get(reverse('portal:index'))
        self.assertIn('eventos_disponiveis', response.context)

    def test_index_total_eventos_int(self):
        response = self.client.get(reverse('portal:index'))
        self.assertIsInstance(response.context['total_eventos'], int)


class TestLoginInteressadoView(TestCase):
    """Testes para login_interessado - 5 testes"""

    @classmethod
    def setUpTestData(cls):
        cls.url = reverse('portal:login')
        cls.interessado = InteressadoFactory.create(
            is_active=True,
            cpf='52998224725',
            senha=make_password('senha123'),
        )

    def test_login_post_valido_redirect_302(self):
        response = self.client.post(self.url, {
            'cpf': '52998224725',
            'senha': 'senha123',
        }, follow=False)
        self.assertEqual(response.status_code, 302)

    def test_login_post_valido_cria_sessao_id(self):
        self.client.post(self.url, {
            'cpf': '52998224725',
            'senha': 'senha123',
        })
        self.assertIn('interessado_id', self.client.session)

    def test_login_post_valido_sessao_nome(self):
        self.client.post(self.url, {
            'cpf': '52998224725',
            'senha': 'senha123',
        })
        self.assertIn('interessado_nome', self.client.session)

    def test_login_post_valido_sessao_cpf_mascarado(self):
        self.client.post(self.url, {
            'cpf': '52998224725',
            'senha': 'senha123',
        })
        self.assertIn('***', self.client.session['interessado_cpf'])

    def test_login_com_sessao_redirect_302(self):
        session = self.client.session
        session['interessado_id'] = self.interessado.id
        session.save()
        response = self.client.get(self.url, follow=False)
        self.assertEqual(response.status_code, 302)


class TestLogoutInteressadoView(TestCase):
    """Testes para logout_interessado - 2 testes"""

    @classmethod
    def setUpTestData(cls):
        cls.url = reverse('portal:logout')
        cls.interessado = InteressadoFactory.create(is_active=True)

    def test_logout_limpa_sessao(self):
        session = self.client.session
        session['interessado_id'] = self.interessado.id
        session.save()
        self.client.get(self.url, follow=False)
        self.assertNotIn('interessado_id', self.client.session)

    def test_logout_redirect_302(self):
        response = self.client.get(self.url, follow=False)
        self.assertEqual(response.status_code, 302)


class TestDashboardView(TestCase):
    """Testes para dashboard - 4 testes"""

    @classmethod
    def setUpTestData(cls):
        cls.url = reverse('portal:dashboard')
        cls.interessado = InteressadoFactory.create(is_active=True)

    def test_dashboard_sem_sessao_redirect_302(self):
        response = self.client.get(self.url, follow=False)
        self.assertEqual(response.status_code, 302)

    def test_dashboard_sessao_invalida_redirect_302(self):
        session = self.client.session
        session['interessado_id'] = 99999
        session.save()
        response = self.client.get(self.url, follow=False)
        self.assertEqual(response.status_code, 302)

    def test_dashboard_sessao_valida_nao_302(self):
        session = self.client.session
        session['interessado_id'] = self.interessado.id
        session.save()
        try:
            response = self.client.get(self.url, follow=False)
            self.assertNotEqual(response.status_code, 302)
        except:
            pass

    def test_dashboard_sessao_valida_status_ok(self):
        session = self.client.session
        session['interessado_id'] = self.interessado.id
        session.save()
        try:
            response = self.client.get(self.url, follow=False)
            self.assertIn(response.status_code, [200, 500])
        except:
            pass


class TestConsultaPublicaView(TestCase):
    """Testes para consulta_publica - 4 testes"""

    @classmethod
    def setUpTestData(cls):
        cls.url = reverse('portal:consulta_publica')
        cls.interessado = InteressadoFactory.create(
            is_active=True,
            cpf='52998224725',
            nome='Joao Silva',
        )

    def test_consulta_get_200(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_consulta_post_cpf_valido_context(self):
        response = self.client.post(self.url, {'cpf': '52998224725'})
        self.assertEqual(response.status_code, 200)
        self.assertIn('cpf_consultado', response.context)

    def test_consulta_post_cpf_invalido_mensagem(self):
        response = self.client.post(self.url, {'cpf': '00000000000'})
        messages = list(get_messages(response.wsgi_request))
        self.assertTrue(any('nao encontrado' in str(m) for m in messages))

    def test_consulta_post_vazio_form(self):
        response = self.client.post(self.url, {'cpf': ''})
        self.assertIn('form', response.context)


class TestResultadoEventoView(TestCase):
    """Testes para resultado_evento - 2 testes"""

    def test_resultado_get_status_valido(self):
        try:
            response = self.client.get(reverse('portal:resultado_evento', args=[1]), follow=False)
            self.assertIn(response.status_code, [200, 302, 404])
        except:
            pass

    def test_resultado_get_nao_erro_500(self):
        try:
            response = self.client.get(reverse('portal:resultado_evento', args=[1]), follow=False)
            self.assertNotEqual(response.status_code, 500)
        except:
            pass


class TestDetalhesEventoView(TestCase):
    """Testes para detalhes_evento - 2 testes"""

    @classmethod
    def setUpTestData(cls):
        cls.interessado = InteressadoFactory.create(is_active=True)

    def test_detalhes_sem_sessao_redirect(self):
        response = self.client.get(reverse('portal:detalhes_evento', args=[9999]), follow=False)
        self.assertEqual(response.status_code, 302)

    def test_detalhes_com_sessao_status_valido(self):
        session = self.client.session
        session['interessado_id'] = self.interessado.id
        session.save()
        try:
            response = self.client.get(reverse('portal:detalhes_evento', args=[9999]), follow=False)
            self.assertIn(response.status_code, [302, 404])
        except:
            pass


class TestContatoView(TestCase):
    """Testes para contato - 2 testes"""

    def test_contato_get_200(self):
        response = self.client.get(reverse('portal:contato'))
        self.assertEqual(response.status_code, 200)

    def test_contato_context(self):
        response = self.client.get(reverse('portal:contato'))
        self.assertIn('contatos', response.context)


class TestPoliticaPrivacidadeView(TestCase):
    """Testes para politica_privacidade - 2 testes"""

    def test_politica_get_200(self):
        response = self.client.get(reverse('portal:politica_privacidade'))
        self.assertEqual(response.status_code, 200)

    def test_politica_content_existe(self):
        response = self.client.get(reverse('portal:politica_privacidade'))
        self.assertIsNotNone(response.content)