"""
ARQUIVO: apps/cursoseoutros/forms.py
AÇÃO: CRIAR arquivo completo
MUDANÇA: Formulários customizados para inscrição em eventos e gestão de turmas
DATA/HORA: 2025-10-29 15:00:00
"""

from django import forms
from django.core.exceptions import ValidationError
from django.utils import timezone
from datetime import date
from .models import (
    Evento, Inscricao, Turma, Matricula, Avaliacao,
    Criterio, EventoCriterio, InscricaoCriterioAtendido
)


# ============================================
# FORM: INSCRIÇÃO EM EVENTO (PÚBLICO)
# ============================================

class InscricaoEventoForm(forms.ModelForm):
    """
    Formulário para interessado se inscrever em evento.
    Usado na área pública do sistema.
    """
    
    aceite_termos = forms.BooleanField(
        label='Li e aceito os termos e condições',
        required=True,
        error_messages={
            'required': 'Você precisa aceitar os termos para se inscrever.'
        }
    )
    
    class Meta:
        model = Inscricao
        fields = ['evento']
        widgets = {
            'evento': forms.HiddenInput()  # Evento já vem selecionado
        }
    
    def __init__(self, *args, **kwargs):
        self.interessado = kwargs.pop('interessado', None)
        self.evento = kwargs.pop('evento', None)
        super().__init__(*args, **kwargs)
        
        if self.evento:
            self.fields['evento'].initial = self.evento
    
    def clean_evento(self):
        """Valida se o evento aceita inscrições"""
        evento = self.cleaned_data.get('evento')
        
        if not evento:
            raise ValidationError('Evento não informado.')
        
        # Verifica se status permite inscrição
        if not evento.status.permite_inscricao:
            raise ValidationError(
                f'Este evento não está aceitando inscrições. '
                f'Status atual: {evento.status.status}'
            )
        
        # Verifica período de inscrição
        hoje = date.today()
        
        if evento.inicio_inscricoes and hoje < evento.inicio_inscricoes:
            raise ValidationError(
                f'As inscrições ainda não foram abertas. '
                f'Início: {evento.inicio_inscricoes.strftime("%d/%m/%Y")}'
            )
        
        if evento.fim_inscricoes and hoje > evento.fim_inscricoes:
            raise ValidationError(
                f'O período de inscrições foi encerrado em '
                f'{evento.fim_inscricoes.strftime("%d/%m/%Y")}.'
            )
        
        return evento
    
    def clean(self):
        """Validações gerais"""
        cleaned_data = super().clean()
        evento = cleaned_data.get('evento')
        
        if evento and self.interessado:
            # Verifica se já está inscrito
            if Inscricao.objects.filter(
                evento=evento,
                interessado=self.interessado
            ).exists():
                raise ValidationError(
                    'Você já está inscrito neste evento.'
                )
        
        return cleaned_data
    
    def save(self, commit=True):
        """Salva a inscrição vinculando ao interessado"""
        inscricao = super().save(commit=False)
        inscricao.interessado = self.interessado
        inscricao.status = 'INSCRITO'
        
        if commit:
            inscricao.save()
        
        return inscricao


# ============================================
# FORM: CADASTRO/EDIÇÃO DE EVENTO (STAFF)
# ============================================

