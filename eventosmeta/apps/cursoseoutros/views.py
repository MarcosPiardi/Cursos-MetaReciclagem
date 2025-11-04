"""
ARQUIVO: apps/cursoseoutros/views.py
AÇÃO: CRIAR arquivo completo
MUDANÇA: Views para área pública (inscrições) e área staff (gestão e classificação)
DATA/HORA: 2025-10-29 15:45:00
"""

import csv
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
from django.db.models import Q, Count
from django.core.paginator import Paginator
from django.views.decorators.http import require_POST
from django.utils import timezone

from .models import (
    Evento, Status, Inscricao, Classificacao, 
    InscricaoCriterioAtendido, Turma, Matricula
)
from .forms import (
    InscricaoEventoForm, EventoForm, EventoCriterioForm,
    ValidarCriterioCustomizadoForm, TurmaForm, MatriculaForm,
    FiltroEventosForm
)
from .services import ClassificadorService


# ============================================
# VIEWS PÚBLICAS - INTERESSADOS
# ============================================

def lista_cursos_publico(request):
    """
    Lista de cursos/eventos abertos para inscrição.
    Área pública - qualquer pessoa pode acessar.
    """
    # Busca apenas eventos com status que permite inscrição
    eventos = Evento.objects.filter(
        status__permite_inscricao=True
    ).select_related('status').order_by('-criado_em')
    
    # Aplica filtros se houver
    form = FiltroEventosForm(request.GET)
    if form.is_valid():
        busca = form.cleaned_data.get('busca')
        status = form.cleaned_data.get('status')
        modalidade = form.cleaned_data.get('modalidade')
        
        if busca:
            eventos = eventos.filter(
                Q(descricao__icontains=busca) |
                Q(docente__icontains=busca) |
                Q(programa__icontains=busca)
            )
        
        if status:
            eventos = eventos.filter(status=status)
        
        if modalidade:
            eventos = eventos.filter(modalidade=modalidade)
    
    # Paginação
    paginator = Paginator(eventos, 12)  # 12 eventos por página
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'eventos': page_obj,
        'form': form,
        'total': eventos.count()
    }
    
    return render(request, 'cursoseoutros/lista_cursos_publico.html', context)


def detalhe_curso_publico(request, evento_id):
    """
    Exibe detalhes completos de um curso/evento.
    Área pública.
    """
    evento = get_object_or_404(
        Evento.objects.select_related('status'),
        id=evento_id
    )
    
    # Verifica se interessado está logado e já se inscreveu
    ja_inscrito = False
    if hasattr(request.user, '__class__') and request.user.__class__.__name__ == 'Interessado':
        ja_inscrito = Inscricao.objects.filter(
            evento=evento,
            interessado=request.user
        ).exists()
    
    context = {
        'evento': evento,
        'ja_inscrito': ja_inscrito,
        'vagas_disponiveis': evento.vagas_disponiveis(),
        'total_inscricoes': evento.total_inscricoes()
    }
    
    return render(request, 'cursoseoutros/detalhe_curso_publico.html', context)


def inscricao_curso(request, evento_id):
    """
    Formulário de inscrição em curso.
    Requer login de interessado.
    """
    # Verifica se é interessado logado
    if not hasattr(request.user, '__class__') or request.user.__class__.__name__ != 'Interessado':
        messages.error(request, 'Você precisa estar logado como interessado para se inscrever.')
        return redirect('interessados:login')
    
    evento = get_object_or_404(Evento, id=evento_id)
    interessado = request.user
    
    # Verifica se já está inscrito
    if Inscricao.objects.filter(evento=evento, interessado=interessado).exists():
        messages.warning(request, 'Você já está inscrito neste evento.')
        return redirect('cursoseoutros:detalhe_curso_publico', evento_id=evento.id)
    
    if request.method == 'POST':
        form = InscricaoEventoForm(
            request.POST,
            interessado=interessado,
            evento=evento
        )
        
        if form.is_valid():
            inscricao = form.save()
            messages.success(
                request,
                f'Inscrição realizada com sucesso em "{evento.descricao}"! '
                f'Número da inscrição: {inscricao.id}'
            )
            return redirect('cursoseoutros:confirmacao_inscricao', inscricao_id=inscricao.id)
        else:
            messages.error(request, 'Por favor, corrija os erros abaixo.')
    else:
        form = InscricaoEventoForm(interessado=interessado, evento=evento)
    
    context = {
        'form': form,
        'evento': evento,
        'interessado': interessado
    }
    
    return render(request, 'cursoseoutros/inscricao_curso.html', context)


