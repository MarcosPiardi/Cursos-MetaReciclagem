from django import forms
from django.contrib.auth.forms import AuthenticationForm


class LoginStaffForm(AuthenticationForm):
    """
    Formulário de login para staff/administradores.
    Usa username e password (padrão Django).
    """
    username = forms.CharField(
        label='Usuário',
        max_length=150,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Digite seu usuário',
            'autofocus': True
        })
    )
    
    password = forms.CharField(
        label='Senha',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Digite sua senha'
        })
    )