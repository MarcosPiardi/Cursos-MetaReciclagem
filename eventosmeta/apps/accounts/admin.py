from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import Usuario


@admin.register(Usuario)
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
            'classes': ('collapse',),  # Deixa essa seção recolhível
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