class EventoForm(forms.ModelForm):
    """
    Formulário completo para cadastro/edição de eventos.
    Usado pela equipe administrativa.
    """
    
    class Meta:
        model = Evento
        fields = [
            'descricao', 'status', 'modalidade', 'docente',
            'programa', 'objetivo', 'pre_requisito', 'carga_horaria',
            'vagas', 'vagas_minimas',
            'inicio_inscricoes', 'fim_inscricoes',
            'inicio_matricula', 'fim_matricula',
            'inicio_aulas', 'fim_aulas', 'horario_aulas',
            'local', 'endereco_local', 'observacao'
        ]
        widgets = {
            'descricao': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ex: Curso de Informática Básica'
            }),
            'programa': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Descreva o conteúdo programático...'
            }),
            'objetivo': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Objetivos do curso...'
            }),
            'pre_requisito': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 2,
                'placeholder': 'Pré-requisitos necessários...'
            }),
            'carga_horaria': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ex: 40 horas'
            }),
            'docente': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nome do instrutor'
            }),
            'vagas': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': 1
            }),
            'vagas_minimas': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': 1
            }),
            'inicio_inscricoes': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'fim_inscricoes': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'inicio_matricula': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'fim_matricula': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'inicio_aulas': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'fim_aulas': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'horario_aulas': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ex: Segunda a Sexta, 14h às 18h'
            }),
            'local': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ex: Sala 3, Lab. de Informática'
            }),
            'endereco_local': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Endereço completo'
            }),
            'observacao': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3
            }),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'modalidade': forms.Select(attrs={'class': 'form-control'}),
        }
    
    def clean(self):
        """Validações de datas"""
        cleaned_data = super().clean()
        
        # Valida período de inscrições
        inicio_insc = cleaned_data.get('inicio_inscricoes')
        fim_insc = cleaned_data.get('fim_inscricoes')
        
        if inicio_insc and fim_insc and fim_insc < inicio_insc:
            raise ValidationError({
                'fim_inscricoes': 'Data final de inscrições deve ser posterior à data inicial.'
            })
        
        # Valida período de matrículas
        inicio_mat = cleaned_data.get('inicio_matricula')
        fim_mat = cleaned_data.get('fim_matricula')
        
        if inicio_mat and fim_mat and fim_mat < inicio_mat:
            raise ValidationError({
                'fim_matricula': 'Data final de matrículas deve ser posterior à data inicial.'
            })
        
        # Valida período de aulas
        inicio_aulas = cleaned_data.get('inicio_aulas')
        fim_aulas = cleaned_data.get('fim_aulas')
        
        if inicio_aulas and fim_aulas and fim_aulas < inicio_aulas:
            raise ValidationError({
                'fim_aulas': 'Data final das aulas deve ser posterior à data inicial.'
            })
        
        # Valida vagas
        vagas = cleaned_data.get('vagas')
        vagas_min = cleaned_data.get('vagas_minimas')
        
        if vagas and vagas_min and vagas_min > vagas:
            raise ValidationError({
                'vagas_minimas': 'Vagas mínimas não pode ser maior que o total de vagas.'
            })
        
        return cleaned_data


# ============================================
# FORM: ADICIONAR CRITÉRIO AO EVENTO
# ============================================

class EventoCriterioForm(forms.ModelForm):
    """
    Formulário para adicionar/configurar critérios em um evento.
    """
    
    class Meta:
        model = EventoCriterio
        fields = [
            'criterio', 'peso', 'tipo_reserva', 'vagas_reservadas',
            'ordem', 'ordem_idade', 'idade_minima', 'idade_maxima',
            'observacao'
        ]
        widgets = {
            'criterio': forms.Select(attrs={'class': 'form-control'}),
            'peso': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': 0,
                'max': 10
            }),
            'tipo_reserva': forms.Select(attrs={'class': 'form-control'}),
            'vagas_reservadas': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': 0
            }),
            'ordem': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': 1
            }),
            'ordem_idade': forms.Select(attrs={'class': 'form-control'}),
            'idade_minima': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': 0,
                'max': 120
            }),
            'idade_maxima': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': 0,
                'max': 120
            }),
            'observacao': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 2
            }),
        }
    
    def clean(self):
        """Validações"""
        cleaned_data = super().clean()
        
        # Valida faixa etária
        idade_min = cleaned_data.get('idade_minima')
        idade_max = cleaned_data.get('idade_maxima')
        
        if idade_min and idade_max and idade_max < idade_min:
            raise ValidationError({
                'idade_maxima': 'Idade máxima deve ser maior que idade mínima.'
            })
        
        # Valida vagas reservadas
        tipo_reserva = cleaned_data.get('tipo_reserva')
        vagas_reservadas = cleaned_data.get('vagas_reservadas')
        
        if tipo_reserva == 'PERCENTUAL' and vagas_reservadas:
            if vagas_reservadas > 100:
                raise ValidationError({
                    'vagas_reservadas': 'Percentual não pode ser maior que 100.'
                })
        
        return cleaned_data


# ============================================
# FORM: VALIDAÇÃO DE CRITÉRIO CUSTOMIZADO
# ============================================

class ValidarCriterioCustomizadoForm(forms.ModelForm):
    """
    Formulário para staff validar se interessado atende critério customizado.
    """
    
    class Meta:
        model = InscricaoCriterioAtendido
        fields = ['validado', 'pontos_obtidos']
        widgets = {
            'validado': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'pontos_obtidos': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': 0,
                'step': 0.01
            }),
        }
    
    def save(self, commit=True, validado_por=None):
        """Salva a validação com informações do validador"""
        instancia = super().save(commit=False)
        
        if instancia.validado and validado_por:
            instancia.validado_por = validado_por
            instancia.data_validacao = timezone.now()
        
        if commit:
            instancia.save()
        
        return instancia


# ============================================
# FORM: CADASTRO DE TURMA
# ============================================

