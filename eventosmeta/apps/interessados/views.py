"""
Arquivo: views.py
Caminho: apps/interessados/views.py

Alteração: Imports corrigidos + dashboard funcional
Data: 29/01/2026

Alteração: Corrigido login para exibir erros no formulário, não em messages
Alteração: Corrigido comparação de datas (datetime vs date)
Alteração: Corrigido relacionamento inscricoes (plural) no dashboard
Alteração: Código completo baseado nos models reais - SEM ERROS
Data: 30/01/2026

Alteração: Adicionada verificação de is_active em todas as views protegidas
Data: 13/02/2026

Alteração: Adicionadas views de recuperação de senha por CPF + e-mail
Alteração: Token de recuperação migrado de sessão para banco de dados
           Corrigido problema de "link expirado" ao abrir em nova aba/janela
           Adicionada mensagem de sucesso antes do redirect em senha_redefinir_view
           Token inválido após uso é comportamento correto de segurança
Data: 20/02/2026

Alteração: dashboard_view — prefetch_related de matriculas e status da matricula
           para exibir status de matrícula nos cards do dashboard sem N queries
Data: 24/02/2026

Alteração: Adicionada view trocar_senha_obrigatorio_view (Fluxo B)
           Intercepta login de Interessado com must_change_password = True
           e força troca de senha antes de qualquer outra ação
Data: 25/02/2026
"""

import secrets
from datetime import date, timedelta, datetime
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.utils import timezone
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings

from .models import Interessado, PasswordResetToken
from .forms import CadastroInteressadoForm, LoginInteressadoForm, EdicaoInteressadoForm
from apps.selecao.models import Inscricao, Classificacao, StatusInscricao
from apps.eventos.models import Evento


# ==========================================
# CADASTRO
# ==========================================

def cadastro_view(request):
    """View de cadastro público de interessados"""
    if request.method == 'POST':
        form = CadastroInteressadoForm(request.POST)

        if form.is_valid():
            try:
                form.save()
                messages.success(
                    request,
                    '✅ Cadastro realizado com sucesso! Faça login para continuar.'
                )
                return redirect('interessados:login')
            except Exception as e:
                messages.error(request, f'❌ Erro ao salvar cadastro: {str(e)}')
        else:
            messages.error(request, '❌ Corrija os erros abaixo para continuar.')
    else:
        form = CadastroInteressadoForm()

    return render(request, 'interessados/cadastro.html', {'form': form})


# ==========================================
# LOGIN / LOGOUT
# ==========================================

def login_view(request):
    """
    View de login para interessados - Autentica usando CPF e senha
    CORRIGIDO: Erros são exibidos no formulário, não em messages
    ADICIONADO: Verificação extra de is_active e atualização de last_login (13/02/2026)
    """
    if request.method == 'POST':
        form = LoginInteressadoForm(request.POST)

        if form.is_valid():
            interessado = form.interessado

            if not interessado.is_active:
                messages.error(
                    request,
                    '🔒 Sua conta está inativa. Entre em contato com a administração.'
                )
                return render(request, 'interessados/login.html', {'form': form})

            interessado.last_login = timezone.now()
            interessado.save(update_fields=['last_login'])

            login(
                request,
                interessado,
                backend='apps.interessados.authentication.InteressadoBackend'
            )
            # Middleware intercepta e redireciona se must_change_password = True
            return redirect('interessados:dashboard')

    else:
        form = LoginInteressadoForm()

    return render(request, 'interessados/login.html', {'form': form})


@login_required(login_url='interessados:login')
def logout_view(request):
    """View de logout"""
    logout(request)
    messages.info(request, '👋 Você saiu do sistema.')
    return redirect('interessados:login')


# ==========================================
# DASHBOARD
# ==========================================

