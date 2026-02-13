"""
Arquivo: forms.py
Caminho: apps/interessados/forms.py
Alterações anteriores:
- Valores padrão para UF Nascimento e Nacionalidade + Senha criptografada (28/01/2026)
- REMOVIDO raca_cor (duplicado de fototipo) + Senha criptografada (26/01/2026)

Alteração: REMOVIDO raca_cor (duplicado de fototipo) + Senha criptografada
Data: 26/01/2026

Alteração: Valores padrão para UF Nascimento e Nacionalidade + Senha criptografada
Data: 28/01/2026

Alteração: LoginInteressadoForm corrigido para validar erros no formulário
Data: 30/01/2026

Alteração: Adicionada verificação de is_active no LoginInteressadoForm
Data: 13/02/2026
"""

from django import forms
from django.contrib.auth.hashers import check_password
from .models import Interessado, Sexo, Fototipo


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
    
    class Meta:
        model = Interessado
        fields = [
            # DADOS PESSOAIS
            'nome',
            'cpf',
            'rg',
            'data_nascimento',
            'sexo',
            'cidade_nascimento',
            'uf_nascimento',
            'nacionalidade',
            'fototipo',
            'escolaridade',
            
            # ENDEREÇO
            'cep',
            'endereco_residencial',
            'num_endereco',
            'bairro',
            'complemento',
            'cidade_residencia',
            'uf_residencia',
            
            # CONTATO
            'telefone',
            'celular',
            'email',
            
            # PROGRAMA SOCIAL / NIS
            'programa_social',
            'num_nis',
            
            # PCD - TODAS
            'necessidades_especiais',
            'pcd_fisica',
            'pcd_visual',
            'pcd_auditiva',
            'pcd_intelectual',
            'pcd_psicossocial',
            'pcd_multiplas',
            
            # RESPONSÁVEL
            'nome_responsavel',
            'telefone_responsavel',
            'celular_responsavel',
            'email_responsavel',
            
            # OBSERVAÇÕES
            'observacao',
        ]
        
        widgets = {
            # DADOS PESSOAIS
            'nome': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nome completo'
            }),
            'cpf': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '000.000.000-00'
            }),
            'rg': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '00.000.000-0'
            }),
            'data_nascimento': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'sexo': forms.Select(attrs={
                'class': 'form-select'
            }),
            'cidade_nascimento': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Cidade onde nasceu'
            }),
            'uf_nascimento': forms.TextInput(attrs={
                'class': 'form-control',
                'value': 'SP',
                'maxlength': '2',
                'style': 'text-transform: uppercase;'
            }),
            'nacionalidade': forms.TextInput(attrs={
                'class': 'form-control',
                'value': 'Brasileira'
            }),
            'fototipo': forms.Select(attrs={
                'class': 'form-select'
            }),
            'escolaridade': forms.Select(attrs={
                'class': 'form-select'
            }),
            
            # ENDEREÇO
            'cep': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '00000-000'
            }),
            'endereco_residencial': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Rua, Avenida...'
            }),
            'num_endereco': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Número'
            }),
            'bairro': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Bairro'
            }),
            'complemento': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Apto, Bloco...'
            }),
            'cidade_residencia': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Cidade'
            }),
            'uf_residencia': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'SP',
                'maxlength': '2',
                'style': 'text-transform: uppercase;'
            }),
            
            # CONTATO
            'telefone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '(15) 3999-9999'
            }),
            'celular': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '(15) 99999-9999'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'seu@email.com'
            }),
            
            # PROGRAMA SOCIAL
            'programa_social': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            }),
            'num_nis': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '000.00000.00-0'
            }),
            
            # PCD
            'necessidades_especiais': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            }),
            'pcd_fisica': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            }),
            'pcd_visual': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            }),
            'pcd_auditiva': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            }),
            'pcd_intelectual': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            }),
            'pcd_psicossocial': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            }),
            'pcd_multiplas': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            }),
            
            # RESPONSÁVEL
            'nome_responsavel': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nome completo do responsável'
            }),
            'telefone_responsavel': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '(15) 3999-9999'
            }),
            'celular_responsavel': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '(15) 99999-9999'
            }),
            'email_responsavel': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'email@responsavel.com'
            }),
            
            # OBSERVAÇÕES
            'observacao': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Informações adicionais (opcional)',
                'rows': 3
            }),
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
        """Define valores padrão no inicializador"""
        super().__init__(*args, **kwargs)
        
        # Valores padrão - só aplica se for novo cadastro (sem dados POST)
        if not self.data:
            self.initial['uf_nascimento'] = 'SP'
            self.initial['nacionalidade'] = 'Brasileira'
    
    def clean_cpf(self):
        """Remove formatação e valida CPF único"""
        cpf = self.cleaned_data.get('cpf', '')
        cpf = ''.join(filter(str.isdigit, cpf))
        
        if len(cpf) != 11:
            raise forms.ValidationError('CPF deve ter 11 dígitos.')
        
        if Interessado.objects.filter(cpf=cpf).exists():
            raise forms.ValidationError('Este CPF já está cadastrado.')
        
        return cpf
    
    def clean_rg(self):
        """Remove formatação do RG"""
        rg = self.cleaned_data.get('rg', '')
        rg = rg.replace('.', '').replace('-', '').strip()
        return rg
    
    def clean_cep(self):
        """Remove formatação do CEP"""
        cep = self.cleaned_data.get('cep', '')
        cep = ''.join(filter(str.isdigit, cep))
        
        if cep and len(cep) != 8:
            raise forms.ValidationError('CEP deve ter 8 dígitos.')
        
        return cep
    
    def clean_telefone(self):
        """Remove formatação do telefone"""
        telefone = self.cleaned_data.get('telefone', '')
        telefone = ''.join(filter(str.isdigit, telefone))
        return telefone
    
    def clean_celular(self):
        """Remove formatação do celular"""
        celular = self.cleaned_data.get('celular', '')
        celular = ''.join(filter(str.isdigit, celular))
        return celular
    
    def clean_num_nis(self):
        """Remove formatação do NIS"""
        nis = self.cleaned_data.get('num_nis', '')
        nis = ''.join(filter(str.isdigit, nis))
        return nis
    
    def clean_telefone_responsavel(self):
        """Remove formatação do telefone do responsável"""
        telefone = self.cleaned_data.get('telefone_responsavel', '')
        telefone = ''.join(filter(str.isdigit, telefone))
        return telefone
    
    def clean_celular_responsavel(self):
        """Remove formatação do celular do responsável"""
        celular = self.cleaned_data.get('celular_responsavel', '')
        celular = ''.join(filter(str.isdigit, celular))
        return celular
    
    def clean_uf_residencia(self):
        """Converte UF para maiúsculas"""
        uf = self.cleaned_data.get('uf_residencia', '').strip().upper()
        return uf
    
    def clean_uf_nascimento(self):
        """Converte UF de nascimento para maiúsculas"""
        uf = self.cleaned_data.get('uf_nascimento', '').strip().upper()
        return uf
    
    def clean(self):
        """Valida se as senhas conferem"""
        cleaned_data = super().clean()
        senha = cleaned_data.get('senha')
        confirmar_senha = cleaned_data.get('confirmar_senha')
        
        if senha and confirmar_senha and senha != confirmar_senha:
            raise forms.ValidationError('As senhas não conferem.')
        
        return cleaned_data
    
    def save(self, commit=True):
        """Salva interessado com senha CRIPTOGRAFADA"""
        interessado = super().save(commit=False)
        interessado.set_password(self.cleaned_data['senha'])
        
        if commit:
            interessado.save()
        
        return interessado


