"""
ARQUIVO: apps/interessados/urls.py
AÇÃO: CRIAR ou SUBSTITUIR o arquivo apps/interessados/urls.py
MUDANÇA: URLs do app interessados
"""

from django.urls import path
from . import views

app_name = 'interessados'

urlpatterns = [
    path('cadastro/', views.cadastro_interessado, name='cadastro'),
    path('login/', views.login_interessado, name='login'),
    path('logout/', views.logout_interessado, name='logout'),
    path('dashboard/', views.dashboard_interessado, name='dashboard'),
]