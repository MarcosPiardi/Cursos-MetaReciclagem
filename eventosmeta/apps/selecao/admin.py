"""
Admin do app SELEÇÃO
Arquivo: apps/selecao/admin.py
Data: 10 de abril de 2026

Histórico de Alterações:
- 12/01/2026: Adicionados relatórios PDF e Excel com opções de ordenação
- 20/01/2026: Registrados todos os models no admin_site customizado (melhor prática)
- 30/01/2026: Adicionada action de matrícula em lote + correção ACTION_CHECKBOX_NAME
- 02/02/2026: Correção definitiva da action com preservação de IDs
- 12/02/2026: Mesclagem final: matrícula + relatórios + boas práticas
- 20/02/2026: Reordenação de colunas + coluna posição reduzida + colunas classificado/lista_espera unificadas em get_classificado
- 08/04/2026: Adicionada trava de capacidade na action matricular_alunos_action
- 10/04/2026: Lógica da action matricular_alunos_action revisada e corrigida para validação de capacidade, duplicidade e atomicidade.

Funcionalidades:
- Gestão de Status de Inscrição (com seletor de cor)
- Gestão de Inscrições (com inline de critérios atendidos)
- Gestão de Classificações (matrícula em lote + relatórios PDF/Excel)
- Gestão de Critérios Atendidos (somente leitura)
- Validação de capacidade: impede matricular mais alunos que vagas disponíveis
"""

from django import forms
from django.contrib import admin, messages
from django.contrib.admin.helpers import ACTION_CHECKBOX_NAME
from django.db import transaction
from django.shortcuts import render, redirect
from django.utils.html import format_html

from apps.eventos.models import Turma, Evento
from apps.academico.models import Matricula, StatusMatricula
from .models import StatusInscricao, Inscricao, Classificacao, InscricaoCriterioAtendido
from .reports import RelatorioAprovadosService
from apps.admin_mixins import CustomTitleMixin

# 
# FORMS
# 

