"""
Arquivo: views_exclusao.py
Caminho: apps/accounts/views_exclusao.py
Finalidade: Views do staff para listar, aprovar e recusar
            solicitações de exclusão de dados (LGPD)
Data: 18/03/2026
"""

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils import timezone

from apps.interessados.models import SolicitacaoExclusao, Interessado


def _apenas_staff(request):
    """Retorna True se o usuário é staff autenticado."""
    return request.user.is_authenticated and request.user.is_staff


@login_required(login_url='/staff/login/')
def listar_solicitacoes_view(request):
    """Lista todas as solicitações de exclusão, agrupadas por status."""
    if not _apenas_staff(request):
        messages.error(request, 'Acesso restrito à equipe.')
        return redirect('/staff/login/')

    pendentes  = SolicitacaoExclusao.objects.filter(status='PENDENTE').order_by('-solicitado_em')
    aprovadas  = SolicitacaoExclusao.objects.filter(status='APROVADA').order_by('-analisado_em')
    recusadas  = SolicitacaoExclusao.objects.filter(status='RECUSADA').order_by('-analisado_em')

    return render(request, 'accounts/exclusao/listar.html', {
        'pendentes': pendentes,
        'aprovadas': aprovadas,
        'recusadas': recusadas,
    })


@login_required(login_url='/staff/login/')
def detalhe_solicitacao_view(request, solicitacao_id):
    """Exibe detalhes de uma solicitação e permite aprovar ou recusar."""
    if not _apenas_staff(request):
        messages.error(request, 'Acesso restrito à equipe.')
        return redirect('/staff/login/')

    solicitacao = get_object_or_404(SolicitacaoExclusao, id=solicitacao_id)

    if request.method == 'POST':
        acao    = request.POST.get('acao', '')
        parecer = request.POST.get('parecer', '').strip()

        if acao not in ('aprovar', 'recusar'):
            messages.error(request, 'Ação inválida.')
            return redirect('accounts:detalhe_solicitacao_exclusao', solicitacao_id=solicitacao_id)

        if not parecer:
            messages.error(request, 'O parecer é obrigatório.')
            return redirect('accounts:detalhe_solicitacao_exclusao', solicitacao_id=solicitacao_id)

        solicitacao.parecer_staff = parecer
        solicitacao.analisado_em  = timezone.now()
        solicitacao.analisado_por = request.user

        if acao == 'aprovar':
            solicitacao.status = 'APROVADA'
            solicitacao.save()

            # Anonimiza os dados do interessado
            interessado = solicitacao.interessado
            if interessado:
                _anonimizar_interessado(interessado)

            messages.success(request, f'Solicitação aprovada. Dados de {solicitacao.nome_solicitante} foram anonimizados.')

        elif acao == 'recusar':
            solicitacao.status = 'RECUSADA'
            solicitacao.save()
            messages.info(request, f'Solicitação de {solicitacao.nome_solicitante} recusada.')

        return redirect('accounts:listar_solicitacoes_exclusao')

    return render(request, 'accounts/exclusao/detalhe.html', {
        'solicitacao': solicitacao,
    })


def _anonimizar_interessado(interessado):
    """
    Anonimiza os dados pessoais do interessado aprovado para exclusão.
    Mantém o registro no banco para integridade das inscrições,
    mas remove todos os dados identificáveis.
    """
    from apps.interessados.models import gerar_hash_cpf
    import uuid

    token = str(uuid.uuid4().hex)[:8]

    interessado.nome              = f'Usuário Removido {token}'
    interessado.cpf               = '00000000000'
    interessado.cpf_hash          = gerar_hash_cpf(f'removido_{token}')
    interessado.rg                = ''
    interessado.data_nascimento   = None
    interessado.cidade_nascimento = ''
    interessado.uf_nascimento     = ''
    interessado.nacionalidade     = ''
    interessado.endereco_residencial = ''
    interessado.num_endereco      = ''
    interessado.bairro            = ''
    interessado.complemento       = ''
    interessado.cep               = ''
    interessado.cidade_residencia = ''
    interessado.uf_residencia     = ''
    interessado.telefone          = ''
    interessado.celular           = ''
    interessado.email             = None
    interessado.num_nis           = ''
    interessado.nome_responsavel  = ''
    interessado.telefone_responsavel = ''
    interessado.celular_responsavel  = ''
    interessado.email_responsavel    = ''
    interessado.observacao           = ''
    interessado.is_active            = False

    interessado.save()