def confirmacao_inscricao(request, inscricao_id):
    """
    Página de confirmação após inscrição realizada.
    """
    # Verifica se é o interessado dono da inscrição
    if not hasattr(request.user, '__class__') or request.user.__class__.__name__ != 'Interessado':
        messages.error(request, 'Acesso negado.')
        return redirect('home')
    
    inscricao = get_object_or_404(
        Inscricao.objects.select_related('evento', 'interessado'),
        id=inscricao_id,
        interessado=request.user
    )
    
    context = {
        'inscricao': inscricao
    }
    
    return render(request, 'cursoseoutros/confirmacao_inscricao.html', context)


# ============================================
# VIEWS STAFF - ÁREA ADMINISTRATIVA
# ============================================

@login_required(login_url='/staff/login/')
def lista_eventos_staff(request):
    """
    Lista de todos os eventos para gestão.
    Área administrativa - requer login staff.
    """
    if not request.user.is_staff:
        messages.error(request, 'Acesso negado.')
        return redirect('home')
    
    # Busca todos eventos
    eventos = Evento.objects.select_related('status').annotate(
        total_inscricoes=Count('inscricoes')
    ).order_by('-criado_em')
    
    # Filtros
    status_filtro = request.GET.get('status')
    modalidade_filtro = request.GET.get('modalidade')
    busca = request.GET.get('busca')
    
    if status_filtro:
        eventos = eventos.filter(status_id=status_filtro)
    
    if modalidade_filtro:
        eventos = eventos.filter(modalidade=modalidade_filtro)
    
    if busca:
        eventos = eventos.filter(
            Q(descricao__icontains=busca) |
            Q(docente__icontains=busca)
        )
    
    # Paginação
    paginator = Paginator(eventos, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    # Lista de status para filtro
    status_lista = Status.objects.all().order_by('ordem')
    
    context = {
        'eventos': page_obj,
        'status_lista': status_lista,
        'total': eventos.count()
    }
    
    return render(request, 'cursoseoutros/staff/lista_eventos.html', context)


@login_required(login_url='/staff/login/')
def criar_evento_staff(request):
    """
    Criar novo evento/curso.
    Área administrativa.
    """
    if not request.user.is_staff:
        messages.error(request, 'Acesso negado.')
        return redirect('home')
    
    if request.method == 'POST':
        form = EventoForm(request.POST)
        if form.is_valid():
            evento = form.save()
            messages.success(request, f'Evento "{evento.descricao}" criado com sucesso!')
            return redirect('cursoseoutros:detalhe_evento_staff', evento_id=evento.id)
        else:
            messages.error(request, 'Por favor, corrija os erros abaixo.')
    else:
        form = EventoForm()
    
    context = {
        'form': form,
        'titulo': 'Criar Novo Evento'
    }
    
    return render(request, 'cursoseoutros/staff/form_evento.html', context)


@login_required(login_url='/staff/login/')
def editar_evento_staff(request, evento_id):
    """
    Editar evento existente.
    Área administrativa.
    """
    if not request.user.is_staff:
        messages.error(request, 'Acesso negado.')
        return redirect('home')
    
    evento = get_object_or_404(Evento, id=evento_id)
    
    if request.method == 'POST':
        form = EventoForm(request.POST, instance=evento)
        if form.is_valid():
            evento = form.save()
            messages.success(request, f'Evento "{evento.descricao}" atualizado com sucesso!')
            return redirect('cursoseoutros:detalhe_evento_staff', evento_id=evento.id)
        else:
            messages.error(request, 'Por favor, corrija os erros abaixo.')
    else:
        form = EventoForm(instance=evento)
    
    context = {
        'form': form,
        'evento': evento,
        'titulo': f'Editar Evento: {evento.descricao}'
    }
    
    return render(request, 'cursoseoutros/staff/form_evento.html', context)


@login_required(login_url='/staff/login/')
def detalhe_evento_staff(request, evento_id):
    """
    Detalhes completos do evento para gestão.
    Área administrativa.
    """
    if not request.user.is_staff:
        messages.error(request, 'Acesso negado.')
        return redirect('home')
    
    evento = get_object_or_404(
        Evento.objects.select_related('status').prefetch_related(
            'evento_criterios__criterio',
            'inscricoes__interessado'
        ),
        id=evento_id
    )
    
    # Estatísticas
    total_inscricoes = evento.inscricoes.count()
    inscricoes_aprovadas = evento.inscricoes.filter(status='APROVADO').count()
    inscricoes_fila = evento.inscricoes.filter(status='FILA_ESPERA').count()
    
    # Verifica se tem classificação
    tem_classificacao = Classificacao.objects.filter(
        inscricao__evento=evento
    ).exists()
    
    context = {
        'evento': evento,
        'total_inscricoes': total_inscricoes,
        'inscricoes_aprovadas': inscricoes_aprovadas,
        'inscricoes_fila': inscricoes_fila,
        'vagas_disponiveis': evento.vagas_disponiveis(),
        'tem_classificacao': tem_classificacao
    }
    
    return render(request, 'cursoseoutros/staff/detalhe_evento.html', context)


@login_required(login_url='/staff/login/')
@require_POST
def classificar_evento_staff(request, evento_id):
    """
    Executa a classificação de um evento.
    Processa todas as inscrições e atribui posições.
    """
    if not request.user.is_staff:
        messages.error(request, 'Acesso negado.')
        return redirect('home')
    
    evento = get_object_or_404(Evento, id=evento_id)
    
    try:
        # Executa classificação
        ClassificadorService.classificar_evento(evento)
        
        messages.success(
            request,
            f'Classificação realizada com sucesso! '
            f'Total de {evento.inscricoes.count()} inscrições processadas.'
        )
    except Exception as e:
        messages.error(request, f'Erro ao classificar evento: {str(e)}')
    
    return redirect('cursoseoutros:ver_classificacao_staff', evento_id=evento.id)


@login_required(login_url='/staff/login/')
def ver_classificacao_staff(request, evento_id):
    """
    Visualiza a classificação completa de um evento.
    Lista ordenada por posição.
    """
    if not request.user.is_staff:
        messages.error(request, 'Acesso negado.')
        return redirect('home')
    
    evento = get_object_or_404(Evento, id=evento_id)
    
    # Busca inscrições com classificação
    inscricoes = Inscricao.objects.filter(
        evento=evento
    ).select_related(
        'interessado', 'classificacao'
    ).prefetch_related(
        'criterios_atendidos__criterio'
    ).order_by('classificacao__posicao')
    
    # Verifica se tem classificação
    if not inscricoes.filter(classificacao__isnull=False).exists():
        messages.warning(
            request,
            'Este evento ainda não foi classificado. Clique em "Classificar Agora".'
        )
    
    # Paginação
    paginator = Paginator(inscricoes, 50)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'evento': evento,
        'inscricoes': page_obj,
        'total': inscricoes.count()
    }
    
    return render(request, 'cursoseoutros/staff/classificacao.html', context)


