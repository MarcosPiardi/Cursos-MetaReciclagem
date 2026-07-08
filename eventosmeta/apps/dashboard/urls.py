"""
Arquivo: urls.py
Caminho: apps/dashboard/urls.py
Descrição: Rotas do app dashboard para visualização e exportação dos painéis administrativos.
Histórico de Alterações:
 - 03/07/2026 - Criação do arquivo para concentrar as rotas do app dashboard
                e remover acoplamento excessivo do config/urls.py
"""

from django.urls import path

from . import views

app_name = 'dashboard'

urlpatterns = [
    path('academico/', views.dashboard_academico, name='academico'),
    path('academico/pdf/', views.dashboard_academico_pdf, name='academico_pdf'),

    path('eventos/', views.dashboard_eventos, name='eventos'),
    path('eventos/pdf/', views.dashboard_eventos_pdf, name='eventos_pdf'),

    path('interessados/', views.dashboard_interessados, name='interessados'),
    path('interessados/pdf/', views.dashboard_interessados_pdf, name='interessados_pdf'),

    path('processo-seletivo/', views.dashboard_processo_seletivo, name='processo_seletivo'),
    path('processo-seletivo/pdf/', views.dashboard_processo_seletivo_pdf, name='processo_seletivo_pdf'),

    path('lgpd/', views.dashboard_lgpd, name='lgpd'),
]



