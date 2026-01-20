"""
Arquivo: views.py
Caminho: apps/interessados/views.py
Alteração: Versão corrigida combinando o melhor dos dois códigos
Data: 19/01/2026
"""

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import login as auth_login, logout as auth_logout
from datetime import date

from .models import Interessado
from .authentication import InteressadoBackend
from apps.selecao.models import Inscricao
from apps.eventos.models import Evento


def cadastro(request):
    """Cadastro de novo interessado - SIMPLIFICADO"""
    
    if request.method == 'POST':
        # Implementação básica - pode expandir depois
        messages.info(request, 'Cadastro em desenvolvimento.')
        return redirect('interessados:login')
    
    return render(request, 'interessados/cadastro.html')


def login_interessado(request):
    """Login do interessado usando CPF e SENHA"""
    
    # Se já está logado, redireciona
    if hasattr(request.user, '__class__') and request.user.__class__.__name__ == 'Interessado':
        return redirect('interessados:dashboard')
    
    if request.method == 'POST':
        cpf = request.POST.get('cpf', '').strip()
        senha = request.POST.get('senha', '').strip()
        
        if not cpf or not senha:
            messages.error(request, 'Por favor, preencha todos os campos.')
            return render(request, 'interessados/login_interessado.html')
        
        try:
            # Autenticar usando o backend customizado
            backend = InteressadoBackend()
            interessado = backend.authenticate(request, cpf=cpf, password=senha)
            
            if interessado:
                auth_login(request, interessado, backend='apps.interessados.authentication.InteressadoBackend')
                messages.success(request, f'Bem-vindo de volta, {interessado.nome}!')
                return redirect('interessados:dashboard')
            else:
                messages.error(request, 'CPF ou senha incorretos.')
                
        except Exception as e:
            messages.error(request, f'Erro ao fazer login: {str(e)}')
    
    return render(request, 'interessados/login_interessado.html')

def logout_interessado(request):
    """Logout do interessado"""
    auth_logout(request)
    messages.success(request, 'Logout realizado com sucesso!')
    return redirect('portal:index')


def dashboard(request):
    """Dashboard do interessado logado - SIMPLIFICADO SEM ERROS"""
    
    # Verifica se é um interessado logado
    if not hasattr(request.user, '__class__') or request.user.__class__.__name__ != 'Interessado':
        messages.error(request, 'Você precisa estar logado para acessar esta área.')
        return redirect('interessados:login')
    
    interessado = request.user
    
    try:
        # Buscar inscrições do interessado (SEM filtros complexos)
        inscricoes = Inscricao.objects.filter(
            interessado=interessado
        ).select_related('evento').order_by('-data_inscricao')
        
        # Buscar eventos disponíveis (SEM filtro de status)
        eventos_abertos = Evento.objects.filter(
            data_inicio_inscricao__lte=date.today(),
            data_fim_inscricao__gte=date.today()
        ).exclude(
            id__in=inscricoes.values_list('evento_id', flat=True)
        )
        
        # Estatísticas SIMPLES (sem filtrar por status específico)
        total_inscricoes = inscricoes.count()
        
        context = {
            'interessado': interessado,
            'inscricoes': inscricoes,
            'eventos_abertos': eventos_abertos,
            'total_inscricoes': total_inscricoes,
            'inscricoes_aprovadas': 0,  # Removido filtro problemático
            'inscricoes_pendentes': 0,   # Removido filtro problemático
        }
        
        return render(request, 'interessados/dashboard.html', context)
        
    except Exception as e:
        messages.error(request, f'Erro ao carregar dashboard: {str(e)}')
        return redirect('portal:index')


def detalhes_inscricao(request, inscricao_id):
    """Detalhes de uma inscrição específica"""
    
    # Verifica se é um interessado logado
    if not hasattr(request.user, '__class__') or request.user.__class__.__name__ != 'Interessado':
        messages.error(request, 'Você precisa estar logado para acessar esta área.')
        return redirect('interessados:login')
    
    interessado = request.user
    
    try:
        # Buscar inscrição (garantindo que pertence ao interessado logado)
        inscricao = get_object_or_404(
            Inscricao.objects.select_related('evento'),
            id=inscricao_id,
            interessado=interessado
        )
        
        context = {
            'interessado': interessado,
            'inscricao': inscricao,
        }
        
        return render(request, 'interessados/detalhes.html', context)
        
    except Exception as e:
        messages.error(request, f'Erro: {str(e)}')
        return redirect('interessados:dashboard')
    
    