"""
Views do app DASHBOARD
Arquivo: dashboard/views.py
Finalidade: Views customizadas para dashboards
Atualizações:
 - 03/02/2026 - Criação do arquivo - Implementação inicial das views
 - 05/02/2026 - Alteração para incluir geração de PDF
              - Views customizadas para dashboards com geração de PDF
 - 10/02/2026 - Correções de imports
 - 10/06/2026 - Refatoração para usar services
 - 13/07/2026 - CORRIGIDO: Removido import de admin_site customizado
              - Usando admin.site padrão do Django
"""

from django.shortcuts import render
from django.contrib import admin
from django.contrib.admin.views.decorators import staff_member_required
from django.http import HttpResponse
from datetime import datetime
from .services import (
    DashboardInteressadosService,
    DashboardEventosService,
    DashboardAcademicoService,
    DashboardProcessoSeletivoService,
)
from .utils_pdf import (
    gerar_pdf_interessados,
    gerar_pdf_eventos,
    gerar_pdf_academico,
    gerar_pdf_processo_seletivo,
)

@staff_member_required
def dashboard_academico(request):
    """Dashboard de Informações Acadêmicas"""
    context = DashboardAcademicoService.obter_contexto_completo()
    context.update({
        'title': 'Dashboard - Informações Acadêmicas',
        'site_title': admin.site.site_title,
        'site_header': admin.site.site_header,
    })
    
    return render(request, 'admin/dashboard/academico.html', context)

@staff_member_required
def dashboard_eventos(request):
    """Dashboard de Eventos e Cursos"""
    context = DashboardEventosService.obter_contexto_completo()
    context.update({
        'title': 'Dashboard - Eventos/Cursos e Turmas',
        'site_title': admin.site.site_title,
        'site_header': admin.site.site_header,
    })
    
    return render(request, 'admin/dashboard/eventos.html', context)

@staff_member_required
def dashboard_interessados(request):
    """Dashboard de Interessados com dados demográficos detalhados"""
    context = DashboardInteressadosService.obter_contexto_completo()
    context.update({
        'title': 'Dashboard - Interessados',
        'site_title': admin.site.site_title,
        'site_header': admin.site.site_header,
    })
    
    return render(request, 'admin/dashboard/interessados.html', context)

@staff_member_required
def dashboard_processo_seletivo(request):
    """Dashboard de Processo Seletivo (Inscrições e Classificações)"""
    context = DashboardProcessoSeletivoService.obter_contexto_completo()
    context.update({
        'title': 'Dashboard - Processo Seletivo',
        'site_title': admin.site.site_title,
        'site_header': admin.site.site_header,
    })
    
    return render(request, 'admin/dashboard/processo_seletivo.html', context)

@staff_member_required
def dashboard_lgpd(request):
    """Dashboard de Solicitações de Exclusão — LGPD"""
    from apps.interessados.models import SolicitacaoExclusao

    pendentes = SolicitacaoExclusao.objects.filter(status='PENDENTE').order_by('-solicitado_em')
    aprovadas = SolicitacaoExclusao.objects.filter(status='APROVADA').order_by('-analisado_em')
    recusadas = SolicitacaoExclusao.objects.filter(status='RECUSADA').order_by('-analisado_em')

    context = {
        'title': 'Dashboard - LGPD / Exclusões',
        'site_title': admin.site.site_title,
        'site_header': admin.site.site_header,
        'pendentes': pendentes,
        'aprovadas': aprovadas,
        'recusadas': recusadas,
        'total_pendentes': pendentes.count(),
        'total_aprovadas': aprovadas.count(),
        'total_recusadas': recusadas.count(),
        'total_solicitacoes': SolicitacaoExclusao.objects.count(),
    }

    return render(request, 'admin/dashboard/lgpd.html', context)

@staff_member_required
def dashboard_geral(request):
    """Renderiza o dashboard administrativo com dados agregados de todos os services."""
    contexto_interessados = DashboardInteressadosService.calcular_metricas_gerais()
    contexto_eventos = DashboardEventosService.calcular_metricas_gerais()
    contexto_academico = DashboardAcademicoService.obter_contexto_completo()
    contexto_seletivo = DashboardProcessoSeletivoService.calcular_metricas_inscricoes()

    # Junta todos os contextos e ajusta o nome da variavel para o template
    contexto = {
        **contexto_interessados,
        **contexto_eventos,
        **contexto_academico,
        **contexto_seletivo,
        # O template HTML usa 'eventos_abertos', mas o service retorna 'eventos_inscricoes_abertas'
        'eventos_abertos': contexto_eventos.get('eventos_inscricoes_abertas', 0),
    }

    return render(request, 'admin/dashgeral.html', contexto)


# @staff_member_required
# def dashboard_geral(request):
#     """Dashboard geral com informações resumidas"""
#     context = DashboardGeralService.obter_contexto_completo()
#     context.update({
#         'title': 'Dashboard - Geral',
#         'site_title': admin.site.site_title,
#         'site_header': admin.site.site_header,
#     })
    
#     return render(request, 'admin/dashboard/interessados.html', context)


# ==========================================
# VIEWS PDF
# ==========================================

@staff_member_required
def dashboard_interessados_pdf(request):
    """Gera PDF do dashboard de interessados"""
    context = DashboardInteressadosService.obter_contexto_completo()
    pdf_buffer = gerar_pdf_interessados(context)
    
    response = HttpResponse(pdf_buffer, content_type='application/pdf')
    filename = f'dashboard_interessados_{datetime.now().strftime("%Y%m%d_%H%M%S")}.pdf'
    response['Content-Disposition'] = f'attachment; filename="{filename}"'
    
    return response

@staff_member_required
def dashboard_eventos_pdf(request):
    """Gera PDF do dashboard de eventos"""
    context = DashboardEventosService.obter_contexto_completo()
    pdf_buffer = gerar_pdf_eventos(context)
    
    response = HttpResponse(pdf_buffer, content_type='application/pdf')
    filename = f'dashboard_eventos_{datetime.now().strftime("%Y%m%d_%H%M%S")}.pdf'
    response['Content-Disposition'] = f'attachment; filename="{filename}"'
    
    return response

@staff_member_required
def dashboard_academico_pdf(request):
    """Gera PDF do dashboard acadêmico"""
    context = DashboardAcademicoService.obter_contexto_completo()
    pdf_buffer = gerar_pdf_academico(context)
    
    response = HttpResponse(pdf_buffer, content_type='application/pdf')
    filename = f'dashboard_academico_{datetime.now().strftime("%Y%m%d_%H%M%S")}.pdf'
    response['Content-Disposition'] = f'attachment; filename="{filename}"'
    
    return response

@staff_member_required
def dashboard_processo_seletivo_pdf(request):
    """Gera PDF do dashboard de processo seletivo"""
    context = DashboardProcessoSeletivoService.obter_contexto_completo()
    pdf_buffer = gerar_pdf_processo_seletivo(context)
    
    response = HttpResponse(pdf_buffer, content_type='application/pdf')
    filename = f'dashboard_processo_seletivo_{datetime.now().strftime("%Y%m%d_%H%M%S")}.pdf'
    response['Content-Disposition'] = f'attachment; filename="{filename}"'
    
    return response

