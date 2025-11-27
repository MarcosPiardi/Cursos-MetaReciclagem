


"""
Admin do app SELEÇÃO
"""
from django.contrib import admin
from .models import StatusInscricao, Inscricao, Classificacao, InscricaoCriterioAtendido


@admin.register(StatusInscricao)
class StatusInscricaoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'cor', 'ordem']
    search_fields = ['nome']
    ordering = ['ordem', 'nome']


class InscricaoCriterioAtendidoInline(admin.TabularInline):
    model = InscricaoCriterioAtendido
    extra = 0
    can_delete = False
    fields = ['criterio', 'pontos_atribuidos', 'validado', 'observacao_validacao']
    readonly_fields = ['criterio', 'pontos_atribuidos']
    
    def has_add_permission(self, request, obj=None):
        # Apenas sistema pode criar (via ClassificadorService)
        return False


@admin.register(Inscricao)
class InscricaoAdmin(admin.ModelAdmin):
    list_display = ['interessado', 'evento', 'status', 'data_inscricao']
    list_filter = ['status', 'evento', 'data_inscricao']
    search_fields = ['interessado__nome', 'interessado__cpf', 'evento__nome']
    date_hierarchy = 'data_inscricao'
    ordering = ['-data_inscricao']
    
    inlines = [InscricaoCriterioAtendidoInline]
    
    fieldsets = (
        ('Dados da Inscrição', {
            'fields': ('interessado', 'evento', 'status')
        }),
        ('Observações', {
            'fields': ('observacoes',)
        }),
        ('Auditoria', {
            'fields': ('data_inscricao', 'data_atualizacao'),
            'classes': ('collapse',)
        }),
    )
    
    readonly_fields = ['data_inscricao', 'data_atualizacao']


@admin.register(Classificacao)
class ClassificacaoAdmin(admin.ModelAdmin):
    list_display = ['posicao', 'get_interessado', 'get_evento', 'pontuacao_total', 
                    'classificado', 'lista_espera']
    list_filter = ['classificado', 'lista_espera', 'inscricao__evento']
    search_fields = ['inscricao__interessado__nome', 'inscricao__interessado__cpf']
    ordering = ['inscricao__evento', 'posicao']
    
    fieldsets = (
        ('Resultado', {
            'fields': ('inscricao', 'posicao', 'pontuacao_total', 'classificado', 'lista_espera')
        }),
        ('Auditoria', {
            'fields': ('processado_em', 'atualizado_em'),
            'classes': ('collapse',)
        }),
    )
    
    readonly_fields = ['inscricao', 'posicao', 'pontuacao_total', 'classificado', 
                       'lista_espera', 'processado_em', 'atualizado_em']
    
    def get_interessado(self, obj):
        return obj.inscricao.interessado.nome
    get_interessado.short_description = 'Interessado'
    get_interessado.admin_order_field = 'inscricao__interessado__nome'
    
    def get_evento(self, obj):
        return obj.inscricao.evento.nome
    get_evento.short_description = 'Evento'
    get_evento.admin_order_field = 'inscricao__evento__nome'
    
    def has_add_permission(self, request):
        # Apenas sistema pode criar (via ClassificadorService)
        return False
    
    def has_change_permission(self, request, obj=None):
        # Apenas superuser pode editar
        return request.user.is_superuser
    
    def has_delete_permission(self, request, obj=None):
        # Apenas superuser pode deletar
        return request.user.is_superuser


@admin.register(InscricaoCriterioAtendido)
class InscricaoCriterioAtendidoAdmin(admin.ModelAdmin):
    list_display = ['get_interessado', 'get_evento', 'criterio', 'pontos_atribuidos', 
                    'validado']
    list_filter = ['validado', 'criterio', 'inscricao__evento']
    search_fields = ['inscricao__interessado__nome', 'criterio__nome']
    ordering = ['inscricao__evento', 'inscricao__interessado__nome']
    
    fieldsets = (
        ('Informações', {
            'fields': ('inscricao', 'criterio', 'pontos_atribuidos')
        }),
        ('Validação Manual', {
            'fields': ('validado', 'observacao_validacao')
        }),
    )
    
    readonly_fields = ['inscricao', 'criterio', 'pontos_atribuidos']
    
    def get_interessado(self, obj):
        return obj.inscricao.interessado.nome
    get_interessado.short_description = 'Interessado'
    
    def get_evento(self, obj):
        return obj.inscricao.evento.nome
    get_evento.short_description = 'Evento'
    
    def has_add_permission(self, request):
        # Apenas sistema pode criar (via ClassificadorService)
        return False
    
    def has_delete_permission(self, request, obj=None):
        # Apenas superuser pode deletar
        return request.user.is_superuser
    
    