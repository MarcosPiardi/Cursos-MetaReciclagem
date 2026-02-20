"""
Admin do app SELEÇÃO
Arquivo: apps/selecao/admin.py

Histórico de Alterações:
- 12/01/2026: Adicionados relatórios PDF e Excel com opções de ordenação
- 20/01/2026: Registrados todos os models no admin_site customizado (melhor prática)
- 30/01/2026: Adicionada action de matrícula em lote + correção ACTION_CHECKBOX_NAME
- 02/02/2026: Correção definitiva da action com preservação de IDs
- 12/02/2026: Mesclagem final: matrícula + relatórios + boas práticas
- 20/02/2026: Reordenação de colunas + coluna posição reduzida +
              colunas classificado/lista_espera unificadas em get_classificado

Funcionalidades:
- Gestão de Status de Inscrição (com seletor de cor)
- Gestão de Inscrições (com inline de critérios atendidos)
- Gestão de Classificações (matrícula em lote + relatórios PDF/Excel)
- Gestão de Critérios Atendidos (somente leitura)
"""

# ==========================================
# IMPORTS
# ==========================================

# Django core
from django import forms
from django.contrib import admin
from django.contrib.admin.helpers import ACTION_CHECKBOX_NAME
from django.shortcuts import render, redirect
from django.contrib import messages
from django.db import transaction
from django.utils.html import format_html

# Apps internos
from apps.accounts.admin import admin_site
from apps.eventos.models import Turma, Evento
from apps.academico.models import Matricula, StatusMatricula

# Models locais
from .models import StatusInscricao, Inscricao, Classificacao, InscricaoCriterioAtendido

# Services
from .reports import RelatorioAprovadosService


# ==========================================
# FORMS
# ==========================================

class StatusInscricaoForm(forms.ModelForm):
    """Form personalizado com seletor de cor para Status de Inscrição"""

    class Meta:
        model = StatusInscricao
        fields = '__all__'
        widgets = {
            'cor': forms.TextInput(attrs={
                'type': 'color',
                'style': 'width: 100px; height: 40px; cursor: pointer; '
                         'border: 2px solid #ccc; border-radius: 4px;'
            })
        }


class MatricularAlunosForm(forms.Form):
    """Form intermediário para seleção de turma antes de matricular alunos"""

    turma = forms.ModelChoiceField(
        queryset=Turma.objects.none(),
        label='Turma',
        help_text='Selecione a turma onde os alunos serão matriculados',
        widget=forms.Select(attrs={
            'style': 'width: 100%; max-width: 500px; padding: 8px;',
            'required': 'required'
        })
    )

    def __init__(self, *args, **kwargs):
        evento = kwargs.pop('evento', None)
        super().__init__(*args, **kwargs)

        if evento:
            self.fields['turma'].queryset = Turma.objects.filter(
                evento=evento
            ).order_by('nome')

            if not self.fields['turma'].queryset.exists():
                self.fields['turma'].widget.attrs['disabled'] = 'disabled'
                self.fields['turma'].help_text = (
                    '⚠️ Nenhuma turma cadastrada para este evento. '
                    'Crie uma turma primeiro.'
                )


# ==========================================
# INLINES
# ==========================================

class InscricaoCriterioAtendidoInline(admin.TabularInline):
    """
    Inline para exibir critérios atendidos por uma inscrição
    (Somente leitura - criado automaticamente pelo ClassificadorService)
    """

    model = InscricaoCriterioAtendido
    extra = 0
    can_delete = False
    fields = ['criterio', 'pontos_atribuidos', 'validado', 'observacao_validacao']
    readonly_fields = ['criterio', 'pontos_atribuidos']

    def has_add_permission(self, request, obj=None):
        return False


# ==========================================
# ADMIN: STATUS INSCRIÇÃO
# ==========================================

@admin.register(StatusInscricao, site=admin_site)
class StatusInscricaoAdmin(admin.ModelAdmin):
    """Admin para gerenciar Status de Inscrição com seletor visual de cor"""

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
        """Exibe quadrado colorido representando a cor do status"""
        if obj.cor:
            return format_html(
                '<span style="display: inline-block; width: 30px; height: 30px; '
                'background-color: {}; border: 2px solid #ccc; '
                'border-radius: 4px;"></span>',
                obj.cor
            )
        return '—'

    cor_display.short_description = 'Cor'
    cor_display.admin_order_field = 'cor'


# ==========================================
# ADMIN: INSCRIÇÃO
# ==========================================

