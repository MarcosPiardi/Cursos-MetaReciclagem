"""
Arquivo: models.py
Caminho: apps/accounts/models.py
Alteração: Admin customizado com dashboard + UsuarioAdmin - IMPORT CORRIGIDO
Data: 20/01/2026
Alteração: Adicionado campo must_change_password para Fluxo B (Senha Provisória)
Data: 25/02/2026
Alteração: Campo email alterado para unique=True e blank=False (obrigatório e único)
Data: 26/02/2026
"""

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import RegexValidator


class Usuario(AbstractUser):
    """
    Modelo de usuário customizado.
    Herda todos os campos padrão do Django (username, password, email, etc.)
    e adiciona campos extras: CPF, telefones, setor e local de trabalho.
    """

    # Validador para CPF (11 dígitos)
    cpf_validator = RegexValidator(
        regex=r'^\d{11}$',
        message='CPF deve conter exatamente 11 dígitos'
    )

    # Validador para telefone (10 ou 11 dígitos)
    telefone_validator = RegexValidator(
        regex=r'^\d{10,11}$',
        message='Telefone deve conter 10 ou 11 dígitos'
    )

    # CAMPOS ADICIONAIS (além dos campos padrão do Django)
    cpf = models.CharField(
        'CPF',
        max_length=11,
        unique=True,
        validators=[cpf_validator],
        help_text='Somente números (11 dígitos)'
    )

    # ============================================================
    # CAMPO EMAIL — ALTERADO EM 26/02/2026
    # unique=True  → não permite dois Staff com o mesmo e-mail
    # blank=False  → e-mail obrigatório no cadastro de Staff
    # Substitui o campo email padrão do AbstractUser
    # ============================================================
    email = models.EmailField(
        'E-mail',
        unique=True,
        blank=False,
        help_text='E-mail institucional ou pessoal — obrigatório e único'
    )

    setor_trabalho = models.CharField(
        'Setor de Trabalho',
        max_length=50,
        blank=True,
        default=''
    )

    local_trabalho = models.CharField(
        'Local de Trabalho',
        max_length=50,
        blank=True,
        default=''
    )

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

    # ============================================================
    # FLUXO B — SENHA PROVISÓRIA
    # Adicionado: 25/02/2026
    # Indica que o usuário deve trocar a senha no próximo login
    # Definido como True quando Staff gera senha provisória no Admin
    # ============================================================
    must_change_password = models.BooleanField(
        'Deve trocar a senha',
        default=False,
        help_text='Se True, o usuário será obrigado a trocar a senha no próximo login'
    )

    def __str__(self):
        nome = self.get_full_name()
        if nome:
            return f"{nome} - CPF: {self.cpf}"
        return f"{self.username} - CPF: {self.cpf}"

    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'
        ordering = ['first_name', 'last_name']

        