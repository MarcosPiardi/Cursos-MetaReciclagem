"""
ARQUIVO: apps/interessados/authentication.py
AÇÃO: CRIAR novo arquivo apps/interessados/authentication.py
MUDANÇA: Backend customizado para autenticação por CPF
"""

"""
Backend de autenticação customizado para Interessados.
Permite login usando CPF + senha ao invés de username + senha.
"""
from django.contrib.auth.backends import BaseBackend
from .models import Interessado


class InteressadoBackend(BaseBackend):
    """
    Backend de autenticação para Interessados usando CPF.
    """
    
    def authenticate(self, request, cpf=None, password=None, **kwargs):
        """
        Autentica um interessado usando CPF e senha.
        
        Args:
            request: HttpRequest object
            cpf: CPF do interessado (11 dígitos)
            password: Senha em texto plano
            
        Returns:
            Interessado object se autenticado, None caso contrário
        """
        if cpf is None or password is None:
            return None
        
        try:
            # Busca interessado pelo CPF
            interessado = Interessado.objects.get(cpf=cpf)
            
            # Verifica a senha
            if interessado.check_password(password):
                return interessado
            
        except Interessado.DoesNotExist:
            # Retorna None se não encontrar o interessado
            return None
        
        return None
    
    def get_user(self, user_id):
        """
        Recupera um interessado pelo ID.
        Necessário para manter a sessão ativa.
        
        Args:
            user_id: ID do interessado
            
        Returns:
            Interessado object ou None
        """
        try:
            return Interessado.objects.get(pk=user_id)
        except Interessado.DoesNotExist:
            return None
        

        