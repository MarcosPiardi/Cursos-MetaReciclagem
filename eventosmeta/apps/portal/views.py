"""
Views do app PORTAL - Sistema MetaReciclagem
Arquivo: apps/portal/views.py
Data: 05/12/2025
Alteração: select_related('status') em detalhes_evento + removida variável inscricoes_abertas
Data: 20/02/2026
Alteração: inscricoes_confirmadas corrigido — filtro por Q objects com iexact
           case-insensitive, sem uso de exclude()
Data: 23/02/2026
"""
from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.decorators.http import require_http_methods
from django.db.models import Q
from django.utils import timezone

from .forms import LoginInteressadoForm, ConsultaPublicaForm
from apps.interessados.models import Interessado
from apps.selecao.models import Inscricao, Classificacao
from apps.eventos.models import Evento


def index(request):
    """
    Página inicial do portal
    Mostra eventos ativos (exceto FINALIZADOS e CANCELADOS)
    """
    eventos_disponiveis = Evento.objects.exclude(
        status_id__in=[7, 8]
    ).order_by('data_inicio_evento')

    context = {
        'eventos_disponiveis': eventos_disponiveis,
        'total_eventos':       eventos_disponiveis.count(),
    }

    return render(request, 'portal/index.html', context)


@require_http_methods(["GET", "POST"])
def login_interessado(request):
    """Login de interessados com CPF e senha"""
    if request.session.get('interessado_id'):
        return redirect('portal:dashboard')

    if request.method == 'POST':
        form = LoginInteressadoForm(request.POST)

        if form.is_valid():
            interessado = form.interessado

            request.session['interessado_id']   = interessado.id
            request.session['interessado_nome'] = interessado.nome
            request.session['interessado_cpf']  = interessado.cpf

            interessado.last_login = timezone.now()
            interessado.save(update_fields=['last_login'])

            messages.success(request, f'Bem-vindo(a), {interessado.nome}!')
            return redirect('portal:dashboard')
    else:
        form = LoginInteressadoForm()

    return render(request, 'portal/login.html', {'form': form})


def logout_interessado(request):
    """Logout de interessados"""
    nome = request.session.get('interessado_nome', 'Interessado')
    request.session.flush()
    messages.info(request, f'Até logo, {nome}!')
    return redirect('portal:index')


def dashboard(request):
    """Dashboard do interessado logado"""
    interessado_id = request.session.get('interessado_id')

    if not interessado_id:
        messages.warning(request, 'Você precisa fazer login para acessar o dashboard.')
        return redirect('portal:login')

    try:
        interessado = Interessado.objects.get(id=interessado_id)
    except Interessado.DoesNotExist:
        request.session.flush()
        messages.error(request, 'Sessão inválida. Faça login novamente.')
        return redirect('portal:login')

    inscricoes = Inscricao.objects.filter(
        interessado=interessado
    ).select_related('evento', 'status').order_by('-data_inscricao')

    classificacoes = Classificacao.objects.filter(
        inscricao__interessado=interessado
    ).select_related('inscricao__evento').order_by('posicao')

    context = {
        'interessado':          interessado,
        'inscricoes':           inscricoes,
        'classificacoes':       classificacoes,
        'total_inscricoes':     inscricoes.count(),
        'total_classificacoes': classificacoes.count(),
    }

    return render(request, 'portal/dashboard.html', context)


@require_http_methods(["GET", "POST"])
def consulta_publica(request):
    """Consulta pública de resultados por CPF"""
    resultados     = None
    cpf_consultado = None

    if request.method == 'POST':
        form = ConsultaPublicaForm(request.POST)

        if form.is_valid():
            cpf            = form.cleaned_data['cpf']
            cpf_consultado = cpf

            try:
                interessado = Interessado.objects.get(cpf=cpf)

                resultados = Classificacao.objects.filter(
                    inscricao__interessado=interessado
                ).select_related(
                    'inscricao__evento',
                    'inscricao__status'
                ).order_by('-inscricao__data_inscricao')

                if not resultados.exists():
                    messages.info(
                        request,
                        'Nenhuma classificação encontrada para este CPF.'
                    )

            except Interessado.DoesNotExist:
                messages.warning(request, 'CPF não encontrado no sistema.')
    else:
        form = ConsultaPublicaForm()

    context = {
        'form':             form,
        'resultados':       resultados,
        'nome_interessado': (
            resultados.first().inscricao.interessado.nome
            if resultados and resultados.exists()
            else ''
        ),
        'cpf_consultado': cpf_consultado,
    }

    return render(request, 'portal/consulta_publica.html', context)


