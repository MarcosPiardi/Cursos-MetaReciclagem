"""
URL Configuration for Eventos MetaReciclagem
Arquivo: eventosmeta/config/urls.py
Alteração: Admin customizado com dashboard + estrutura completa
Data: 20/01/2026
Alteração: Admin customizado + rotas de dashboard integradas
Data: 03/02/2026
Alteração: Adicionadas rotas PDF para todos os dashboards
Data: 05/02/2026
Alteração: Adicionadas rotas de recuperação de senha para Staff e Interessados
Data: 20/02/2026
Alteração: Templates de recuperação de senha Staff renomeados com prefixo adm_
Data: 24/02/2026
"""

from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

from apps.accounts.admin import admin_site
from dashboard import views as dashboard_views

urlpatterns = [

    # ==========================================
    # DASHBOARDS CUSTOMIZADOS
    # ==========================================
    path('admin/dashboard/', include([
        path('academico/',
             dashboard_views.dashboard_academico,
             name='dashboard_academico'),
        path('academico/pdf/',
             dashboard_views.dashboard_academico_pdf,
             name='dashboard_academico_pdf'),
        path('eventos/',
             dashboard_views.dashboard_eventos,
             name='dashboard_eventos'),
        path('eventos/pdf/',
             dashboard_views.dashboard_eventos_pdf,
             name='dashboard_eventos_pdf'),
        path('interessados/',
             dashboard_views.dashboard_interessados,
             name='dashboard_interessados'),
        path('interessados/pdf/',
             dashboard_views.dashboard_interessados_pdf,
             name='dashboard_interessados_pdf'),
        path('processo-seletivo/',
             dashboard_views.dashboard_processo_seletivo,
             name='dashboard_processo_seletivo'),
        path('processo-seletivo/pdf/',
             dashboard_views.dashboard_processo_seletivo_pdf,
             name='dashboard_processo_seletivo_pdf'),
    ])),

    # ==========================================
    # DJANGO ADMIN CUSTOMIZADO
    # ==========================================
    path('admin/', admin_site.urls),

    # ==========================================
    # SISTEMA 1: Staff/Administração
    # ==========================================
    path('staff/', include('apps.accounts.urls')),

    # ==========================================
    # RECUPERAÇÃO DE SENHA — STAFF
    # Templates com prefixo adm_ em accounts/senha/
    # Alteração: 20/02/2026
    # Alteração: Nomes corrigidos para prefixo adm_
    # Data: 24/02/2026
    # ==========================================
    path('staff/senha/', include([

        # Passo 1: Formulário — informa o e-mail
        path(
            'recuperar/',
            auth_views.PasswordResetView.as_view(
                template_name='accounts/senha/adm_recuperar.html',
                email_template_name='accounts/senha/adm_email_recuperar.txt',
                html_email_template_name='accounts/senha/adm_email_recuperar.html',
                subject_template_name='accounts/senha/adm_email_assunto.txt',
                success_url='/staff/senha/recuperar/enviado/',
            ),
            name='staff_senha_recuperar',
        ),

        # Passo 2: Confirmação de envio
        path(
            'recuperar/enviado/',
            auth_views.PasswordResetDoneView.as_view(
                template_name='accounts/senha/adm_recuperar_enviado.html',
            ),
            name='staff_senha_recuperar_enviado',
        ),

        # Passo 3: Formulário de nova senha (link do e-mail)
        path(
            'redefinir/<uidb64>/<token>/',
            auth_views.PasswordResetConfirmView.as_view(
                template_name='accounts/senha/adm_redefinir.html',
                success_url='/staff/senha/redefinir/concluido/',
            ),
            name='staff_senha_redefinir',
        ),

        # Passo 4: Senha redefinida com sucesso
        path(
            'redefinir/concluido/',
            auth_views.PasswordResetCompleteView.as_view(
                template_name='accounts/senha/adm_redefinir_concluido.html',
            ),
            name='staff_senha_redefinir_concluido',
        ),

    ])),

    # ==========================================
    # SISTEMA 2: Público/Interessados
    # ==========================================
    path('inscricao/', include('apps.interessados.urls')),

    # ==========================================
    # SISTEMA 3: Portal Público
    # ==========================================
    path('', include('apps.portal.urls')),

    # ==========================================
    # SISTEMA 4: Gestão Acadêmica
    # ==========================================
    path('academico/', include('apps.academico.urls')),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,  document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

    