@login_required(login_url='interessados:login')
def dashboard_view(request):
    """
    Dashboard do interessado
    ADICIONADO: Verificação de is_active (13/02/2026)
    ADICIONADO: prefetch_related de matriculas para exibir status
                de matrícula nos cards sem gerar N queries (24/02/2026)
    """
    interessado = request.user

    if not interessado.is_active:
        logout(request)
        messages.error(request, '🔒 Sua conta foi desativada.')
        return redirect('interessados:login')

    inscricoes = Inscricao.objects.filter(
        interessado=interessado
    ).select_related(
        'evento',
        'evento__status',
        'status',
    ).prefetch_related(
        'matriculas',
        'matriculas__status',
    ).order_by('-data_inscricao')

    classificacoes = Classificacao.objects.filter(
        inscricao__interessado=interessado
    ).select_related(
        'inscricao__evento',
        'inscricao__evento__status',
    ).prefetch_related(
        'inscricao__matriculas',
        'inscricao__matriculas__status',
    ).order_by('-processado_em')

    total_inscricoes     = inscricoes.count()
    total_classificacoes = classificacoes.count()
    inscricoes_aprovadas = inscricoes.filter(status__nome='APROVADO').count()
    inscricoes_pendentes = inscricoes.filter(status__nome='INSCRITO').count()

    eventos_abertos = Evento.objects.filter(
        data_fim_inscricao__date__gte=date.today()
    ).select_related(
        'status'
    ).exclude(
        inscricoes__interessado=interessado
    ).distinct()

    context = {
        'interessado'         : interessado,
        'inscricoes'          : inscricoes,
        'classificacoes'      : classificacoes,
        'total_inscricoes'    : total_inscricoes,
        'total_classificacoes': total_classificacoes,
        'inscricoes_aprovadas': inscricoes_aprovadas,
        'inscricoes_pendentes': inscricoes_pendentes,
        'eventos_abertos'     : eventos_abertos,
    }

    return render(request, 'interessados/dashboard.html', context)


# ==========================================
# MEUS DADOS
# ==========================================

@login_required(login_url='interessados:login')
def meus_dados_view(request):
    """
    View de edição de dados do interessado logado
    ADICIONADO: Verificação de is_active (13/02/2026)
    """
    interessado = request.user

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
        'form'       : form,
        'interessado': interessado,
    })


# ==========================================
# DETALHES DE INSCRIÇÃO
# ==========================================

@login_required(login_url='interessados:login')
def detalhes_view(request, inscricao_id):
    """
    Detalhes de uma inscrição específica
    ADICIONADO: Verificação de is_active (13/02/2026)
    """
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
        'inscricao': inscricao,
    })


# ==========================================
# INSCREVER EM EVENTO
# ==========================================

@login_required(login_url='interessados:login')
def inscrever_evento_view(request, evento_id):
    """
    Inscreve o interessado logado em um evento
    ADICIONADO: Verificação de is_active (13/02/2026)
    """
    interessado = request.user

    if not interessado.is_active:
        logout(request)
        messages.error(request, '🔒 Sua conta foi desativada.')
        return redirect('interessados:login')

    try:
        evento = Evento.objects.get(id=evento_id)
    except Evento.DoesNotExist:
        messages.error(request, '❌ Evento não encontrado.')
        return redirect('interessados:dashboard')

    inscricao_existente = Inscricao.objects.filter(
        interessado=interessado,
        evento=evento
    ).first()

    if inscricao_existente:
        messages.warning(
            request,
            f'⚠️ Você já está inscrito no evento "{evento.nome}".'
        )
        return redirect('interessados:dashboard')

    agora = timezone.now()

    if not (evento.data_inicio_inscricao <= agora <= evento.data_fim_inscricao):
        messages.error(
            request,
            f'❌ O período de inscrições para "{evento.nome}" está encerrado.'
        )
        return redirect('interessados:dashboard')

    try:
        status_pendente = StatusInscricao.objects.get(nome='Pendente')
    except StatusInscricao.DoesNotExist:
        messages.error(
            request,
            '❌ Status PENDENTE não encontrado. Contate o administrador.'
        )
        return redirect('interessados:dashboard')

    try:
        Inscricao.objects.create(
            interessado  = interessado,
            evento       = evento,
            status       = status_pendente,
            data_inscricao = timezone.now()
        )
        messages.success(
            request,
            f'✅ Inscrição realizada com sucesso no evento "{evento.nome}"! '
            f'Sua inscrição está com status PENDENTE e será analisada pela equipe.'
        )
    except Exception as e:
        messages.error(request, f'❌ Erro ao criar inscrição: {str(e)}')

    return redirect('interessados:dashboard')


# ==========================================
# RECUPERAÇÃO DE SENHA — INTERESSADOS
# Alteração: 20/02/2026 — Token salvo no BANCO DE DADOS
# ==========================================

