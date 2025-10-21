
"""
ARQUIVO: apps/interessados/models.py
AÇÃO: SUBSTITUIR o arquivo apps/interessados/models.py COMPLETO
MUDANÇA: Adiciona campo 'senha' e métodos set_password() e check_password()
"""
"""
ARQUIVO: apps/interessados/models.py
AÇÃO: SUBSTITUIR o arquivo apps/interessados/models.py COMPLETO
MUDANÇA: Adiciona campo 'senha' e métodos set_password() e check_password()
"""


# apps/interessados/models.py
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
    """Modelo para cadastro de interessados"""
    
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
    
    # AUTENTICAÇÃO (NOVO!)
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
    
    # NECESSIDADES ESPECIAIS
    necessidades_especiais = models.BooleanField(
        'Possui Necessidades Especiais',
        default=False
    )
    
    fisica = models.BooleanField(
        'Necessidade Física',
        default=False
    )
    
    visual = models.BooleanField(
        'Necessidade Visual',
        default=False
    )
    
    auditiva = models.BooleanField(
        'Necessidade Auditiva',
        default=False
    )
    
    intelectual = models.BooleanField(
        'Necessidade Intelectual',
        default=False
    )
    
    psicossocial = models.BooleanField(
        'Necessidade Psicossocial',
        default=False
    )
    
    multiplas = models.BooleanField(
        'Necessidades Múltiplas',
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
    
    # MÉTODOS DE SENHA (NOVO!)
    def set_password(self, raw_password):
        """Define a senha criptografada"""
        self.senha = make_password(raw_password)
    
    def check_password(self, raw_password):
        """Verifica se a senha está correta"""
        return check_password(raw_password, self.senha)
    
    def __str__(self):
        return f"{self.nome} - CPF: {self.cpf}"
    
    class Meta:
        verbose_name = 'Interessado'
        verbose_name_plural = 'Interessados'
        ordering = ['nome']