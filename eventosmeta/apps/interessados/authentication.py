"""
ARQUIVO: apps/interessados/authentication.py
Finalidade: Backend customizado para autenticacao por CPF
Atualizações: 
13/02/2026 — Adicionada verificacao de is_active nos metodos authenticate e get_user
29/05/2026 — Busca por cpf_hash em vez de cpf (EncryptedCharField)
"""

from django.contrib.auth.backends import BaseBackend
from .models import Interessado, gerar_hash_cpf


class InteressadoBackend(BaseBackend):
    """
    Backend de autenticacao para Interessados usando CPF.
    Corrigido: busca por cpf_hash porque cpf e EncryptedCharField.
    """

    def authenticate(self, request, cpf=None, password=None, **kwargs):
        """
        Autentica um interessado usando CPF e senha.
        Busca por cpf_hash (campo de busca deterministica) em vez de cpf
        (EncryptedCharField com criptografia nao-deterministica).

        Args:
            request: HttpRequest object
            cpf: CPF do interessado (11 digitos, pode estar formatado)
            password: Senha em texto plano

        Returns:
            Interessado object se autenticado, None caso contrario
        """
        if cpf is None or password is None:
            return None

        # Remove formatacao (pontos, tracos) para normalizar
        cpf_clean = ''.join(filter(str.isdigit, cpf))
        cpf_hash = gerar_hash_cpf(cpf_clean)

        try:
            interessado = Interessado.objects.get(cpf_hash=cpf_hash)

            if not interessado.is_active:
                return None

            if interessado.check_password(password):
                return interessado

        except Interessado.DoesNotExist:
            return None

        return None

    def get_user(self, user_id):
        """
        Recupera um interessado pelo ID.
        Necessario para manter a sessao ativa.

        Args:
            user_id: ID do interessado

        Returns:
            Interessado object se ativo, None caso contrario
        """
        try:
            interessado = Interessado.objects.get(pk=user_id)

            if interessado.is_active:
                return interessado
            return None

        except Interessado.DoesNotExist:
            return None
        
        