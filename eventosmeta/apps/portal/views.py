"""
Views do app PORTAL - Sistema MetaReciclagem
Arquivo: apps/portal/views.py
Data: 05/12/2025
"""
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
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
    # Buscar eventos que NÃO sejam FINALIZADOS (id=7) ou CANCELADOS (id=8)
    eventos_disponiveis = Evento.objects.exclude(
        status_id__in=[7, 8]
    ).order_by('data_inicio_evento')
    
    context = {
        'eventos_disponiveis': eventos_disponiveis,
        'total_eventos': eventos_disponiveis.count()
    }
    
    return render(request, 'portal/index.html', context)


@require_http_methods(["GET", "POST"])
def login_interessado(request):
    """
    Login de interessados com CPF e senha
    """
    # Se já está logado, redireciona para dashboard
    if request.session.get('interessado_id'):
        return redirect('portal:dashboard')
    
    if request.method == 'POST':
        form = LoginInteressadoForm(request.POST)
        
        if form.is_valid():
            interessado = form.interessado
            
            # Criar sessão
            request.session['interessado_id'] = interessado.id
            request.session['interessado_nome'] = interessado.nome
            request.session['interessado_cpf'] = interessado.cpf
            
            # Atualizar último login
            interessado.last_login = timezone.now()
            interessado.save(update_fields=['last_login'])
            
            messages.success(request, f'Bem-vindo(a), {interessado.nome}!')
            return redirect('portal:dashboard')
    else:
        form = LoginInteressadoForm()
    
    context = {
        'form': form
    }
    
    return render(request, 'portal/login.html', context)


def logout_interessado(request):
    """
    Logout de interessados
    """
    nome = request.session.get('interessado_nome', 'Interessado')
    
    # Limpar sessão
    request.session.flush()
    
    messages.info(request, f'Até logo, {nome}!')
    return redirect('portal:index')


def dashboard(request):
    """
    Dashboard do interessado logado
    Mostra suas inscrições e classificações
    """
    # Verificar se está logado
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
    
    # Buscar inscrições do interessado
    inscricoes = Inscricao.objects.filter(
        interessado=interessado
    ).select_related('evento', 'status').order_by('-data_inscricao')
    
    # Buscar classificações
    classificacoes = Classificacao.objects.filter(
        inscricao__interessado=interessado
    ).select_related('inscricao__evento').order_by('posicao')
    
    context = {
        'interessado': interessado,
        'inscricoes': inscricoes,
        'classificacoes': classificacoes,
        'total_inscricoes': inscricoes.count(),
        'total_classificacoes': classificacoes.count()
    }
    
    return render(request, 'portal/dashboard.html', context)


@require_http_methods(["GET", "POST"])
def consulta_publica(request):
    """
    Consulta pública de resultados por CPF
    Não requer login
    """
    resultados = None
    cpf_consultado = None
    
    if request.method == 'POST':
        form = ConsultaPublicaForm(request.POST)
        
        if form.is_valid():
            cpf = form.cleaned_data['cpf']
            cpf_consultado = cpf
            
            try:
                interessado = Interessado.objects.get(cpf=cpf)
                
                # Buscar classificações
                resultados = Classificacao.objects.filter(
                    inscricao__interessado=interessado
                ).select_related(
                    'inscricao__evento',
                    'inscricao__status'
                ).order_by('-inscricao__data_inscricao')
                
                if not resultados.exists():
                    messages.info(request, 'Nenhuma classificação encontrada para este CPF.')
                
            except Interessado.DoesNotExist:
                messages.warning(request, 'CPF não encontrado no sistema.')
    else:
        form = ConsultaPublicaForm()
    
    context = {
        'form': form,
        'resultados': resultados,
        'cpf_consultado': cpf_consultado
    }
    
    return render(request, 'portal/consulta_publica.html', context)


def resultado_evento(request, evento_id):
    """
    Exibe resultado completo de um evento
    Lista todos os classificados e lista de espera
    """
    try:
        evento = Evento.objects.get(id=evento_id)
    except Evento.DoesNotExist:
        messages.error(request, 'Evento não encontrado.')
        return redirect('portal:index')
    
    # Buscar classificações do evento
    classificacoes = Classificacao.objects.filter(
        inscricao__evento=evento
    ).select_related(
        'inscricao__interessado'
    ).order_by('posicao')
    
    # Separar classificados e lista de espera
    classificados = classificacoes.filter(classificado=True)
    lista_espera = classificacoes.filter(lista_espera=True)
    
    context = {
        'evento': evento,
        'classificados': classificados,
        'lista_espera': lista_espera,
        'total_classificados': classificados.count(),
        'total_lista_espera': lista_espera.count()
    }
    
    return render(request, 'portal/resultado_evento.html', context)

def detalhes_evento(request, evento_id):
    """
    Exibe detalhes completos de um evento/curso
    Informações sobre o curso, requisitos, datas, vagas, etc.
    """
    try:
        evento = Evento.objects.get(id=evento_id)
    except Evento.DoesNotExist:
        messages.error(request, 'Evento não encontrado.')
        return redirect('portal:index')
    
    # Calcular vagas disponíveis
    inscricoes_confirmadas = Inscricao.objects.filter(
        evento=evento,
        status__nome__in=['INSCRITO', 'APROVADO', 'CONFIRMADO']
    ).count()
    
    vagas_disponiveis = evento.total_vagas - inscricoes_confirmadas
    
    # Verificar se inscrições estão abertas
    agora = timezone.now()
    inscricoes_abertas = (
        evento.data_inicio_inscricao <= agora <= evento.data_fim_inscricao
    )
    
    context = {
        'evento': evento,
        'inscricoes_confirmadas': inscricoes_confirmadas,
        'vagas_disponiveis': vagas_disponiveis,
        'inscricoes_abertas': inscricoes_abertas,
    }
    
    return render(request, 'portal/detalhes_evento.html', context)

def contato(request):
    """
    Página de contatos da MetaReciclagem
    Exibe informações de contato, endereço, redes sociais
    """
    context = {
        'contatos': {
            'telefone': '(15) 3261-8000',
            'whatsapp': '(15) 99999-9999',
            'email': 'contato@metareciclagem.sp.gov.br',
            'endereco': 'Rua Exemplo, 123 - Centro - Sorocaba/SP',
            'cep': '18000-000',
            'horario': 'Segunda a Sexta, das 8h às 17h',
        },
        'redes_sociais': {
            'facebook': 'https://facebook.com/metareciclagemsorocaba',
            'instagram': 'https://instagram.com/metareciclagemsorocaba',
            'youtube': 'https://youtube.com/metareciclagemsorocaba',
        }
    }
    
    return render(request, 'portal/contato.html', context)

