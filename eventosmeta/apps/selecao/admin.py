"""
Admin do app SELEÇÃO
Arquivo: apps/selecao/admin.py

Alteração: Adicionados relatórios PDF e Excel com opções de ordenação
Data: 12/01/2026

Alteração: Registrados todos os models no admin_site customizado (melhor prática)
Data: 20/01/2026

Alteração: Adicionada action de matrícula em lote na Classificação
Alteração: Corrigido import ACTION_CHECKBOX_NAME para Django 5.2.4
Alteração: Action de matrícula corrigida com validação melhorada
Data: 30/01/2026

Alteração: Corrigido reconstrução do queryset no POST da action
Alteração: Correção definitiva da action com preservação de IDs
Alteração: Versão final limpa e corrigida - matrícula em lote funcional
Alteração: Busca case-insensitive para status (Ativa/ATIVA/ativa)
Alteração: Versão final limpa - matrícula em lote funcional
Data: 02/02/2026
"""

from django import forms
from django.contrib import admin
from django.contrib.admin.helpers import ACTION_CHECKBOX_NAME
from django.shortcuts import render, redirect
from django.contrib import messages
from django.db import transaction
from django.utils.html import format_html
from django.http import HttpResponseRedirect

from apps.accounts.admin import admin_site
from apps.eventos.models import Turma
from apps.academico.models import Matricula, StatusMatricula

from .models import StatusInscricao, Inscricao, Classificacao, InscricaoCriterioAtendido


# ==========================================
# FORM INTERMEDIÁRIO PARA SELEÇÃO DE TURMA
# ==========================================

class MatricularAlunosForm(forms.Form):
    """Form intermediário para selecionar turma antes de matricular"""
    
    _selected_action = forms.CharField(widget=forms.MultipleHiddenInput, required=False)
    action = forms.CharField(widget=forms.HiddenInput, initial='matricular_alunos_action')
    
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
                self.fields['turma'].help_text = '⚠️ Nenhuma turma cadastrada para este evento. Crie uma turma primeiro.'


# ==========================================
# STATUS INSCRIÇÃO
# ==========================================

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


@admin.register(StatusInscricao, site=admin_site)
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


# ==========================================
# INSCRIÇÃO
# ==========================================

@admin.register(Inscricao, site=admin_site)
class InscricaoAdmin(admin.ModelAdmin):
    list_display = ['get_interessado', 'evento', 'status', 'data_inscricao']
    list_filter = ['status', 'evento', 'data_inscricao']
    search_fields = ['interessado__nome', 'interessado__cpf', 'evento__nome']
    date_hierarchy = 'data_inscricao'
    ordering = ['-data_inscricao']

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
        return obj.interessado.nome
    get_interessado.short_description = 'Interessado'
    get_interessado.admin_order_field = 'interessado__nome'


# ==========================================
# CLASSIFICAÇÃO (COM ACTION DE MATRÍCULA)
# ==========================================

