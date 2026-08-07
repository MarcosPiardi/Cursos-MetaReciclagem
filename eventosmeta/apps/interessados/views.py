"""
Arquivo: views.py
Caminho: apps/interessados/views.py
Atualizações:
 - 29/01/2026 - Imports corrigidos + dashboard funcional
 - 30/01/2026 - Corrigido login para exibir erros no formulário, não em messages
                Corrigido comparação de datas (datetime vs date)
                Corrigido relacionamento inscricoes (plural) no dashboard
                Código completo baseado nos models reais - SEM ERROS
 - 13/02/2026 - Adicionada verificação de is_active em todas as views protegidas
 - 20/02/2026 - Adicionadas views de recuperação de senha por CPF + e-mail
                Token de recuperação migrado de sessão para banco de dados
 - 24/02/2026 - Dashboard_view — prefetch_related de matriculas e status da matricula
 - 25/02/2026 - Adicionada view trocar_senha_obrigatorio_view (Fluxo B)
 - 12/03/2026 - Rate limiting via middleware axes
 - 17/03/2026 - Senha_recuperar_view migrada para busca por cpf_hash (CPF criptografado no banco)
 - 29/05/2026 - CORRECOES:
                1. inscrever_evento_view: select_for_update + get_or_create (race condition)
                2. senha_recuperar_view: try/except no send_mail (evita 500 se SMTP falhar)
                3. senha_redefinir_view: mensagem diferente para token expirado vs ja usado
                4. detalhes_view: fallback se template portal/detalhes_evento.html nao existir
"""

import secrets
from datetime import date, timedelta, datetime
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.utils import timezone
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail, BadHeaderError
from django.template.loader import render_to_string, TemplateDoesNotExist
from django.conf import settings
from django.template import TemplateDoesNotExist
from django.db import transaction
from django.urls import reverse