@login_required(login_url='/staff/login/')
def exportar_classificacao_csv(request, evento_id):
    """
    Exporta a classificação para arquivo CSV.
    """
    if not request.user.is_staff:
        messages.error(request, 'Acesso negado.')
        return redirect('home')
    
    evento = get_object_or_404(Evento, id=evento_id)
    
    # Gera dados
    dados = ClassificadorService.exportar_classificacao_csv(evento)
    
    # Cria response CSV
    response = HttpResponse(content_type='text/csv; charset=utf-8')
    response['Content-Disposition'] = f'attachment; filename="classificacao_{evento.id}_{evento.descricao[:30]}.csv"'
    
    # Adiciona BOM para Excel reconhecer UTF-8
    response.write('\ufeff')
    
    writer = csv.DictWriter(response, fieldnames=dados[0].keys() if dados else [])
    writer.writeheader()
    writer.writerows(dados)
    
    return response


@login_required(login_url='/staff/login/')
def lista_inscricoes_staff(request, evento_id):
    """
    Lista todas as inscrições de um evento.
    Permite visualizar e gerenciar inscrições.
    """
    if not request.user.is_staff:
        messages.error(request, 'Acesso negado.')
        return redirect('home')
    
    evento = get_object_or_404(Evento, id=evento_id)
    
    inscricoes = Inscricao.objects.filter(
        evento=evento
    ).select_related('interessado').order_by('-data_inscricao')
    
    # Filtro por status
    status_filtro = request.GET.get('status')
    if status_filtro:
        inscricoes = inscricoes.filter(status=status_filtro)
    
    # Paginação
    paginator = Paginator(inscricoes, 50)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'evento': evento,
        'inscricoes': page_obj,
        'total': inscricoes.count()
    }
    
    return render(request, 'cursoseoutros/staff/lista_inscricoes.html', context)


