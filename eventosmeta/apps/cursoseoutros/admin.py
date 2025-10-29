"""
ARQUIVO: apps/cursoseoutros/admin.py
AÇÃO: CRIAR/SUBSTITUIR arquivo completo
MUDANÇA: Configuração completa do Django Admin para todos os models
DATA/HORA: 2025-10-29 14:45:00
"""

from django.contrib import admin
from django.utils.html import format_html
from django.db.models import Count, Q
from .models import (
    Status, Criterio, Evento, EventoCriterio,
    Inscricao, Classificacao, InscricaoCriterioAtendido,
    Turma, Matricula, Avaliacao
)


# ============================================
# INLINES (Tabelas relacionadas na mesma tela)
# ============================================

class EventoCriterioInline(admin.TabularInline):
    """Permite adicionar critérios diretamente na tela de Evento"""
    model = EventoCriterio
    extra = 1
    fields = ['criterio', 'peso', 'tipo_reserva', 'vagas_reservadas', 'ordem', 
              'ordem_idade', 'idade_minima', 'idade_maxima']
    autocomplete_fields = ['criterio']


class MatriculaInline(admin.TabularInline):
    """Permite ver/adicionar matrículas diretamente na tela de Turma"""
    model = Matricula
    extra = 0
    fields = ['interessado', 'data_matricula', 'status']
    readonly_fields = ['data_matricula']
    autocomplete_fields = ['interessado']


# ============================================
# ADMIN: STATUS
# ============================================

@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = ['status', 'permite_inscricao', 'ordem', 'total_eventos']
    list_editable = ['permite_inscricao', 'ordem']
    search_fields = ['status']
    ordering = ['ordem', 'status']
    
    def total_eventos(self, obj):
        """Exibe quantidade de eventos com este status"""
        total = obj.eventos.count()
        return format_html('<strong>{}</strong>', total)
    total_eventos.short_description = 'Total de Eventos'


# ============================================
# ADMIN: CRITERIO
# ============================================

@admin.register(Criterio)
class CriterioAdmin(admin.ModelAdmin):
    list_display = ['descricao_criterio', 'tipo_badge', 'ativo', 'total_eventos', 'criado_em']
    list_filter = ['tipo_criterio', 'ativo', 'criado_em']
    search_fields = ['descricao_criterio']
    list_editable = ['ativo']
    ordering = ['tipo_criterio', 'descricao_criterio']
    date_hierarchy = 'criado_em'
    
    fieldsets = (
        ('Informações Básicas', {
            'fields': ('descricao_criterio', 'tipo_criterio', 'ativo')
        }),
        ('Auditoria', {
            'fields': ('criado_em',),
            'classes': ('collapse',)
        }),
    )
    
    readonly_fields = ['criado_em']
    
    def tipo_badge(self, obj):
        """Exibe tipo do critério com badge colorido"""
        cores = {
            'NIS': '#28a745',
            'PCD': '#007bff',
            'FOTOTIPO': '#6f42c1',
            'IDADE_CRESC': '#fd7e14',
            'IDADE_DECRESC': '#fd7e14',
            'FAIXA_ETARIA': '#fd7e14',
            'ORDEM': '#6c757d',
            'CUSTOMIZADO': '#17a2b8',
        }
        cor = cores.get(obj.tipo_criterio, '#6c757d')
        return format_html(
            '<span style="background-color: {}; color: white; padding: 3px 10px; '
            'border-radius: 3px; font-size: 11px;">{}</span>',
            cor, obj.get_tipo_criterio_display()
        )
    tipo_badge.short_description = 'Tipo'
    
    def total_eventos(self, obj):
        """Quantidade de eventos usando este critério"""
        total = obj.eventos.count()
        return total
    total_eventos.short_description = 'Eventos'


# ============================================
# ADMIN: EVENTO
# ============================================

