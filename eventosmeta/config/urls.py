"""
URL Configuration for Eventos MetaReciclagem
Arquivo: eventosmeta/config/urls.py
Alteração: Admin customizado com dashboard + estrutura completa
Data: 20/01/2026

Alteração: Admin customizado + rotas de dashboard integradas
Data: 03/02/2026

Alteração: Adicionadas rotas PDF para todos os dashboards
Data: 05/02/2026
"""

from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static

# Admin customizado
from apps.accounts.admin import admin_site

# Importar views de dashboard
from dashboard import views as dashboard_views

urlpatterns = [
    # ==========================================
    # DASHBOARDS CUSTOMIZADOS
    # Adicionado em 03/02/2026
    # Atualizado em 05/02/2026: Adicionadas rotas PDF
    # ==========================================
    path('admin/dashboard/', include([
        # Dashboard Acadêmico
        path('academico/', dashboard_views.dashboard_academico, name='dashboard_academico'),
        path('academico/pdf/', dashboard_views.dashboard_academico_pdf, name='dashboard_academico_pdf'),
        
        # Dashboard Eventos
        path('eventos/', dashboard_views.dashboard_eventos, name='dashboard_eventos'),
        path('eventos/pdf/', dashboard_views.dashboard_eventos_pdf, name='dashboard_eventos_pdf'),
        
        # Dashboard Interessados
        path('interessados/', dashboard_views.dashboard_interessados, name='dashboard_interessados'),
        path('interessados/pdf/', dashboard_views.dashboard_interessados_pdf, name='dashboard_interessados_pdf'),
        
        # Dashboard Processo Seletivo
        path('processo-seletivo/', dashboard_views.dashboard_processo_seletivo, name='dashboard_processo_seletivo'),
        path('processo-seletivo/pdf/', dashboard_views.dashboard_processo_seletivo_pdf, name='dashboard_processo_seletivo_pdf'),
    ])),
    
    # ==========================================
    # DJANGO ADMIN CUSTOMIZADO
    # Alterado em 20/01/2026: admin.site.urls → admin_site.urls
    # ==========================================
    path('admin/', admin_site.urls),
    
    # ==========================================
    # SISTEMA 1: Staff/Administração (Usuario)
    # ==========================================
    path('staff/', include('apps.accounts.urls')),
    
    # ==========================================
    # SISTEMA 2: Público/Interessados (Interessado)
    # ==========================================
    path('inscricao/', include('apps.interessados.urls')),
    
    # ==========================================
    # SISTEMA 3: Portal Público (Dashboard e Consultas)
    # ==========================================
    path('', include('apps.portal.urls')),

    # ==========================================
    # SISTEMA 4: Gestão Acadêmica (Matrículas)
    # Adicionado em 12/01/2026
    # ==========================================
    path('academico/', include('apps.academico.urls')),
    
    # ==========================================
    # SISTEMA 5: Cursos/Eventos (visualização pública)
    # TODO: Descomentar na ETAPA 2 quando criar os models de Curso
    # ==========================================
    # path('cursos/', include('apps.cursoseoutros.urls')),
]

# ==========================================
# SERVIR ARQUIVOS ESTÁTICOS/MEDIA EM DEV
# ==========================================
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

    