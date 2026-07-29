"""
Arquivo: admin.py
Caminho: apps/accounts/admin.py
Atualização: 
 - 20/01/2026 - Criação do admin customizado com dashboard + UsuarioAdmin
 - 25/02/2026 - IMPORT CORRIGIDO
              - Adicionada ação 'Gerar Senha Provisória' para usuários Staff
              - Senha de 8 caracteres exibida uma única vez na tela
              - Campo must_change_password marcado como True automaticamente
 - 17/06/2026 - Corrigido naive datetime warning no dashboard_view
              - Substituído date.today() por timezone.now().date()
              - Adicionado lookup __date__gte para evitar warning
 - 08/07/2026 - REMOVIDO CustomAdminSite (causava erro 500)
              - Usando admin.site padrão do Django
              - Dashboard movido para app separado (apps.dashboard)
"""

import secrets
import string

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin, GroupAdmin
from django.contrib.auth.models import Group
from django.shortcuts import render, redirect
from django.contrib import messages
from django.utils.html import format_html
from django.utils import timezone

from .models import Usuario
from apps.admin_mixins import CustomTitleMixin


# ==========================================
# REMOVIDO: CustomAdminSite (linhas 27-54 do arquivo original)
# ==========================================
# class CustomAdminSite(admin.AdminSite):
#     site_header = 'MetaReciclagem - Administração'
#     site_title  = 'MetaReciclagem Admin'
#     index_title = 'Painel de Controle'
#
#     def get_urls(self):
#         urls = super().get_urls()
#         custom_urls = [
#             path('dashboard/', self.admin_view(self.dashboard_view), name='dashboard'),
#         ]
#         return custom_urls + urls
#
#     def dashboard_view(self, request):
#         """View personalizada de dashboard"""
#         total_eventos       = Evento.objects.count()
#         total_interessados  = Interessado.objects.count()
#         total_inscricoes    = Inscricao.objects.count()
#         eventos_abertos     = Evento.objects.filter(
#             data_fim_inscricao__date__gte=timezone.now().date()
#         ).count()
#
#         context = {
#             **self.each_context(request),
#             'title'              : 'Dashboard',
#             'total_eventos'      : total_eventos,
#             'total_interessados' : total_interessados,
#             'total_inscricoes'   : total_inscricoes,
#             'eventos_abertos'    : eventos_abertos,
#         }
#         return render(request, 'admin/dashboard.html', context)
#
# # Instância do admin customizado
# admin_site = CustomAdminSite(name='custom_admin')

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
        'must_change_password',
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

        alfabeto = string.ascii_letters + string.digits
        senha    = ''.join(secrets.choice(alfabeto) for _ in range(8))

        usuario.set_password(senha)
        usuario.must_change_password = True
        usuario.save()

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

admin.site.register(Usuario, UsuarioAdmin)