@admin.register(Evento)
class EventoAdmin(admin.ModelAdmin):
    list_display = ['descricao', 'status_badge', 'modalidade', 'vagas_info', 
                    'periodo_inscricoes', 'periodo_aulas', 'total_inscricoes']
    list_filter = ['status', 'modalidade', 'criado_em', 'inicio_inscricoes']
    search_fields = ['descricao', 'docente', 'local']
    date_hierarchy = 'inicio_inscricoes'
    ordering = ['-criado_em']
    
    fieldsets = (
        ('Informações Básicas', {
            'fields': ('descricao', 'status', 'modalidade', 'docente')
        }),
        ('Conteúdo Programático', {
            'fields': ('programa', 'objetivo', 'pre_requisito', 'carga_horaria'),
            'classes': ('collapse',)
        }),
        ('Vagas', {
            'fields': ('vagas', 'vagas_minimas')
        }),
        ('Período de Inscrições', {
            'fields': ('inicio_inscricoes', 'fim_inscricoes')
        }),
        ('Período de Matrículas', {
            'fields': ('inicio_matricula', 'fim_matricula')
        }),
        ('Período de Aulas', {
            'fields': ('inicio_aulas', 'fim_aulas', 'horario_aulas')
        }),
        ('Local', {
            'fields': ('local', 'endereco_local')
        }),
        ('Observações', {
            'fields': ('observacao',),
            'classes': ('collapse',)
        }),
        ('Auditoria', {
            'fields': ('criado_em', 'atualizado_em'),
            'classes': ('collapse',)
        }),
    )
    
    readonly_fields = ['criado_em', 'atualizado_em']
    inlines = [EventoCriterioInline]
    
    def status_badge(self, obj):
        """Exibe status com cor"""
        cor = '#28a745' if obj.status.permite_inscricao else '#6c757d'
        return format_html(
            '<span style="background-color: {}; color: white; padding: 5px 10px; '
            'border-radius: 5px;">{}</span>',
            cor, obj.status.status
        )
    status_badge.short_description = 'Status'
    
    def vagas_info(self, obj):
        """Exibe vagas totais e disponíveis"""
        disponiveis = obj.vagas_disponiveis()
        cor = '#28a745' if disponiveis > 0 else '#dc3545'
        return format_html(
            '<strong>{}</strong> vagas<br>'
            '<span style="color: {};">{} disponíveis</span>',
            obj.vagas, cor, disponiveis
        )
    vagas_info.short_description = 'Vagas'
    
    def periodo_inscricoes(self, obj):
        """Exibe período de inscrições"""
        if obj.inicio_inscricoes and obj.fim_inscricoes:
            return format_html(
                '{}<br>até {}',
                obj.inicio_inscricoes.strftime('%d/%m/%Y'),
                obj.fim_inscricoes.strftime('%d/%m/%Y')
            )
        return '-'
    periodo_inscricoes.short_description = 'Inscrições'
    
    def periodo_aulas(self, obj):
        """Exibe período de aulas"""
        if obj.inicio_aulas and obj.fim_aulas:
            return format_html(
                '{}<br>até {}',
                obj.inicio_aulas.strftime('%d/%m/%Y'),
                obj.fim_aulas.strftime('%d/%m/%Y')
            )
        return '-'
    periodo_aulas.short_description = 'Aulas'
    
    def total_inscricoes(self, obj):
        """Total de inscrições"""
        total = obj.total_inscricoes()
        return format_html('<strong>{}</strong>', total)
    total_inscricoes.short_description = 'Inscrições'


# ============================================
# ADMIN: EVENTO_CRITERIO
# ============================================

@admin.register(EventoCriterio)
class EventoCriterioAdmin(admin.ModelAdmin):
    list_display = ['evento', 'criterio', 'peso', 'tipo_reserva', 
                    'vagas_reservadas', 'ordem']
    list_filter = ['tipo_reserva', 'evento__status']
    search_fields = ['evento__descricao', 'criterio__descricao_criterio']
    ordering = ['evento', 'ordem']
    autocomplete_fields = ['evento', 'criterio']
    
    fieldsets = (
        ('Relacionamentos', {
            'fields': ('evento', 'criterio')
        }),
        ('Pontuação', {
            'fields': ('peso', 'ordem')
        }),
        ('Reserva de Vagas', {
            'fields': ('tipo_reserva', 'vagas_reservadas')
        }),
        ('Configurações de Idade', {
            'fields': ('ordem_idade', 'idade_minima', 'idade_maxima'),
            'classes': ('collapse',),
            'description': 'Configurações específicas para critérios de idade'
        }),
        ('Observações', {
            'fields': ('observacao',),
            'classes': ('collapse',)
        }),
    )