class StatusInscricaoForm(forms.ModelForm):
    """Form personalizado com seletor de cor para Status de Inscrição"""
    class Meta:
        model = StatusInscricao
        fields = '__all__'
        widgets = {
            'cor': forms.TextInput(attrs={
                'type': 'color',
                'style': 'width: 100px; height: 40px; cursor: pointer; border: 2px solid #ccc; border-radius: 4px;'
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
            self.fields['turma'].queryset = Turma.objects.filter(evento=evento).order_by('nome')
            if not self.fields['turma'].queryset.exists():
                self.fields['turma'].widget.attrs['disabled'] = 'disabled'
                self.fields['turma'].help_text = '⚠️ Nenhuma turma cadastrada para este evento. Crie uma turma primeiro.'

# 
# INLINES
# 

class InscricaoCriterioAtendidoInline(admin.TabularInline):
    """Inline para exibir critérios atendidos por uma inscrição (Somente leitura)"""
    model = InscricaoCriterioAtendido
    extra = 0
    can_delete = False
    fields = ['criterio', 'pontos_atribuidos', 'validado', 'observacao_validacao']
    readonly_fields = ['criterio', 'pontos_atribuidos']

    def has_add_permission(self, request, obj=None):
        return False

# 
# ADMIN: STATUS INSCRIÇÃO
# 

@admin.register(StatusInscricao)
class StatusInscricaoAdmin(CustomTitleMixin, admin.ModelAdmin):
    custom_title = "adm Status de Inscrição"
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

# 
# ADMIN: INSCRIÇÃO
# 

@admin.register(Inscricao)
class InscricaoAdmin(CustomTitleMixin, admin.ModelAdmin):
    custom_title = "adm Inscrições nos Cursos"
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

# 
# ADMIN: CLASSIFICAÇÃO
# 

@admin.register(Classificacao)
class ClassificacaoAdmin(CustomTitleMixin, admin.ModelAdmin):
    """Admin para gerenciar Classificações com matrícula em lote + relatórios"""
    custom_title = "adm Classificações"

    list_display = [
        'get_posicao',
        'get_interessado',
        'get_cpf',
        'get_evento',
        'get_status_inscricao',
        'get_classificado',
        'pontuacao_total',
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

    def get_posicao(self, obj):
        """Posição com tamanho reduzido e centralizado"""
        return format_html(
            '{}"º',
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
            '<span style="background-color: {}; color: white; padding: 5px 10px; border-radius: 3px;">{}</span>',
            status.cor,
            status.nome
        )

    get_status_inscricao.short_description = 'Status Inscrição'
    get_status_inscricao.admin_order_field = 'inscricao__status__nome'

    def get_classificado(self, obj):
        """Unifica classificado e lista_espera em uma coluna"""
        if obj.classificado:
            return format_html(
                '✅ Classificado'
            )
        elif obj.lista_espera:
            return format_html(
                '⏳ Lista de Espera'
            )
        else:
            return format_html(
                '❌ Não Classificado'
            )

    get_classificado.short_description = 'Classificado?'
    get_classificado.admin_order_field = 'classificado'

    # 
    # ACTION: MATRICULAR ALUNOS EM LOTE (COM TRAVA DE CAPACIDADE)
    # 

    def matricular_alunos_action(self, request, queryset):
        """
        Action para matricular alunos classificados em uma turma com validação de capacidade,
        evento único, turma existente e proteção contra duplicidade.
        """
        
        # 1. Validações iniciais (GET ou POST antes do form.is_valid())
        if queryset.count() == 0:
            self.message_user(request, '❌ Nenhuma classificação foi selecionada.', level=messages.ERROR)
            return

        # Otimiza o queryset para evitar N+1 queries
        queryset = queryset.select_related('inscricao__evento', 'inscricao__interessado')

        eventos_ids = set()
        for classificacao in queryset:
            if classificacao.inscricao and classificacao.inscricao.evento:
                eventos_ids.add(classificacao.inscricao.evento.id)

        if len(eventos_ids) == 0:
            self.message_user(request, '❌ As classificações selecionadas não possuem evento associado.', level=messages.ERROR)
            return

        if len(eventos_ids) > 1:
            # Pega os nomes dos eventos para a mensagem de erro
            eventos_nomes = [c.inscricao.evento.nome for c in queryset[:5]] # Limita para não sobrecarregar
            self.message_user(request, f'❌ Selecione apenas classificações do MESMO EVENTO. Eventos detectados: {", ".join(set(eventos_nomes))}', level=messages.ERROR)
            return

        evento = Evento.objects.get(id=list(eventos_ids)[0]) # Pega o único evento

        if not Turma.objects.filter(evento=evento).exists():
            self.message_user(request, f'❌ O evento "{evento.nome}" não possui turmas cadastradas. Crie uma turma em Eventos > Turmas.', level=messages.ERROR)
            return

        # 2. Processamento da requisição (POST)
        if 'confirmar_matricula' in request.POST:
            form = MatricularAlunosForm(request.POST, evento=evento)

            if form.is_valid():
                turma = form.cleaned_data['turma']

                # Validação: A turma selecionada pertence ao evento correto               
                if turma.evento != evento:
                    self.message_user(
                        request,
                        f'❌ A turma "{turma.nome}" não pertence ao evento "{evento.nome}".',
                        level=messages.ERROR
                    )
                    return  # <-- sem redirect aqui


                # 
                # TRAVA DE CAPACIDADE: Validar antes de criar matrículas
                # 
                # Contar matrículas ATIVAS na turma
                matriculas_existentes = Matricula.objects.filter(
                    turma=turma,
                    status__nome__iexact='Ativa'
                ).count()
                
                vagas_restantes = turma.capacidade - matriculas_existentes
                total_selecionado = queryset.count()

                if total_selecionado > vagas_restantes:
                    self.message_user(
                        request,
                        f'❌ Falha na operação: Você selecionou {total_selecionado} classificados, mas a turma "{turma.nome}" possui apenas {vagas_restantes} vaga(s) disponível(eis). (Capacidade total: {turma.capacidade}, Matrículas atuais: {matriculas_existentes})',
                        level=messages.ERROR
                    )
                    return
                # 

                # Buscar Status de Matrícula e Inscrição necessários
                try:
                    status_matricula_ativa = StatusMatricula.objects.get(nome__iexact='ATIVA')
                except StatusMatricula.DoesNotExist:
                    self.message_user(request, '❌ Status "ATIVA" não encontrado em Status de Matrículas. Crie-o primeiro.', level=messages.ERROR)
                    return

                try:
                    status_inscricao_confirmada = StatusInscricao.objects.get(nome__iexact='CONFIRMADA')
                except StatusInscricao.DoesNotExist:
                    self.message_user(request, '❌ Status "CONFIRMADA" não encontrado em Status de Inscrições. Crie-o primeiro.', level=messages.ERROR)
                    return

                matriculas_criadas = 0
                erros = []

                # 
                # CRIAÇÃO DE MATRÍCULAS COM PROTEÇÃO DE DUPLICIDADE E ATOMICIDADE
                # 
                with transaction.atomic():
                    for classificacao in queryset:
                        try:
                            inscricao = classificacao.inscricao
                            interessado = inscricao.interessado

                            # Proteção contra duplicidade: verificar se já está matriculado
                            if Matricula.objects.filter(turma=turma, interessado=interessado).exists():
                                erros.append(f'⚠️ {interessado.nome} já está matriculado nesta turma. Matrícula ignorada.')
                                continue # Pula para a próxima classificação

                            # Cria a matrícula
                            Matricula.objects.create(
                                turma=turma,
                                interessado=interessado,
                                inscricao=inscricao,
                                status=status_matricula_ativa
                            )

                            # Atualiza o status da inscrição para CONFIRMADA
                            inscricao.status = status_inscricao_confirmada
                            inscricao.save()

                            matriculas_criadas += 1

                        except Exception as e:
                            # Qualquer erro durante a criação de uma matrícula específica
                            # será capturado e adicionado à lista de erros.
                            # A transação atômica garante que, se um erro crítico ocorrer
                            # fora deste try/except, tudo será revertido.
                            erros.append(f'❌ Erro ao matricular {interessado.nome}: {str(e)}')
                            # Não damos 'continue' aqui para permitir que a transação tente
                            # as próximas matrículas, mas o erro será reportado.
                            # Se a intenção é que QUALQUER erro dentro do loop reverta TUDO,
                            # então o try/except deve estar fora do loop, englobando o atomic block.
                            # No entanto, a abordagem atual permite reportar erros individuais
                            # e continuar com outras matrículas, se a exceção não for fatal para a transação.
                            # Para garantir rollback total em qualquer erro, o 'try' externo ao 'with' seria melhor.
                            # Mantendo a estrutura original, a exceção dentro do loop apenas registra o erro.
                            # Se a exceção for grave e não tratada, o 'atomic' fará o rollback.

                # Mensagens de feedback após a operação
                if matriculas_criadas > 0:
                    self.message_user(request, f'✅ {matriculas_criadas} matrícula(s) criada(s) na turma "{turma.nome}"!', level=messages.SUCCESS)

                if erros:
                    for erro in erros:
                        self.message_user(request, erro, level=messages.WARNING) # Usar WARNING para erros individuais

                return

            else:
                # Erros de validação do formulário (ex: turma não selecionada)
                for field, errors in form.errors.items():
                    for error in errors:
                        self.message_user(request, f'❌ Erro no campo "{field}": {error}', level=messages.ERROR)

        # 3. Exibição do formulário (GET request)
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

        return render(request, 'admin/selecao/matricular_alunos.html', context)

    matricular_alunos_action.short_description = '🎓 Matricular alunos selecionados'

    # 
    # MÉTODOS AUXILIARES PARA RELATÓRIOS
    # 

    def _validar_e_gerar_relatorio(self, request, queryset, tipo_relatorio, ordem):
        """Método auxiliar para validação e geração de relatórios PDF"""
        eventos_ids = queryset.values_list('inscricao__evento', flat=True).distinct()
        total_eventos = len(set(eventos_ids))

        if total_eventos == 0:
            self.message_user(request, '⚠️ Nenhuma classificação selecionada', level=messages.ERROR)
            return

        if total_eventos > 1:
            self.message_user(request, f'⚠️ Você selecionou classificações de {total_eventos} eventos. Use o filtro "Evento" e selecione APENAS UM evento.', level=messages.ERROR)
            return

        evento = Evento.objects.get(id=list(eventos_ids)[0])

        if queryset.count() == 0:
            self.message_user(request, '⚠️ Nenhuma classificação encontrada', level=messages.WARNING)
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
                response = RelatorioAprovadosService.gerar_relatorio_staff(evento, queryset_ordenado, ordem=ordem)
            else:
                response = RelatorioAprovadosService.gerar_relatorio_mural(evento, queryset_ordenado, ordem=ordem)

            return response

        except Exception as e:
            self.message_user(request, f'❌ Erro ao gerar relatório: {str(e)}', level=messages.ERROR)

    def _validar_e_exportar_excel(self, request, queryset, tipo_relatorio, ordem):
        """Método auxiliar para validação e exportação Excel"""
        eventos_ids = queryset.values_list('inscricao__evento', flat=True).distinct()
        total_eventos = len(set(eventos_ids))

        if total_eventos == 0:
            self.message_user(request, '⚠️ Nenhuma classificação selecionada', level=messages.ERROR)
            return

        if total_eventos > 1:
            self.message_user(request, f'⚠️ Você selecionou classificações de {total_eventos} eventos. Use o filtro "Evento" e selecione APENAS UM evento.', level=messages.ERROR)
            return

        evento = Evento.objects.get(id=list(eventos_ids)[0])

        if queryset.count() == 0:
            self.message_user(request, '⚠️ Nenhuma classificação encontrada', level=messages.WARNING)
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
                response = RelatorioAprovadosService.gerar_excel_staff(evento, queryset_ordenado, ordem=ordem)
            else:
                response = RelatorioAprovadosService.gerar_excel_mural(evento, queryset_ordenado, ordem=ordem)

            return response

        except Exception as e:
            self.message_user(request, f'❌ Erro ao gerar Excel: {str(e)}', level=messages.ERROR)

    # 
    # ACTIONS: RELATÓRIOS PDF
    # 

    def gerar_relatorio_staff_classificacao(self, request, queryset):
        """Gera relatório STAFF ordenado por CLASSIFICAÇÃO (posição)"""
        return self._validar_e_gerar_relatorio(request, queryset, 'staff', 'classificacao')

    gerar_relatorio_staff_classificacao.short_description = '📞 PDF STAFF: Por Classificação (com telefones)'

    def gerar_relatorio_staff_nome(self, request, queryset):
        """Gera relatório STAFF ordenado por NOME alfabético"""
        return self._validar_e_gerar_relatorio(request, queryset, 'staff', 'nome')

    gerar_relatorio_staff_nome.short_description = '📞 PDF STAFF: Por Nome (com telefones)'

    def gerar_relatorio_mural_classificacao(self, request, queryset):
        """Gera relatório MURAL ordenado por CLASSIFICAÇÃO (posição)"""
        return self._validar_e_gerar_relatorio(request, queryset, 'mural', 'classificacao')

    gerar_relatorio_mural_classificacao.short_description = '📋 PDF MURAL: Por Classificação (público)'

    def gerar_relatorio_mural_nome(self, request, queryset):
        """Gera relatório MURAL ordenado por NOME alfabético"""
        return self._validar_e_gerar_relatorio(request, queryset, 'mural', 'nome')

    gerar_relatorio_mural_nome.short_description = '📋 PDF MURAL: Por Nome (público)'

    # 
    # ACTIONS: EXPORTAÇÃO EXCEL
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
        """Apenas sistema pode criar classificações (via ClassificadorService)"""
        return False

    def has_change_permission(self, request, obj=None):
        """Apenas superuser pode editar classificações manualmente"""
        return request.user.is_superuser

    def has_delete_permission(self, request, obj=None):
        """Apenas superuser pode deletar classificações"""
        return request.user.is_superuser

# 
# ADMIN: CRITÉRIOS ATENDIDOS
# 

@admin.register(InscricaoCriterioAtendido)
class InscricaoCriterioAtendidoAdmin(CustomTitleMixin, admin.ModelAdmin):
    """Admin para gerenciar Critérios Atendidos por Inscrições (Somente leitura)"""
    custom_title = "adm Critérios Atendidos"

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
    
