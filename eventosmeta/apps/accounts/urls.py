"""
Arquivo: urls.py
Caminho: apps/accounts/urls.py
Alteração: Login staff redireciona para admin
Data: 20/01/2026
Alteração: Removidas rotas de recuperação de senha — já definidas em config/urls.py
Data: 24/02/2026
"""
from django.urls import path
from . import views

# Importar no topo
from . import views_exclusao

app_name = 'accounts'

urlpatterns = [
    path('login/',  views.login_staff,  name='login_staff'),
    path('logout/', views.logout_staff, name='logout_staff'),
    path('exclusao/', views_exclusao.listar_solicitacoes_view, name='listar_solicitacoes_exclusao'),
    path('exclusao/<int:solicitacao_id>/', views_exclusao.detalhe_solicitacao_view, name='detalhe_solicitacao_exclusao'),
]

"""
Arquivo: urls.py
Caminho: apps/accounts/urls.py
Alteração: Login staff redireciona para admin
Data: 20/01/2026
Alteração: Removidas rotas de recuperação de senha — já definidas em config/urls.py
Data: 24/02/2026
Alteração: Padronizado parâmetro para solicitacao_id em todas as rotas de exclusão
Data: 14/07/2026
"""
from django.urls import path
from . import views
from . import views_exclusao

app_name = 'accounts'

urlpatterns = [
    path('login/',  views.login_staff,  name='login_staff'),
    path('logout/', views.logout_staff, name='logout_staff'),
    path('exclusao/', views_exclusao.listar_solicitacoes_view, name='listar_solicitacoes_exclusao'),
    path('exclusao/<int:solicitacao_id>/', views_exclusao.detalhe_solicitacao_view, name='detalhe_solicitacao_exclusao'),
]