# ============================================
# ADMIN: INSCRICAO
# ============================================

@admin.register(Inscricao)
class InscricaoAdmin(admin.ModelAdmin):
    list_display = ['id', 'interessado_nome', 'evento', 'data_inscricao_fmt', 
                    'status_badge', 'classificacao_info']
    list_filter = ['status', 'evento__status', 'data_inscricao']
    search_fields = ['interessado__nome', 'interessado__cpf', 'evento__descricao']
    date_hierarchy = 'data_inscricao'
    ordering = ['-data_inscricao']
    autocomplete_fields = ['evento', 'interessado']
    
    fieldsets = (
        ('Inscrição', {
            'fields': ('evento', 'interessado', 'data_inscricao', 'status')
        }),
    )
    
    readonly_fields = ['data_inscricao']
    
    def interessado_nome(self, obj):
        """Nome e CPF do interessado"""
        return format_html(
            '<strong>{}</strong><br><small>CPF: {}</small>',
            obj.interessado.nome, obj.interessado.cpf
        )
    interessado_nome.short_description = 'Interessado'
    
    def data_inscricao_fmt(self, obj):
        """Data formatada"""
        return obj.data_inscricao.strftime('%d/%m/%Y %H:%M')
    data_inscricao_fmt.short_description = 'Data Inscrição'
    
    def status_badge(self, obj):
        """Status com cor"""
        cores = {
            'INSCRITO': '#17a2b8',
            'AGUARD_CLASS': '#ffc107',
            'CLASSIFICADO': '#007bff',
            'APROVADO': '#28a745',
            'FILA_ESPERA': '#fd7e14',
            'MATRICULADO': '#28a745',
            'DESISTENTE': '#6c757d',
            'NAO_COMPARECEU': '#dc3545',
        }
        cor = cores.get(obj.status, '#6c757d')
        return format_html(
            '<span style="background-color: {}; color: white; padding: 3px 8px; '
            'border-radius: 3px; font-size: 11px;">{}</span>',
            cor, obj.get_status_display()
        )
    status_badge.short_description = 'Status'
    
    def classificacao_info(self, obj):
        """Informações da classificação se existir"""
        try:
            classificacao = obj.classificacao
            return format_html(
                '<strong>Posição: {}</strong><br>Score: {:.2f}',
                classificacao.posicao, classificacao.score_total
            )
        except Classificacao.DoesNotExist:
            return '-'
    classificacao_info.short_description = 'Classificação'


# ============================================
# ADMIN: CLASSIFICACAO
# ============================================

@admin.register(Classificacao)
class ClassificacaoAdmin(admin.ModelAdmin):
    list_display = ['posicao', 'interessado_nome', 'evento', 'score_total', 
                    'situacao', 'data_classificacao_fmt']
    list_filter = ['inscricao__evento', 'data_classificacao']
    search_fields = ['inscricao__interessado__nome', 'inscricao__interessado__cpf',
                     'inscricao__evento__descricao']
    ordering = ['inscricao__evento', 'posicao']
    
    fieldsets = (
        ('Classificação', {
            'fields': ('inscricao', 'score_total', 'posicao', 'data_classificacao')
        }),
    )
    
    readonly_fields = ['data_classificacao']
    
    def interessado_nome(self, obj):
        """Nome do interessado"""
        return obj.inscricao.interessado.nome
    interessado_nome.short_description = 'Interessado'
    
    def evento(self, obj):
        """Evento da inscrição"""
        return obj.inscricao.evento.descricao
    evento.short_description = 'Evento'
    
    def situacao(self, obj):
        """Se está aprovado ou em fila de espera"""
        vagas = obj.inscricao.evento.vagas
        if obj.posicao <= vagas:
            return format_html(
                '<span style="color: #28a745; font-weight: bold;">✓ APROVADO</span>'
            )
        else:
            return format_html(
                '<span style="color: #fd7e14; font-weight: bold;">⏳ FILA DE ESPERA</span>'
            )
    situacao.short_description = 'Situação'
    
    def data_classificacao_fmt(self, obj):
        """Data formatada"""
        return obj.data_classificacao.strftime('%d/%m/%Y %H:%M')
    data_classificacao_fmt.short_description = 'Data Classificação'


