"""
ARQUIVO: apps/interessados/models.py
Models do app INTERESSADOS
Responsável por: Cadastro de interessados e dados auxiliares (Sexo, Fototipo)
Arquivo: apps/interessados/models.py
Alteração: Adicionar campos CEP e Raça/Cor para cadastro completo
Data: 26/01/2026
"""

from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.hashers import make_password, check_password


class Sexo(models.Model):
    """Modelo para Sexo/Gênero"""
    nome = models.CharField('Sexo', max_length=20)
    
    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = 'Sexo'
        verbose_name_plural = 'Sexos'


class Fototipo(models.Model):
    """Modelo para Fototipo (classificação de pele)"""
    nome = models.CharField('Fototipo', max_length=50)
    descricao = models.TextField('Descrição', blank=True)
    
    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = 'Fototipo'
        verbose_name_plural = 'Fototipos'


class Interessado(models.Model):
    """Modelo para cadastro de interessados com autenticação"""
    
    # Validadores
    cpf_validator = RegexValidator(
        regex=r'^\d{11}$',
        message='CPF deve conter exatamente 11 dígitos'
    )
    
    telefone_validator = RegexValidator(
        regex=r'^\d{10,11}$',
        message='Telefone deve conter 10 ou 11 dígitos'
    )
    
    uf_validator = RegexValidator(
        regex=r'^[A-Z]{2}$',
        message='UF deve conter 2 letras maiúsculas'
    )
    
    nis_validator = RegexValidator(
        regex=r'^\d{11,15}$',
        message='NIS deve conter entre 11 e 15 dígitos'
    )
    
    # ============================================================
    # VALIDADOR CEP - ADICIONADO EM 26/01/2026
    # ============================================================
    cep_validator = RegexValidator(
        regex=r'^\d{8}$',
        message='CEP deve conter exatamente 8 dígitos'
    )
    
    # ============================================================
    # CAMPOS DE AUTENTICAÇÃO - Adicionados em 05/12/2025
    # ============================================================
    senha = models.CharField(
        'Senha',
        max_length=128,
        help_text='Senha criptografada para login'
    )
    
    last_login = models.DateTimeField(
        'Último Login',
        null=True,
        blank=True,
        help_text='Data e hora do último login'
    )
    
    is_active = models.BooleanField(
        'Ativo',
        default=True,
        help_text='Indica se o interessado pode fazer login no sistema'
    )
    
    is_staff = models.BooleanField(
        'Membro da Equipe',
        default=False,
        help_text='Indica se o interessado pode acessar o admin (normalmente False)'
    )
    
    is_superuser = models.BooleanField(
        'Superusuário',
        default=False,
        help_text='Indica se o interessado tem todas as permissões (normalmente False)'
    )
    
    # DADOS PESSOAIS
    cpf = models.CharField(
        'CPF',
        max_length=11,
        unique=True,
        validators=[cpf_validator],
        help_text='Somente números (11 dígitos)'
    )
     
    nome = models.CharField(
        'Nome Completo',
        max_length=50
    )
    
    # DOCUMENTO
    rg = models.CharField(
        'RG/Identidade',
        max_length=20,
        blank=True,
        default='',
        help_text='Número do RG ou documento de identidade'
    )

    sexo = models.ForeignKey(
        Sexo,
        on_delete=models.PROTECT,
        verbose_name='Sexo',
        null=True,
        blank=True
    )
    
    data_nascimento = models.DateField(
        'Data de Nascimento',
        null=True,
        blank=True
    )
    
    cidade_nascimento = models.CharField(
        'Cidade de Nascimento',
        max_length=50,
        blank=True,
        default=''
    )
    
    uf_nascimento = models.CharField(
        'UF Nascimento',
        max_length=2,
        blank=True,
        default='',
        validators=[uf_validator],
        help_text='Ex: SP, RJ, MG'
    )
    
    nacionalidade = models.CharField(
        'Nacionalidade',
        max_length=50,
        blank=True,
        default=''
    )
    
    
    # ENDEREÇO
    endereco_residencial = models.CharField(
        'Endereço Residencial',
        max_length=50,
        blank=True,
        default=''
    )
    
    num_endereco = models.CharField(
        'Número',
        max_length=7,
        blank=True,
        default=''
    )
    
    bairro = models.CharField(
        'Bairro',
        max_length=30,
        blank=True,
        default=''
    )
    
    complemento = models.CharField(
        'Complemento',
        max_length=50,
        blank=True,
        default=''
    )
    
    # ============================================================
    # CEP - ADICIONADO EM 26/01/2026
    # ============================================================
    cep = models.CharField(
        'CEP',
        max_length=8,
        blank=True,
        default='',
        validators=[cep_validator],
        help_text='Somente números (8 dígitos)'
    )
    
    cidade_residencia = models.CharField(
        'Cidade de Residência',
        max_length=50,
        blank=True,
        default=''
    )
    
    uf_residencia = models.CharField(
        'UF Residência',
        max_length=2,
        blank=True,
        default='',
        validators=[uf_validator],
        help_text='Ex: SP, RJ, MG'
    )
    
    # CONTATOS
    telefone = models.CharField(
        'Telefone',
        max_length=11,
        blank=True,
        default='',
        validators=[telefone_validator],
        help_text='Somente números (10 ou 11 dígitos)'
    )
    
    celular = models.CharField(
        'Celular',
        max_length=11,
        blank=True,
        default='',
        validators=[telefone_validator],
        help_text='Somente números (10 ou 11 dígitos)'
    )
    
    email = models.EmailField(
        'E-mail',
        max_length=100,
        blank=True,
        default=''
    )
    
    # CARACTERÍSTICAS
    fototipo = models.ForeignKey(
        Fototipo,
        on_delete=models.SET_NULL,
        verbose_name='Fototipo',
        null=True,
        blank=True
    )

    # ESCOLARIDADE
    ESCOLARIDADE_CHOICES = [
        ('FUNDAMENTAL_INCOMPLETO', 'Ensino Fundamental Incompleto'),
        ('FUNDAMENTAL_COMPLETO', 'Ensino Fundamental Completo'),
        ('MEDIO_INCOMPLETO', 'Ensino Médio Incompleto'),
        ('MEDIO_COMPLETO', 'Ensino Médio Completo'),
        ('SUPERIOR_INCOMPLETO', 'Ensino Superior Incompleto'),
        ('SUPERIOR_COMPLETO', 'Ensino Superior Completo'),
        ('POS_GRADUACAO', 'Pós-Graduação'),
    ]
    
    escolaridade = models.CharField(
        'Escolaridade',
        max_length=30,
        choices=ESCOLARIDADE_CHOICES,
        blank=True,
        default='',
        help_text='Nível de escolaridade do interessado'
    )
    
    # PROGRAMA SOCIAL
    programa_social = models.BooleanField(
        'Participa de Programa Social',
        default=False
    )
    
    num_nis = models.CharField(
        'Número NIS',
        max_length=15,
        blank=True,
        default='',
        validators=[nis_validator],
        help_text='Número de Identificação Social (11 a 15 dígitos)'
    )
    
    # NECESSIDADES ESPECIAIS / PCD
    necessidades_especiais = models.BooleanField(
        'Possui Necessidades Especiais',
        default=False
    )
    
    pcd_fisica = models.BooleanField(
        'PCD Física',
        default=False
    )
    
    pcd_visual = models.BooleanField(
        'PCD Visual',
        default=False
    )
    
    pcd_auditiva = models.BooleanField(
        'PCD Auditiva',
        default=False
    )
    
    pcd_intelectual = models.BooleanField(
        'PCD Intelectual',
        default=False
    )
    
    pcd_psicossocial = models.BooleanField(
        'PCD Psicossocial',
        default=False
    )
    
    pcd_multiplas = models.BooleanField(
        'PCD Múltiplas',
        default=False
    )
    
    # RESPONSÁVEL
    nome_responsavel = models.CharField(
        'Nome do Responsável',
        max_length=50,
        blank=True,
        default=''
    )
    
    telefone_responsavel = models.CharField(
        'Telefone do Responsável',
        max_length=11,
        blank=True,
        default='',
        validators=[telefone_validator]
    )
    
    celular_responsavel = models.CharField(
        'Celular do Responsável',
        max_length=11,
        blank=True,
        default='',
        validators=[telefone_validator]
    )
    
    email_responsavel = models.EmailField(
        'E-mail do Responsável',
        max_length=100,
        blank=True,
        default=''
    )
    
    # OUTROS
    observacao = models.TextField(
        'Observações',
        blank=True,
        default=''
    )
    
    # METADATA
    criado_em = models.DateTimeField('Criado em', auto_now_add=True)
    atualizado_em = models.DateTimeField('Atualizado em', auto_now=True)
    
    # ============================================================
    # MÉTODOS DE SENHA
    # ============================================================
    def set_password(self, raw_password):
        """Define a senha criptografada"""
        self.senha = make_password(raw_password)
    
    def check_password(self, raw_password):
        """Verifica se a senha está correta"""
        return check_password(raw_password, self.senha)
    
    # ============================================================
    # MÉTODOS DE PERMISSÃO - Adicionados em 05/12/2025
    # Necessários para compatibilidade com sistema de autenticação Django
    # ============================================================
    def has_perm(self, perm, obj=None):
        """
        Verifica se o interessado tem uma permissão específica
        Superusuários têm todas as permissões
        """
        return self.is_superuser
    
    def has_perms(self, perm_list, obj=None):
        """
        Verifica se o interessado tem uma lista de permissões
        """
        return all(self.has_perm(perm, obj) for perm in perm_list)
    
    def has_module_perms(self, app_label):
        """
        Verifica se o interessado tem permissões para acessar um módulo/app
        Staff e superusuários têm acesso
        """
        return self.is_staff or self.is_superuser
    
    @property
    def is_anonymous(self):
        """
        Sempre False para usuários autenticados
        """
        return False
    
    @property
    def is_authenticated(self):
        """
        Sempre True para usuários autenticados
        """
        return True
    
    def get_username(self):
        """
        Retorna o identificador único do interessado (CPF)
        """
        return self.cpf
    
    @property
    def username(self):
        """
        Propriedade username para compatibilidade com Django admin
        """
        return self.cpf
    
    # ============================================================
    # PROPRIEDADES E MÉTODOS AUXILIARES
    # ============================================================
    @property
    def tem_deficiencia(self):
        """Verifica se tem alguma deficiência"""
        return any([
            self.pcd_fisica,
            self.pcd_visual,
            self.pcd_auditiva,
            self.pcd_intelectual,
            self.pcd_psicossocial,
            self.pcd_multiplas
        ])
    
    def __str__(self):
        return f"{self.nome} - CPF: {self.cpf}"
    
    class Meta:
        verbose_name = 'Interessado'
        verbose_name_plural = 'Interessados'

        