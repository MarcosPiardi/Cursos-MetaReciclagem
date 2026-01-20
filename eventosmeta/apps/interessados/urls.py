# """
# ARQUIVO: apps/interessados/urls.py
# AÇÃO: CRIAR ou SUBSTITUIR o arquivo apps/interessados/urls.py
# MUDANÇA: URLs do app interessados
# """

# from django.urls import path
# from . import views

# app_name = 'interessados'

# urlpatterns = [
#     path('cadastro/', views.cadastro_interessado, name='cadastro'),
#     path('login/', views.login_interessado, name='login'),
#     path('logout/', views.logout_interessado, name='logout'),
#     path('dashboard/', views.dashboard_interessado, name='dashboard'),
# ]


"""
Arquivo: urls.py
Caminho: apps/interessados/urls.py
Alteração: Garantir que dashboard está configurada
Data: 19/01/2026
"""

from django.urls import path
from . import views

app_name = 'interessados'

urlpatterns = [
    path('cadastro/', views.cadastro, name='cadastro'),
    path('login/', views.login_interessado, name='login'),
    path('logout/', views.logout_interessado, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),  # ← Essa linha
    path('detalhes/<int:inscricao_id>/', views.detalhes_inscricao, name='detalhes'),
]