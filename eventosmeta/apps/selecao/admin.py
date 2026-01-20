"""
Admin do app SELEÇÃO
Arquivo: apps/selecao/admin.py
Alteração: Registrados todos os models no admin_site customizado (melhor prática)
Data: 20/01/2026
"""

"""
Admin do app SELEÇÃO
Arquivo: apps/selecao/admin.py
Alteração: Adicionados relatórios PDF e Excel com opções de ordenação
Data: 12/01/2026
"""

from django import forms
from django.contrib import admin
from django.utils.html import format_html

# ==========================================
# IMPORT DO ADMIN CUSTOMIZADO
# Adicionado em 20/01/2026
# ==========================================
from apps.accounts.admin import admin_site

from .models import StatusInscricao, Inscricao, Classificacao, InscricaoCriterioAtendido
from .reports import RelatorioAprovadosService


class StatusInscricaoForm(forms.ModelForm):
    """Form personalizado com seletor de cor"""
    class Meta:
        model = StatusInscricao
        fields = '__all__'
        widgets = {
            'cor': forms.TextInput(attrs={
                'type': 'color',
                'style': 'width: 100px; height: 40px; cursor: pointer; border: 2px solid #ccc; border-radius: 4px;'
            })
        }


@admin.register(StatusInscricao)
class StatusInscricaoAdmin(admin.ModelAdmin):
    form = StatusInscricaoForm
    list_display = ['nome', 'cor_display', 'ordem']
    search_fields = ['nome']
    ordering = ['ordem', 'nome']

    fieldsets = (
        (None, {
            'fields': ('nome', 'cor', 'ordem'),
            'description': 'Clique no quadrado de cor para selecionar visualmente'
        }),
    )

    def cor_display(self, obj):
        """Exibe apenas o quadrado colorido (sem texto)"""
        if obj.cor:
            return format_html(
                '<span style="display: inline-block; width: 30px; height: 30px; '
                'background-color: {}; border: 2px solid #ccc; border-radius: 4px;"></span>',
                obj.cor
            )
        return '—'
    cor_display.short_description = 'Cor'
    cor_display.admin_order_field = 'cor'


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

    actions = [
        'gerar_relatorio_staff_classificacao',
        'gerar_relatorio_staff_nome',
        'gerar_relatorio_mural_classificacao',
        'gerar_relatorio_mural_nome',
        'exportar_excel_staff_classificacao',
        'exportar_excel_staff_nome',
        'exportar_excel_mural_classificacao',
        'exportar_excel_mural_nome'
    ]

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

    #
    # MÉTODOS PARA LIST_DISPLAY
    #

    def get_interessado(self, obj):
        return obj.inscricao.interessado.nome
    get_interessado.short_description = 'Interessado'
    get_interessado.admin_order_field = 'inscricao__interessado__nome'

    def get_evento(self, obj):
        return obj.inscricao.evento.nome
    get_evento.short_description = 'Evento'
    get_evento.admin_order_field = 'inscricao__evento__nome'

    #
    # MÉTODOS AUXILIARES PARA RELATÓRIOS
    #

    def _validar_e_gerar_relatorio(self, request, queryset, tipo_relatorio, ordem):
        """
        Método auxiliar para validação e geração de relatórios PDF

        Args:
            request: HttpRequest
            queryset: QuerySet de Classificacao
            tipo_relatorio: 'staff' ou 'mural'
            ordem: 'classificacao' ou 'nome'
        """
        from django.contrib import messages
        from apps.eventos.models import Evento

        # Pegar eventos distintos do queryset
        eventos_ids = queryset.values_list('inscricao__evento', flat=True).distinct()
        total_eventos = len(set(eventos_ids))

        # Validação: precisa ser de apenas 1 evento
        if total_eventos == 0:
            self.message_user(
                request,
                '⚠️ Nenhuma classificação selecionada',
                level=messages.ERROR
            )
            return

        if total_eventos > 1:
            self.message_user(
                request,
                f'⚠️ Você selecionou classificações de {total_eventos} eventos diferentes. '
                f'FILTRO OBRIGATÓRIO: Use o filtro "Evento" na lateral direita e selecione APENAS UM evento antes de gerar o relatório.',
                level=messages.ERROR
            )
            return

        # Pegar o evento
        evento_id = list(eventos_ids)[0]
        evento = Evento.objects.get(id=evento_id)

        # Validar se tem classificações
        total_classificacoes = queryset.count()
        if total_classificacoes == 0:
            self.message_user(
                request,
                '⚠️ Nenhuma classificação encontrada com os filtros aplicados',
                level=messages.WARNING
            )
            return

        # Aplicar ordenação
        if ordem == 'classificacao':
            classificacoes_ordenadas = queryset.order_by('posicao')
            texto_ordem = 'por classificação'
        else:  # nome
            classificacoes_ordenadas = queryset.order_by('inscricao__interessado__nome')
            texto_ordem = 'por nome'

        # Contar aprovados e lista de espera
        total_aprovados = queryset.filter(classificado=True).count()
        total_lista_espera = queryset.filter(lista_espera=True).count()

        # Gerar PDF
        try:
            if tipo_relatorio == 'staff':
                response = RelatorioAprovadosService.gerar_relatorio_staff(
                    evento,
                    classificacoes_ordenadas,
                    ordem=ordem
                )
            else:  # mural
                response = RelatorioAprovadosService.gerar_relatorio_mural(
                    evento,
                    classificacoes_ordenadas,
                    ordem=ordem
                )

            # Mensagem de sucesso
            self.message_user(
                request,
                f'✅ Relatório {tipo_relatorio.upper()} gerado com sucesso ({texto_ordem})! '
                f'Evento: {evento.nome} | '
                f'Total: {total_classificacoes} | '
                f'Aprovados: {total_aprovados} | '
                f'Lista de Espera: {total_lista_espera}',
                level=messages.SUCCESS
            )

            return response

        except Exception as e:
            self.message_user(
                request,
                f'❌ Erro ao gerar relatório: {str(e)}',
                level=messages.ERROR
            )

    def _validar_e_exportar_excel(self, request, queryset, tipo_relatorio, ordem):
        """
        Método auxiliar para validação e exportação Excel

        Args:
            request: HttpRequest
            queryset: QuerySet de Classificacao
            tipo_relatorio: 'staff' ou 'mural'
            ordem: 'classificacao' ou 'nome'
        """
        from django.contrib import messages
        from apps.eventos.models import Evento

        # Pegar eventos distintos do queryset
        eventos_ids = queryset.values_list('inscricao__evento', flat=True).distinct()
        total_eventos = len(set(eventos_ids))

        # Validação: precisa ser de apenas 1 evento
        if total_eventos == 0:
            self.message_user(
                request,
                '⚠️ Nenhuma classificação selecionada',
                level=messages.ERROR
            )
            return

        if total_eventos > 1:
            self.message_user(
                request,
                f'⚠️ Você selecionou classificações de {total_eventos} eventos diferentes. '
                f'FILTRO OBRIGATÓRIO: Use o filtro "Evento" na lateral direita e selecione APENAS UM evento.',
                level=messages.ERROR
            )
            return

        # Pegar o evento
        evento_id = list(eventos_ids)[0]
        evento = Evento.objects.get(id=evento_id)

        # Validar se tem classificações
        total_classificacoes = queryset.count()
        if total_classificacoes == 0:
            self.message_user(
                request,
                '⚠️ Nenhuma classificação encontrada com os filtros aplicados',
                level=messages.WARNING
            )
            return

        # Aplicar ordenação
        if ordem == 'classificacao':
            classificacoes_ordenadas = queryset.order_by('posicao')
            texto_ordem = 'por classificação'
        else:  # nome
            classificacoes_ordenadas = queryset.order_by('inscricao__interessado__nome')
            texto_ordem = 'por nome'

        # Contar aprovados e lista de espera
        total_aprovados = queryset.filter(classificado=True).count()
        total_lista_espera = queryset.filter(lista_espera=True).count()

        # Gerar Excel
        try:
            if tipo_relatorio == 'staff':
                response = RelatorioAprovadosService.gerar_excel_staff(
                    evento,
                    classificacoes_ordenadas,
                    ordem=ordem
                )
            else:  # mural
                response = RelatorioAprovadosService.gerar_excel_mural(
                    evento,
                    classificacoes_ordenadas,
                    ordem=ordem
                )

            # Mensagem de sucesso
            self.message_user(
                request,
                f'✅ Excel {tipo_relatorio.upper()} gerado com sucesso ({texto_ordem})! '
                f'Evento: {evento.nome} | '
                f'Total: {total_classificacoes} | '
                f'Aprovados: {total_aprovados} | '
                f'Lista de Espera: {total_lista_espera}',
                level=messages.SUCCESS
            )

            return response

        except Exception as e:
            self.message_user(
                request,
                f'❌ Erro ao gerar Excel: {str(e)}',
                level=messages.ERROR
            )

    #
    # ACTIONS DE RELATÓRIOS PDF
    #

    def gerar_relatorio_staff_classificacao(self, request, queryset):
        """Gera relatório STAFF ordenado por CLASSIFICAÇÃO (posição)"""
        return self._validar_e_gerar_relatorio(request, queryset, 'staff', 'classificacao')

    gerar_relatorio_staff_classificacao.short_description = '📞 STAFF: Por Classificação (com telefones)'

    def gerar_relatorio_staff_nome(self, request, queryset):
        """Gera relatório STAFF ordenado por NOME alfabético"""
        return self._validar_e_gerar_relatorio(request, queryset, 'staff', 'nome')

    gerar_relatorio_staff_nome.short_description = '📞 STAFF: Por Nome (com telefones)'

    def gerar_relatorio_mural_classificacao(self, request, queryset):
        """Gera relatório MURAL ordenado por CLASSIFICAÇÃO (posição)"""
        return self._validar_e_gerar_relatorio(request, queryset, 'mural', 'classificacao')

    gerar_relatorio_mural_classificacao.short_description = '📋 MURAL: Por Classificação (público)'

    def gerar_relatorio_mural_nome(self, request, queryset):
        """Gera relatório MURAL ordenado por NOME alfabético"""
        return self._validar_e_gerar_relatorio(request, queryset, 'mural', 'nome')

    gerar_relatorio_mural_nome.short_description = '📋 MURAL: Por Nome (público)'

    #
    # ACTIONS DE EXPORTAÇÃO EXCEL
    #

    def exportar_excel_staff_classificacao(self, request, queryset):
        """Exporta Excel STAFF ordenado por CLASSIFICAÇÃO"""
        return self._validar_e_exportar_excel(request, queryset, 'staff', 'classificacao')

    exportar_excel_staff_classificacao.short_description = '📊 EXCEL STAFF: Por Classificação'

    def exportar_excel_staff_nome(self, request, queryset):
        """Exporta Excel STAFF ordenado por NOME"""
        return self._validar_e_exportar_excel(request, queryset, 'staff', 'nome')

    exportar_excel_staff_nome.short_description = '📊 EXCEL STAFF: Por Nome'

    def exportar_excel_mural_classificacao(self, request, queryset):
        """Exporta Excel MURAL ordenado por CLASSIFICAÇÃO"""
        return self._validar_e_exportar_excel(request, queryset, 'mural', 'classificacao')

    exportar_excel_mural_classificacao.short_description = '📊 EXCEL MURAL: Por Classificação'

    def exportar_excel_mural_nome(self, request, queryset):
        """Exporta Excel MURAL ordenado por NOME"""
        return self._validar_e_exportar_excel(request, queryset, 'mural', 'nome')

    exportar_excel_mural_nome.short_description = '📊 EXCEL MURAL: Por Nome'

    #
    # PERMISSÕES
    #

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


# ==========================================
# REGISTRAR NO ADMIN CUSTOMIZADO
# Adicionado em 20/01/2026
# ==========================================
admin_site.register(StatusInscricao, StatusInscricaoAdmin)
admin_site.register(Inscricao, InscricaoAdmin)
admin_site.register(Classificacao, ClassificacaoAdmin)
admin_site.register(InscricaoCriterioAtendido, InscricaoCriterioAtendidoAdmin)

