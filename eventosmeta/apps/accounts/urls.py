from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('login/', views.login_staff, name='login_staff'),
    path('logout/', views.logout_staff, name='logout_staff'),
    path('dashboard/', views.dashboard_staff, name='dashboard_staff'),
]