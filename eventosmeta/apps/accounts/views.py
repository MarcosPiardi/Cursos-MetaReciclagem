"""
Arquivo: views.py
Caminho: apps/accounts/views.py
Alteração: Login staff redireciona para admin
Data: 20/01/2026
Alteração: Adicionado link de recuperação de senha no contexto do login
Data: 24/02/2026
Alteração: URL de recuperação corrigida para staff_senha_recuperar
Data: 24/02/2026
Alteração: Adicionada view trocar_senha_obrigatorio_view (Fluxo B)
           Intercepta login de Staff com must_change_password = True
           e força troca de senha antes de qualquer outra ação
Data: 25/02/2026
Atualização:
 - 22/07/2026 - Redirects hardcoded /admin/ trocados por reverse('admin:index')
                para incluir automaticamente o prefixo /eventosmeta/
"""

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required

def login_staff(request):
    """Login para usuários staff - redireciona para admin customizado"""

    if request.user.is_authenticated and request.user.is_staff:
        return redirect('admin:index')

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request=request, username=username, password=password)

            if user is not None and user.is_staff:
                login(request, user)
                messages.success(request, f'Bem-vindo, {user.username}!')
                # Middleware intercepta e redireciona se must_change_password = True
                return redirect('admin:index')
            else:
                messages.error(
                    request,
                    'Você não tem permissão para acessar esta área.'
                )
        else:
            messages.error(request, 'Usuário ou senha incorretos.')
    else:
        form = AuthenticationForm()

    return render(request, 'accounts/login_staff.html', {
        'form': form,
        'url_recuperar_senha': 'staff_senha_recuperar',
    })

def logout_staff(request):
    """Logout do staff"""
    logout(request)
    messages.success(request, 'Você saiu do sistema.')
    return redirect('accounts:login_staff')

# ==============================================================================
# FLUXO B — TROCA OBRIGATÓRIA DE SENHA — STAFF
# Adicionado: 25/02/2026
# Acionado pelo middleware TrocarSenhaObrigatorioMiddleware quando
# must_change_password = True no model Usuario.
# O usuário não consegue acessar nenhuma outra página até trocar a senha.
# ==============================================================================

@login_required(login_url='/staff/login/')
def trocar_senha_obrigatorio_view(request):
    """
    View de troca obrigatória de senha para usuários Staff.

    Exibida pelo middleware quando must_change_password = True.
    Após a troca bem-sucedida:
      - must_change_password é definido como False
      - Usuário é redirecionado para o admin normalmente
    """
    usuario = request.user

    # Segurança extra: se chegou aqui sem must_change_password, redireciona
    if not usuario.must_change_password:
        # 22/07/2026 - Alterado de '/admin/' para reverse('admin:index')
        return redirect('admin:index')

    erro = None

    if request.method == 'POST':
        nova_senha      = request.POST.get('nova_senha', '').strip()
        confirmar_senha = request.POST.get('confirmar_senha', '').strip()

        if len(nova_senha) < 8:
            erro = 'A nova senha deve ter no mínimo 8 caracteres.'
        elif nova_senha != confirmar_senha:
            erro = 'As senhas não coincidem. Tente novamente.'
        else:
            usuario.set_password(nova_senha)
            usuario.must_change_password = False
            usuario.save()

            # Re-autentica para não perder a sessão após troca de senha
            from django.contrib.auth import update_session_auth_hash
            update_session_auth_hash(request, usuario)

            messages.success(
                request,
                '✅ Senha alterada com sucesso! Bem-vindo ao sistema.'
            )
            # 22/07/2026 - Alterado de '/admin/' para reverse('admin:index')
            return redirect('admin:index')

    return render(request, 'accounts/senha/adm_trocar_obrigatorio.html', {
        'erro'   : erro,
        'usuario': usuario,
    })