class TurmaForm(forms.ModelForm):
    """
    Formulário para criação/edição de turmas.
    """
    
    class Meta:
        model = Turma
        fields = [
            'descricao_turma', 'evento', 'data_inicio', 'data_fim',
            'horario_aulas', 'local_aulas'
        ]
        widgets = {
            'descricao_turma': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ex: Turma A - Manhã'
            }),
            'evento': forms.Select(attrs={'class': 'form-control'}),
            'data_inicio': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'data_fim': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'horario_aulas': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ex: Segunda a Sexta, 8h às 12h'
            }),
            'local_aulas': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ex: Sala 3'
            }),
        }
    
    def clean(self):
        """Valida período"""
        cleaned_data = super().clean()
        
        data_inicio = cleaned_data.get('data_inicio')
        data_fim = cleaned_data.get('data_fim')
        
        if data_inicio and data_fim and data_fim < data_inicio:
            raise ValidationError({
                'data_fim': 'Data final deve ser posterior à data inicial.'
            })
        
        return cleaned_data


# ============================================
# FORM: MATRÍCULA EM TURMA
# ============================================

class MatriculaForm(forms.ModelForm):
    """
    Formulário para matricular interessado em turma.
    """
    
    class Meta:
        model = Matricula
        fields = ['turma', 'interessado', 'status']
        widgets = {
            'turma': forms.Select(attrs={'class': 'form-control'}),
            'interessado': forms.Select(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
        }
    
    def clean(self):
        """Valida matrícula"""
        cleaned_data = super().clean()
        
        turma = cleaned_data.get('turma')
        interessado = cleaned_data.get('interessado')
        
        if turma and interessado:
            # Verifica se já está matriculado
            if Matricula.objects.filter(
                turma=turma,
                interessado=interessado
            ).exists():
                raise ValidationError(
                    'Este interessado já está matriculado nesta turma.'
                )
            
            # Verifica vagas disponíveis
            vagas_ocupadas = turma.total_alunos()
            if vagas_ocupadas >= turma.evento.vagas:
                raise ValidationError(
                    f'Esta turma já está com todas as vagas ocupadas '
                    f'({turma.evento.vagas} vagas).'
                )
        
        return cleaned_data


# ============================================
# FORM: AVALIAÇÃO DO ALUNO
# ============================================

class AvaliacaoForm(forms.ModelForm):
    """
    Formulário para lançamento de frequência, nota e aprovação.
    """
    
    class Meta:
        model = Avaliacao
        fields = ['frequencia', 'nota', 'aprovado', 'emite_certificado']
        widgets = {
            'frequencia': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': 0,
                'max': 100,
                'step': 0.01,
                'placeholder': 'Ex: 85.5'
            }),
            'nota': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': 0,
                'max': 10,
                'step': 0.01,
                'placeholder': 'Ex: 7.5'
            }),
            'aprovado': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'emite_certificado': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
    
    def clean(self):
        """Validações automáticas"""
        cleaned_data = super().clean()
        
        frequencia = cleaned_data.get('frequencia')
        nota = cleaned_data.get('nota')
        aprovado = cleaned_data.get('aprovado')
        
        # Sugestão automática de aprovação
        # (frequência >= 75% E nota >= 6.0)
        if frequencia is not None and nota is not None:
            if frequencia >= 75 and nota >= 6.0:
                # Sugestão: marcar como aprovado
                if not aprovado:
                    self.add_error(
                        None,
                        'Sugestão: Este aluno atende aos critérios de aprovação '
                        '(frequência ≥75% e nota ≥6.0). Considere marcá-lo como aprovado.'
                    )
        
        # Se emite certificado, deve estar aprovado
        emite_cert = cleaned_data.get('emite_certificado')
        if emite_cert and not aprovado:
            raise ValidationError({
                'emite_certificado': 'Só é possível emitir certificado para alunos aprovados.'
            })
        
        return cleaned_data


# ============================================
# FORM: FILTRO DE EVENTOS (BUSCA)
# ============================================

class FiltroEventosForm(forms.Form):
    """
    Formulário para filtrar eventos na listagem pública.
    """
    busca = forms.CharField(
        label='Buscar',
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Nome do curso, instrutor...'
        })
    )
    
    status = forms.ModelChoiceField(
        label='Status',
        queryset=None,
        required=False,
        empty_label='Todos',
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    
    modalidade = forms.ChoiceField(
        label='Modalidade',
        choices=[('', 'Todas')] + list(Evento._meta.get_field('modalidade').choices),
        required=False,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Carrega apenas status que permitem inscrição
        from .models import Status
        self.fields['status'].queryset = Status.objects.filter(permite_inscricao=True)