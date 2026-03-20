"""
Arquivo: views_exclusao.py
Caminho: apps/interessados/views_exclusao.py
Finalidade: Views de solicitação de exclusão de dados (direito ao esquecimento — LGPD)
Data: 18/03/2026
"""

from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

from .models import SolicitacaoExclusao


@login_required(login_url='interessados:login')
def solicitar_exclusao_view(request):
    """
    Tela onde o interessado solicita a exclusão dos seus dados.
    Exibe formulário com campo de motivo (opcional) e confirmação.
    """
    interessado = request.user

    if not interessado.is_active:
        logout(request)
        messages.error(request, 'Sua conta foi desativada.')
        return redirect('interessados:login')

    # Verifica se já existe solicitação pendente
    solicitacao_pendente = SolicitacaoExclusao.objects.filter(
        interessado=interessado,
        status='PENDENTE'
    ).first()

    if solicitacao_pendente:
        messages.warning(
            request,
            'Você já possui uma solicitação de exclusão pendente. '
            'Aguarde a análise da equipe.'
        )
        return redirect('interessados:dashboard')

    erro = None

    if request.method == 'POST':
        confirmacao = request.POST.get('confirmacao', '')
        motivo = request.POST.get('motivo', '').strip()

        if confirmacao != 'CONFIRMAR':
            erro = 'Digite CONFIRMAR para prosseguir com a solicitação.'
        else:
            SolicitacaoExclusao.objects.create(
                interessado      = interessado,
                nome_solicitante = interessado.nome,
                email_solicitante = interessado.email or '',
                motivo           = motivo,
                status           = 'PENDENTE',
            )

            messages.success(
                request,
                'Sua solicitação de exclusão foi registrada e será analisada pela equipe. '
                'Você receberá um retorno em breve.'
            )
            return redirect('interessados:exclusao_solicitada')

    return render(request, 'interessados/exclusao/solicitar.html', {
        'interessado': interessado,
        'erro':        erro,
    })


@login_required(login_url='interessados:login')
def exclusao_solicitada_view(request):
    """Confirmação de que a solicitação foi registrada."""
    return render(request, 'interessados/exclusao/solicitada.html')


