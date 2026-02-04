"""
Arquivo: admin.py
Caminho: apps/accounts/admin.py
Alteração: Admin customizado com dashboard + UsuarioAdmin - IMPORT CORRIGIDO
Data: 20/01/2026
"""

from datetime import date
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.urls import path
from django.shortcuts import render

from .models import Usuario
from apps.eventos.models import Evento
from apps.interessados.models import Interessado
from apps.selecao.models import Inscricao


# ==========================================
# ADMIN SITE CUSTOMIZADO COM DASHBOARD
# ==========================================

class CustomAdminSite(admin.AdminSite):
    site_header = 'MetaReciclagem - Administração'
    site_title = 'MetaReciclagem Admin'
    index_title = 'Painel de Controle'
    
    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('dashboard/', self.admin_view(self.dashboard_view), name='dashboard'),
        ]
        return custom_urls + urls
    
    def dashboard_view(self, request):
        """View personalizada de dashboard"""
        
        # Estatísticas
        total_eventos = Evento.objects.count()
        total_interessados = Interessado.objects.count()
        total_inscricoes = Inscricao.objects.count()
        
        eventos_abertos = Evento.objects.filter(
            data_fim_inscricao__gte=date.today()
        ).count()
        
        context = {
            **self.each_context(request),
            'title': 'Dashboard',
            'total_eventos': total_eventos,
            'total_interessados': total_interessados,
            'total_inscricoes': total_inscricoes,
            'eventos_abertos': eventos_abertos,
        }
        
        return render(request, 'admin/dashboard.html', context)


# Criar instância do admin customizado
admin_site = CustomAdminSite(name='custom_admin')


# ==========================================
# CONFIGURAÇÃO DO USUARIO ADMIN
# ==========================================

class UsuarioAdmin(BaseUserAdmin):
    """
    Configuração do admin para o modelo Usuario customizado.
    Herda todas as funcionalidades do UserAdmin padrão do Django
    e adiciona os campos customizados.
    """
    
    # Campos exibidos na listagem
    list_display = ['username', 'email', 'first_name', 'last_name', 'cpf', 'setor_trabalho', 'is_staff', 'is_active']
    list_filter = ['is_staff', 'is_superuser', 'is_active', 'setor_trabalho', 'local_trabalho']
    search_fields = ['username', 'email', 'first_name', 'last_name', 'cpf']
    
    # Organização dos campos no formulário de edição
    fieldsets = (
        (None, {
            'fields': ('username', 'password')
        }),
        ('Informações Pessoais', {
            'fields': ('first_name', 'last_name', 'email', 'cpf')
        }),
        ('Informações de Trabalho', {
            'fields': ('setor_trabalho', 'local_trabalho')
        }),
        ('Contatos', {
            'fields': ('telefone', 'celular')
        }),
        ('Permissões', {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
            'classes': ('collapse',),
        }),
        ('Datas Importantes', {
            'fields': ('last_login', 'date_joined'),
            'classes': ('collapse',),
        }),
    )
    
    # Campos exibidos no formulário de criação de novo usuário
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'cpf', 'password1', 'password2'),
        }),
        ('Informações Adicionais', {
            'classes': ('wide',),
            'fields': ('first_name', 'last_name', 'setor_trabalho', 'local_trabalho', 'telefone', 'celular'),
        }),
        ('Permissões', {
            'classes': ('wide',),
            'fields': ('is_staff', 'is_superuser'),
        }),
    )
    
    ordering = ['username']


# Registrar Usuario no admin customizado
admin_site.register(Usuario, UsuarioAdmin)


# No final do arquivo, ADICIONAR:

from django.urls import reverse
from django.utils.html import format_html

class DashboardMenuAdmin(admin.ModelAdmin):
    """Classe para adicionar item Dashboard no menu"""
    
    def has_module_permission(self, request):
        return True

# Registrar para aparecer no menu
admin_site.register([], DashboardMenuAdmin)


