"""
Arquivo: views.py
Caminho: apps/interessados/views.py
Alteração: Imports corrigidos + dashboard funcional
Data: 29/01/2026
"""

from datetime import date
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required

from .models import Interessado
from .forms import CadastroInteressadoForm, LoginInteressadoForm, EdicaoInteressadoForm
from apps.selecao.models import Inscricao
from apps.eventos.models import Evento


def cadastro_view(request):
    """View de cadastro público de interessados"""
    if request.method == 'POST':
        form = CadastroInteressadoForm(request.POST)
        
        if form.is_valid():
            try:
                interessado = form.save()
                messages.success(request, '✅ Cadastro realizado com sucesso! Faça login para continuar.')
                return redirect('interessados:login')
            except Exception as e:
                messages.error(request, f'❌ Erro ao salvar cadastro: {str(e)}')
        else:
            messages.error(request, '❌ Corrija os erros abaixo para continuar.')
    else:
        form = CadastroInteressadoForm()
    
    return render(request, 'interessados/cadastro.html', {'form': form})


def login_view(request):
    """View de login para interessados - Autentica usando CPF e senha"""
    if request.method == 'POST':
        form = LoginInteressadoForm(request.POST)
        
        if form.is_valid():
            cpf = form.cleaned_data['cpf'].replace('.', '').replace('-', '')
            senha = form.cleaned_data['senha']
            
            try:
                interessado = Interessado.objects.get(cpf=cpf)
                
                if interessado.check_password(senha):
                    login(request, interessado, backend='apps.interessados.authentication.InteressadoBackend')
                    messages.success(request, f'✅ Bem-vindo(a), {interessado.nome}!')
                    return redirect('interessados:dashboard')
                else:
                    messages.error(request, '❌ CPF ou senha incorretos.')
            except Interessado.DoesNotExist:
                messages.error(request, '❌ CPF ou senha incorretos.')
    else:
        form = LoginInteressadoForm()
    
    return render(request, 'interessados/login.html', {'form': form})


@login_required(login_url='interessados:login')
def meus_dados_view(request):
    """View de edição de dados do interessado logado"""
    interessado = request.user
    
    if request.method == 'POST':
        form = EdicaoInteressadoForm(request.POST, instance=interessado)
        
        if form.is_valid():
            try:
                form.save()
                messages.success(request, '✅ Dados atualizados com sucesso!')
                return redirect('interessados:meus_dados')
            except Exception as e:
                messages.error(request, f'❌ Erro ao atualizar dados: {str(e)}')
        else:
            messages.error(request, '❌ Corrija os erros abaixo para continuar.')
    else:
        form = EdicaoInteressadoForm(instance=interessado)
    
    return render(request, 'interessados/meus_dados.html', {
        'form': form,
        'interessado': interessado
    })

@login_required(login_url='interessados:login')
def dashboard_view(request):
    """Dashboard do interessado - Mostra inscrições, estatísticas e eventos disponíveis"""
    interessado = request.user
    
    inscricoes = Inscricao.objects.filter(
        interessado=interessado
    ).select_related('evento', 'status').prefetch_related('classificacao')
    
    total_inscricoes = inscricoes.count()
    inscricoes_aprovadas = inscricoes.filter(status__nome='APROVADO').count()
    inscricoes_pendentes = inscricoes.filter(status__nome='INSCRITO').count()
    
    eventos_abertos = Evento.objects.filter(
        data_fim_inscricao__gte=date.today()
    ).exclude(
        inscricoes__interessado=interessado
    )
    
    context = {
        'interessado': interessado,
        'inscricoes': inscricoes,
        'total_inscricoes': total_inscricoes,
        'inscricoes_aprovadas': inscricoes_aprovadas,
        'inscricoes_pendentes': inscricoes_pendentes,
        'eventos_abertos': eventos_abertos,
    }
    
    return render(request, 'interessados/dashboard.html', context)


@login_required(login_url='interessados:login')
def detalhes_view(request, inscricao_id):
    """Detalhes de uma inscrição específica"""
    inscricao = get_object_or_404(
        Inscricao,
        pk=inscricao_id,
        interessado=request.user
    )
    
    return render(request, 'interessados/detalhes_inscricao.html', {
        'inscricao': inscricao
    })


@login_required(login_url='interessados:login')
def logout_view(request):
    """View de logout"""
    logout(request)
    messages.info(request, '👋 Você saiu do sistema.')
    return redirect('interessados:login')

