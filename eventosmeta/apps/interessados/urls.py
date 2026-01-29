"""
Arquivo: urls.py
Caminho: apps/interessados/urls.py
Alteração: Rota detalhes adicionada
Data: 29/01/2026
"""

from django.urls import path
from . import views

app_name = 'interessados'

urlpatterns = [
    path('cadastro/', views.cadastro_view, name='cadastro'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('meus-dados/', views.meus_dados_view, name='meus_dados'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('inscricao/<int:inscricao_id>/detalhes/', views.detalhes_view, name='detalhes'),
]
