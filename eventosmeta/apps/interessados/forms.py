
"""
ARQUIVO: apps/interessados/forms.py
AÇÃO: CRIAR novo arquivo apps/interessados/forms.py
MUDANÇA: Formulários de cadastro e login
"""

from django import forms
from .models import Interessado


class CadastroInteressadoForm(forms.ModelForm):
    """
    Formulário de cadastro inicial para interessados.
    Apenas campos essenciais: CPF, nome, email e senha.
    """
    senha = forms.CharField(
        label='Senha',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Crie uma senha'
        }),
        min_length=6,
        help_text='Mínimo 6 caracteres'
    )
    
    confirmar_senha = forms.CharField(
        label='Confirmar Senha',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Digite a senha novamente'
        })
    )
    
    class Meta:
        model = Interessado
        fields = ['cpf', 'nome', 'email']
        widgets = {
            'cpf': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Somente números (11 dígitos)',
                'maxlength': '11'
            }),
            'nome': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nome completo'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'seu@email.com'
            }),
        }
    
    def clean_cpf(self):
        """Valida se CPF já existe"""
        cpf = self.cleaned_data.get('cpf')
        if Interessado.objects.filter(cpf=cpf).exists():
            raise forms.ValidationError('Este CPF já está cadastrado.')
        return cpf
    
    def clean(self):
        """Valida se as senhas conferem"""
        cleaned_data = super().clean()
        senha = cleaned_data.get('senha')
        confirmar_senha = cleaned_data.get('confirmar_senha')
        
        if senha and confirmar_senha and senha != confirmar_senha:
            raise forms.ValidationError('As senhas não conferem.')
        
        return cleaned_data
    
    def save(self, commit=True):
        """Salva o interessado com senha criptografada"""
        interessado = super().save(commit=False)
        interessado.set_password(self.cleaned_data['senha'])
        
        if commit:
            interessado.save()
        
        return interessado


class LoginInteressadoForm(forms.Form):
    """
    Formulário de login para interessados usando CPF.
    """
    cpf = forms.CharField(
        label='CPF',
        max_length=11,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Digite seu CPF (somente números)',
            'autofocus': True,
            'maxlength': '11'
        })
    )
    
    senha = forms.CharField(
        label='Senha',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Digite sua senha'
        })
    )