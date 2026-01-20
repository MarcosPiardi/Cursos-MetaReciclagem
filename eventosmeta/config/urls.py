"""
URL Configuration for Eventos MetaReciclagem
Arquivo: eventosmeta/config/urls.py
Alteração: Admin customizado com dashboard + estrutura completa
Data: 20/01/2026
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static

# ✅ NOVO: Importar admin customizado
from apps.accounts.admin import admin_site

urlpatterns = [
    # Django Admin Customizado (com Dashboard)
    # Alterado em 20/01/2026: admin.site.urls → admin_site.urls
    path('admin/', admin_site.urls),
    
    # SISTEMA 1: Staff/Administração (Usuario)
    path('staff/', include('apps.accounts.urls')),
    
    # SISTEMA 2: Público/Interessados (Interessado)
    path('inscricao/', include('apps.interessados.urls')),
    
    # SISTEMA 3: Portal Público (Dashboard e Consultas)
    path('', include('apps.portal.urls')),

    # SISTEMA 4: Gestão Acadêmica (Matrículas)
    # Adicionado em 12/01/2026
    path('academico/', include('apps.academico.urls')),
    
    # SISTEMA 5: Cursos/Eventos (visualização pública)
    # TODO: Descomentar na ETAPA 2 quando criar os models de Curso
    # path('cursos/', include('apps.cursoseoutros.urls')),
]

# Servir arquivos de media em desenvolvimento
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
