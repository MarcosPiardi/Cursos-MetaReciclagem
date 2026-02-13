"""
ARQUIVO: apps/interessados/authentication.py
AÇÃO: CRIAR novo arquivo apps/interessados/authentication.py
MUDANÇA: Backend customizado para autenticação por CPF

Alteração: Adicionada verificação de is_active nos métodos authenticate e get_user
Data: 13/02/2026
"""

"""
Backend de autenticação customizado para Interessados.
Permite login usando CPF + senha ao invés de username + senha.
ADICIONADO: Verificação de is_active para segurança (13/02/2026)
"""
from django.contrib.auth.backends import BaseBackend
from .models import Interessado


class InteressadoBackend(BaseBackend):
    """
    Backend de autenticação para Interessados usando CPF.
    ADICIONADO: Verificação de is_active em 13/02/2026
    """
    
    def authenticate(self, request, cpf=None, password=None, **kwargs):
        """
        Autentica um interessado usando CPF e senha.
        ADICIONADO: Verificação de is_active em 13/02/2026
        
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
            
            # ============================================================
            # VALIDAÇÃO CRÍTICA: VERIFICAR SE ESTÁ ATIVO
            # Data: 13/02/2026
            # ============================================================
            if not interessado.is_active:
                return None
            
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
        ADICIONADO: Verificação de is_active em 13/02/2026
        
        Args:
            user_id: ID do interessado
            
        Returns:
            Interessado object ou None
        """
        try:
            interessado = Interessado.objects.get(pk=user_id)
            
            # ============================================================
            # VALIDAÇÃO CRÍTICA: VERIFICAR SE AINDA ESTÁ ATIVO
            # Data: 13/02/2026
            # ============================================================
            if interessado.is_active:
                return interessado
            return None
            
        except Interessado.DoesNotExist:
            return None
        
        