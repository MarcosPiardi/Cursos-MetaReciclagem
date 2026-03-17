"""
ARQUIVO: apps/interessados/models.py
Models do app INTERESSADOS
Responsável por: Cadastro de interessados e dados auxiliares (Sexo, Fototipo)
Alteração: Adicionar campos CEP e Raça/Cor para cadastro completo — 26/01/2026
Alteração: Adicionado modelo PasswordResetToken — 20/02/2026
Alteração: Campo email unique=True — 26/02/2026
Alteração: Criptografia CPF e NIS — 12/03/2026
Alteração: Campo cpf_hash para busca eficiente — 17/03/2026
Alteração: Campos consentimento_lgpd e consentimento_lgpd_em — 17/03/2026
"""
import hashlib
from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.hashers import make_password, check_password
from django.utils import timezone
from encrypted_model_fields.fields import EncryptedCharField


def gerar_hash_cpf(cpf):
    """Gera hash SHA-256 do CPF para busca no banco. Não reversível."""
    return hashlib.sha256(cpf.encode()).hexdigest()


class Sexo(models.Model):
    nome = models.CharField('Sexo', max_length=20)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Sexo'
        verbose_name_plural = 'Sexos'


class Fototipo(models.Model):
    nome = models.CharField('Fototipo', max_length=50)
    descricao = models.TextField('Descrição', blank=True)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Fototipo'
        verbose_name_plural = 'Fototipos'


