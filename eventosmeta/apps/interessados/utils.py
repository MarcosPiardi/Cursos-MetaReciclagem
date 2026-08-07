"""
Arquivo: utils.py
Caminho: apps/interessados/utils.py
Finalidade: Backends de e-mail customizados para o servidor SMTP interno da prefeitura
Atualizacoes:
 - 23/02/2026 - CustomEmailBackend — desabilita verificacao SSL/TLS
                necessaria para servidor SMTP interno da prefeitura
                (IP: 10.30.166.54 porta 587)
 - 07/08/2026 - Adicionado FallbackEmailBackend — tenta SMTP e se falhar
                usa console.EmailBackend, permitindo desenvolvimento local
                fora da rede da prefeitura sem alterar o .env
 - 07/08/2026 - Refatoracao: FallbackEmailBackend agora herda de CustomEmailBackend
                eliminando duplicacao do ssl_context (DRY)
"""
import ssl
import socket
import logging

from django.core.mail.backends.smtp import EmailBackend
from django.core.mail.backends.console import EmailBackend as ConsoleEmailBackend
from django.utils.functional import cached_property

logger = logging.getLogger(__name__)

class CustomEmailBackend(EmailBackend):
    """
    Backend SMTP customizado para o servidor interno da prefeitura.

    O servidor usa TLS na porta 587 mas com certificado autoassinado,
    por isso desabilitamos a verificacao de hostname e certificado.

    Sem isso, o Django levanta SSLCertVerificationError ao conectar.
    """

    @cached_property
    def ssl_context(self):
        if self.ssl_certfile or self.ssl_keyfile:
            # Certificado explicito fornecido — usa verificacao normal
            ssl_context = ssl.SSLContext(protocol=ssl.PROTOCOL_TLS_CLIENT)
            ssl_context.load_cert_chain(self.ssl_certfile, self.ssl_keyfile)
            return ssl_context
        else:
            # Servidor interno com certificado autoassinado
            # Desabilita verificacao para funcionar na rede da prefeitura
            ssl_context = ssl.create_default_context()
            ssl_context.check_hostname = False
            ssl_context.verify_mode = ssl.CERT_NONE
            return ssl_context

class FallbackEmailBackend(CustomEmailBackend):
    """
    Backend com fallback automatico.

    Herda de CustomEmailBackend (mesma configuracao de SSL/TLS).
    Antes de enviar, verifica se o servidor SMTP responde.
    Se nao responder em 5 segundos, redireciona para o console.

    Permite desenvolver fora da rede da prefeitura sem alterar
    o .env ou a configuracao do settings.
    """

    def _servidor_disponivel(self):
        """Verifica se o servidor SMTP responde na porta configurada."""
        try:
            sock = socket.create_connection(
                (self.host, self.port),
                timeout=5
            )
            sock.close()
            return True
        except (socket.timeout, ConnectionRefusedError, OSError):
            return False

    def send_messages(self, email_messages):
        """
        Envia mensagens via SMTP. Se o servidor nao responder,
        cai para o console automaticamente.
        """
        if not self._servidor_disponivel():
            logger.warning(
                'Servidor SMTP %s:%s nao respondeu. '
                'Redirecionando e-mails para o console.',
                self.host, self.port
            )
            console = ConsoleEmailBackend(
                fail_silently=self.fail_silently
            )
            return console.send_messages(email_messages)

        return super().send_messages(email_messages)



    