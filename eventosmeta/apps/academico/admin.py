
"""
Admin do app ACADÊMICO
Arquivo: apps/academico/admin.py
Alteração: Adicionado seletor de cor visual e removido código hex da listagem
Data: 11/12/2025

Alteração: Registrados todos os models no admin_site customizado (melhor prática)
Data: 20/01/2026

Alteração: Adicionado filtro por evento e action para certificados
Alteração: Sistema completo de certificados com 2 opções
Data: 02/02/2026
"""

from django import forms
from django.contrib import admin
from django.utils.html import format_html
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.urls import reverse

from apps.accounts.admin import admin_site
from .models import StatusMatricula, Matricula, Avaliacao


# ==========================================
# STATUS MATRÍCULA
# ==========================================

class StatusMatriculaForm(forms.ModelForm):
    """Form personalizado com seletor de cor"""
    class Meta:
        model = StatusMatricula
        fields = '__all__'
        widgets = {
            'cor': forms.TextInput(attrs={
                'type': 'color',
                'style': 'width: 100px; height: 40px; cursor: pointer; border: 2px solid #ccc; border-radius: 4px;'
            })
        }


@admin.register(StatusMatricula, site=admin_site)
class StatusMatriculaAdmin(admin.ModelAdmin):
    form = StatusMatriculaForm
    list_display = ['nome', 'cor_display', 'ordem']
    search_fields = ['nome']
    ordering = ['ordem', 'nome']

    fieldsets = (
        (None, {
            'fields': ('nome', 'cor', 'ordem'),
        }),
    )

    def cor_display(self, obj):
        """Exibe quadrado colorido"""
        if obj.cor:
            return format_html(
                '<span style="display: inline-block; width: 30px; height: 30px; '
                'background-color: {}; border: 2px solid #ccc; border-radius: 4px;"></span>',
                obj.cor
            )
        return '—'
    cor_display.short_description = 'Cor'
    cor_display.admin_order_field = 'cor'


# ==========================================
# MATRÍCULA
# ==========================================

@admin.register(Matricula, site=admin_site)
class MatriculaAdmin(admin.ModelAdmin):
    list_display = [
        'numero_matricula',
        'get_interessado',
        'get_evento',
        'turma',
        'status',
        'data_matricula'
    ]
    list_filter = [
        'status',
        'turma__evento',
        'turma',
        'data_matricula'
    ]
    search_fields = [
        'numero_matricula',
        'interessado__nome',
        'interessado__cpf',
        'turma__nome',
        'turma__evento__nome'
    ]
    date_hierarchy = 'data_matricula'
    ordering = ['-data_matricula']

    fieldsets = (
        ('Matrícula', {
            'fields': ('numero_matricula', 'turma', 'status')
        }),
        ('Dados do Aluno', {
            'fields': ('interessado', 'inscricao')
        }),
        ('Observações', {
            'fields': ('observacoes',)
        }),
        ('Auditoria', {
            'fields': ('data_matricula', 'data_atualizacao'),
            'classes': ('collapse',)
        }),
    )

    readonly_fields = ['numero_matricula', 'data_matricula', 'data_atualizacao']

    def get_interessado(self, obj):
        return obj.interessado.nome
    get_interessado.short_description = 'Interessado'
    get_interessado.admin_order_field = 'interessado__nome'

    def get_evento(self, obj):
        return obj.turma.evento.nome
    get_evento.short_description = 'Evento'
    get_evento.admin_order_field = 'turma__evento__nome'


# ==========================================
# AVALIAÇÃO (COM FILTRO POR EVENTO E EDIÇÃO EM MASSA)
# ==========================================

