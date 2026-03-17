"""
Arquivo: forms.py
Caminho: apps/interessados/forms.py
Alterações anteriores:
- Valores padrão para UF Nascimento e Nacionalidade + Senha criptografada (28/01/2026)
- REMOVIDO raca_cor (duplicado de fototipo) + Senha criptografada (26/01/2026)
- LoginInteressadoForm corrigido para validar erros no formulário (30/01/2026)
- Adicionada verificação de is_active no LoginInteressadoForm (13/02/2026)
- clean_email adicionado em CadastroInteressadoForm e EdicaoInteressadoForm (26/02/2026)
- clean_cpf atualizado com validação de dígitos verificadores (16/03/2026)
- Buscas por CPF migradas para cpf_hash (17/03/2026)

Alteração: Adicionado campo consentimento_lgpd no CadastroInteressadoForm
           save() registra data/hora do aceite em consentimento_lgpd_em
Data: 17/03/2026
"""

from django import forms
from django.contrib.auth.hashers import check_password
from django.utils import timezone
from .models import Interessado, Sexo, Fototipo, gerar_hash_cpf


class CadastroInteressadoForm(forms.ModelForm):
    """
    Formulário COMPLETO de cadastro para interessados.
    Valores padrão: UF Nascimento = SP, Nacionalidade = Brasileira
    """
    senha = forms.CharField(
        label='Senha',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Mínimo 6 caracteres'
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

    # ============================================================
    # LGPD — ADICIONADO 17/03/2026
    # Campo fora do Meta.fields pois é tratado manualmente no save()
    # ============================================================
    consentimento_lgpd = forms.BooleanField(
        label='Declaro que li e aceito o Termo de Consentimento para o tratamento dos meus dados pessoais conforme a LGPD.',
        required=True,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        error_messages={'required': 'Você deve aceitar o termo de consentimento para se cadastrar.'}
    )

    class Meta:
        model = Interessado
        fields = [
            # DADOS PESSOAIS
            'nome', 'cpf', 'rg', 'data_nascimento', 'sexo',
            'cidade_nascimento', 'uf_nascimento', 'nacionalidade',
            'fototipo', 'escolaridade',

            # ENDEREÇO
            'cep', 'endereco_residencial', 'num_endereco', 'bairro',
            'complemento', 'cidade_residencia', 'uf_residencia',

            # CONTATO
            'telefone', 'celular', 'email',

            # PROGRAMA SOCIAL / NIS
            'programa_social', 'num_nis',

            # PCD
            'necessidades_especiais', 'pcd_fisica', 'pcd_visual',
            'pcd_auditiva', 'pcd_intelectual', 'pcd_psicossocial', 'pcd_multiplas',

            # RESPONSÁVEL
            'nome_responsavel', 'telefone_responsavel', 'celular_responsavel',
            'email_responsavel',

            # OBSERVAÇÕES
            'observacao',
        ]

        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome completo'}),
            'cpf': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '000.000.000-00'}),
            'rg': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '00.000.000-0'}),
            'data_nascimento': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'sexo': forms.Select(attrs={'class': 'form-select'}),
            'cidade_nascimento': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Cidade onde nasceu'}),
            'uf_nascimento': forms.TextInput(attrs={'class': 'form-control', 'value': 'SP', 'maxlength': '2', 'style': 'text-transform: uppercase;'}),
            'nacionalidade': forms.TextInput(attrs={'class': 'form-control', 'value': 'Brasileira'}),
            'fototipo': forms.Select(attrs={'class': 'form-select'}),
            'escolaridade': forms.Select(attrs={'class': 'form-select'}),
            'cep': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '00000-000'}),
            'endereco_residencial': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Rua, Avenida...'}),
            'num_endereco': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Número'}),
            'bairro': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Bairro'}),
            'complemento': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Apto, Bloco...'}),
            'cidade_residencia': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Cidade'}),
            'uf_residencia': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'SP', 'maxlength': '2', 'style': 'text-transform: uppercase;'}),
            'telefone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '(15) 3999-9999'}),
            'celular': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '(15) 99999-9999'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'seu@email.com'}),
            'programa_social': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'num_nis': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '000.00000.00-0'}),
            'necessidades_especiais': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'pcd_fisica': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'pcd_visual': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'pcd_auditiva': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'pcd_intelectual': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'pcd_psicossocial': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'pcd_multiplas': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'nome_responsavel': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome completo do responsável'}),
            'telefone_responsavel': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '(15) 3999-9999'}),
            'celular_responsavel': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '(15) 99999-9999'}),
            'email_responsavel': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'email@responsavel.com'}),
            'observacao': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Informações adicionais (opcional)', 'rows': 3}),
        }

        labels = {
            'nome': 'Nome Completo',
            'cpf': 'CPF',
            'rg': 'RG/Identidade',
            'data_nascimento': 'Data de Nascimento',
            'sexo': 'Sexo',
            'cidade_nascimento': 'Cidade de Nascimento',
            'uf_nascimento': 'UF de Nascimento',
            'nacionalidade': 'Nacionalidade',
            'fototipo': 'Fototipo/Raça-Cor (Tom de Pele)',
            'escolaridade': 'Escolaridade',
            'cep': 'CEP',
            'endereco_residencial': 'Endereço',
            'num_endereco': 'Número',
            'bairro': 'Bairro',
            'complemento': 'Complemento',
            'cidade_residencia': 'Cidade',
            'uf_residencia': 'UF',
            'telefone': 'Telefone Fixo',
            'celular': 'Celular',
            'email': 'E-mail',
            'programa_social': 'Participa de Programa Social (Bolsa Família, etc.)',
            'num_nis': 'Número NIS',
            'necessidades_especiais': 'Possui Necessidades Especiais',
            'pcd_fisica': 'Deficiência Física',
            'pcd_visual': 'Deficiência Visual',
            'pcd_auditiva': 'Deficiência Auditiva',
            'pcd_intelectual': 'Deficiência Intelectual',
            'pcd_psicossocial': 'Deficiência Psicossocial',
            'pcd_multiplas': 'Deficiências Múltiplas',
            'nome_responsavel': 'Nome do Responsável',
            'telefone_responsavel': 'Telefone do Responsável',
            'celular_responsavel': 'Celular do Responsável',
            'email_responsavel': 'E-mail do Responsável',
            'observacao': 'Observações',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if not self.data:
            self.initial['uf_nascimento'] = 'SP'
            self.initial['nacionalidade'] = 'Brasileira'

    def clean_cpf(self):
        """Remove formatação, valida dígitos verificadores e unicidade via hash"""
        cpf = self.cleaned_data.get('cpf', '')
        cpf = ''.join(filter(str.isdigit, cpf))

        if len(cpf) != 11:
            raise forms.ValidationError('CPF deve ter 11 dígitos.')

        if len(set(cpf)) == 1:
            raise forms.ValidationError('CPF inválido.')

        soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
        resto = (soma * 10) % 11
        if resto == 10:
            resto = 0
        if resto != int(cpf[9]):
            raise forms.ValidationError('CPF inválido.')

        soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
        resto = (soma * 10) % 11
        if resto == 10:
            resto = 0
        if resto != int(cpf[10]):
            raise forms.ValidationError('CPF inválido.')

        if Interessado.objects.filter(cpf_hash=gerar_hash_cpf(cpf)).exists():
            raise forms.ValidationError('Este CPF já está cadastrado.')

        return cpf

    def clean_email(self):
        """Converte e-mail vazio para None e valida unicidade"""
        email = (self.cleaned_data.get('email') or '').strip()
        if not email:
            return None
        qs = Interessado.objects.filter(email__iexact=email)
        if self.instance.pk:
            qs = qs.exclude(pk=self.instance.pk)
        if qs.exists():
            raise forms.ValidationError('Este e-mail já está cadastrado.')
        return email

    def clean_rg(self):
        rg = self.cleaned_data.get('rg', '')
        return rg.replace('.', '').replace('-', '').strip()

    def clean_cep(self):
        cep = self.cleaned_data.get('cep', '')
        cep = ''.join(filter(str.isdigit, cep))
        if cep and len(cep) != 8:
            raise forms.ValidationError('CEP deve ter 8 dígitos.')
        return cep

    def clean_telefone(self):
        return ''.join(filter(str.isdigit, self.cleaned_data.get('telefone', '')))

    def clean_celular(self):
        return ''.join(filter(str.isdigit, self.cleaned_data.get('celular', '')))

    def clean_num_nis(self):
        return ''.join(filter(str.isdigit, self.cleaned_data.get('num_nis', '')))

    def clean_telefone_responsavel(self):
        return ''.join(filter(str.isdigit, self.cleaned_data.get('telefone_responsavel', '')))

    def clean_celular_responsavel(self):
        return ''.join(filter(str.isdigit, self.cleaned_data.get('celular_responsavel', '')))

    def clean_uf_residencia(self):
        return self.cleaned_data.get('uf_residencia', '').strip().upper()

    def clean_uf_nascimento(self):
        return self.cleaned_data.get('uf_nascimento', '').strip().upper()

    def clean(self):
        cleaned_data = super().clean()
        senha = cleaned_data.get('senha')
        confirmar_senha = cleaned_data.get('confirmar_senha')
        if senha and confirmar_senha and senha != confirmar_senha:
            raise forms.ValidationError('As senhas não conferem.')
        return cleaned_data

    def save(self, commit=True):
        """Salva com senha criptografada, cpf_hash e registro do consentimento LGPD"""
        interessado = super().save(commit=False)
        interessado.set_password(self.cleaned_data['senha'])
        interessado.cpf_hash = gerar_hash_cpf(self.cleaned_data['cpf'])

        # Registra consentimento LGPD com data/hora
        interessado.consentimento_lgpd = True
        interessado.consentimento_lgpd_em = timezone.now()

        if commit:
            interessado.save()

        return interessado


class LoginInteressadoForm(forms.Form):
    """
    Formulário de login com validação de CPF e senha
    ATUALIZADO: Busca por cpf_hash em 17/03/2026
    """
    cpf = forms.CharField(
        label='CPF',
        max_length=14,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': '000.000.000-00',
            'autofocus': True
        })
    )

    senha = forms.CharField(
        label='Senha',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Digite sua senha'
        })
    )

    def clean(self):
        cleaned_data = super().clean()
        cpf = ''.join(filter(str.isdigit, cleaned_data.get('cpf', '')))
        senha = cleaned_data.get('senha')

        if cpf and senha:
            try:
                interessado = Interessado.objects.get(cpf_hash=gerar_hash_cpf(cpf))

                if not interessado.is_active:
                    raise forms.ValidationError(
                        'Sua conta está inativa. Entre em contato com a administração.'
                    )

                if not check_password(senha, interessado.senha):
                    raise forms.ValidationError('CPF ou senha incorretos.')

                self.interessado = interessado

            except Interessado.DoesNotExist:
                raise forms.ValidationError('CPF ou senha incorretos.')

        return cleaned_data


