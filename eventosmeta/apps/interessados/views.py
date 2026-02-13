"""
Arquivo: views.py
Caminho: apps/interessados/views.py

Alteração: Imports corrigidos + dashboard funcional
Data: 29/01/2026

Alteração: Corrigido login para exibir erros no formulário, não em messages

Alteração: Corrigido comparação de datas (datetime vs date)

Alteração: Corrigido relacionamento inscricoes (plural) no dashboard
Data: 30/01/2026

Alteração: Código completo baseado nos models reais - SEM ERROS
Data: 30/01/2026

Alteração: Adicionada verificação de is_active em todas as views protegidas
Data: 13/02/2026
"""

from datetime import date
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.utils import timezone
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required

from .models import Interessado
from .forms import CadastroInteressadoForm, LoginInteressadoForm, EdicaoInteressadoForm
from apps.selecao.models import Inscricao, Classificacao, StatusInscricao
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
    """
    View de login para interessados - Autentica usando CPF e senha
    CORRIGIDO: Erros são exibidos no formulário, não em messages
    ADICIONADO: Verificação extra de is_active e atualização de last_login (13/02/2026)
    """
    if request.method == 'POST':
        form = LoginInteressadoForm(request.POST)
        
        if form.is_valid():
            # Se chegou aqui, o formulário validou CPF, senha e is_active
            interessado = form.interessado
            
            # ============================================================
            # VALIDAÇÃO EXTRA: VERIFICAR SE ESTÁ ATIVO (CAMADA 3)
            # Data: 13/02/2026
            # ============================================================
            if not interessado.is_active:
                messages.error(
                    request,
                    '🔒 Sua conta está inativa. Entre em contato com a administração.'
                )
                return render(request, 'interessados/login.html', {'form': form})
            
            # Atualizar last_login
            interessado.last_login = timezone.now()
            interessado.save(update_fields=['last_login'])
            
            # Fazer login
            login(request, interessado, backend='apps.interessados.authentication.InteressadoBackend')
            
            # Redireciona direto pro dashboard
            return redirect('interessados:dashboard')
        
        # Se form.is_valid() retornou False, os erros já estão em form.errors
        
    else:
        form = LoginInteressadoForm()
    
    return render(request, 'interessados/login.html', {'form': form})


@login_required(login_url='interessados:login')
def meus_dados_view(request):
    """
    View de edição de dados do interessado logado
    ADICIONADO: Verificação de is_active (13/02/2026)
    """
    interessado = request.user
    
    # ============================================================
    # VALIDAÇÃO: VERIFICAR SE AINDA ESTÁ ATIVO
    # Data: 13/02/2026
    # ============================================================
    if not interessado.is_active:
        logout(request)
        messages.error(request, '🔒 Sua conta foi desativada.')
        return redirect('interessados:login')
    
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
    """
    Dashboard do interessado - Mostra inscrições, estatísticas e eventos disponíveis
    ADICIONADO: Verificação de is_active (13/02/2026)
    """
    interessado = request.user
    
    # ============================================================
    # VALIDAÇÃO: VERIFICAR SE AINDA ESTÁ ATIVO
    # Data: 13/02/2026
    # ============================================================
    if not interessado.is_active:
        logout(request)
        messages.error(request, '🔒 Sua conta foi desativada.')
        return redirect('interessados:login')
    
    # Inscrições do interessado
    inscricoes = Inscricao.objects.filter(
        interessado=interessado
    ).select_related('evento', 'status')
    
    # Classificações do interessado
    classificacoes = Classificacao.objects.filter(
        inscricao__interessado=interessado
    ).select_related('inscricao__evento').order_by('-processado_em')
    
    # Estatísticas
    total_inscricoes = inscricoes.count()
    total_classificacoes = classificacoes.count()
    inscricoes_aprovadas = inscricoes.filter(status__nome='APROVADO').count()
    inscricoes_pendentes = inscricoes.filter(status__nome='INSCRITO').count()
    
    # Eventos disponíveis (que ainda aceitam inscrições e o interessado NÃO está inscrito)
    eventos_abertos = Evento.objects.filter(
        data_fim_inscricao__date__gte=date.today()
    ).exclude(
        inscricoes__interessado=interessado
    ).distinct()
    
    context = {
        'interessado': interessado,
        'inscricoes': inscricoes,
        'classificacoes': classificacoes,
        'total_inscricoes': total_inscricoes,
        'total_classificacoes': total_classificacoes,
        'inscricoes_aprovadas': inscricoes_aprovadas,
        'inscricoes_pendentes': inscricoes_pendentes,
        'eventos_abertos': eventos_abertos,
    }
    
    return render(request, 'interessados/dashboard.html', context)