@login_required(login_url='/staff/login/')
def validar_criterios_customizados(request, evento_id):
    """
    Lista critérios customizados que precisam de validação manual.
    """
    if not request.user.is_staff:
        messages.error(request, 'Acesso negado.')
        return redirect('home')
    
    evento = get_object_or_404(Evento, id=evento_id)
    
    # Busca critérios customizados não validados
    criterios_pendentes = InscricaoCriterioAtendido.objects.filter(
        inscricao__evento=evento,
        criterio__tipo_criterio='CUSTOMIZADO',
        validado=False
    ).select_related('inscricao__interessado', 'criterio')
    
    context = {
        'evento': evento,
        'criterios_pendentes': criterios_pendentes,
        'total': criterios_pendentes.count()
    }
    
    return render(request, 'cursoseoutros/staff/validar_criterios.html', context)


@login_required(login_url='/staff/login/')
@require_POST
def validar_criterio_acao(request, criterio_atendido_id):
    """
    Valida ou rejeita um critério customizado específico.
    """
    if not request.user.is_staff:
        return JsonResponse({'error': 'Acesso negado'}, status=403)
    
    criterio_atendido = get_object_or_404(
        InscricaoCriterioAtendido,
        id=criterio_atendido_id
    )
    
    acao = request.POST.get('acao')  # 'validar' ou 'rejeitar'
    
    if acao == 'validar':
        criterio_atendido.validado = True
        criterio_atendido.validado_por = request.user
        criterio_atendido.data_validacao = timezone.now()
        criterio_atendido.save()
        
        messages.success(request, 'Critério validado com sucesso!')
    
    elif acao == 'rejeitar':
        criterio_atendido.validado = False
        criterio_atendido.pontos_obtidos = 0
        criterio_atendido.save()
        
        messages.info(request, 'Critério rejeitado.')
    
    return redirect('cursoseoutros:validar_criterios_customizados', 
                    evento_id=criterio_atendido.inscricao.evento.id)


# ============================================
# VIEWS AJAX - PARA INTERAÇÕES DINÂMICAS
# ============================================

@login_required(login_url='/staff/login/')
def evento_info_ajax(request, evento_id):
    """
    Retorna informações do evento em JSON.
    Para uso em chamadas AJAX.
    """
    if not request.user.is_staff:
        return JsonResponse({'error': 'Acesso negado'}, status=403)
    
    evento = get_object_or_404(Evento, id=evento_id)
    
    data = {
        'id': evento.id,
        'descricao': evento.descricao,
        'vagas': evento.vagas,
        'vagas_disponiveis': evento.vagas_disponiveis(),
        'total_inscricoes': evento.total_inscricoes(),
        'status': evento.status.status,
        'permite_inscricao': evento.status.permite_inscricao,
    }
    
    return JsonResponse(data)