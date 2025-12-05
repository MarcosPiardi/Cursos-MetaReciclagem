"""
Admin do app INTERESSADOS - Sistema MetaReciclagem
Arquivo: apps/interessados/admin.py
Alteração: Adicionar campos is_active, is_staff, is_superuser para autenticação completa
Data: 05/12/2025
"""

"""
Admin do app INTERESSADOS - Sistema MetaReciclagem
Arquivo: apps/interessados/admin.py
Alteração: Corrigir nomes dos campos de PCD (adicionar prefixo pcd_) e remover campo inexistente
Data: 04/12/2025
"""

from django.contrib import admin
from django.utils.html import format_html
from .models import Interessado, Sexo, Fototipo


@admin.register(Sexo)
class SexoAdmin(admin.ModelAdmin):
    """Administração de Sexo"""
    list_display = ['nome']
    search_fields = ['nome']


@admin.register(Fototipo)
class FototipoAdmin(admin.ModelAdmin):
    """Administração de Fototipo"""
    list_display = ['nome', 'descricao']
    search_fields = ['nome', 'descricao']


@admin.register(Interessado)
class InteressadoAdmin(admin.ModelAdmin):
    """Administração de Interessados"""
    
    # Listagem
    list_display = [
        'cpf',
        'nome',
        'data_nascimento',
        'cidade_residencia',
        'uf_residencia',
        'celular',
        'necessidades_especiais',
        'is_active_display',  # Adicionado em 05/12/2025
        'criado_em'
    ]
    
    # Filtros
    list_filter = [
        'is_active',  # Adicionado em 05/12/2025
        'sexo',
        'uf_residencia',
        'necessidades_especiais',
        'programa_social',
        'fototipo',
        'criado_em'
    ]
    
    # Busca
    search_fields = [
        'cpf',
        'nome',
        'email',
        'celular',
        'cidade_residencia',
        'bairro'
    ]
    
    # Campos somente leitura
    readonly_fields = ['criado_em', 'atualizado_em', 'last_login']
    
    # Organização do formulário
    fieldsets = (
        ('Dados Pessoais', {
            'fields': (
                'cpf',
                'nome',
                'rg',
                'sexo',
                'data_nascimento',
                'cidade_nascimento',
                'uf_nascimento',
                'nacionalidade',
                'fototipo',
                'escolaridade'
            )
        }),
        ('Endereço', {
            'fields': (
                'endereco_residencial',
                'num_endereco',
                'complemento',
                'bairro',
                'cidade_residencia',
                'uf_residencia'
            )
        }),
        ('Contatos', {
            'fields': (
                'telefone',
                'celular',
                'email'
            )
        }),
        ('Programa Social', {
            'fields': (
                'programa_social',
                'num_nis'
            ),
            'classes': ('collapse',)
        }),
        ('Necessidades Especiais / PCD', {
            'fields': (
                'necessidades_especiais',
                'pcd_fisica',
                'pcd_visual',
                'pcd_auditiva',
                'pcd_intelectual',
                'pcd_psicossocial',
                'pcd_multiplas'
            ),
            'classes': ('collapse',),
            'description': 'Marque as deficiências que o interessado possui'
        }),
        ('Responsável (Para menores de idade)', {
            'fields': (
                'nome_responsavel',
                'telefone_responsavel',
                'celular_responsavel',
                'email_responsavel'
            ),
            'classes': ('collapse',)
        }),
        ('🔐 Autenticação e Permissões', {
            'fields': (
                'senha',
                'last_login',
                'is_active',
                'is_staff',
                'is_superuser'
            ),
            'classes': ('collapse',),
            'description': (
                '<div style="background-color: #f8f9fa; padding: 15px; border-left: 4px solid #007bff; margin-bottom: 15px;">'
                '<strong>📋 CONTROLE DE ACESSO AO SISTEMA:</strong><br><br>'
                '<strong>🔑 Senha:</strong> Digite a senha do interessado (será criptografada automaticamente)<br>'
                '<strong>🕒 Último Login:</strong> Data/hora do último acesso (preenchido automaticamente)<br><br>'
                '<strong>✅ Ativo:</strong> Permite que o interessado faça login no sistema<br>'
                '&nbsp;&nbsp;&nbsp;&nbsp;• Marcado = Pode fazer login<br>'
                '&nbsp;&nbsp;&nbsp;&nbsp;• Desmarcado = Login bloqueado<br><br>'
                '<strong>👔 Membro da Equipe:</strong> Permite acesso ao painel administrativo<br>'
                '&nbsp;&nbsp;&nbsp;&nbsp;• Normalmente DESMARCADO para interessados comuns<br>'
                '&nbsp;&nbsp;&nbsp;&nbsp;• Marcar apenas para funcionários/colaboradores<br><br>'
                '<strong>⚡ Superusuário:</strong> Concede todas as permissões do sistema<br>'
                '&nbsp;&nbsp;&nbsp;&nbsp;• Normalmente DESMARCADO<br>'
                '&nbsp;&nbsp;&nbsp;&nbsp;• Marcar apenas para administradores do sistema<br>'
                '</div>'
            )
        }),
        ('Observações', {
            'fields': ('observacao',)
        }),
        ('Informações do Sistema', {
            'fields': ('criado_em', 'atualizado_em'),
            'classes': ('collapse',)
        })
    )
    
    # Ordenação
    ordering = ['nome']
    
    # Quantidade de itens por página
    list_per_page = 25
    
    # Actions
    actions = ['ativar_interessados', 'desativar_interessados']
    
    def is_active_display(self, obj):
        """
        Exibe o status ativo/inativo com ícone colorido
        Adicionado em 05/12/2025
        """
        if obj.is_active:
            return format_html(
                '<span style="color: green; font-weight: bold;">✅ Ativo</span>'
            )
        return format_html(
            '<span style="color: red; font-weight: bold;">❌ Inativo</span>'
        )
    is_active_display.short_description = 'Status'
    is_active_display.admin_order_field = 'is_active'
    
    def save_model(self, request, obj, form, change):
        """
        Sobrescreve o método save_model para garantir que a senha seja criptografada
        """
        if 'senha' in form.changed_data:
            # Se o campo senha foi alterado, criptografa
            obj.set_password(form.cleaned_data['senha'])
        super().save_model(request, obj, form, change)
    
    def ativar_interessados(self, request, queryset):
        """
        Action para ativar interessados selecionados
        Adicionado em 05/12/2025
        """
        count = queryset.update(is_active=True)
        self.message_user(
            request,
            f'✅ {count} interessado(s) ativado(s) com sucesso! Agora podem fazer login.'
        )
    ativar_interessados.short_description = '✅ Ativar interessados selecionados'
    
    def desativar_interessados(self, request, queryset):
        """
        Action para desativar interessados selecionados
        Adicionado em 05/12/2025
        """
        count = queryset.update(is_active=False)
        self.message_user(
            request,
            f'❌ {count} interessado(s) desativado(s)! Login bloqueado.',
            level='WARNING'
        )
    desativar_interessados.short_description = '❌ Desativar interessados selecionados'