def resultado_evento(request, evento_id):
    """Exibe resultado completo de um evento"""
    try:
        evento = Evento.objects.get(id=evento_id)
    except Evento.DoesNotExist:
        messages.error(request, 'Evento não encontrado.')
        return redirect('portal:index')

    classificacoes = Classificacao.objects.filter(
        inscricao__evento=evento
    ).select_related('inscricao__interessado').order_by('posicao')

    classificados = classificacoes.filter(classificado=True)
    lista_espera  = classificacoes.filter(lista_espera=True)

    context = {
        'evento':              evento,
        'classificados':       classificados,
        'lista_espera':        lista_espera,
        'total_classificados': classificados.count(),
        'total_lista_espera':  lista_espera.count(),
    }

    return render(request, 'portal/resultado_evento.html', context)


def detalhes_evento(request, evento_id):
    """
    Exibe detalhes completos de um evento/curso

    CORREÇÃO 23/02/2026:
    Antes: status__nome__in=['INSCRITO', 'APROVADO', 'CONFIRMADO']
           → sempre zero (nomes reais no banco são diferentes)
    Agora: Q objects com __iexact — case-insensitive, sem exclude()
           Cobre todas as variações de grafia dos status válidos
    """
    try:
        evento = Evento.objects.select_related('status').get(id=evento_id)
    except Evento.DoesNotExist:
        messages.error(request, 'Evento não encontrado.')
        return redirect('portal:index')

    # ==========================================
    # CORREÇÃO 23/02/2026
    # Q objects com iexact — case-insensitive
    # Cobre: 'Pendente', 'PENDENTE', 'pendente'
    #        'Confirmada', 'CONFIRMADA', 'confirmada'
    #        'Inscrito', 'INSCRITO', 'inscrito'
    #        'Aprovado', 'APROVADO', 'aprovado'
    #        'Confirmado', 'CONFIRMADO', 'confirmado'
    # ==========================================
    inscricoes_confirmadas = Inscricao.objects.filter(
        evento=evento
    ).filter(
        Q(status__nome__iexact='pendente')   |
        Q(status__nome__iexact='confirmada') |
        Q(status__nome__iexact='confirmado') |
        Q(status__nome__iexact='inscrito')   |
        Q(status__nome__iexact='aprovado')
    ).count()

    vagas_disponiveis = max(evento.total_vagas - inscricoes_confirmadas, 0)

    context = {
        'evento':                 evento,
        'inscricoes_confirmadas': inscricoes_confirmadas,
        'vagas_disponiveis':      vagas_disponiveis,
    }

    return render(request, 'portal/detalhes_evento.html', context)


def contato(request):
    """Página de contatos da MetaReciclagem"""
    context = {
        'contatos': {
            'telefone': '(15) 3417-3825',
            'whatsapp': '(15) 99999-9999',
            'email':    'meta.recicla@gmail.com',
            'endereco': 'Avenida Armando Sales de Oliveira, 762 – Sorocaba/SP',
            'cep':      '18000-000',
            'horario':  'Segunda a Sexta, das 8h às 16h',
        },
        'redes_sociais': {
            'facebook':  'https://facebook.com/metareciclagemsorocaba',
            'instagram': 'https://instagram.com/metareciclagemsorocaba',
            'youtube':   'https://youtube.com/metareciclagemsorocaba',
            'blog':      'https://metareciclagemdesorocaba.blogspot.com/',
        }
    }

    return render(request, 'portal/contato.html', context)

def politica_privacidade(request):
    """Página de política de privacidade — LGPD"""
    return render(request, 'portal/politica_privacidade.html')


    