# ============================================
# ADMIN: INSCRICAO_CRITERIO_ATENDIDO
# ============================================

@admin.register(InscricaoCriterioAtendido)
class InscricaoCriterioAtendidoAdmin(admin.ModelAdmin):
    list_display = ['inscricao_info', 'criterio', 'pontos_obtidos', 
                    'validado_badge', 'validado_por', 'data_validacao_fmt']
    list_filter = ['validado', 'criterio__tipo_criterio', 'data_validacao']
    search_fields = ['inscricao__interessado__nome', 'criterio__descricao_criterio']
    ordering = ['inscricao', '-pontos_obtidos']
    
    fieldsets = (
        ('Informações', {
            'fields': ('inscricao', 'criterio', 'pontos_obtidos')
        }),
        ('Validação (Para Critérios Customizados)', {
            'fields': ('validado', 'validado_por', 'data_validacao')
        }),
    )
    
    readonly_fields = ['data_validacao']
    
    def inscricao_info(self, obj):
        """Informações da inscrição"""
        return format_html(
            '<strong>{}</strong><br><small>{}</small>',
            obj.inscricao.interessado.nome,
            obj.inscricao.evento.descricao
        )
    inscricao_info.short_description = 'Inscrição'
    
    def validado_badge(self, obj):
        """Badge de validação"""
        if obj.validado:
            return format_html(
                '<span style="color: #28a745; font-weight: bold;">✓ VALIDADO</span>'
            )
        return format_html(
            '<span style="color: #6c757d;">⏳ Pendente</span>'
        )
    validado_badge.short_description = 'Status'
    
    def data_validacao_fmt(self, obj):
        """Data formatada"""
        if obj.data_validacao:
            return obj.data_validacao.strftime('%d/%m/%Y %H:%M')
        return '-'
    data_validacao_fmt.short_description = 'Data Validação'


# ============================================
# ADMIN: TURMA
# ============================================

@admin.register(Turma)
class TurmaAdmin(admin.ModelAdmin):
    list_display = ['descricao_turma', 'evento', 'periodo', 'horario_aulas', 
                    'total_alunos_info']
    list_filter = ['evento', 'data_inicio']
    search_fields = ['descricao_turma', 'evento__descricao']
    ordering = ['evento', 'descricao_turma']
    
    fieldsets = (
        ('Informações Básicas', {
            'fields': ('descricao_turma', 'evento')
        }),
        ('Período', {
            'fields': ('data_inicio', 'data_fim', 'horario_aulas')
        }),
        ('Local', {
            'fields': ('local_aulas',)
        }),
    )
    
    inlines = [MatriculaInline]
    
    def periodo(self, obj):
        """Período da turma"""
        if obj.data_inicio and obj.data_fim:
            return format_html(
                '{}<br>até {}',
                obj.data_inicio.strftime('%d/%m/%Y'),
                obj.data_fim.strftime('%d/%m/%Y')
            )
        return '-'
    periodo.short_description = 'Período'
    
    def total_alunos_info(self, obj):
        """Total de alunos matriculados"""
        total = obj.total_alunos()
        return format_html('<strong>{}</strong> alunos', total)
    total_alunos_info.short_description = 'Total Alunos'


# ============================================
# ADMIN: MATRICULA
# ============================================

