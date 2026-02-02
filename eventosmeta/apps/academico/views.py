"""
Arquivo: views.py
Caminho: apps/academico/views.py
Descrição: Views para gestão de matrícula
Data: 12/01/2026
"""

"""
Views do app ACADÊMICO
Arquivo: apps/academico/views.py
Data: 02/02/2026
"""

from django.http import HttpResponse, FileResponse
from django.shortcuts import get_object_or_404
from django.contrib.admin.views.decorators import staff_member_required
from django.views.decorators.http import require_http_methods
import io
import zipfile

from .models import Avaliacao
from .certificado import GeradorCertificado


@staff_member_required
@require_http_methods(["GET"])
def download_certificado_individual(request, avaliacao_id):
    """
    Download individual de certificado em PDF
    """
    avaliacao = get_object_or_404(Avaliacao, pk=avaliacao_id)
    
    # Verificar se está aprovado
    if not avaliacao.aprovado:
        return HttpResponse("❌ Certificado disponível apenas para alunos aprovados.", status=400)
    
    # Gerar PDF
    buffer = io.BytesIO()
    gerador = GeradorCertificado(avaliacao)
    gerador.gerar_pdf(buffer)
    buffer.seek(0)
    
    # Nome do arquivo
    aluno_nome = avaliacao.matricula.interessado.nome.replace(' ', '_')
    curso_nome = avaliacao.matricula.turma.evento.nome.replace(' ', '_')
    filename = f"Certificado_{aluno_nome}_{curso_nome}.pdf"
    
    # Retornar PDF para download
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
    
    # Verificar se está aprovado
    if not avaliacao.aprovado:
        return HttpResponse("❌ Certificado disponível apenas para alunos aprovados.", status=400)
    
    # Gerar PDF
    buffer = io.BytesIO()
    gerador = GeradorCertificado(avaliacao)
    gerador.gerar_pdf(buffer)
    buffer.seek(0)
    
    # Retornar PDF para visualização inline
    response = FileResponse(buffer, content_type='application/pdf')
    response['Content-Disposition'] = 'inline'
    
    return response


@staff_member_required
@require_http_methods(["GET"])
def download_certificados_lote(request):
    """
    Download em lote de certificados (ZIP)
    """
    # Pegar IDs da query string
    ids_str = request.GET.get('ids', '')
    ids = [int(id) for id in ids_str.split(',') if id.strip().isdigit()]
    
    if not ids:
        return HttpResponse("❌ Nenhuma avaliação selecionada.", status=400)
    
    # Buscar avaliações aprovadas
    avaliacoes = Avaliacao.objects.filter(pk__in=ids, aprovado=True)
    
    if avaliacoes.count() == 0:
        return HttpResponse("❌ Nenhum aluno aprovado foi selecionado.", status=400)
    
    # Criar ZIP em memória
    zip_buffer = io.BytesIO()
    
    with zipfile.ZipFile(zip_buffer, 'w', zipfile.ZIP_DEFLATED) as zip_file:
        for avaliacao in avaliacoes:
            # Gerar PDF de cada certificado
            pdf_buffer = io.BytesIO()
            gerador = GeradorCertificado(avaliacao)
            gerador.gerar_pdf(pdf_buffer)
            pdf_buffer.seek(0)
            
            # Nome do arquivo dentro do ZIP
            aluno_nome = avaliacao.matricula.interessado.nome.replace(' ', '_')
            matricula_num = avaliacao.matricula.numero_matricula
            filename = f"Certificado_{matricula_num}_{aluno_nome}.pdf"
            
            # Adicionar ao ZIP
            zip_file.writestr(filename, pdf_buffer.read())
    
    zip_buffer.seek(0)
    
    # Retornar ZIP para download
    response = HttpResponse(zip_buffer, content_type='application/zip')
    response['Content-Disposition'] = f'attachment; filename="Certificados_{len(avaliacoes)}_alunos.zip"'
    
    return response