class LoginInteressadoForm(forms.Form):
    """
    Formulário de login com validação de CPF e senha
    CORRIGIDO: Erros são exibidos no formulário, não em messages
    ADICIONADO: Verificação de is_active em 13/02/2026
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
        """
        Valida CPF e senha
        ADICIONADO: Verificação de is_active em 13/02/2026
        Se houver erro, levanta ValidationError que será exibido em form.non_field_errors
        """
        cleaned_data = super().clean()
        cpf = cleaned_data.get('cpf', '')
        senha = cleaned_data.get('senha')
        
        # Remove formatação do CPF
        cpf = ''.join(filter(str.isdigit, cpf))
        
        if cpf and senha:
            try:
                # Busca o interessado pelo CPF
                interessado = Interessado.objects.get(cpf=cpf)
                
                # ============================================================
                # VALIDAÇÃO CRÍTICA: VERIFICAR SE ESTÁ ATIVO
                # Data: 13/02/2026
                # ============================================================
                if not interessado.is_active:
                    raise forms.ValidationError(
                        '🔒 Sua conta está inativa. Entre em contato com a administração.'
                    )
                
                # Verifica a senha usando check_password
                if not check_password(senha, interessado.senha):
                    raise forms.ValidationError('CPF ou senha incorretos.')
                
                # Armazena o interessado no formulário para a view usar
                self.interessado = interessado
                
            except Interessado.DoesNotExist:
                # CPF não existe no banco
                raise forms.ValidationError('CPF ou senha incorretos.')
        
        return cleaned_data


class EdicaoInteressadoForm(forms.ModelForm):
    """
    Formulário de EDIÇÃO de dados do interessado.
    Permite alterar TUDO, EXCETO CPF (identificador único)
    NÃO inclui senha (precisa de formulário separado para trocar senha)
    """
    
    class Meta:
        model = Interessado
        fields = [
            # DADOS PESSOAIS (SEM CPF - não pode mudar)
            'nome',
            'rg',
            'data_nascimento',
            'sexo',
            'cidade_nascimento',
            'uf_nascimento',
            'nacionalidade',
            'fototipo',
            'escolaridade',
            
            # ENDEREÇO
            'cep',
            'endereco_residencial',
            'num_endereco',
            'bairro',
            'complemento',
            'cidade_residencia',
            'uf_residencia',
            
            # CONTATO
            'telefone',
            'celular',
            'email',
            
            # PROGRAMA SOCIAL / NIS
            'programa_social',
            'num_nis',
            
            # PCD - TODAS
            'necessidades_especiais',
            'pcd_fisica',
            'pcd_visual',
            'pcd_auditiva',
            'pcd_intelectual',
            'pcd_psicossocial',
            'pcd_multiplas',
            
            # RESPONSÁVEL
            'nome_responsavel',
            'telefone_responsavel',
            'celular_responsavel',
            'email_responsavel',
            
            # OBSERVAÇÕES
            'observacao',
        ]
        
        # Reutiliza os mesmos widgets do cadastro
        widgets = CadastroInteressadoForm.Meta.widgets.copy()
        labels = CadastroInteressadoForm.Meta.labels.copy()
    
    def __init__(self, *args, **kwargs):
        """Inicializa o formulário de edição"""
        super().__init__(*args, **kwargs)
    
    # Reutiliza os mesmos métodos de limpeza
    clean_cep = CadastroInteressadoForm.clean_cep
    clean_telefone = CadastroInteressadoForm.clean_telefone
    clean_celular = CadastroInteressadoForm.clean_celular
    clean_num_nis = CadastroInteressadoForm.clean_num_nis
    clean_telefone_responsavel = CadastroInteressadoForm.clean_telefone_responsavel
    clean_celular_responsavel = CadastroInteressadoForm.clean_celular_responsavel
    clean_uf_residencia = CadastroInteressadoForm.clean_uf_residencia
    clean_uf_nascimento = CadastroInteressadoForm.clean_uf_nascimento
    clean_rg = CadastroInteressadoForm.clean_rg

    