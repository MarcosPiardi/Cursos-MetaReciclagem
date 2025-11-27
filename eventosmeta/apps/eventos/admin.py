

"""
Admin do app EVENTOS
"""
from django.contrib import admin
from .models import Status, Criterio, Evento, EventoCriterio, Turma


@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = ['nome', 'ordem', 'ativo']
    list_filter = ['ativo']
    search_fields = ['nome']
    ordering = ['ordem', 'nome']


@admin.register(Criterio)
class CriterioAdmin(admin.ModelAdmin):
    list_display = ['nome', 'tipo', 'pontos', 'ativo', 'requer_validacao_manual']
    list_filter = ['tipo', 'ativo', 'requer_validacao_manual']
    search_fields = ['nome']
    ordering = ['nome']
    
    fieldsets = (
        ('Informações Básicas', {
            'fields': ('nome', 'tipo', 'descricao')
        }),
        ('Pontuação', {
            'fields': ('pontos', 'ordem_idade')
        }),
        ('Controle', {
            'fields': ('requer_validacao_manual', 'ativo')
        }),
    )


class EventoCriterioInline(admin.TabularInline):
    model = EventoCriterio
    extra = 1
    fields = ['criterio', 'pontos_customizados', 'reserva_vagas', 'ordem']


class TurmaInline(admin.TabularInline):
    model = Turma
    extra = 1
    fields = ['nome', 'turno', 'capacidade', 'local', 'data_inicio', 'data_fim']


@admin.register(Evento)
class EventoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'status', 'data_inicio_inscricao', 'data_fim_inscricao', 
                    'total_vagas', 'vagas_disponiveis']
    list_filter = ['status', 'data_inicio_evento']
    search_fields = ['nome', 'descricao']
    date_hierarchy = 'data_inicio_inscricao'
    ordering = ['-data_inicio_inscricao']
    
    inlines = [EventoCriterioInline, TurmaInline]
    
    fieldsets = (
        ('Informações Básicas', {
            'fields': ('nome', 'descricao', 'status')
        }),
        ('Período de Inscrições', {
            'fields': ('data_inicio_inscricao', 'data_fim_inscricao')
        }),
        ('Período do Evento', {
            'fields': ('data_inicio_evento', 'data_fim_evento')
        }),
        ('Vagas', {
            'fields': ('total_vagas', 'vagas_disponiveis'),
            'description': 'Vagas disponíveis é calculado automaticamente'
        }),
    )
    
    readonly_fields = ['vagas_disponiveis']


@admin.register(Turma)
class TurmaAdmin(admin.ModelAdmin):
    list_display = ['nome', 'evento', 'turno', 'capacidade', 'data_inicio', 'data_fim']
    list_filter = ['turno', 'evento']
    search_fields = ['nome', 'evento__nome']
    date_hierarchy = 'data_inicio'
    ordering = ['evento', 'nome']

    