"""
Arquivo: test_authentication.py
Caminho: apps/interessados/tests/test_authentication.py
Testes para o backend de autenticacao customizado InteressadoBackend
Data: 29/05/2026
"""

from django.test import TestCase
from django.http import HttpRequest

from apps.interessados.authentication import InteressadoBackend
from .factories import InteressadoFactory


class TestInteressadoBackendAuthenticate(TestCase):
    """Testes para o metodo authenticate do InteressadoBackend"""

    @classmethod
    def setUpTestData(cls):
        cls.cpf = '52998224725'
        cls.senha = 'senha123'
        cls.interessado_ativo = InteressadoFactory.create(
            cpf=cls.cpf,
            is_active=True,
        )
        cls.interessado_inativo = InteressadoFactory.create(
            cpf='98765432100',
            is_active=False,
        )
        cls.backend = InteressadoBackend()
        cls.request = HttpRequest()

    def test_autentica_com_cpf_e_senha_validos(self):
        result = self.backend.authenticate(
            self.request,
            cpf=self.cpf,
            password=self.senha,
        )
        self.assertIsNotNone(result)
        self.assertEqual(result.pk, self.interessado_ativo.pk)

    def test_autentica_com_senha_errada_retorna_none(self):
        result = self.backend.authenticate(
            self.request,
            cpf=self.cpf,
            password='senha_errada',
        )
        self.assertIsNone(result)

    def test_autentica_com_cpf_inexistente_retorna_none(self):
        result = self.backend.authenticate(
            self.request,
            cpf='00000000000',
            password=self.senha,
        )
        self.assertIsNone(result)

    def test_autentica_com_cpf_none_retorna_none(self):
        result = self.backend.authenticate(
            self.request,
            cpf=None,
            password=self.senha,
        )
        self.assertIsNone(result)

    def test_autentica_com_senha_none_retorna_none(self):
        result = self.backend.authenticate(
            self.request,
            cpf=self.cpf,
            password=None,
        )
        self.assertIsNone(result)

    def test_autentica_interessado_inativo_retorna_none(self):
        result = self.backend.authenticate(
            self.request,
            cpf=self.interessado_inativo.cpf,
            password='senha123',
        )
        self.assertIsNone(result)

    def test_autentica_sem_request_mas_com_cpf_valido(self):
        result = self.backend.authenticate(
            None,
            cpf=self.cpf,
            password=self.senha,
        )
        self.assertIsNotNone(result)
        self.assertEqual(result.pk, self.interessado_ativo.pk)


class TestInteressadoBackendGetUser(TestCase):
    """Testes para o metodo get_user do InteressadoBackend"""

    @classmethod
    def setUpTestData(cls):
        cls.interessado_ativo = InteressadoFactory.create(is_active=True)
        cls.interessado_inativo = InteressadoFactory.create(is_active=False)
        cls.backend = InteressadoBackend()

    def test_get_user_com_id_valido_retorna_interessado(self):
        result = self.backend.get_user(self.interessado_ativo.pk)
        self.assertIsNotNone(result)
        self.assertEqual(result.pk, self.interessado_ativo.pk)

    def test_get_user_com_id_inexistente_retorna_none(self):
        pk_inexistente = 99999
        result = self.backend.get_user(pk_inexistente)
        self.assertIsNone(result)

    def test_get_user_interessado_inativo_retorna_none(self):
        result = self.backend.get_user(self.interessado_inativo.pk)
        self.assertIsNone(result)

        