class EdicaoInteressadoForm(forms.ModelForm):
    """
    Formulário de EDIÇÃO de dados do interessado.
    Permite alterar TUDO, EXCETO CPF.
    NÃO inclui senha nem consentimento LGPD.
    """

    class Meta:
        model = Interessado
        fields = [
            'nome', 'rg', 'data_nascimento', 'sexo',
            'cidade_nascimento', 'uf_nascimento', 'nacionalidade',
            'fototipo', 'escolaridade',
            'cep', 'endereco_residencial', 'num_endereco', 'bairro',
            'complemento', 'cidade_residencia', 'uf_residencia',
            'telefone', 'celular', 'email',
            'programa_social', 'num_nis',
            'necessidades_especiais', 'pcd_fisica', 'pcd_visual',
            'pcd_auditiva', 'pcd_intelectual', 'pcd_psicossocial', 'pcd_multiplas',
            'nome_responsavel', 'telefone_responsavel', 'celular_responsavel',
            'email_responsavel', 'observacao',
        ]

        widgets = CadastroInteressadoForm.Meta.widgets.copy()
        labels = CadastroInteressadoForm.Meta.labels.copy()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    clean_rg                   = CadastroInteressadoForm.clean_rg
    clean_cep                  = CadastroInteressadoForm.clean_cep
    clean_telefone             = CadastroInteressadoForm.clean_telefone
    clean_celular              = CadastroInteressadoForm.clean_celular
    clean_num_nis              = CadastroInteressadoForm.clean_num_nis
    clean_telefone_responsavel = CadastroInteressadoForm.clean_telefone_responsavel
    clean_celular_responsavel  = CadastroInteressadoForm.clean_celular_responsavel
    clean_uf_residencia        = CadastroInteressadoForm.clean_uf_residencia
    clean_uf_nascimento        = CadastroInteressadoForm.clean_uf_nascimento
    clean_email                = CadastroInteressadoForm.clean_email


