"""
Admin do app ACADÊMICO
Arquivo: apps/academico/admin.py
Alteração: Corrigido display da cor no StatusMatricula para exibir visualmente
Data: 11/12/2025
"""

from django.contrib import admin
from django.utils.html import format_html
from .models import StatusMatricula, Matricula, Avaliacao


@admin.register(StatusMatricula)
class StatusMatriculaAdmin(admin.ModelAdmin):
    list_display = ['nome', 'cor_display', 'ordem']
    search_fields = ['nome']
    ordering = ['ordem', 'nome']
    
    def cor_display(self, obj):
        """Exibe a cor visualmente com um quadrado colorido"""
        if obj.cor:
            return format_html(
                '<div style="display: flex; align-items: center; gap: 8px;">'
                '<span style="display: inline-block; width: 20px; height: 20px; '
                'background-color: {}; border: 1px solid #ccc; border-radius: 3px;"></span>'
                '<span>{}</span>'
                '</div>',
                obj.cor,
                obj.cor
            )
        return '—'
    cor_display.short_description = 'Cor'
    cor_display.admin_order_field = 'cor'


class AvaliacaoInline(admin.StackedInline):
    model = Avaliacao
    extra = 0
    can_delete = False
    fields = [
        ('nota_final', 'frequencia'),
        'aprovado',
        'observacoes',
        ('certificado_emitido', 'data_emissao_certificado')
    ]


@admin.register(Matricula)
class MatriculaAdmin(admin.ModelAdmin):
    list_display = ['interessado', 'turma', 'get_evento', 'status', 'data_matricula']
    list_filter = ['status', 'turma__evento', 'turma', 'data_matricula']
    search_fields = ['interessado__nome', 'interessado__cpf', 'turma__nome', 
                     'turma__evento__nome']
    date_hierarchy = 'data_matricula'
    ordering = ['-data_matricula']
    
    inlines = [AvaliacaoInline]
    
    fieldsets = (
        ('Dados da Matrícula', {
            'fields': ('turma', 'interessado', 'inscricao', 'status')
        }),
        ('Observações', {
            'fields': ('observacoes',)
        }),
        ('Auditoria', {
            'fields': ('data_matricula', 'data_atualizacao'),
            'classes': ('collapse',)
        }),
    )
    
    readonly_fields = ['data_matricula', 'data_atualizacao']
    
    def get_evento(self, obj):
        return obj.turma.evento.nome
    get_evento.short_description = 'Evento'
    get_evento.admin_order_field = 'turma__evento__nome'


@admin.register(Avaliacao)
class AvaliacaoAdmin(admin.ModelAdmin):
    list_display = ['get_interessado', 'get_turma', 'nota_final', 'frequencia', 
                    'aprovado', 'certificado_emitido']
    list_filter = ['aprovado', 'certificado_emitido', 'matricula__turma__evento']
    search_fields = ['matricula__interessado__nome', 'matricula__interessado__cpf', 
                     'matricula__turma__nome']
    ordering = ['-avaliado_em']
    
    fieldsets = (
        ('Matrícula', {
            'fields': ('matricula',)
        }),
        ('Desempenho', {
            'fields': ('nota_final', 'frequencia', 'aprovado')
        }),
        ('Observações', {
            'fields': ('observacoes',)
        }),
        ('Certificado', {
            'fields': ('certificado_emitido', 'data_emissao_certificado')
        }),
        ('Auditoria', {
            'fields': ('avaliado_em', 'atualizado_em'),
            'classes': ('collapse',)
        }),
    )
    
    readonly_fields = ['avaliado_em', 'atualizado_em']
    
    def get_interessado(self, obj):
        return obj.matricula.interessado.nome
    get_interessado.short_description = 'Aluno'
    get_interessado.admin_order_field = 'matricula__interessado__nome'
    
    def get_turma(self, obj):
        return obj.matricula.turma.nome
    get_turma.short_description = 'Turma'
    get_turma.admin_order_field = 'matricula__turma__nome'

    