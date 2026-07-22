"""
Arquivo: urls.py
Caminho: apps/accounts/urls.py
Finalidade: Rotas para views de login/logout do staff e views de exclusão de dados (LGPD)
Atualizações:
 - 20/01/2026 - Login staff redireciona para admin
 - 24/02/2026 - Removidas rotas de recuperação de senha — já definidas em config/urls.py
 - 14/07/2026 - Padronizado parâmetro para solicitacao_id em todas as rotas de exclusão
"""
from django.urls import path
from . import views
from . import views_exclusao

app_name = 'accounts'

urlpatterns = [
    path('login/',  views.login_staff,  name='login_staff'),
    path('logout/', views.logout_staff, name='logout_staff'),
    path('exclusao/<int:solicitacao_id>/', views_exclusao.detalhe_solicitacao_view, name='detalhe_solicitacao_exclusao'),
]