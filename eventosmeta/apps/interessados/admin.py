
# interessados/admin.py
from django.contrib import admin
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
        'criado_em'
    ]
    
    # Filtros
    list_filter = [
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
    readonly_fields = ['criado_em', 'atualizado_em']
    
    # Organização do formulário
    fieldsets = (
        ('Dados Pessoais', {
            'fields': (
                'cpf',
                'nome',
                'sexo',
                'data_nascimento',
                'cidade_nascimento',
                'uf_nascimento',
                'nacionalidade',
                'fototipo'
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
        ('Necessidades Especiais', {
            'fields': (
                'necessidades_especiais',
                'fisica',
                'visual',
                'auditiva',
                'intelectual',
                'psicossocial',
                'multiplas'
            ),
            'classes': ('collapse',)
        }),
        ('Responsável', {
            'fields': (
                'nome_responsavel',
                'contato_responsavel',
                'telefone_responsavel',
                'celular_responsavel',
                'email_responsavel'
            ),
            'classes': ('collapse',)
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