@admin.register(Inscricao, site=admin_site)
class InscricaoAdmin(admin.ModelAdmin):
    """Admin para gerenciar Inscrições de interessados em eventos"""

    list_display = ['get_interessado', 'evento', 'status', 'data_inscricao']
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

    def get_interessado(self, obj):
        """Retorna nome do interessado"""
        return obj.interessado.nome

    get_interessado.short_description = 'Interessado'
    get_interessado.admin_order_field = 'interessado__nome'


# ==========================================
# ADMIN: CLASSIFICAÇÃO
# ==========================================

@admin.register(Classificacao, site=admin_site)
class ClassificacaoAdmin(admin.ModelAdmin):
    """
    Admin para gerenciar Classificações de interessados

    Funcionalidades:
    - Matrícula em lote de alunos classificados
    - Geração de relatórios PDF (Staff e Mural)
    - Exportação para Excel (Staff e Mural)
    """

    # ==========================================
    # ALTERAÇÃO 20/02/2026:
    # - Reordenadas colunas
    # - Unificadas classificado + lista_espera em get_classificado
    # - posicao exibida via get_posicao (com estilo reduzido)
    # ==========================================

    list_display = [
        'get_posicao',          # ← Posição (reduzida)
        'get_interessado',      # ← Nome
        'get_cpf',              # ← CPF
        'get_evento',           # ← Evento
        'get_status_inscricao', # ← Status da inscrição
        'get_classificado',     # ← Classificado / Lista de Espera (unificado)
        'pontuacao_total',      # ← Pontuação
    ]

    list_filter = [
        'classificado',
        'lista_espera',
        'inscricao__evento',
        'inscricao__status'
    ]

    search_fields = [
        'inscricao__interessado__nome',
        'inscricao__interessado__cpf',
        'inscricao__evento__nome'
    ]

    ordering = ['inscricao__evento', 'posicao']

    actions = [
        'matricular_alunos_action',
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
        ('Inscrição', {
            'fields': ('inscricao',)
        }),
        ('Classificação', {
            'fields': ('posicao', 'pontuacao_total', 'classificado', 'lista_espera')
        }),
        ('Auditoria', {
            'fields': ('processado_em', 'atualizado_em'),
            'classes': ('collapse',)
        }),
    )

    readonly_fields = [
        'inscricao', 'posicao', 'pontuacao_total',
        'classificado', 'lista_espera',
        'processado_em', 'atualizado_em'
    ]

    # ==========================================
    # MÉTODOS PARA LIST_DISPLAY
    # ==========================================

    def get_posicao(self, obj):
        """Posição com tamanho reduzido e centralizado"""
        return format_html(
            '<span style="display: block; text-align: center; '
            'font-weight: bold; width: 36px; margin: auto;">'
            '{}º</span>',
            obj.posicao
        )

    get_posicao.short_description = '#'
    get_posicao.admin_order_field = 'posicao'

    def get_interessado(self, obj):
        """Retorna nome do interessado"""
        return obj.inscricao.interessado.nome

    get_interessado.short_description = 'Interessado'
    get_interessado.admin_order_field = 'inscricao__interessado__nome'

    def get_cpf(self, obj):
        """Retorna CPF formatado"""
        cpf = obj.inscricao.interessado.cpf
        return f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"

    get_cpf.short_description = 'CPF'

    def get_evento(self, obj):
        """Retorna nome do evento"""
        return obj.inscricao.evento.nome

    get_evento.short_description = 'Evento'
    get_evento.admin_order_field = 'inscricao__evento__nome'

    def get_status_inscricao(self, obj):
        """Retorna badge colorido com status da inscrição"""
        status = obj.inscricao.status
        return format_html(
            '<span style="display: inline-block; padding: 3px 8px; '
            'background-color: {}; color: white; border-radius: 3px; '
            'font-size: 11px;">{}</span>',
            status.cor,
            status.nome
        )

    get_status_inscricao.short_description = 'Status Inscrição'
    get_status_inscricao.admin_order_field = 'inscricao__status__nome'

    def get_classificado(self, obj):
        """
        Unifica classificado e lista_espera em uma coluna.
        Alteração: 20/02/2026
        """
        if obj.classificado:
            return format_html(
                '<span style="display: inline-block; padding: 4px 10px; '
                'background-color: #27ae60; color: white; border-radius: 12px; '
                'font-size: 11px; font-weight: 600;">'
                '✅ Classificado</span>'
            )
        elif obj.lista_espera:
            return format_html(
                '<span style="display: inline-block; padding: 4px 10px; '
                'background-color: #f39c12; color: white; border-radius: 12px; '
                'font-size: 11px; font-weight: 600;">'
                '⏳ Lista de Espera</span>'
            )
        else:
            return format_html(
                '<span style="display: inline-block; padding: 4px 10px; '
                'background-color: #95a5a6; color: white; border-radius: 12px; '
                'font-size: 11px; font-weight: 600;">'
                '❌ Não Classificado</span>'
            )

    get_classificado.short_description = 'Classificado?'
    get_classificado.admin_order_field = 'classificado'

    # ==========================================
    # ACTION: MATRICULAR ALUNOS EM LOTE
    # ==========================================

    def matricular_alunos_action(self, request, queryset):
        """
        Action para matricular alunos classificados em uma turma
        """
        if queryset.count() == 0:
            self.message_user(
                request,
                '❌ Nenhuma classificação foi selecionada.',
                level=messages.ERROR
            )
            return

        queryset = queryset.select_related(
            'inscricao__evento',
            'inscricao__interessado'
        )

        eventos_unicos = set()
        for classificacao in queryset:
            if classificacao.inscricao and classificacao.inscricao.evento:
                eventos_unicos.add(classificacao.inscricao.evento.id)

        if len(eventos_unicos) == 0:
            self.message_user(
                request,
                '❌ As classificações selecionadas não possuem evento associado.',
                level=messages.ERROR
            )
            return

        if len(eventos_unicos) > 1:
            eventos_nomes = [c.inscricao.evento.nome for c in queryset[:5]]
            self.message_user(
                request,
                f'❌ Selecione apenas classificações do MESMO EVENTO. '
                f'Eventos detectados: {", ".join(set(eventos_nomes))}',
                level=messages.ERROR
            )
            return

        evento = queryset.first().inscricao.evento

        if not Turma.objects.filter(evento=evento).exists():
            self.message_user(
                request,
                f'❌ O evento "{evento.nome}" não possui turmas cadastradas. '
                f'Crie uma turma em Eventos > Turmas.',
                level=messages.ERROR
            )
            return

        # POST: Processar matrícula
        if 'confirmar_matricula' in request.POST:
            form = MatricularAlunosForm(request.POST, evento=evento)

            if form.is_valid():
                turma = form.cleaned_data['turma']

                if turma.evento != evento:
                    self.message_user(
                        request,
                        f'❌ A turma "{turma.nome}" não pertence ao evento "{evento.nome}".',
                        level=messages.ERROR
                    )
                    return redirect(request.get_full_path())

                try:
                    status_matricula = StatusMatricula.objects.get(
                        nome__iexact='ATIVA'
                    )
                except StatusMatricula.DoesNotExist:
                    self.message_user(
                        request,
                        '❌ Status "ATIVA" (ou variação) não encontrado em '
                        'Status de Matrículas.',
                        level=messages.ERROR
                    )
                    return redirect(request.get_full_path())

                try:
                    status_inscricao = StatusInscricao.objects.get(
                        nome__iexact='CONFIRMADA'
                    )
                except StatusInscricao.DoesNotExist:
                    self.message_user(
                        request,
                        '❌ Status "CONFIRMADA" (ou variação) não encontrado em '
                        'Status de Inscrições.',
                        level=messages.ERROR
                    )
                    return redirect(request.get_full_path())

                matriculas_criadas = 0
                erros = []

                with transaction.atomic():
                    for classificacao in queryset:
                        try:
                            inscricao = classificacao.inscricao
                            interessado = inscricao.interessado

                            if Matricula.objects.filter(
                                turma=turma,
                                interessado=interessado
                            ).exists():
                                erros.append(
                                    f'{interessado.nome} já está matriculado nesta turma.'
                                )
                                continue

                            Matricula.objects.create(
                                turma=turma,
                                interessado=interessado,
                                inscricao=inscricao,
                                status=status_matricula
                            )

                            inscricao.status = status_inscricao
                            inscricao.save()

                            matriculas_criadas += 1

                        except Exception as e:
                            erros.append(f'{interessado.nome}: {str(e)}')

                if matriculas_criadas > 0:
                    self.message_user(
                        request,
                        f'✅ {matriculas_criadas} matrícula(s) criada(s) '
                        f'na turma "{turma.nome}"!',
                        level=messages.SUCCESS
                    )

                if erros:
                    for erro in erros:
                        self.message_user(
                            request, f'⚠️ {erro}', level=messages.WARNING
                        )

                return redirect(request.get_full_path())

            else:
                for field, errors in form.errors.items():
                    for error in errors:
                        self.message_user(
                            request, f'❌ {error}', level=messages.ERROR
                        )

        # GET: Exibir form
        else:
            form = MatricularAlunosForm(evento=evento)

        context = {
            'title': 'Matricular Alunos Selecionados',
            'form': form,
            'classificacoes': queryset,
            'evento': evento,
            'opts': self.model._meta,
            'action_checkbox_name': ACTION_CHECKBOX_NAME,
        }

        return render(
            request,
            'admin/selecao/matricular_alunos.html',
            context
        )

    matricular_alunos_action.short_description = '🎓 Matricular alunos selecionados'

    # ==========================================
    # MÉTODOS AUXILIARES PARA RELATÓRIOS
    # ==========================================

    def _validar_e_gerar_relatorio(self, request, queryset, tipo_relatorio, ordem):
        """Método auxiliar para validação e geração de relatórios PDF"""
        eventos_ids = queryset.values_list(
            'inscricao__evento', flat=True
        ).distinct()
        total_eventos = len(set(eventos_ids))

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
                f'⚠️ Você selecionou classificações de {total_eventos} eventos. '
                f'Use o filtro "Evento" e selecione APENAS UM evento.',
                level=messages.ERROR
            )
            return

        evento = Evento.objects.get(id=list(eventos_ids)[0])

        if queryset.count() == 0:
            self.message_user(
                request,
                '⚠️ Nenhuma classificação encontrada',
                level=messages.WARNING
            )
            return

        if ordem == 'classificacao':
            queryset_ordenado = queryset.order_by('posicao')
            texto_ordem = 'por classificação'
        else:
            queryset_ordenado = queryset.order_by('inscricao__interessado__nome')
            texto_ordem = 'por nome'

        total = queryset.count()
        aprovados = queryset.filter(classificado=True).count()
        lista_espera = queryset.filter(lista_espera=True).count()

        try:
            if tipo_relatorio == 'staff':
                response = RelatorioAprovadosService.gerar_relatorio_staff(
                    evento, queryset_ordenado, ordem=ordem
                )
            else:
                response = RelatorioAprovadosService.gerar_relatorio_mural(
                    evento, queryset_ordenado, ordem=ordem
                )

            self.message_user(
                request,
                f'✅ Relatório {tipo_relatorio.upper()} gerado ({texto_ordem})! '
                f'Evento: {evento.nome} | Total: {total} | '
                f'Aprovados: {aprovados} | Lista de Espera: {lista_espera}',
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
        """Método auxiliar para validação e exportação Excel"""
        eventos_ids = queryset.values_list(
            'inscricao__evento', flat=True
        ).distinct()
        total_eventos = len(set(eventos_ids))

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
                f'⚠️ Você selecionou classificações de {total_eventos} eventos. '
                f'Use o filtro "Evento" e selecione APENAS UM evento.',
                level=messages.ERROR
            )
            return

        evento = Evento.objects.get(id=list(eventos_ids)[0])

        if queryset.count() == 0:
            self.message_user(
                request,
                '⚠️ Nenhuma classificação encontrada',
                level=messages.WARNING
            )
            return

        if ordem == 'classificacao':
            queryset_ordenado = queryset.order_by('posicao')
            texto_ordem = 'por classificação'
        else:
            queryset_ordenado = queryset.order_by('inscricao__interessado__nome')
            texto_ordem = 'por nome'

        total = queryset.count()
        aprovados = queryset.filter(classificado=True).count()
        lista_espera = queryset.filter(lista_espera=True).count()

        try:
            if tipo_relatorio == 'staff':
                response = RelatorioAprovadosService.gerar_excel_staff(
                    evento, queryset_ordenado, ordem=ordem
                )
            else:
                response = RelatorioAprovadosService.gerar_excel_mural(
                    evento, queryset_ordenado, ordem=ordem
                )

            self.message_user(
                request,
                f'✅ Excel {tipo_relatorio.upper()} gerado ({texto_ordem})! '
                f'Evento: {evento.nome} | Total: {total} | '
                f'Aprovados: {aprovados} | Lista de Espera: {lista_espera}',
                level=messages.SUCCESS
            )

            return response

        except Exception as e:
            self.message_user(
                request,
                f'❌ Erro ao gerar Excel: {str(e)}',
                level=messages.ERROR
            )

    # ==========================================
    # ACTIONS: RELATÓRIOS PDF
    # ==========================================

    def gerar_relatorio_staff_classificacao(self, request, queryset):
        """Gera relatório STAFF ordenado por CLASSIFICAÇÃO (posição)"""
        return self._validar_e_gerar_relatorio(
            request, queryset, 'staff', 'classificacao'
        )

    gerar_relatorio_staff_classificacao.short_description = (
        '📞 PDF STAFF: Por Classificação (com telefones)'
    )

    def gerar_relatorio_staff_nome(self, request, queryset):
        """Gera relatório STAFF ordenado por NOME alfabético"""
        return self._validar_e_gerar_relatorio(
            request, queryset, 'staff', 'nome'
        )

    gerar_relatorio_staff_nome.short_description = (
        '📞 PDF STAFF: Por Nome (com telefones)'
    )

    def gerar_relatorio_mural_classificacao(self, request, queryset):
        """Gera relatório MURAL ordenado por CLASSIFICAÇÃO (posição)"""
        return self._validar_e_gerar_relatorio(
            request, queryset, 'mural', 'classificacao'
        )

    gerar_relatorio_mural_classificacao.short_description = (
        '📋 PDF MURAL: Por Classificação (público)'
    )

    def gerar_relatorio_mural_nome(self, request, queryset):
        """Gera relatório MURAL ordenado por NOME alfabético"""
        return self._validar_e_gerar_relatorio(
            request, queryset, 'mural', 'nome'
        )

    gerar_relatorio_mural_nome.short_description = (
        '📋 PDF MURAL: Por Nome (público)'
    )

    # ==========================================
    # ACTIONS: EXPORTAÇÃO EXCEL
    # ==========================================

    def exportar_excel_staff_classificacao(self, request, queryset):
        """Exporta Excel STAFF ordenado por CLASSIFICAÇÃO"""
        return self._validar_e_exportar_excel(
            request, queryset, 'staff', 'classificacao'
        )

    exportar_excel_staff_classificacao.short_description = (
        '📊 EXCEL STAFF: Por Classificação'
    )

    def exportar_excel_staff_nome(self, request, queryset):
        """Exporta Excel STAFF ordenado por NOME"""
        return self._validar_e_exportar_excel(
            request, queryset, 'staff', 'nome'
        )

    exportar_excel_staff_nome.short_description = (
        '📊 EXCEL STAFF: Por Nome'
    )

    def exportar_excel_mural_classificacao(self, request, queryset):
        """Exporta Excel MURAL ordenado por CLASSIFICAÇÃO"""
        return self._validar_e_exportar_excel(
            request, queryset, 'mural', 'classificacao'
        )

    exportar_excel_mural_classificacao.short_description = (
        '📊 EXCEL MURAL: Por Classificação'
    )

    def exportar_excel_mural_nome(self, request, queryset):
        """Exporta Excel MURAL ordenado por NOME"""
        return self._validar_e_exportar_excel(
            request, queryset, 'mural', 'nome'
        )

    exportar_excel_mural_nome.short_description = (
        '📊 EXCEL MURAL: Por Nome'
    )

    # ==========================================
    # PERMISSÕES
    # ==========================================

    def has_add_permission(self, request):
        """Apenas sistema pode criar classificações (via ClassificadorService)"""
        return False

    def has_change_permission(self, request, obj=None):
        """Apenas superuser pode editar classificações manualmente"""
        return request.user.is_superuser

    def has_delete_permission(self, request, obj=None):
        """Apenas superuser pode deletar classificações"""
        return request.user.is_superuser


