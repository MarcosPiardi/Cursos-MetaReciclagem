"""
Arquivo: base.py
Caminho: apps/selecao/tests/base.py
Classes base para testes do app Seleção
Data: 04/08/2026
"""

from django.test import TestCase, RequestFactory
from django.contrib.auth import get_user_model

from apps.academico.tests.factories import StatusMatriculaFactory


class BaseAdminTest(TestCase):
    """Classe base para testes de admin actions."""

    def setUp(self):
        super().setUp()
        self.factory = RequestFactory()
        self.User = get_user_model()
        self.staff_user = self.User.objects.create_user(
            username='staff',
            email='staff@test.com',
            password='pass123',
            is_staff=True
        )
        StatusMatriculaFactory(nome='Ativa')

        