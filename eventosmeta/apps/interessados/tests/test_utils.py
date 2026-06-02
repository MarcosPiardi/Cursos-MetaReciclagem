"""
Arquivo: test_utils.py
Caminho: apps/interessados/tests/test_utils.py
Testes para CustomEmailBackend (utils.py)
Data: 29/05/2026
"""

import ssl
from unittest.mock import patch

from django.test import SimpleTestCase
from django.core.mail.backends.smtp import EmailBackend

from apps.interessados.utils import CustomEmailBackend


class TestCustomEmailBackendSSLContext(SimpleTestCase):
    """Testes para ssl_context do CustomEmailBackend"""

    def test_sem_certificate_desabilita_verificacao(self):
        backend = CustomEmailBackend(
            host='10.28.10.54',
            port=587,
            username='teste',
            password='senha',
            use_tls=True,
        )
        ctx = backend.ssl_context
        self.assertFalse(ctx.check_hostname)
        self.assertEqual(ctx.verify_mode, ssl.CERT_NONE)

    @patch.object(ssl.SSLContext, 'load_cert_chain')
    def test_com_ssl_certfile_mantem_verificacao(self, mock_load):
        backend = CustomEmailBackend(
            host='10.28.10.54',
            port=587,
            username='teste',
            password='senha',
            use_tls=True,
            ssl_certfile='/fake/cert.pem',
            ssl_keyfile='/fake/key.pem',
        )
        ctx = backend.ssl_context
        self.assertTrue(ctx.check_hostname)
        mock_load.assert_called_once_with('/fake/cert.pem', '/fake/key.pem')

    def test_context_e_cached_property(self):
        backend = CustomEmailBackend(
            host='10.28.10.54',
            port=587,
            username='teste',
            password='senha',
            use_tls=True,
        )
        ctx1 = backend.ssl_context
        ctx2 = backend.ssl_context
        self.assertIs(ctx1, ctx2)

    def test_ssl_context_sem_cert_e_sem_keyfile(self):
        backend = CustomEmailBackend(
            host='10.28.10.54',
            port=587,
            username='teste',
            password='senha',
            use_tls=True,
            ssl_certfile=None,
            ssl_keyfile=None,
        )
        ctx = backend.ssl_context
        self.assertFalse(ctx.check_hostname)
        self.assertEqual(ctx.verify_mode, ssl.CERT_NONE)


class TestCustomEmailBackendHeranca(SimpleTestCase):
    """Testes de heranca e configuracao basica"""

    def test_herda_de_emailbackend(self):
        self.assertTrue(issubclass(CustomEmailBackend, EmailBackend))


class TestCustomEmailBackend(SimpleTestCase):
    """Testes de configuracao e comportamento"""

    def test_timeout_padrao_nao_definido(self):
        backend = CustomEmailBackend(
            host='10.28.10.54',
            port=587,
            username='teste',
            password='senha',
            use_tls=True,
        )
        self.assertIsNone(backend.timeout)

    def test_timeout_personalizado(self):
        backend = CustomEmailBackend(
            host='10.28.10.54',
            port=587,
            username='teste',
            password='senha',
            use_tls=True,
            timeout=30,
        )
        self.assertEqual(backend.timeout, 30)

        


