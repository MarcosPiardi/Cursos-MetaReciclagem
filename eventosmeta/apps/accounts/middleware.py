"""
Arquivo: middleware.py
Caminho: apps/accounts/middleware.py
Alteração: Criado middleware de troca obrigatória de senha
           Intercepta qualquer requisição autenticada e redireciona
           para tela de troca de senha se must_change_password = True
           Libera URLs de logout, troca de senha e arquivos estáticos
Data: 25/02/2026
Alteração: Removido '/admin/' dos prefixos liberados — Staff com
           must_change_password = True não pode acessar o admin
           sem trocar a senha primeiro.
           Adicionadas URLs mínimas do admin necessárias para
           que o redirect funcione sem loop.
Data: 26/02/2026
"""

from django.shortcuts import redirect


# URLs liberadas mesmo com must_change_password = True
URLS_LIBERADAS = [
    # Staff
    '/staff/senha/trocar-obrigatorio/',
    '/staff/logout/',
    # Interessado
    '/inscricao/senha/trocar-obrigatorio/',
    '/inscricao/logout/',
    # Admin mínimo — necessário para não causar loop no redirect
    '/admin/login/',
    '/admin/logout/',
    '/admin/jsi18n/',
]

# Prefixos sempre liberados (estáticos e mídia apenas)
PREFIXOS_LIBERADOS = [
    '/static/',
    '/media/',
]


class TrocarSenhaObrigatorioMiddleware:
    """
    Middleware que intercepta requisições de usuários autenticados
    com must_change_password = True e os redireciona para a tela
    de troca obrigatória de senha antes de qualquer outra ação.

    Funciona para dois tipos de usuário:
      - Usuario (Staff) → apps.accounts.models.Usuario
      - Interessado     → apps.interessados.models.Interessado
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        usuario = request.user
        path    = request.path

        # Verifica se há usuário autenticado com must_change_password
        if (
            usuario.is_authenticated
            and hasattr(usuario, 'must_change_password')
            and usuario.must_change_password
        ):
            # Libera prefixos (estáticos e mídia)
            for prefixo in PREFIXOS_LIBERADOS:
                if path.startswith(prefixo):
                    return self.get_response(request)

            # Libera URLs específicas
            if path in URLS_LIBERADAS:
                return self.get_response(request)

            # Determina para qual tela redirecionar
            # Staff → Usuario do Django (tem atributo username nativo)
            from apps.accounts.models import Usuario
            if isinstance(usuario, Usuario):
                return redirect('/staff/senha/trocar-obrigatorio/')

            # Interessado → redireciona para tela própria
            return redirect('/inscricao/senha/trocar-obrigatorio/')

        return self.get_response(request)
    
    