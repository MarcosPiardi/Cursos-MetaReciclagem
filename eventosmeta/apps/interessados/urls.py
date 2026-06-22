"""
Arquivo: urls.py
Caminho: apps/interessados/urls.py
Atualizações:
 - 29/01/2026 - Rota detalhes adicionada
 - 20/02/2026 - Adicionadas rotas de recuperação de senha por CPF
 - 15/03/2026 - Adicionadas rotas de exclusão de conta
 - 29/05/2026 - Revisão geral e organização das rotas
"""

from django.urls import path
from . import views
from . import views_exclusao

app_name = 'interessados'

urlpatterns = [
    path('cadastro/', views.cadastro_view, name='cadastro'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('meus-dados/', views.meus_dados_view, name='meus_dados'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('inscricao/<int:inscricao_id>/detalhes/', views.detalhes_view, name='detalhes'),
    path('inscrever/<int:evento_id>/', views.inscrever_evento_view, name='inscrever_evento'),

    # ==========================================
    # RECUPERAÇÃO DE SENHA — INTERESSADOS
    # Alteração: 20/02/2026
    # ==========================================
    path('senha/recuperar/', views.senha_recuperar_view, name='senha_recuperar'),
    path('senha/recuperar/enviado/', views.senha_recuperar_enviado_view, name='senha_recuperar_enviado'),
    # <- CONCLUIDO ANTES DE <str:token> para evitar conflito ->
    path('senha/redefinir/concluido/', views.senha_redefinir_concluido_view, name='senha_redefinir_concluido'),
    path('senha/redefinir/<str:token>/', views.senha_redefinir_view, name='senha_redefinir'),
    path('senha/sem-email/', views.senha_sem_email_view, name='senha_sem_email'),
    
    # Adicionar no urlpatterns
    path('exclusao/solicitar/', views_exclusao.solicitar_exclusao_view, name='solicitar_exclusao'),
    path('exclusao/solicitada/', views_exclusao.exclusao_solicitada_view, name='exclusao_solicitada'),
    path('senha/trocar-obrigatorio/', views.trocar_senha_obrigatorio_view, name='trocar_senha_obrigatorio'),
    


]


