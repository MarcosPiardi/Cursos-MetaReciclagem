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

app_name = 'accounts'

urlpatterns = [
    path('login/',  views.login_staff,  name='login_staff'),
    path('logout/', views.logout_staff, name='logout_staff'),
]

