"""
Arquivo: utils.py
Caminho: apps/interessados/utils.py
Alteração: CustomEmailBackend — desabilita verificação SSL/TLS
           necessária para servidor SMTP interno da prefeitura
           (IP: 10.28.10.54 porta 587)
Data: 23/02/2026
"""

import ssl
from django.core.mail.backends.smtp import EmailBackend
from django.utils.functional import cached_property


class CustomEmailBackend(EmailBackend):
    """
    Backend SMTP customizado para o servidor interno da prefeitura.

    O servidor usa TLS na porta 587 mas com certificado autoassinado,
    por isso desabilitamos a verificação de hostname e certificado.

    Sem isso, o Django levanta SSLCertVerificationError ao conectar.
    """

    @cached_property
    def ssl_context(self):
        if self.ssl_certfile or self.ssl_keyfile:
            # Certificado explícito fornecido — usa verificação normal
            ssl_context = ssl.SSLContext(protocol=ssl.PROTOCOL_TLS_CLIENT)
            ssl_context.load_cert_chain(self.ssl_certfile, self.ssl_keyfile)
            return ssl_context
        else:
            # Servidor interno com certificado autoassinado
            # Desabilita verificação para funcionar na rede da prefeitura
            ssl_context = ssl.create_default_context()
            ssl_context.check_hostname = False
            ssl_context.verify_mode = ssl.CERT_NONE
            return ssl_context