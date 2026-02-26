"""
Arquivo: admin.py
Caminho: apps/accounts/admin.py
Alteração: Admin customizado com dashboard + UsuarioAdmin - IMPORT CORRIGIDO
Data: 20/01/2026
Alteração: Adicionada ação 'Gerar Senha Provisória' para usuários Staff
           Senha de 8 caracteres exibida uma única vez na tela
           Campo must_change_password marcado como True automaticamente
Data: 25/02/2026
"""

import secrets
import string
from datetime import date

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin, GroupAdmin
from django.contrib.auth.models import Group
from django.urls import path, reverse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.utils.html import format_html

from .models import Usuario
from apps.eventos.models import Evento
from apps.interessados.models import Interessado
from apps.selecao.models import Inscricao


# ==========================================
# ADMIN SITE CUSTOMIZADO COM DASHBOARD
# ==========================================

class CustomAdminSite(admin.AdminSite):
    site_header = 'MetaReciclagem - Administração'
    site_title  = 'MetaReciclagem Admin'
    index_title = 'Painel de Controle'

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('dashboard/', self.admin_view(self.dashboard_view), name='dashboard'),
        ]
        return custom_urls + urls

    def dashboard_view(self, request):
        """View personalizada de dashboard"""
        total_eventos       = Evento.objects.count()
        total_interessados  = Interessado.objects.count()
        total_inscricoes    = Inscricao.objects.count()
        eventos_abertos     = Evento.objects.filter(
            data_fim_inscricao__gte=date.today()
        ).count()

        context = {
            **self.each_context(request),
            'title'              : 'Dashboard',
            'total_eventos'      : total_eventos,
            'total_interessados' : total_interessados,
            'total_inscricoes'   : total_inscricoes,
            'eventos_abertos'    : eventos_abertos,
        }
        return render(request, 'admin/dashboard.html', context)


# Instância do admin customizado
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

    list_display  = [
        'username', 'email', 'first_name', 'last_name',
        'cpf', 'setor_trabalho', 'is_staff', 'is_active',
        'must_change_password',                             # ← adicionado 25/02/2026
    ]
    list_filter   = ['is_staff', 'is_superuser', 'is_active', 'must_change_password',
                     'setor_trabalho', 'local_trabalho']
    search_fields = ['username', 'email', 'first_name', 'last_name', 'cpf']

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
        # ── Adicionado: 25/02/2026 ──
        ('Senha Provisória', {
            'fields': ('must_change_password',),
            'classes': ('collapse',),
            'description': 'Use a ação "Gerar Senha Provisória" na listagem para gerar '
                           'uma senha aleatória e marcar este campo automaticamente.',
        }),
        ('Datas Importantes', {
            'fields': ('last_login', 'date_joined'),
            'classes': ('collapse',),
        }),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'cpf', 'password1', 'password2'),
        }),
        ('Informações Adicionais', {
            'classes': ('wide',),
            'fields': ('first_name', 'last_name', 'setor_trabalho', 'local_trabalho',
                       'telefone', 'celular'),
        }),
        ('Permissões', {
            'classes': ('wide',),
            'fields': ('is_staff', 'is_superuser'),
        }),
    )

    ordering = ['username']

    # ============================================================
    # AÇÃO: GERAR SENHA PROVISÓRIA — STAFF
    # Adicionado: 25/02/2026
    # Gera senha aleatória de 8 caracteres, exibe UMA VEZ na tela,
    # e marca must_change_password = True no usuário selecionado.
    # Uso: selecionar 1 usuário na listagem → escolher a ação
    # ============================================================
    actions = ['gerar_senha_provisoria']

    @admin.action(description='🔑 Gerar Senha Provisória')
    def gerar_senha_provisoria(self, request, queryset):
        if queryset.count() != 1:
            self.message_user(
                request,
                '⚠️ Selecione exatamente 1 usuário para gerar a senha provisória.',
                level=messages.WARNING,
            )
            return

        usuario = queryset.first()

        # Gera senha com letras maiúsculas, minúsculas e dígitos
        alfabeto = string.ascii_letters + string.digits
        senha    = ''.join(secrets.choice(alfabeto) for _ in range(8))

        # Aplica a senha e marca troca obrigatória
        usuario.set_password(senha)
        usuario.must_change_password = True
        usuario.save()

        # Exibe a senha UMA ÚNICA VEZ no topo da página
        self.message_user(
            request,
            format_html(
                '<strong>✅ Senha provisória gerada para {}:</strong> '
                '<code style="font-size:1.2em; background:#f0f0f0; padding:4px 10px;">{}</code>'
                ' — Anote e entregue presencialmente. Esta senha não será exibida novamente.',
                usuario.username,
                senha,
            ),
            level=messages.SUCCESS,
        )


# Registrar Usuario no admin customizado
admin_site.register(Usuario, UsuarioAdmin)


# ==========================================
# REGISTRAR GRUPOS (GROUP) NO ADMIN CUSTOMIZADO
# ==========================================
admin_site.register(Group, GroupAdmin)

