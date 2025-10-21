from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import LoginStaffForm


def login_staff(request):
    """
    View de login para staff/administradores.
    Usa o sistema padrão de autenticação do Django (username + password).
    """
    # Se já está logado, redireciona para dashboard
    if request.user.is_authenticated and request.user.is_staff:
        return redirect('accounts:dashboard_staff')
    
    if request.method == 'POST':
        form = LoginStaffForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            
            # Verifica se o usuário tem permissão de staff
            if user.is_staff:
                login(request, user)
                messages.success(request, f'Bem-vindo(a), {user.get_full_name() or user.username}!')
                
                # Redireciona para página solicitada ou dashboard
                next_page = request.GET.get('next', 'accounts:dashboard_staff')
                return redirect(next_page)
            else:
                messages.error(request, 'Você não tem permissão para acessar esta área.')
        else:
            messages.error(request, 'Usuário ou senha incorretos.')
    else:
        form = LoginStaffForm()
    
    return render(request, 'accounts/login_staff.html', {'form': form})


@login_required(login_url='/staff/login/')
def logout_staff(request):
    """
    View de logout para staff.
    """
    logout(request)
    messages.info(request, 'Você saiu do sistema.')
    return redirect('home')


@login_required(login_url='/staff/login/')
def dashboard_staff(request):
    """
    Dashboard/painel principal para staff.
    Apenas usuários com is_staff=True podem acessar.
    """
    # Verifica se realmente é staff
    if not request.user.is_staff:
        messages.error(request, 'Você não tem permissão para acessar esta área.')
        return redirect('home')
    
    context = {
        'usuario': request.user,
    }
    return render(request, 'accounts/dashboard_staff.html', context)