from .models import Interessado, PasswordResetToken, gerar_hash_cpf
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
                    'Cadastro realizado com sucesso! Faça login para continuar.'
                )
                return redirect('interessados:login')
            except Exception as e:
                messages.error(request, f'Erro ao salvar cadastro: {str(e)}')
        else:
            messages.error(request, 'Corrija os erros abaixo para continuar.')
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
    PROTEGIDO: Rate limiting via middleware axes (máximo 5 tentativas, bloqueio 30 min)
    """
    if request.method == 'POST':
        form = LoginInteressadoForm(request.POST)

        if form.is_valid():
            interessado = form.interessado

            if not interessado.is_active:
                messages.error(
                    request,
                    'Sua conta está inativa. Entre em contato com a administração.'
                )
                return render(request, 'interessados/login.html', {'form': form})

            interessado.last_login = timezone.now()
            interessado.save(update_fields=['last_login'])

            login(
                request,
                interessado,
                backend='apps.interessados.authentication.InteressadoBackend'
            )
            return redirect('interessados:dashboard')

    else:
        form = LoginInteressadoForm()

    return render(request, 'interessados/login.html', {'form': form})


@login_required(login_url='interessados:login')
def logout_view(request):
    """View de logout"""
    logout(request)
    messages.info(request, 'Você saiu do sistema.')
    return redirect('interessados:login')


# ==========================================
# DASHBOARD
# ==========================================

@login_required(login_url='interessados:login')
def dashboard_view(request):
    """
    Dashboard do interessado
    ADICIONADO: Verificação de is_active (13/02/2026)
    ADICIONADO: prefetch_related de matriculas (24/02/2026)
    """
    interessado = request.user

    if not interessado.is_active:
        logout(request)
        messages.error(request, 'Sua conta foi desativada.')
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
        messages.error(request, 'Sua conta foi desativada.')
        return redirect('interessados:login')

    if request.method == 'POST':
        form = EdicaoInteressadoForm(request.POST, instance=interessado)

        if form.is_valid():
            try:
                form.save()
                messages.success(request, 'Dados atualizados com sucesso!')
                return redirect('interessados:meus_dados')
            except Exception as e:
                messages.error(request, f'Erro ao atualizar dados: {str(e)}')
        else:
            messages.error(request, 'Corrija os erros abaixo para continuar.')
    else:
        form = EdicaoInteressadoForm(instance=interessado)

    return render(request, 'interessados/meus_dados.html', {
        'form'       : form,
        'interessado': interessado,
    })


# ==========================================
# DETALHES DE INSCRICAO
# ==========================================

@login_required(login_url='interessados:login')
def detalhes_view(request, inscricao_id):
    """
    Detalhes de uma inscricao especifica
    CORRIGIDO (29/05/2026): fallback se template portal/detalhes_evento.html nao existir
    """
    if not request.user.is_active:
        logout(request)
        messages.error(request, 'Sua conta foi desativada.')
        return redirect('interessados:login')

    inscricao = get_object_or_404(
        Inscricao.objects.select_related('evento', 'status', 'classificacao'),
        pk=inscricao_id,
        interessado=request.user
    )

    # Tenta template do portal, fallback para template proprio
    template_name = 'portal/detalhes_evento.html'
    try:
        render_to_string(template_name, {'inscricao': inscricao}, request=request)
    except TemplateDoesNotExist:
        template_name = 'interessados/detalhes_inscricao.html'

    return render(request, template_name, {
        'inscricao': inscricao,
    })


# ==========================================
# INSCREVER EM EVENTO
# ==========================================

@login_required(login_url='interessados:login')
def inscrever_evento_view(request, evento_id):
    """
    Inscreve o interessado logado em um evento
    CORRIGIDO (29/05/2026): select_for_update + get_or_create para evitar duplicatas
                            em caso de requests simultaneos
    """
    interessado = request.user

    if not interessado.is_active:
        logout(request)
        messages.error(request, 'Sua conta foi desativada.')
        return redirect('interessados:login')

    try:
        evento = Evento.objects.get(id=evento_id)
    except Evento.DoesNotExist:
        messages.error(request, 'Evento nao encontrado.')
        return redirect('interessados:dashboard')

    agora = timezone.now()

    if not (evento.data_inicio_inscricao <= agora <= evento.data_fim_inscricao):
        messages.error(
            request,
            f'O periodo de inscricoes para "{evento.nome}" esta encerrado.'
        )
        return redirect('interessados:dashboard')

    try:
        status_pendente = StatusInscricao.objects.get(nome='Pendente')
    except StatusInscricao.DoesNotExist:
        messages.error(
            request,
            'Status PENDENTE nao encontrado. Contate o administrador.'
        )
        return redirect('interessados:dashboard')

    # Bloqueia a linha do evento para evitar duplicatas em requests concorrentes
    with transaction.atomic():
        Evento.objects.select_for_update().get(id=evento_id)

        inscricao, created = Inscricao.objects.get_or_create(
            interessado=interessado,
            evento=evento,
            defaults={
                'status': status_pendente,
                'data_inscricao': timezone.now(),
            }
        )

        if not created:
            messages.warning(
                request,
                f'Voce ja esta inscrito no evento "{evento.nome}".'
            )
            return redirect('interessados:dashboard')

    messages.success(
        request,
        f'Inscricao realizada com sucesso no evento "{evento.nome}"! '
        f'Sua inscricao esta com status PENDENTE e sera analisada pela equipe.'
    )

    return redirect('interessados:dashboard')


# ==========================================
# RECUPERACAO DE SENHA — INTERESSADOS
# Alteracao: 20/02/2026 — Token salvo no BANCO DE DADOS
# Alteracao: 12/03/2026 — Rate limiting via middleware
# Alteracao: 17/03/2026 — Busca por cpf_hash (CPF criptografado no banco)
# Alteracao: 29/05/2026 — try/except no send_mail (evita 500 se SMTP falhar)
# Alteracao: 07/08/2026 — Corrigido link de recuperacao: URL hardcoded
#                          trocada por reverse() para incluir prefixo eventosmeta/
# ==========================================

def senha_recuperar_view(request):
    """
    Passo 1: Interessado informa o CPF.
    - Com e-mail cadastrado → envia link de recuperacao (valido 30 min)
    - Sem e-mail cadastrado → redireciona para pagina de orientacao
    - CPF nao encontrado   → exibe erro no formulario
    CORRIGIDO (29/05/2026): send_mail com try/except — mensagem amigavel em vez de 500
    CORRIGIDO (07/08/2026): Link gerado via reverse() em vez de URL hardcoded
    """
    erro      = None
    cpf_value = ''

    if request.method == 'POST':
        cpf_raw   = request.POST.get('cpf', '').strip()
        cpf       = ''.join(filter(str.isdigit, cpf_raw))
        cpf_value = cpf_raw

        try:
            interessado = Interessado.objects.get(
                cpf_hash=gerar_hash_cpf(cpf),
                is_active=True
            )

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

                # 07/08/2026 - CORRECAO: Usar reverse() em vez de URL hardcoded
                # Antes:  f'/inscricao/senha/redefinir/{token}/'
                # Depois: reverse() resolve automaticamente o prefixo eventosmeta/
                link = request.build_absolute_uri(
                    reverse('interessados:senha_redefinir', kwargs={'token': token})
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

                try:
                    send_mail(
                        subject        = 'MetaReciclagem — Recuperacao de Senha',
                        message        = corpo_txt,
                        html_message   = corpo_html,
                        from_email     = settings.DEFAULT_FROM_EMAIL,
                        recipient_list = [interessado.email],
                        fail_silently  = False,
                    )
                except (ConnectionRefusedError, TimeoutError, BadHeaderError, OSError) as e:
                    erro = (
                        'Nao foi possivel enviar o e-mail de recuperacao. '
                        'Tente novamente mais tarde ou entre em contato com a administracao.'
                    )
                    return render(request, 'interessados/senha/recuperar.html', {
                        'erro'     : erro,
                        'cpf_value': cpf_value,
                    })

                return redirect('interessados:senha_recuperar_enviado')

            else:
                return redirect('interessados:senha_sem_email')

        except Interessado.DoesNotExist:
            erro = 'CPF nao encontrado ou conta inativa no sistema.'

    return render(request, 'interessados/senha/recuperar.html', {
        'erro'     : erro,
        'cpf_value': cpf_value,
    })


def senha_recuperar_enviado_view(request):
    """Passo 2: Confirmacao de envio."""
    return render(request, 'interessados/senha/recuperar_enviado.html')


def senha_redefinir_view(request, token):
    """
    Passo 3: Formulario de nova senha.
    CORRIGIDO (29/05/2026): mensagem diferente para token expirado vs ja usado
    """
    reset_token = None
    try:
        reset_token = PasswordResetToken.objects.select_related('interessado').get(
            token=token,
            usado=False,
            expira_em__gt=timezone.now()
        )
        interessado = reset_token.interessado

    except PasswordResetToken.DoesNotExist:
        # Verifica se o token existe mas esta expirado ou ja foi usado
        token_existente = PasswordResetToken.objects.filter(token=token).first()
        if token_existente and token_existente.usado:
            return render(request, 'interessados/senha/token_invalido.html', {
                'senha_ja_trocada': True,
                'token_expirado': False,
            })
        else:
            return render(request, 'interessados/senha/token_invalido.html', {
                'senha_ja_trocada': False,
                'token_expirado': True,
            })

    erro = None

    if request.method == 'POST':
        nova_senha      = request.POST.get('nova_senha', '')
        confirmar_senha = request.POST.get('confirmar_senha', '')

        if len(nova_senha) < 8:
            erro = 'A senha deve ter no minimo 8 caracteres.'
        elif nova_senha != confirmar_senha:
            erro = 'As senhas nao coincidem.'
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
# FLUXO B — TROCA OBRIGATORIA DE SENHA — INTERESSADOS
# Adicionado: 25/02/2026
# ==============================================================================

@login_required(login_url='interessados:login')
def trocar_senha_obrigatorio_view(request):
    """
    View de troca obrigatoria de senha para Interessados.
    Exibida pelo middleware quando must_change_password = True.
    """
    interessado = request.user

    if not interessado.must_change_password:
        return redirect('interessados:dashboard')

    erro = None

    if request.method == 'POST':
        nova_senha      = request.POST.get('nova_senha', '').strip()
        confirmar_senha = request.POST.get('confirmar_senha', '').strip()

        if len(nova_senha) < 8:
            erro = 'A nova senha deve ter no minimo 8 caracteres.'
        elif nova_senha != confirmar_senha:
            erro = 'As senhas nao coincidem. Tente novamente.'
        else:
            interessado.set_password(nova_senha)
            interessado.must_change_password = False
            interessado.save()
            login(request, interessado, backend='apps.interessados.authentication.InteressadoBackend')
            messages.success(request, 'Senha alterada com sucesso! Bem-vindo ao sistema.')
            return redirect('interessados:dashboard')

    return render(request, 'interessados/senha/int_trocar_obrigatorio.html', {
        'erro'       : erro,
        'interessado': interessado,
    })



