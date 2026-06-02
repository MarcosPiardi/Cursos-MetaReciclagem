"""
Formularios do app PORTAL - Sistema MetaReciclagem
Arquivo: apps/portal/forms.py
Atualizações
 - 05/12/2025 - Criação do arquivo
 - 29/05/2026 - Busca por cpf_hash em vez de cpf (EncryptedCharField)
                Adicionada validação de conta ativa
                max_length=14 nos campos CPF para aceitar entrada formatada

"""



from django import forms
from apps.interessados.models import Interessado, gerar_hash_cpf


class LoginInteressadoForm(forms.Form):
    """
    Formulario de login para interessados
    Login com CPF e senha
    """
    cpf = forms.CharField(
        label='CPF',
        max_length=14,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Digite seu CPF (somente numeros)',
            'autofocus': True,
            'pattern': '[0-9]{11}',
            'title': 'Digite 11 digitos numericos'
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
        """Remove caracteres nao numericos do CPF"""
        cpf = self.cleaned_data.get('cpf', '')
        cpf = ''.join(filter(str.isdigit, cpf))

        if len(cpf) != 11:
            raise forms.ValidationError('CPF deve conter 11 digitos')

        return cpf

    def clean(self):
        """Valida CPF e senha"""
        cleaned_data = super().clean()
        cpf = cleaned_data.get('cpf')
        senha = cleaned_data.get('senha')

        if cpf and senha:
            try:
                interessado = Interessado.objects.get(cpf_hash=gerar_hash_cpf(cpf))

                if not interessado.is_active:
                    raise forms.ValidationError(
                        'Sua conta esta inativa. Entre em contato com a administracao.'
                    )

                if not interessado.check_password(senha):
                    raise forms.ValidationError('CPF ou senha incorretos.')

                self.interessado = interessado

            except Interessado.DoesNotExist:
                raise forms.ValidationError('CPF ou senha incorretos.')

        return cleaned_data


class ConsultaPublicaForm(forms.Form):
    """
    Formulario de consulta publica de resultados
    Consulta por CPF sem necessidade de login
    """
    cpf = forms.CharField(
        label='CPF',
        max_length=14,
        widget=forms.TextInput(attrs={
            'class': 'form-control form-control-lg',
            'placeholder': 'Digite seu CPF para consultar',
            'autofocus': True,
            'pattern': '[0-9]{11}',
            'title': 'Digite 11 digitos numericos'
        })
    )

    def clean_cpf(self):
        """Remove caracteres nao numericos do CPF"""
        cpf = self.cleaned_data.get('cpf', '')
        cpf = ''.join(filter(str.isdigit, cpf))

        if len(cpf) != 11:
            raise forms.ValidationError('CPF deve conter 11 digitos')

        return cpf
    
