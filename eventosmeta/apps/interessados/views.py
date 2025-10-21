"""
ARQUIVO: apps/interessados/views.py
AÇÃO: SUBSTITUIR completamente o arquivo apps/interessados/views.py
MUDANÇA: Views de cadastro, login, logout e dashboard
"""

from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login as auth_login, logout as auth_logout
from .forms import CadastroInteressadoForm, LoginInteressadoForm
from .models import Interessado
from .authentication import InteressadoBackend


def cadastro_interessado(request):
    """
    View de cadastro para novos interessados.
    Primeiro acesso - cria conta com CPF, nome, email e senha.
    """
    # Se já está logado como interessado, redireciona para dashboard
    if hasattr(request.user, '__class__') and request.user.__class__.__name__ == 'Interessado':
        return redirect('interessados:dashboard')
    
    if request.method == 'POST':
        form = CadastroInteressadoForm(request.POST)
        if form.is_valid():
            interessado = form.save()
            messages.success(request, f'Cadastro realizado com sucesso! Bem-vindo(a), {interessado.nome}!')
            
            # Faz login automático após cadastro
            backend = InteressadoBackend()
            interessado_autenticado = backend.authenticate(
                request,
                cpf=interessado.cpf,
                password=form.cleaned_data['senha']
            )
            
            if interessado_autenticado:
                auth_login(request, interessado_autenticado, backend='apps.interessados.authentication.InteressadoBackend')
                return redirect('interessados:dashboard')
            else:
                return redirect('interessados:login')
        else:
            messages.error(request, 'Por favor, corrija os erros abaixo.')
    else:
        form = CadastroInteressadoForm()
    
    return render(request, 'interessados/cadastro.html', {'form': form})


def login_interessado(request):
    """
    View de login para interessados usando CPF + senha.
    """
    # Se já está logado, redireciona para dashboard
    if hasattr(request.user, '__class__') and request.user.__class__.__name__ == 'Interessado':
        return redirect('interessados:dashboard')
    
    if request.method == 'POST':
        form = LoginInteressadoForm(request.POST)
        if form.is_valid():
            cpf = form.cleaned_data['cpf']
            senha = form.cleaned_data['senha']
            
            # Autentica usando o backend customizado
            backend = InteressadoBackend()
            interessado = backend.authenticate(request, cpf=cpf, password=senha)
            
            if interessado:
                auth_login(request, interessado, backend='apps.interessados.authentication.InteressadoBackend')
                messages.success(request, f'Bem-vindo(a) de volta, {interessado.nome}!')
                return redirect('interessados:dashboard')
            else:
                messages.error(request, 'CPF ou senha incorretos.')
    else:
        form = LoginInteressadoForm()
    
    return render(request, 'interessados/login_interessado.html', {'form': form})


def logout_interessado(request):
    """
    View de logout para interessados.
    """
    auth_logout(request)
    messages.info(request, 'Você saiu do sistema.')
    return redirect('home')


def dashboard_interessado(request):
    """
    Dashboard/área do interessado.
    Apenas interessados logados podem acessar.
    """
    # Verifica se é um interessado logado
    if not hasattr(request.user, '__class__') or request.user.__class__.__name__ != 'Interessado':
        messages.error(request, 'Você precisa estar logado para acessar esta área.')
        return redirect('interessados:login')
    
    interessado = request.user
    
    context = {
        'interessado': interessado,
    }
    
    return render(request, 'interessados/dashboard.html', context)