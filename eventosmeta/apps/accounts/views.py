"""
Arquivo: views.py
Caminho: apps/accounts/views.py
Alteração: Login staff redireciona para admin
Data: 20/01/2026
Alteração: Adicionado link de recuperação de senha no contexto do login
Data: 24/02/2026
Alteração: URL de recuperação corrigida para staff_senha_recuperar
Data: 24/02/2026
"""
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm


def login_staff(request):
    """Login para usuários staff - redireciona para admin"""

    if request.user.is_authenticated and request.user.is_staff:
        return redirect('/admin/')

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)

            if user is not None and user.is_staff:
                login(request, user)
                messages.success(request, f'Bem-vindo, {user.username}!')
                return redirect('/admin/')
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
        'url_recuperar_senha': 'staff_senha_recuperar',  # ← corrigido
    })


def logout_staff(request):
    """Logout do staff"""
    logout(request)
    messages.success(request, 'Você saiu do sistema.')
    return redirect('accounts:login_staff')

