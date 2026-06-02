"""
Arquivo: test_views_exclusao.py
Caminho: apps/interessados/tests/test_views_exclusao.py
Testes para views de exclusao de dados (LGPD) - views_exclusao.py
Data: 29/05/2026
"""

from django.test import TestCase, override_settings
from django.urls import reverse

from apps.interessados.models import SolicitacaoExclusao
from .factories import InteressadoFactory


BACKEND = 'apps.interessados.authentication.InteressadoBackend'


class TestSolicitarExclusaoView(TestCase):
    """Testes para solicitar_exclusao_view"""

    @classmethod
    def setUpTestData(cls):
        cls.interessado = InteressadoFactory.create(is_active=True)
        cls.url = reverse('interessados:solicitar_exclusao')
        cls.login_url = reverse('interessados:login')
        cls.dashboard_url = reverse('interessados:dashboard')

    # --- ACESSO SEM LOGIN ---

    def test_sem_login_redirect_para_login(self):
        response = self.client.get(self.url)
        self.assertRedirects(response, self.login_url + '?next=' + self.url)

    def test_post_sem_login_redirect_para_login(self):
        response = self.client.post(self.url, {'confirmacao': 'CONFIRMAR'})
        self.assertRedirects(response, self.login_url + '?next=' + self.url)

    # --- INTERESSADO INATIVO ---

    def test_interessado_inativo_logout_e_redirect(self):
        self.interessado.is_active = False
        self.interessado.save()
        self.client.force_login(self.interessado, backend=BACKEND)
        response = self.client.get(self.url)
        self.assertRedirects(response, self.login_url + '?next=' + self.url)

    # --- GET SEM SOLICITACAO PENDENTE ---

    def test_get_sem_pendente_retorna_200(self):
        self.client.force_login(self.interessado, backend=BACKEND)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'interessados/exclusao/solicitar.html')

    # --- GET COM SOLICITACAO PENDENTE ---

    def test_get_com_pendente_redirect_dashboard(self):
        SolicitacaoExclusao.objects.create(
            interessado=self.interessado,
            nome_solicitante=self.interessado.nome,
            email_solicitante=self.interessado.email or '',
            status='PENDENTE',
        )
        self.client.force_login(self.interessado, backend=BACKEND)
        response = self.client.get(self.url)
        self.assertRedirects(response, self.dashboard_url)

    # --- POST COM CONFIRMACAO VALIDA ---

    def test_post_confirmacao_valida_cria_solicitacao(self):
        self.client.force_login(self.interessado, backend=BACKEND)
        response = self.client.post(self.url, {
            'confirmacao': 'CONFIRMAR',
            'motivo': 'Quero excluir meus dados',
        })
        self.assertRedirects(response, reverse('interessados:exclusao_solicitada'))

        solicitacao = SolicitacaoExclusao.objects.get(interessado=self.interessado)
        self.assertEqual(solicitacao.status, 'PENDENTE')
        self.assertEqual(solicitacao.motivo, 'Quero excluir meus dados')
        self.assertEqual(solicitacao.nome_solicitante, self.interessado.nome)

    def test_post_confirmacao_valida_sem_motivo(self):
        self.client.force_login(self.interessado, backend=BACKEND)
        response = self.client.post(self.url, {'confirmacao': 'CONFIRMAR'})
        self.assertRedirects(response, reverse('interessados:exclusao_solicitada'))
        self.assertTrue(
            SolicitacaoExclusao.objects.filter(interessado=self.interessado).exists()
        )

    # --- POST COM CONFIRMACAO INVALIDA ---

    def test_post_confirmacao_invalida_mostra_erro(self):
        self.client.force_login(self.interessado, backend=BACKEND)
        response = self.client.post(self.url, {
            'confirmacao': 'NAO_CONFIRMO',
            'motivo': 'Teste',
        })
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'interessados/exclusao/solicitar.html')
        self.assertIn('erro', response.context)
        self.assertIsNotNone(response.context['erro'])
        self.assertFalse(
            SolicitacaoExclusao.objects.filter(interessado=self.interessado).exists()
        )

    def test_post_confirmacao_vazia_mostra_erro(self):
        self.client.force_login(self.interessado, backend=BACKEND)
        response = self.client.post(self.url, {
            'confirmacao': '',
            'motivo': 'Teste',
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn('erro', response.context)
        self.assertIsNotNone(response.context['erro'])
        self.assertFalse(
            SolicitacaoExclusao.objects.filter(interessado=self.interessado).exists()
        )

    # --- POST COM SOLICITACAO PENDENTE ---

    def test_post_com_pendente_nao_cria_nova(self):
        SolicitacaoExclusao.objects.create(
            interessado=self.interessado,
            nome_solicitante=self.interessado.nome,
            email_solicitante=self.interessado.email or '',
            status='PENDENTE',
        )
        self.client.force_login(self.interessado, backend=BACKEND)
        response = self.client.post(self.url, {'confirmacao': 'CONFIRMAR'})
        self.assertRedirects(response, self.dashboard_url)
        self.assertEqual(
            SolicitacaoExclusao.objects.filter(interessado=self.interessado).count(),
            1,
        )


class TestExclusaoSolicitadaView(TestCase):
    """Testes para exclusao_solicitada_view"""

    @classmethod
    def setUpTestData(cls):
        cls.interessado = InteressadoFactory.create(is_active=True)
        cls.url = reverse('interessados:exclusao_solicitada')
        cls.login_url = reverse('interessados:login')

    def test_sem_login_redirect_para_login(self):
        response = self.client.get(self.url)
        self.assertRedirects(response, self.login_url + '?next=' + self.url)

    def test_get_com_login_retorna_200(self):
        self.client.force_login(self.interessado, backend=BACKEND)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'interessados/exclusao/solicitada.html')

        