@admin.register(Classificacao, site=admin_site)
class ClassificacaoAdmin(admin.ModelAdmin):
    list_display = [
        'posicao',
        'get_interessado',
        'get_cpf',
        'get_evento',
        'pontuacao_total',
        'classificado',
        'lista_espera',
        'get_status_inscricao'
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
    
    actions = ['matricular_alunos_action']

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

    readonly_fields = ['processado_em', 'atualizado_em']

    def get_interessado(self, obj):
        return obj.inscricao.interessado.nome
    get_interessado.short_description = 'Interessado'
    get_interessado.admin_order_field = 'inscricao__interessado__nome'

    def get_cpf(self, obj):
        cpf = obj.inscricao.interessado.cpf
        return f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"
    get_cpf.short_description = 'CPF'

    def get_evento(self, obj):
        return obj.inscricao.evento.nome
    get_evento.short_description = 'Evento'
    get_evento.admin_order_field = 'inscricao__evento__nome'

    def get_status_inscricao(self, obj):
        status = obj.inscricao.status
        return format_html(
            '<span style="display: inline-block; padding: 3px 8px; '
            'background-color: {}; color: white; border-radius: 3px; font-size: 11px;">{}</span>',
            status.cor,
            status.nome
        )
    get_status_inscricao.short_description = 'Status Inscrição'
    get_status_inscricao.admin_order_field = 'inscricao__status__nome'

    def matricular_alunos_action(self, request, queryset):
        """
        Action para matricular alunos selecionados em uma turma
        """
        # POST: Processar matrícula com turma selecionada
        if 'confirmar_matricula' in request.POST:
            # Reconstruir queryset a partir dos IDs
            ids = request.POST.getlist('_selected_action')
            ids = [int(id) for id in ids if id.isdigit()]
            
            if not ids:
                self.message_user(
                    request,
                    '❌ Nenhum aluno foi selecionado.',
                    level=messages.ERROR
                )
                return HttpResponseRedirect(request.get_full_path())
            
            queryset = Classificacao.objects.filter(pk__in=ids)
            queryset = queryset.select_related('inscricao__evento', 'inscricao__interessado')
            
            if queryset.count() == 0:
                self.message_user(
                    request,
                    '❌ Classificações não encontradas.',
                    level=messages.ERROR
                )
                return HttpResponseRedirect(request.get_full_path())
            
            evento = queryset.first().inscricao.evento
            form = MatricularAlunosForm(request.POST, evento=evento)
            
            if not form.is_valid():
                for field, errors in form.errors.items():
                    for error in errors:
                        self.message_user(request, f'❌ {field}: {error}', level=messages.ERROR)
                return HttpResponseRedirect(request.get_full_path())
            
            turma = form.cleaned_data['turma']
            
            # Validar que a turma pertence ao evento
            if turma.evento != evento:
                self.message_user(
                    request,
                    f'❌ A turma "{turma.nome}" não pertence ao evento "{evento.nome}".',
                    level=messages.ERROR
                )
                return HttpResponseRedirect(request.get_full_path())
            
            # Buscar status necessários (CASE-INSENSITIVE)
            try:
                status_matricula_ativa = StatusMatricula.objects.get(nome__iexact='ativa')
            except StatusMatricula.DoesNotExist:
                self.message_user(
                    request,
                    '❌ Status de matrícula "Ativa" não encontrado. Crie-o no menu Acadêmico > Status de Matrículas.',
                    level=messages.ERROR
                )
                return HttpResponseRedirect(request.get_full_path())
            
            try:
                status_inscricao_confirmada = StatusInscricao.objects.get(nome__iexact='confirmada')
            except StatusInscricao.DoesNotExist:
                self.message_user(
                    request,
                    '❌ Status de inscrição "Confirmada" não encontrado. Crie-o no menu Seleção > Status de Inscrições.',
                    level=messages.ERROR
                )
                return HttpResponseRedirect(request.get_full_path())
            
            # Processar matrículas
            matriculas_criadas = 0
            erros = []
            
            with transaction.atomic():
                for classificacao in queryset:
                    try:
                        inscricao = classificacao.inscricao
                        interessado = inscricao.interessado
                        
                        # Verificar se já existe matrícula
                        if Matricula.objects.filter(turma=turma, interessado=interessado).exists():
                            erros.append(f'{interessado.nome} já está matriculado nesta turma.')
                            continue
                        
                        # Criar matrícula
                        Matricula.objects.create(
                            turma=turma,
                            interessado=interessado,
                            inscricao=inscricao,
                            status=status_matricula_ativa
                        )
                        
                        # Atualizar status da inscrição
                        inscricao.status = status_inscricao_confirmada
                        inscricao.save()
                        
                        matriculas_criadas += 1
                        
                    except Exception as e:
                        erros.append(f'{interessado.nome}: {str(e)}')
            
            # Mensagens de feedback
            if matriculas_criadas > 0:
                self.message_user(
                    request,
                    f'✅ {matriculas_criadas} matrícula(s) criada(s) com sucesso na turma "{turma.nome}"!',
                    level=messages.SUCCESS
                )
            
            if erros:
                for erro in erros:
                    self.message_user(request, f'⚠️ {erro}', level=messages.WARNING)
            
            if matriculas_criadas == 0 and len(erros) == 0:
                self.message_user(
                    request,
                    '⚠️ Nenhuma matrícula foi processada.',
                    level=messages.WARNING
                )
            
            return HttpResponseRedirect(request.get_full_path())
        
        # GET: Mostrar tela de seleção de turma
        queryset = queryset.select_related('inscricao__evento', 'inscricao__interessado')
        
        if queryset.count() == 0:
            self.message_user(request, '❌ Nenhuma classificação selecionada.', level=messages.ERROR)
            return
        
        # Verificar eventos únicos
        eventos_unicos = set()
        for classificacao in queryset:
            if classificacao.inscricao and classificacao.inscricao.evento:
                eventos_unicos.add(classificacao.inscricao.evento.id)
        
        if len(eventos_unicos) > 1:
            self.message_user(
                request,
                '❌ Selecione apenas classificações do MESMO EVENTO.',
                level=messages.ERROR
            )
            return
        
        evento = queryset.first().inscricao.evento
        
        # Verificar turmas disponíveis
        if Turma.objects.filter(evento=evento).count() == 0:
            self.message_user(
                request,
                f'❌ O evento "{evento.nome}" não possui turmas cadastradas.',
                level=messages.ERROR
            )
            return
        
        # Preparar formulário
        form = MatricularAlunosForm(evento=evento)
        ids = ','.join(str(c.pk) for c in queryset)
        
        context = {
            'title': 'Matricular Alunos Selecionados',
            'form': form,
            'classificacoes': queryset,
            'evento': evento,
            'ids': ids,
            'opts': self.model._meta,
            'action_checkbox_name': ACTION_CHECKBOX_NAME,
        }
        
        return render(request, 'admin/selecao/matricular_alunos.html', context)
    
    matricular_alunos_action.short_description = '🎓 Matricular alunos selecionados'


# ==========================================
# CRITÉRIOS ATENDIDOS
# ==========================================

@admin.register(InscricaoCriterioAtendido, site=admin_site)
class InscricaoCriterioAtendidoAdmin(admin.ModelAdmin):
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
        ('Validação', {
            'fields': ('validado', 'observacao_validacao')
        }),
    )

    def get_interessado(self, obj):
        return obj.inscricao.interessado.nome
    get_interessado.short_description = 'Interessado'

    def get_evento(self, obj):
        return obj.inscricao.evento.nome
    get_evento.short_description = 'Evento'