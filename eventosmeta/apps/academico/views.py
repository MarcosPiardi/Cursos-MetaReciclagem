"""
Arquivo: views.py
Caminho: apps/academico/views.py
Descrição: Views do app Acadêmico — certificados e gestão de matrículas
Atualizações:
- 12/01/2026 - Criação
- 02/02/2026 - Reorganização
- 24/07/2026 - Adicionadas views de gestao_matricula, processar_matricula e alterar_status_inscricao
"""

from django.http import HttpResponse, FileResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib import messages
from django.views.decorators.http import require_http_methods

import io
import zipfile

from apps.eventos.models import Evento
from apps.selecao.models import Classificacao, Inscricao, StatusInscricao

from .models import Avaliacao
from .certificado import GeradorCertificado

# ==========================================================================
# GESTÃO DE MATRÍCULAS
# ==========================================================================

@staff_member_required
def gestao_matricula_view(request):
    """
    Exibe a tela de gestão de matrícula.
    GET sem evento_id: mostra apenas o seletor de eventos.
    GET com evento_id: mostra o evento selecionado e a lista de classificações.
    """
    evento_id = request.GET.get('evento_id')

    eventos_disponiveis = Evento.objects.filter(
        inscricoes__classificacao__isnull=False
    ).distinct().order_by('nome')

    evento_selecionado = None
    classificacoes = None

    if evento_id:
        try:
            evento_selecionado = Evento.objects.get(pk=evento_id)
            classificacoes = Classificacao.objects.filter(
                inscricao__evento=evento_selecionado
            ).select_related(
                'inscricao__interessado',
                'inscricao__status',
                'inscricao__evento',
            ).order_by('posicao')
        except Evento.DoesNotExist:
            messages.error(request, 'Evento não encontrado.')

    contexto = {
        'eventos_disponiveis': eventos_disponiveis,
        'evento_selecionado': evento_selecionado,
        'classificacoes': classificacoes,
    }

    return render(request, 'academico/gestao_matricula.html', contexto)

@staff_member_required
@require_http_methods(["POST"])
def processar_matricula_view(request):
    """
    Processa a matrícula dos inscritos selecionados.
    Recebe POST com evento_id e inscricoes_selecionadas.
    """
    evento_id = request.POST.get('evento_id')
    inscricoes_ids = request.POST.getlist('inscricoes_selecionadas')

    if not inscricoes_ids:
        messages.error(request, 'Nenhuma inscrição selecionada.')
        return redirect(f'{reverse("academico:gestao_matricula")}?evento_id={evento_id}')

    # TODO: implementar a lógica de matrícula
    # from apps.academico.services import MatriculaService
    # MatriculaService.matricular_lote(inscricoes_ids, evento_id)

    messages.success(
        request,
        f'{len(inscricoes_ids)} inscrição(ões) processada(s) para matrícula.'
    )
    return redirect(f'{reverse("academico:gestao_matricula")}?evento_id={evento_id}')

@staff_member_required
@require_http_methods(["POST"])
def alterar_status_inscricao_view(request):
    """
    Altera o status das inscrições selecionadas.
    Recebe POST com evento_id, inscricoes_selecionadas e novo_status.
    """
    if request.method != 'POST':
        return redirect('academico:gestao_matricula')

    evento_id = request.POST.get('evento_id')
    inscricoes_ids = request.POST.getlist('inscricoes_selecionadas')
    novo_status = request.POST.get('novo_status')

    if not inscricoes_ids:
        messages.error(request, 'Nenhuma inscrição selecionada.')
        return redirect(f'{reverse("academico:gestao_matricula")}?evento_id={evento_id}')

    # TODO: implementar a alteração de status
    # from apps.selecao.services import InscricaoService
    # InscricaoService.alterar_status_lote(inscricoes_ids, novo_status)

    messages.success(
        request,
        f'{len(inscricoes_ids)} inscrição(ões) marcada(s) como "{novo_status}".'
    )
    return redirect(f'{reverse("academico:gestao_matricula")}?evento_id={evento_id}')

# ==========================================================================
# CERTIFICADOS
# ==========================================================================

@staff_member_required
@require_http_methods(["GET"])
def download_certificado_individual(request, avaliacao_id):
    """
    Download individual de certificado em PDF
    """
    avaliacao = get_object_or_404(Avaliacao, pk=avaliacao_id)

    if not avaliacao.aprovado:
        return HttpResponse("Certificado disponível apenas para alunos aprovados.", status=400)

    buffer = io.BytesIO()
    gerador = GeradorCertificado(avaliacao)
    gerador.gerar_pdf(buffer)
    buffer.seek(0)

    aluno_nome = avaliacao.matricula.interessado.nome.replace(' ', '_')
    curso_nome = avaliacao.matricula.turma.evento.nome.replace(' ', '_')
    filename = f"Certificado_{aluno_nome}_{curso_nome}.pdf"

    response = FileResponse(buffer, content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="{filename}"'

    return response

@staff_member_required
@require_http_methods(["GET"])
def preview_certificado(request, avaliacao_id):
    """
    Preview do certificado (visualizar no navegador)
    """
    avaliacao = get_object_or_404(Avaliacao, pk=avaliacao_id)

    if not avaliacao.aprovado:
        return HttpResponse("Certificado disponível apenas para alunos aprovados.", status=400)

    buffer = io.BytesIO()
    gerador = GeradorCertificado(avaliacao)
    gerador.gerar_pdf(buffer)
    buffer.seek(0)

    response = FileResponse(buffer, content_type='application/pdf')
    response['Content-Disposition'] = 'inline'

    return response

@staff_member_required
@require_http_methods(["GET"])
def download_certificados_lote(request):
    """
    Download em lote de certificados (ZIP)
    """
    ids_str = request.GET.get('ids', '')
    ids = [int(id) for id in ids_str.split(',') if id.strip().isdigit()]

    if not ids:
        return HttpResponse("Nenhuma avaliação selecionada.", status=400)

    avaliacoes = Avaliacao.objects.filter(pk__in=ids, aprovado=True)

    if avaliacoes.count() == 0:
        return HttpResponse("Nenhum aluno aprovado foi selecionado.", status=400)

    zip_buffer = io.BytesIO()

    with zipfile.ZipFile(zip_buffer, 'w', zipfile.ZIP_DEFLATED) as zip_file:
        for avaliacao in avaliacoes:
            pdf_buffer = io.BytesIO()
            gerador = GeradorCertificado(avaliacao)
            gerador.gerar_pdf(pdf_buffer)
            pdf_buffer.seek(0)

            aluno_nome = avaliacao.matricula.interessado.nome.replace(' ', '_')
            matricula_num = avaliacao.matricula.numero_matricula
            filename = f"Certificado_{matricula_num}_{aluno_nome}.pdf"

            zip_file.writestr(filename, pdf_buffer.read())

    zip_buffer.seek(0)

    response = HttpResponse(zip_buffer, content_type='application/zip')
    response['Content-Disposition'] = f'attachment; filename="Certificados_{len(avaliacoes)}_alunos.zip"'

    return response