@admin.register(Matricula)
class MatriculaAdmin(admin.ModelAdmin):
    list_display = ['id', 'interessado_nome', 'turma', 'data_matricula_fmt', 
                    'status_badge', 'tem_avaliacao']
    list_filter = ['status', 'turma__evento', 'data_matricula']
    search_fields = ['interessado__nome', 'interessado__cpf', 
                     'turma__descricao_turma', 'turma__evento__descricao']
    date_hierarchy = 'data_matricula'
    ordering = ['-data_matricula']
    autocomplete_fields = ['turma', 'interessado']
    
    fieldsets = (
        ('Matrícula', {
            'fields': ('turma', 'interessado', 'data_matricula', 'status')
        }),
    )
    
    readonly_fields = ['data_matricula']
    
    def interessado_nome(self, obj):
        """Nome e CPF"""
        return format_html(
            '<strong>{}</strong><br><small>CPF: {}</small>',
            obj.interessado.nome, obj.interessado.cpf
        )
    interessado_nome.short_description = 'Aluno'
    
    def data_matricula_fmt(self, obj):
        """Data formatada"""
        return obj.data_matricula.strftime('%d/%m/%Y %H:%M')
    data_matricula_fmt.short_description = 'Data Matrícula'
    
    def status_badge(self, obj):
        """Status com cor"""
        cores = {
            'PENDENTE': '#ffc107',
            'CONFIRMADA': '#28a745',
            'CANCELADA': '#dc3545',
            'TRANCADA': '#6c757d',
        }
        cor = cores.get(obj.status, '#6c757d')
        return format_html(
            '<span style="background-color: {}; color: white; padding: 3px 8px; '
            'border-radius: 3px; font-size: 11px;">{}</span>',
            cor, obj.get_status_display()
        )
    status_badge.short_description = 'Status'
    
    def tem_avaliacao(self, obj):
        """Verifica se tem avaliação"""
        try:
            obj.avaliacao
            return format_html('<span style="color: #28a745;">✓</span>')
        except Avaliacao.DoesNotExist:
            return format_html('<span style="color: #dc3545;">✗</span>')
    tem_avaliacao.short_description = 'Avaliação'


# ============================================
# ADMIN: AVALIACAO
# ============================================

@admin.register(Avaliacao)
class AvaliacaoAdmin(admin.ModelAdmin):
    list_display = ['aluno_nome', 'turma', 'frequencia_fmt', 'nota', 
                    'aprovado_badge', 'emite_certificado_badge']
    list_filter = ['aprovado', 'emite_certificado', 'matricula__turma__evento']
    search_fields = ['matricula__interessado__nome', 'matricula__interessado__cpf',
                     'matricula__turma__descricao_turma']
    ordering = ['matricula__turma', '-aprovado']
    
    fieldsets = (
        ('Matrícula', {
            'fields': ('matricula',)
        }),
        ('Desempenho', {
            'fields': ('frequencia', 'nota')
        }),
        ('Resultado', {
            'fields': ('aprovado', 'emite_certificado')
        }),
    )
    
    def aluno_nome(self, obj):
        """Nome do aluno"""
        return obj.matricula.interessado.nome
    aluno_nome.short_description = 'Aluno'
    
    def turma(self, obj):
        """Turma"""
        return obj.matricula.turma.descricao_turma
    turma.short_description = 'Turma'
    
    def frequencia_fmt(self, obj):
        """Frequência formatada com cor"""
        cor = '#28a745' if obj.frequencia >= 75 else '#dc3545'
        return format_html(
            '<span style="color: {}; font-weight: bold;">{:.1f}%</span>',
            cor, obj.frequencia
        )
    frequencia_fmt.short_description = 'Frequência'
    
    def aprovado_badge(self, obj):
        """Badge de aprovação"""
        if obj.aprovado:
            return format_html(
                '<span style="color: #28a745; font-weight: bold;">✓ APROVADO</span>'
            )
        return format_html(
            '<span style="color: #dc3545; font-weight: bold;">✗ REPROVADO</span>'
        )
    aprovado_badge.short_description = 'Situação'
    
    def emite_certificado_badge(self, obj):
        """Badge de certificado"""
        if obj.emite_certificado:
            return format_html(
                '<span style="color: #007bff;">🎓 SIM</span>'
            )
        return format_html(
            '<span style="color: #6c757d;">✗ NÃO</span>'
        )
    emite_certificado_badge.short_description = 'Certificado'