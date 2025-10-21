"""
URL Configuration for Eventos MetaReciclagem
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Django Admin (superusuário)
    path('admin/', admin.site.urls),
    
    # Página inicial
    path('', TemplateView.as_view(template_name='index.html'), name='home'),
    
    # SISTEMA 1: Staff/Administração (Usuario)
    path('staff/', include('apps.accounts.urls')),
    
    # SISTEMA 2: Público/Interessados (Interessado)
    path('inscricao/', include('apps.interessados.urls')),
    
    # SISTEMA 3: Cursos/Eventos (visualização pública)
    # TODO: Descomentar na ETAPA 2 quando criar os models de Curso
    # path('cursos/', include('apps.cursoseoutros.urls')),
]

# Servir arquivos de media em desenvolvimento
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)