@login_required(login_url='interessados:login')
def detalhes_view(request, inscricao_id):
    """
    Detalhes de uma inscrição específica
    ADICIONADO: Verificação de is_active (13/02/2026)
    """
    # ============================================================
    # VALIDAÇÃO: VERIFICAR SE AINDA ESTÁ ATIVO
    # Data: 13/02/2026
    # ============================================================
    if not request.user.is_active:
        logout(request)
        messages.error(request, '🔒 Sua conta foi desativada.')
        return redirect('interessados:login')
    
    inscricao = get_object_or_404(
        Inscricao.objects.select_related('evento', 'status', 'classificacao'),
        pk=inscricao_id,
        interessado=request.user
    )
    
    return render(request, 'portal/detalhes_evento.html', {
        'inscricao': inscricao
    })


@login_required(login_url='interessados:login')
def logout_view(request):
    """View de logout"""
    logout(request)
    messages.info(request, '👋 Você saiu do sistema.')
    return redirect('interessados:login')


@login_required(login_url='interessados:login')
def inscrever_evento_view(request, evento_id):
    """
    Inscreve o interessado logado em um evento
    Cria inscrição com status PENDENTE automaticamente
    ADICIONADO: Verificação de is_active (13/02/2026)
    """
    interessado = request.user
    
    # ============================================================
    # VALIDAÇÃO: VERIFICAR SE AINDA ESTÁ ATIVO
    # Data: 13/02/2026
    # ============================================================
    if not interessado.is_active:
        logout(request)
        messages.error(request, '🔒 Sua conta foi desativada.')
        return redirect('interessados:login')
    
    try:
        evento = Evento.objects.get(id=evento_id)
    except Evento.DoesNotExist:
        messages.error(request, '❌ Evento não encontrado.')
        return redirect('interessados:dashboard')
    
    # Verificar se já existe inscrição
    inscricao_existente = Inscricao.objects.filter(
        interessado=interessado,
        evento=evento
    ).first()
    
    if inscricao_existente:
        messages.warning(request, f'⚠️ Você já está inscrito no evento "{evento.nome}".')
        return redirect('interessados:dashboard')
    
    # Verificar se o período de inscrições está aberto
    agora = timezone.now()
    
    if not (evento.data_inicio_inscricao <= agora <= evento.data_fim_inscricao):
        messages.error(request, f'❌ O período de inscrições para "{evento.nome}" está encerrado.')
        return redirect('interessados:dashboard')
    
    # Buscar status PENDENTE
    try:
        status_pendente = StatusInscricao.objects.get(nome='Pendente')
    except StatusInscricao.DoesNotExist:
        messages.error(request, '❌ Status PENDENTE não encontrado no sistema. Contate o administrador.')
        return redirect('interessados:dashboard')
    
    # Criar inscrição
    try:
        inscricao = Inscricao.objects.create(
            interessado=interessado,
            evento=evento,
            status=status_pendente,
            data_inscricao=timezone.now()
        )
        
        messages.success(
            request, 
            f'✅ Inscrição realizada com sucesso no evento "{evento.nome}"! '
            f'Sua inscrição está com status PENDENTE e será analisada pela equipe.'
        )
        
    except Exception as e:
        messages.error(request, f'❌ Erro ao criar inscrição: {str(e)}')
    
    return redirect('interessados:dashboard')

