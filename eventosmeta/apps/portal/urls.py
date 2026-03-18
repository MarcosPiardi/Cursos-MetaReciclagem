"""
URLs do app PORTAL - Sistema MetaReciclagem
Arquivo: apps/portal/urls.py
Data: 29/01/2026
"""

"""
URLs do app PORTAL - Sistema MetaReciclagem
Arquivo: apps/portal/urls.py
Data: 05/12/2025
"""

from django.urls import path
from . import views

app_name = 'portal'

urlpatterns = [
    # Página inicial
    path('', views.index, name='index'),
    
    # Autenticação
    path('login/', views.login_interessado, name='login'),
    path('logout/', views.logout_interessado, name='logout'),
    
    # Dashboard do interessado
    path('dashboard/', views.dashboard, name='dashboard'),
    
    # Consulta pública
    path('consulta/', views.consulta_publica, name='consulta_publica'),
    path('resultado/<int:evento_id>/', views.resultado_evento, name='resultado_evento'),
    
    # Detalhes do evento
    path('evento/<int:evento_id>/', views.detalhes_evento, name='detalhes_evento'),

     # Página de contato
    path('contato/', views.contato, name='contato'),

    # Política de privacidade
    path('privacidade/', views.politica_privacidade, name='politica_privacidade'),
]