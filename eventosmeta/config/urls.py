"""
URL Configuration for Eventos MetaReciclagem
Arquivo: config/urls.py

Atualizações:
 - 20/01/2026 - Admin customizado com dashboard + estrutura completa
 - 03/02/2026 - Admin customizado + rotas de dashboard integradas
 - 05/02/2026 - Adicionadas rotas PDF para todos os dashboards
 - 20/02/2026 - Adicionadas rotas de recuperação de senha para Staff e Interessados
 - 24/02/2026 - Templates de recuperação de senha Staff renomeados com prefixo adm_
 - 25/02/2026 - Adicionadas rotas de troca obrigatória de senha (Fluxo B) para Staff e Interessados
 - 27/02/2026 - Desabilitado Sistema 3 (Portal login duplicado)
                Mantida apenas página inicial (/)
 - 29/05/2026 - Correção de rotas de dashboard (removido namespace admin: e ajustado nomes)
 - 03/07/2026 - Refatoração inicial: rotas do dashboard movidas para apps.dashboard.urls
              - Adicionada integração condicional com debug_toolbar em DEBUG
 - 08/07/2026 - REMOVIDO admin_site customizado (causava erro 500)
              - Usando admin.site padrão do Django
"""

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import include, path, reverse_lazy

from apps.accounts import views as accounts_views
# REMOVIDO: from apps.accounts.admin import admin_site
from apps.interessados import views as interessados_views

admin.site.site_title = 'MetaReciclagem Admin'
admin.site.site_header = 'MetaReciclagem - Administracao'
admin.site.index_title = 'Painel de Controle'

admin.site.index_template = 'admin/accounts/cards-admin.html'

sistema_urlpatterns = [
    # ==========================================
    # ADMIN CUSTOMIZADO
    # ==========================================
    path('admin/dashboard/', include('apps.dashboard.urls')),
    path('admin/', admin.site.urls),

    # ==========================================
    # SISTEMA 1: Staff/Administração
    # ==========================================
    path('staff/', include('apps.accounts.urls')),

    # ==========================================
    # RECUPERAÇÃO DE SENHA — STAFF
    # ==========================================
    path('staff/senha/', include([
        path(
            'recuperar/',
            auth_views.PasswordResetView.as_view(
                template_name='accounts/senha/adm_recuperar.html',
                email_template_name='accounts/senha/adm_email_recuperar.txt',
                html_email_template_name='accounts/senha/adm_email_recuperar.html',
                subject_template_name='accounts/senha/adm_email_assunto.txt',
                success_url=reverse_lazy('staff_senha_recuperar_enviado'),
            ),
            name='staff_senha_recuperar',
        ),
        path(
            'recuperar/enviado/',
            auth_views.PasswordResetDoneView.as_view(
                template_name='accounts/senha/adm_recuperar_enviado.html',
            ),
            name='staff_senha_recuperar_enviado',
        ),
        path(
            'redefinir/<uidb64>/<token>/',
            auth_views.PasswordResetConfirmView.as_view(
                template_name='accounts/senha/adm_redefinir.html',
                success_url=reverse_lazy('staff_senha_redefinir_concluido'),
            ),
            name='staff_senha_redefinir',
        ),
        path(
            'redefinir/concluido/',
            auth_views.PasswordResetCompleteView.as_view(
                template_name='accounts/senha/adm_redefinir_concluido.html',
            ),
            name='staff_senha_redefinir_concluido',
        ),
        path(
            'trocar-obrigatorio/',
            accounts_views.trocar_senha_obrigatorio_view,
            name='staff_trocar_senha_obrigatorio',
        ),
    ])),

    # ==========================================
    # SISTEMA 2: Público/Interessados
    # ==========================================
    path('inscricao/', include('apps.interessados.urls')),
    path(
        'inscricao/senha/trocar-obrigatorio/',
        interessados_views.trocar_senha_obrigatorio_view,
        name='interessados_trocar_senha_obrigatorio',
    ),

    # ==========================================
    # SISTEMA 4: Gestão Acadêmica
    # ==========================================
    path('academico/', include('apps.academico.urls')),
]

urlpatterns = [
    # ==========================================
    # PORTAL PÚBLICO
    # ==========================================
    path('', include('apps.portal.urls')),

    # ==========================================
    # SISTEMA INTERNO
    # ==========================================
    path('eventosmeta/', include(sistema_urlpatterns)),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

    