@admin.register(Avaliacao, site=admin_site)
class AvaliacaoAdmin(admin.ModelAdmin):
    list_display = [
        'get_numero_matricula',
        'get_aluno',
        'get_evento',
        'get_turma',
        'nota_final',
        'frequencia',
        'aprovado',
        'certificado_emitido',
        'acoes_certificado'
    ]
    
    # ✅ EDIÇÃO EM MASSA - Campos editáveis diretamente na lista
    list_editable = [
        'nota_final',
        'frequencia',
        'aprovado'
    ]
    
    # ✅ FILTROS - Incluindo por Evento
    list_filter = [
        'aprovado',
        'certificado_emitido',
        'matricula__turma__evento',
        'matricula__turma',
        'avaliado_em'
    ]
    
    search_fields = [
        'matricula__numero_matricula',
        'matricula__interessado__nome',
        'matricula__interessado__cpf',
        'matricula__turma__nome',
        'matricula__turma__evento__nome'
    ]
    
    date_hierarchy = 'avaliado_em'
    ordering = ['matricula__turma__evento', 'matricula__turma', 'matricula__interessado__nome']
    
    # ✅ ACTIONS
    actions = ['gerar_certificados', 'download_certificados_lote_action']

    fieldsets = (
        ('Matrícula', {
            'fields': ('matricula',)
        }),
        ('Avaliação', {
            'fields': ('nota_final', 'frequencia', 'aprovado', 'observacoes')
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

    def get_numero_matricula(self, obj):
        return obj.matricula.numero_matricula
    get_numero_matricula.short_description = 'Matrícula'
    get_numero_matricula.admin_order_field = 'matricula__numero_matricula'

    def get_aluno(self, obj):
        return obj.matricula.interessado.nome
    get_aluno.short_description = 'Aluno'
    get_aluno.admin_order_field = 'matricula__interessado__nome'

    def get_evento(self, obj):
        return obj.matricula.turma.evento.nome
    get_evento.short_description = 'Evento/Curso'
    get_evento.admin_order_field = 'matricula__turma__evento__nome'

    def get_turma(self, obj):
        return obj.matricula.turma.nome
    get_turma.short_description = 'Turma'
    get_turma.admin_order_field = 'matricula__turma__nome'

    def acoes_certificado(self, obj):
        """Botão de visualização para certificados"""
        if not obj.aprovado:
            return format_html('<span style="color: #999;">Não aprovado</span>')
        
        preview_url = reverse('academico:preview_certificado', args=[obj.pk])
        
        return format_html(
            '<a href="{}" target="_blank" class="button" style="padding: 5px 12px; background-color: #417690; color: white; text-decoration: none; border-radius: 4px;">👁️ Ver Certificado</a>',
            preview_url
        )
    
    acoes_certificado.short_description = 'Certificado'

    def gerar_certificados(self, request, queryset):
        """
        Marca certificados como emitidos
        """
        from datetime import date
        
        aprovados = queryset.filter(aprovado=True)
        
        if aprovados.count() == 0:
            self.message_user(
                request,
                '❌ Nenhum aluno aprovado foi selecionado.',
                level=messages.ERROR
            )
            return
        
        certificados_gerados = 0
        erros = []
        
        for avaliacao in aprovados:
            try:
                if not avaliacao.certificado_emitido:
                    avaliacao.certificado_emitido = True
                    avaliacao.data_emissao_certificado = date.today()
                    avaliacao.save()
                    certificados_gerados += 1
                else:
                    erros.append(f'{avaliacao.matricula.interessado.nome} já possui certificado emitido.')
                    
            except Exception as e:
                erros.append(f'{avaliacao.matricula.interessado.nome}: {str(e)}')
        
        if certificados_gerados > 0:
            self.message_user(
                request,
                f'✅ {certificados_gerados} certificado(s) marcado(s) como emitido(s)!',
                level=messages.SUCCESS
            )
        
        if erros:
            for erro in erros:
                self.message_user(request, f'⚠️ {erro}', level=messages.WARNING)
    
    gerar_certificados.short_description = '✅ Marcar certificados como emitidos'

    def download_certificados_lote_action(self, request, queryset):
        """
        Redireciona para view de download em lote
        """
        # Filtrar apenas aprovados
        aprovados = queryset.filter(aprovado=True)
        
        if aprovados.count() == 0:
            self.message_user(
                request,
                '❌ Nenhum aluno aprovado foi selecionado.',
                level=messages.ERROR
            )
            return
        
        # Criar string com IDs
        ids = ','.join(str(av.pk) for av in aprovados)
        
        # Redirecionar para view de download
        url = reverse('academico:download_certificados_lote')
        return HttpResponseRedirect(f"{url}?ids={ids}")
    
    download_certificados_lote_action.short_description = '📦 Baixar certificados em lote (ZIP)'

