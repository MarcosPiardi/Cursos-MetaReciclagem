"""
Arquivo: urls.py
Caminho: apps/academico/urls.py
Descrição: URLs do módulo acadêmico
Data: 12/01/2026
"""

from django.urls import path
from . import views

app_name = 'academico'

urlpatterns = [
    path('gestao-matricula/', views.gestao_matricula, name='gestao_matricula'),
    path('gestao-matricula/processar/', views.processar_matricula, name='processar_matricula'),
    path('gestao-matricula/alterar-status/', views.alterar_status_inscricao, name='alterar_status_inscricao'),
]