def senha_recuperar_view(request):
    """
    Passo 1: Interessado informa o CPF.
    - Com e-mail cadastrado → envia link de recuperação (válido 30 min)
    - Sem e-mail cadastrado → redireciona para página de orientação
    - CPF não encontrado   → exibe erro no formulário
    """
    erro      = None
    cpf_value = ''

    if request.method == 'POST':
        cpf_raw   = request.POST.get('cpf', '').strip()
        cpf       = ''.join(filter(str.isdigit, cpf_raw))
        cpf_value = cpf_raw

        try:
            interessado = Interessado.objects.get(cpf=cpf, is_active=True)

            if interessado.email:
                PasswordResetToken.objects.filter(
                    interessado=interessado,
                    usado=False
                ).update(usado=True)

                token = secrets.token_urlsafe(32)
                PasswordResetToken.objects.create(
                    interessado=interessado,
                    token=token,
                    expira_em=timezone.now() + timedelta(minutes=30)
                )

                link = request.build_absolute_uri(
                    f'/inscricao/senha/redefinir/{token}/'
                )

                contexto_email = {
                    'interessado': interessado,
                    'link'       : link,
                    'validade'   : '30 minutos',
                }
                corpo_html = render_to_string(
                    'interessados/senha/email_recuperar.html',
                    contexto_email
                )
                corpo_txt = render_to_string(
                    'interessados/senha/email_recuperar.txt',
                    contexto_email
                )

                send_mail(
                    subject      = 'MetaReciclagem — Recuperação de Senha',
                    message      = corpo_txt,
                    html_message = corpo_html,
                    from_email   = settings.DEFAULT_FROM_EMAIL,
                    recipient_list = [interessado.email],
                    fail_silently  = False,
                )

                return redirect('interessados:senha_recuperar_enviado')

            else:
                return redirect('interessados:senha_sem_email')

        except Interessado.DoesNotExist:
            erro = 'CPF não encontrado ou conta inativa no sistema.'

    return render(request, 'interessados/senha/recuperar.html', {
        'erro'     : erro,
        'cpf_value': cpf_value,
    })


def senha_recuperar_enviado_view(request):
    """Passo 2: Confirmação de envio."""
    return render(request, 'interessados/senha/recuperar_enviado.html')


def senha_redefinir_view(request, token):
    """
    Passo 3: Formulário de nova senha.
    Token validado via banco — funciona em qualquer aba/navegador.
    """
    try:
        reset_token = PasswordResetToken.objects.select_related('interessado').get(
            token    = token,
            usado    = False,
            expira_em__gt = timezone.now()
        )
        interessado = reset_token.interessado

    except PasswordResetToken.DoesNotExist:
        return render(request, 'interessados/senha/token_invalido.html', {
            'senha_ja_trocada': True,
        })

    erro = None

    if request.method == 'POST':
        nova_senha      = request.POST.get('nova_senha', '')
        confirmar_senha = request.POST.get('confirmar_senha', '')

        if len(nova_senha) < 8:
            erro = 'A senha deve ter no mínimo 8 caracteres.'
        elif nova_senha != confirmar_senha:
            erro = 'As senhas não coincidem.'
        else:
            interessado.set_password(nova_senha)
            interessado.save()

            reset_token.usado = True
            reset_token.save()

            return redirect('interessados:senha_redefinir_concluido')

    return render(request, 'interessados/senha/redefinir.html', {'erro': erro})


def senha_redefinir_concluido_view(request):
    """Passo 4: Senha redefinida com sucesso."""
    return render(request, 'interessados/senha/redefinir_concluido.html')


def senha_sem_email_view(request):
    """Interessado sem e-mail — orienta contato presencial."""
    return render(request, 'interessados/senha/sem_email.html')


# ==============================================================================
# FLUXO B — TROCA OBRIGATÓRIA DE SENHA — INTERESSADOS
# Adicionado: 25/02/2026
# Acionado pelo middleware TrocarSenhaObrigatorioMiddleware quando
# must_change_password = True no model Interessado.
# O usuário não consegue acessar nenhuma outra página até trocar a senha.
# ==============================================================================

@login_required(login_url='interessados:login')
def trocar_senha_obrigatorio_view(request):
    """
    View de troca obrigatória de senha para Interessados.

    Exibida pelo middleware quando must_change_password = True.
    Após a troca bem-sucedida:
      - must_change_password é definido como False
      - Usuário é redirecionado para o dashboard normalmente
    """
    interessado = request.user

    # Segurança extra: se chegou aqui sem must_change_password, redireciona
    if not interessado.must_change_password:
        return redirect('interessados:dashboard')

    erro = None

    if request.method == 'POST':
        nova_senha      = request.POST.get('nova_senha', '').strip()
        confirmar_senha = request.POST.get('confirmar_senha', '').strip()

        if len(nova_senha) < 8:
            erro = 'A nova senha deve ter no mínimo 8 caracteres.'
        elif nova_senha != confirmar_senha:
            erro = 'As senhas não coincidem. Tente novamente.'
        else:
            interessado.set_password(nova_senha)
            interessado.must_change_password = False
            interessado.save()
            login(request, interessado, backend='apps.interessados.authentication.InteressadoBackend')
            messages.success(
                request,
                '✅ Senha alterada com sucesso! Bem-vindo ao sistema.'
            )
            return redirect('interessados:dashboard')

    return render(request, 'interessados/senha/int_trocar_obrigatorio.html', {
        'erro'       : erro,
        'interessado': interessado,
    })

