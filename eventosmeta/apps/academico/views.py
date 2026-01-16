"""
Arquivo: views.py
Caminho: apps/academico/views.py
Descrição: Views para gestão de matrícula
Data: 12/01/2026
"""

from django.shortcuts import render, redirect
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib import messages
from django.http import JsonResponse
from apps.eventos.models import Evento, Status
from apps.selecao.models import Classificacao, Inscricao
from .services import MatriculaService


@staff_member_required
def gestao_matricula(request):
    """
    View principal para gestão de matrícula
    Exibe lista de eventos com classificação concluída
    """
    # Buscar eventos com status "Resultado Divulgado" (ID=5)
    eventos_disponiveis = Evento.objects.filter(
        status__id=5
    ).order_by('-data_inicio_evento')
    
    evento_selecionado = None
    classificacoes = None
    
    # Se um evento foi selecionado
    if request.GET.get('evento_id'):
        evento_id = request.GET.get('evento_id')
        try:
            evento_selecionado = Evento.objects.get(id=evento_id)
            
            # Buscar classificações do evento ordenadas por posição
            classificacoes = Classificacao.objects.filter(
                inscricao__evento=evento_selecionado
            ).select_related(
                'inscricao__interessado',
                'inscricao__status'
            ).order_by('posicao')
            
        except Evento.DoesNotExist:
            messages.error(request, '❌ Evento não encontrado')
    
    context = {
        'eventos_disponiveis': eventos_disponiveis,
        'evento_selecionado': evento_selecionado,
        'classificacoes': classificacoes,
        'title': 'Gestão de Matrícula'
    }
    
    return render(request, 'academico/gestao_matricula.html', context)


@staff_member_required
def processar_matricula(request):
    """
    Processa ação de matrícula de múltiplos alunos
    """
    if request.method != 'POST':
        return JsonResponse({'erro': 'Método não permitido'}, status=405)
    
    # Obter IDs das inscrições selecionadas
    inscricoes_ids = request.POST.getlist('inscricoes_selecionadas')
    
    if not inscricoes_ids:
        messages.warning(request, '⚠️ Nenhuma inscrição selecionada')
        return redirect('academico:gestao_matricula')
    
    # Processar matrícula
    try:
        resultado = MatriculaService.matricular_alunos(
            inscricoes_ids=inscricoes_ids,
            usuario=request.user
        )
        
        # Mensagens de feedback
        if resultado['total_sucesso'] > 0:
            messages.success(
                request,
                f"✅ {resultado['total_sucesso']} matrícula(s) realizada(s) com sucesso!"
            )
        
        if resultado['total_ja_matriculados'] > 0:
            messages.info(
                request,
                f"ℹ️ {resultado['total_ja_matriculados']} aluno(s) já possuíam matrícula"
            )
        
        if resultado['erros']:
            for erro in resultado['erros']:
                messages.error(request, f"❌ {erro}")
        
    except Exception as e:
        messages.error(request, f"❌ Erro ao processar matrículas: {str(e)}")
    
    # Redirecionar de volta com o evento selecionado
    evento_id = request.POST.get('evento_id')
    if evento_id:
        return redirect(f"/academico/gestao-matricula/?evento_id={evento_id}")
    
    return redirect('academico:gestao_matricula')


@staff_member_required
def alterar_status_inscricao(request):
    """
    Altera status de múltiplas inscrições
    """
    if request.method != 'POST':
        return JsonResponse({'erro': 'Método não permitido'}, status=405)
    
    # Obter dados
    inscricoes_ids = request.POST.getlist('inscricoes_selecionadas')
    novo_status = request.POST.get('novo_status')
    
    if not inscricoes_ids:
        messages.warning(request, '⚠️ Nenhuma inscrição selecionada')
        return redirect('academico:gestao_matricula')
    
    if not novo_status:
        messages.error(request, '❌ Status não informado')
        return redirect('academico:gestao_matricula')
    
    # Processar alteração de status
    try:
        resultado = MatriculaService.alterar_status_inscricao(
            inscricoes_ids=inscricoes_ids,
            novo_status_nome=novo_status,
            usuario=request.user
        )
        
        # Mensagens de feedback
        if resultado['total_atualizadas'] > 0:
            messages.success(
                request,
                f"✅ {resultado['total_atualizadas']} inscrição(ões) atualizada(s) para '{novo_status}'"
            )
        
        if resultado['erros']:
            for erro in resultado['erros']:
                messages.error(request, f"❌ {erro}")
        
    except Exception as e:
        messages.error(request, f"❌ Erro ao alterar status: {str(e)}")
    
    # Redirecionar de volta com o evento selecionado
    evento_id = request.POST.get('evento_id')
    if evento_id:
        return redirect(f"/academico/gestao-matricula/?evento_id={evento_id}")
    
    return redirect('academico:gestao_matricula')