# ==========================================
# ADMIN: CRITÉRIOS ATENDIDOS
# ==========================================

@admin.register(InscricaoCriterioAtendido, site=admin_site)
class InscricaoCriterioAtendidoAdmin(admin.ModelAdmin):
    """
    Admin para gerenciar Critérios Atendidos por Inscrições
    (Criado automaticamente pelo ClassificadorService)
    """

    list_display = [
        'get_interessado',
        'get_evento',
        'criterio',
        'pontos_atribuidos',
        'validado'
    ]

    list_filter = [
        'validado',
        'criterio',
        'inscricao__evento'
    ]

    search_fields = [
        'inscricao__interessado__nome',
        'inscricao__interessado__cpf',
        'criterio__nome'
    ]

    ordering = ['inscricao__evento', 'inscricao__interessado__nome']

    fieldsets = (
        ('Inscrição e Critério', {
            'fields': ('inscricao', 'criterio', 'pontos_atribuidos')
        }),
        ('Validação Manual', {
            'fields': ('validado', 'observacao_validacao')
        }),
    )

    readonly_fields = ['inscricao', 'criterio', 'pontos_atribuidos']

    def get_interessado(self, obj):
        """Retorna nome do interessado"""
        return obj.inscricao.interessado.nome

    get_interessado.short_description = 'Interessado'

    def get_evento(self, obj):
        """Retorna nome do evento"""
        return obj.inscricao.evento.nome

    get_evento.short_description = 'Evento'

    def has_add_permission(self, request):
        """Apenas sistema pode criar (via ClassificadorService)"""
        return False

    def has_delete_permission(self, request, obj=None):
        """Apenas superuser pode deletar"""
        return request.user.is_superuser
    
    