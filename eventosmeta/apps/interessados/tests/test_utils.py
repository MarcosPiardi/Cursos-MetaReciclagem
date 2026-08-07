"""
Arquivo: test_utils.py
Caminho: apps/interessados/tests/test_utils.py
Testes para CustomEmailBackend (utils.py)
Atualizações: 
 - 29/05/2026 - Criacao do arquivo
 - 18/06/2026 - Refatorado para pytest
"""

import ssl
from unittest.mock import patch

from django.core.mail.backends.smtp import EmailBackend

from apps.interessados.utils import CustomEmailBackend

class TestCustomEmailBackendSSLContext:
    """Testes para ssl_context do CustomEmailBackend"""

    def test_sem_certificate_desabilita_verificacao(self):
        backend = CustomEmailBackend(
            host="10.30.166.54",
            port=587,
            username="teste",
            password="senha",
            use_tls=True,
        )
        ctx = backend.ssl_context
        assert not ctx.check_hostname
        assert ctx.verify_mode == ssl.CERT_NONE

    @patch.object(ssl.SSLContext, "load_cert_chain")
    def test_com_ssl_certfile_mantem_verificacao(self, mock_load):
        backend = CustomEmailBackend(
            host="10.30.166.54",
            port=587,
            username="teste",
            password="senha",
            use_tls=True,
            ssl_certfile="/fake/cert.pem",
            ssl_keyfile="/fake/key.pem",
        )
        ctx = backend.ssl_context
        assert ctx.check_hostname
        mock_load.assert_called_once_with("/fake/cert.pem", "/fake/key.pem")

    def test_context_e_cached_property(self):
        backend = CustomEmailBackend(
            host="10.30.166.54",
            port=587,
            username="teste",
            password="senha",
            use_tls=True,
        )
        ctx1 = backend.ssl_context
        ctx2 = backend.ssl_context
        assert ctx1 is ctx2

    def test_ssl_context_sem_cert_e_sem_keyfile(self):
        backend = CustomEmailBackend(
            host="10.30.166.54",
            port=587,
            username="teste",
            password="senha",
            use_tls=True,
            ssl_certfile=None,
            ssl_keyfile=None,
        )
        ctx = backend.ssl_context
        assert not ctx.check_hostname
        assert ctx.verify_mode == ssl.CERT_NONE

class TestCustomEmailBackendHeranca:
    """Testes de heranca e configuracao basica"""

    def test_herda_de_emailbackend(self):
        assert issubclass(CustomEmailBackend, EmailBackend)

class TestCustomEmailBackend:
    """Testes de configuracao e comportamento"""

    def test_timeout_padrao_nao_definido(self):
        backend = CustomEmailBackend(
            host="10.30.166.54",
            port=587,
            username="teste",
            password="senha",
            use_tls=True,
        )
        assert backend.timeout is None

    def test_timeout_personalizado(self):
        backend = CustomEmailBackend(
            host="10.30.166.54",
            port=587,
            username="teste",
            password="senha",
            use_tls=True,
            timeout=30,
        )
        assert backend.timeout == 30


