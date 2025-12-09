"""
Formulários do app PORTAL - Sistema MetaReciclagem
Arquivo: apps/portal/forms.py
Data: 05/12/2025
"""
from django import forms
from apps.interessados.models import Interessado


class LoginInteressadoForm(forms.Form):
    """
    Formulário de login para interessados
    Login com CPF e senha
    """
    cpf = forms.CharField(
        label='CPF',
        max_length=11,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Digite seu CPF (somente números)',
            'autofocus': True,
            'pattern': '[0-9]{11}',
            'title': 'Digite 11 dígitos numéricos'
        })
    )
    
    senha = forms.CharField(
        label='Senha',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Digite sua senha'
        })
    )
    
    def clean_cpf(self):
        """Remove caracteres não numéricos do CPF"""
        cpf = self.cleaned_data.get('cpf', '')
        # Remove pontos, traços e espaços
        cpf = ''.join(filter(str.isdigit, cpf))
        
        if len(cpf) != 11:
            raise forms.ValidationError('CPF deve conter 11 dígitos')
        
        return cpf
    
    def clean(self):
        """Valida CPF e senha"""
        cleaned_data = super().clean()
        cpf = cleaned_data.get('cpf')
        senha = cleaned_data.get('senha')
        
        if cpf and senha:
            try:
                interessado = Interessado.objects.get(cpf=cpf)
                
                # Verificar se está ativo
                if not interessado.is_active:
                    raise forms.ValidationError(
                        'Sua conta está inativa. Entre em contato com a administração.'
                    )
                
                # Verificar senha
                if not interessado.check_password(senha):
                    raise forms.ValidationError('CPF ou senha incorretos.')
                
                # Armazenar o interessado para uso posterior
                self.interessado = interessado
                
            except Interessado.DoesNotExist:
                raise forms.ValidationError('CPF ou senha incorretos.')
        
        return cleaned_data


class ConsultaPublicaForm(forms.Form):
    """
    Formulário de consulta pública de resultados
    Consulta por CPF sem necessidade de login
    """
    cpf = forms.CharField(
        label='CPF',
        max_length=11,
        widget=forms.TextInput(attrs={
            'class': 'form-control form-control-lg',
            'placeholder': 'Digite seu CPF para consultar',
            'autofocus': True,
            'pattern': '[0-9]{11}',
            'title': 'Digite 11 dígitos numéricos'
        })
    )
    
    def clean_cpf(self):
        """Remove caracteres não numéricos do CPF"""
        cpf = self.cleaned_data.get('cpf', '')
        cpf = ''.join(filter(str.isdigit, cpf))
        
        if len(cpf) != 11:
            raise forms.ValidationError('CPF deve conter 11 dígitos')
        
        return cpf
    