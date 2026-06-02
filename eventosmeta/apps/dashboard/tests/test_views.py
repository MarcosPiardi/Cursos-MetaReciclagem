"""
Arquivo: test_views.py
Caminho: apps/dashboard/tests/test_views.py
Atualizações
29/05/2026 - Criação do arquivo 
"""

from django.test import TestCase, Client
from django.contrib.auth import get_user_model


class TestDashboardViews(TestCase):
    """Smoke tests para as views de dashboard HTML"""

    @classmethod
    def setUpTestData(cls):
        User = get_user_model()
        cls.staff = User.objects.create_user(
            username="staff",
            email="staff@test.com",
            password="test123",
            cpf="11111111111",
            is_staff=True,
        )
        cls.user = User.objects.create_user(
            username="user",
            email="user@test.com",
            password="test123",
            cpf="22222222222",
            is_staff=False,
        )

    def setUp(self):
        self.client = Client()

    def _login_staff(self):
        self.client.force_login(self.staff)

    def _login_user(self):
        self.client.force_login(self.user)

    @staticmethod
    def _url(name, *args):
        from django.urls import reverse
        return reverse(name, args=args)

    # --- Dashboard Academico ---

    def test_dashboard_academico_sem_auth_redireciona(self):
        response = self.client.get(self._url("dashboard_academico"))
        self.assertEqual(response.status_code, 302)
        self.assertIn("/admin/login/", response.url)

    def test_dashboard_academico_non_staff_redireciona(self):
        self._login_user()
        response = self.client.get(self._url("dashboard_academico"))
        self.assertEqual(response.status_code, 302)
        self.assertIn("/admin/login/", response.url)

    def test_dashboard_academico_staff_200(self):
        self._login_staff()
        response = self.client.get(self._url("dashboard_academico"))
        self.assertEqual(response.status_code, 200)

    def test_dashboard_academico_sem_dados_nao_quebra(self):
        """Banco vazio nao causa erro 500"""
        self._login_staff()
        response = self.client.get(self._url("dashboard_academico"))
        self.assertEqual(response.status_code, 200)

    # --- Dashboard Eventos ---

    def test_dashboard_eventos_sem_auth_redireciona(self):
        response = self.client.get(self._url("dashboard_eventos"))
        self.assertEqual(response.status_code, 302)

    def test_dashboard_eventos_staff_200(self):
        self._login_staff()
        response = self.client.get(self._url("dashboard_eventos"))
        self.assertEqual(response.status_code, 200)

    # --- Dashboard Interessados ---

    def test_dashboard_interessados_sem_auth_redireciona(self):
        response = self.client.get(self._url("dashboard_interessados"))
        self.assertEqual(response.status_code, 302)

    def test_dashboard_interessados_staff_200(self):
        self._login_staff()
        response = self.client.get(self._url("dashboard_interessados"))
        self.assertEqual(response.status_code, 200)

    def test_dashboard_interessados_total_zero_nao_quebra(self):
        """Divisao por zero nos percentuais com banco vazio"""
        self._login_staff()
        response = self.client.get(self._url("dashboard_interessados"))
        self.assertEqual(response.status_code, 200)

    # --- Dashboard Processo Seletivo ---

    def test_dashboard_processo_seletivo_sem_auth_redireciona(self):
        response = self.client.get(self._url("dashboard_processo_seletivo"))
        self.assertEqual(response.status_code, 302)

    def test_dashboard_processo_seletivo_staff_200(self):
        self._login_staff()
        response = self.client.get(self._url("dashboard_processo_seletivo"))
        self.assertEqual(response.status_code, 200)

    # --- Dashboard LGPD ---

    def test_dashboard_lgpd_sem_auth_redireciona(self):
        response = self.client.get(self._url("dashboard_lgpd"))
        self.assertEqual(response.status_code, 302)

    def test_dashboard_lgpd_staff_200(self):
        self._login_staff()
        response = self.client.get(self._url("dashboard_lgpd"))
        self.assertEqual(response.status_code, 200)


class TestDashboardPdfViews(TestCase):
    """Smoke tests para as views de PDF"""

    @classmethod
    def setUpTestData(cls):
        User = get_user_model()
        cls.staff = User.objects.create_user(
            username="staff2",
            email="staff2@test.com",
            password="test123",
            cpf="33333333333",
            is_staff=True,
        )

    def setUp(self):
        self.client = Client()

    def _login(self):
        self.client.force_login(self.staff)

    @staticmethod
    def _url(name, *args):
        from django.urls import reverse
        return reverse(name, args=args)

    # --- PDF Interessados ---

    def test_pdf_interessados_sem_auth_redireciona(self):
        response = self.client.get(self._url("dashboard_interessados_pdf"))
        self.assertEqual(response.status_code, 302)

    def test_pdf_interessados_staff_200(self):
        self._login()
        response = self.client.get(self._url("dashboard_interessados_pdf"))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response["Content-Type"], "application/pdf")

    def test_pdf_interessados_sem_dados_nao_quebra(self):
        self._login()
        response = self.client.get(self._url("dashboard_interessados_pdf"))
        self.assertEqual(response.status_code, 200)

    # --- PDF Eventos ---

    def test_pdf_eventos_sem_auth_redireciona(self):
        response = self.client.get(self._url("dashboard_eventos_pdf"))
        self.assertEqual(response.status_code, 302)

    def test_pdf_eventos_staff_200(self):
        self._login()
        response = self.client.get(self._url("dashboard_eventos_pdf"))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response["Content-Type"], "application/pdf")

    # --- PDF Academico ---

    def test_pdf_academico_sem_auth_redireciona(self):
        response = self.client.get(self._url("dashboard_academico_pdf"))
        self.assertEqual(response.status_code, 302)

    def test_pdf_academico_staff_200(self):
        self._login()
        response = self.client.get(self._url("dashboard_academico_pdf"))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response["Content-Type"], "application/pdf")

    # --- PDF Processo Seletivo ---

    def test_pdf_processo_seletivo_sem_auth_redireciona(self):
        response = self.client.get(self._url("dashboard_processo_seletivo_pdf"))
        self.assertEqual(response.status_code, 302)

    def test_pdf_processo_seletivo_staff_200(self):
        self._login()
        response = self.client.get(self._url("dashboard_processo_seletivo_pdf"))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response["Content-Type"], "application/pdf")

        



