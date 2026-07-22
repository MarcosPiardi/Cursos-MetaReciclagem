"""
Arquivo: middleware.py
Caminho: apps/accounts/middleware.py
Atualização:
 - 25/02/2026 - Criado middleware de troca obrigatória de senha
                Intercepta qualquer requisição autenticada e redireciona
                para tela de troca de senha se must_change_password = True
                Libera URLs de logout, troca de senha e arquivos estáticos
 - 26/02/2026 - Alteração: Removido '/admin/' dos prefixos liberados — Staff com
                must_change_password = True não pode acessar o admin
                sem trocar a senha primeiro.
                Adicionadas URLs mínimas do admin necessárias para
                que o redirect funcione sem loop.
 - 22/07/2026 - Refatorado: substituído paths hardcoded por resolve() e
                nomes de URL. Elimina dependência do prefixo /eventosmeta/
                que causava redirect loop e 404 nos testes.
              - Adicionada verificação por path para /trocar-obrigatorio/
                e /logout/, eliminando dependência de nomes de URL com
                ou sem namespace (interessados: vs interessados_).
"""

from django.shortcuts import redirect
from django.urls import resolve

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

            # 22/07/2026 - Libera URLs de logout (independente de prefixo)
            if path.endswith('/logout/'):
                return self.get_response(request)

            # 22/07/2026 - Libera URLs de troca obrigatória de senha
            # (independente de namespace: interessados: vs interessados_)
            if '/trocar-obrigatorio/' in path:
                return self.get_response(request)

            # Verifica por nome de URL para liberar URLs mínimas do admin
            try:
                match = resolve(path)
                if match.view_name in (
                    'admin:login',
                    'admin:logout',
                    'admin:jsi18n',
                ):
                    return self.get_response(request)
            except Exception:
                pass

            # Determina para qual tela redirecionar
            from apps.accounts.models import Usuario
            if isinstance(usuario, Usuario):
                return redirect('staff_trocar_senha_obrigatorio')

            # Interessado → redireciona para tela própria
            return redirect('interessados_trocar_senha_obrigatorio')

        return self.get_response(request)
