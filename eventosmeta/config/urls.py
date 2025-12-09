"""
URL Configuration for Eventos MetaReciclagem
Arquivo: eventosmeta/config/urls.py
Alteração: Corrigir duplicação de namespace portal
Data: 05/12/2025
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Django Admin (superusuário)
    path('admin/', admin.site.urls),
    
    # SISTEMA 1: Staff/Administração (Usuario)
    path('staff/', include('apps.accounts.urls')),
    
    # SISTEMA 2: Público/Interessados (Interessado)
    path('inscricao/', include('apps.interessados.urls')),
    
    # SISTEMA 3: Portal Público (Dashboard e Consultas)
    path('', include('apps.portal.urls')),  # ← APENAS UMA VEZ, na raiz
    
    # SISTEMA 4: Cursos/Eventos (visualização pública)
    # TODO: Descomentar na ETAPA 2 quando criar os models de Curso
    # path('cursos/', include('apps.cursoseoutros.urls')),
]

# Servir arquivos de media em desenvolvimento
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)