class Interessado(models.Model):

    cpf_validator = RegexValidator(regex=r'^\d{11}$', message='CPF deve conter exatamente 11 dígitos')
    telefone_validator = RegexValidator(regex=r'^\d{10,11}$', message='Telefone deve conter 10 ou 11 dígitos')
    uf_validator = RegexValidator(regex=r'^[A-Z]{2}$', message='UF deve conter 2 letras maiúsculas')
    nis_validator = RegexValidator(regex=r'^\d{11,15}$', message='NIS deve conter entre 11 e 15 dígitos')
    cep_validator = RegexValidator(regex=r'^\d{8}$', message='CEP deve conter exatamente 8 dígitos')

    # ============================================================
    # AUTENTICAÇÃO
    # ============================================================
    senha = models.CharField('Senha', max_length=128, help_text='Senha criptografada para login')
    last_login = models.DateTimeField('Último Login', null=True, blank=True)
    is_active = models.BooleanField('Ativo', default=True)
    is_staff = models.BooleanField('Membro da Equipe', default=False)
    is_superuser = models.BooleanField('Superusuário', default=False)
    must_change_password = models.BooleanField('Deve trocar a senha', default=False)

    # ============================================================
    # LGPD — ADICIONADO 17/03/2026
    # ============================================================
    consentimento_lgpd = models.BooleanField(
        'Consentimento LGPD',
        default=False,
        help_text='Indica se o interessado aceitou o termo de consentimento'
    )

    consentimento_lgpd_em = models.DateTimeField(
        'Data do Consentimento',
        null=True,
        blank=True,
        help_text='Data e hora em que o interessado aceitou o termo'
    )

    # ============================================================
    # DADOS PESSOAIS
    # ============================================================
    cpf = EncryptedCharField(
        'CPF', max_length=11, unique=True,
        validators=[cpf_validator],
        help_text='Somente números (11 dígitos) - CRIPTOGRAFADO'
    )

    cpf_hash = models.CharField(
        'Hash do CPF', max_length=64, unique=True, blank=True, default='',
        help_text='SHA-256 do CPF — gerado automaticamente, não editar'
    )

    nome = models.CharField('Nome Completo', max_length=50)
    rg = models.CharField('RG/Identidade', max_length=20, blank=True, default='')

    sexo = models.ForeignKey(Sexo, on_delete=models.PROTECT, verbose_name='Sexo', null=True, blank=True)
    data_nascimento = models.DateField('Data de Nascimento', null=True, blank=True)
    cidade_nascimento = models.CharField('Cidade de Nascimento', max_length=50, blank=True, default='')
    uf_nascimento = models.CharField('UF Nascimento', max_length=2, blank=True, default='', validators=[uf_validator])
    nacionalidade = models.CharField('Nacionalidade', max_length=50, blank=True, default='')

    # ENDEREÇO
    endereco_residencial = models.CharField('Endereço Residencial', max_length=50, blank=True, default='')
    num_endereco = models.CharField('Número', max_length=7, blank=True, default='')
    bairro = models.CharField('Bairro', max_length=30, blank=True, default='')
    complemento = models.CharField('Complemento', max_length=50, blank=True, default='')
    cep = models.CharField('CEP', max_length=8, blank=True, default='', validators=[cep_validator])
    cidade_residencia = models.CharField('Cidade de Residência', max_length=50, blank=True, default='')
    uf_residencia = models.CharField('UF Residência', max_length=2, blank=True, default='', validators=[uf_validator])

    # CONTATOS
    telefone = models.CharField('Telefone', max_length=11, blank=True, default='', validators=[telefone_validator])
    celular = models.CharField('Celular', max_length=11, blank=True, default='', validators=[telefone_validator])
    email = models.EmailField('E-mail', max_length=100, blank=True, null=True, default=None, unique=True)

    # CARACTERÍSTICAS
    fototipo = models.ForeignKey(Fototipo, on_delete=models.SET_NULL, verbose_name='Fototipo', null=True, blank=True)

    ESCOLARIDADE_CHOICES = [
        ('FUNDAMENTAL_INCOMPLETO', 'Ensino Fundamental Incompleto'),
        ('FUNDAMENTAL_COMPLETO', 'Ensino Fundamental Completo'),
        ('MEDIO_INCOMPLETO', 'Ensino Médio Incompleto'),
        ('MEDIO_COMPLETO', 'Ensino Médio Completo'),
        ('SUPERIOR_INCOMPLETO', 'Ensino Superior Incompleto'),
        ('SUPERIOR_COMPLETO', 'Ensino Superior Completo'),
        ('POS_GRADUACAO', 'Pós-Graduação'),
    ]
    escolaridade = models.CharField('Escolaridade', max_length=30, choices=ESCOLARIDADE_CHOICES, blank=True, default='')

    # PROGRAMA SOCIAL
    programa_social = models.BooleanField('Participa de Programa Social', default=False)
    num_nis = EncryptedCharField(
        'Número NIS', max_length=15, blank=True, default='',
        validators=[nis_validator],
        help_text='Número de Identificação Social - CRIPTOGRAFADO'
    )

    # PCD
    necessidades_especiais = models.BooleanField('Possui Necessidades Especiais', default=False)
    pcd_fisica = models.BooleanField('PCD Física', default=False)
    pcd_visual = models.BooleanField('PCD Visual', default=False)
    pcd_auditiva = models.BooleanField('PCD Auditiva', default=False)
    pcd_intelectual = models.BooleanField('PCD Intelectual', default=False)
    pcd_psicossocial = models.BooleanField('PCD Psicossocial', default=False)
    pcd_multiplas = models.BooleanField('PCD Múltiplas', default=False)

    # RESPONSÁVEL
    nome_responsavel = models.CharField('Nome do Responsável', max_length=50, blank=True, default='')
    telefone_responsavel = models.CharField('Telefone do Responsável', max_length=11, blank=True, default='', validators=[telefone_validator])
    celular_responsavel = models.CharField('Celular do Responsável', max_length=11, blank=True, default='', validators=[telefone_validator])
    email_responsavel = models.EmailField('E-mail do Responsável', max_length=100, blank=True, default='')

    observacao = models.TextField('Observações', blank=True, default='')

    criado_em = models.DateTimeField('Criado em', auto_now_add=True)
    atualizado_em = models.DateTimeField('Atualizado em', auto_now=True)

    # ============================================================
    # MÉTODOS
    # ============================================================
    def set_password(self, raw_password):
        self.senha = make_password(raw_password)

    def check_password(self, raw_password):
        return check_password(raw_password, self.senha)

    def set_cpf_hash(self, cpf_plain):
        self.cpf_hash = gerar_hash_cpf(cpf_plain)

    def has_perm(self, perm, obj=None):
        return self.is_superuser

    def has_perms(self, perm_list, obj=None):
        return all(self.has_perm(perm, obj) for perm in perm_list)

    def has_module_perms(self, app_label):
        return self.is_staff or self.is_superuser

    @property
    def is_anonymous(self):
        return False

    @property
    def is_authenticated(self):
        return True

    def get_username(self):
        return self.cpf

    @property
    def username(self):
        return self.cpf

    @property
    def tem_deficiencia(self):
        return any([
            self.pcd_fisica, self.pcd_visual, self.pcd_auditiva,
            self.pcd_intelectual, self.pcd_psicossocial, self.pcd_multiplas
        ])

    def __str__(self):
        return f"{self.nome} - CPF: {self.cpf}"

    class Meta:
        verbose_name = 'Interessado'
        verbose_name_plural = 'Interessados'


class PasswordResetToken(models.Model):
    interessado = models.ForeignKey(Interessado, on_delete=models.CASCADE, related_name='reset_tokens', verbose_name='Interessado')
    token = models.CharField('Token', max_length=100, unique=True)
    criado_em = models.DateTimeField('Criado em', auto_now_add=True)
    expira_em = models.DateTimeField('Expira em')
    usado = models.BooleanField('Usado', default=False)

    @property
    def esta_valido(self):
        return not self.usado and timezone.now() < self.expira_em

    def __str__(self):
        status = 'válido' if self.esta_valido else 'inválido'
        return f'Token {status} — {self.interessado.nome} ({self.expira_em.strftime("%d/%m/%Y %H:%M")})'

    class Meta:
        verbose_name = 'Token de Recuperação de Senha'
        verbose_name_plural = 'Tokens de Recuperação de Senha'
        ordering = ['-criado_em']


