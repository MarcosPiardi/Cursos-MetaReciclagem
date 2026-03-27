"""
Arquivo: test_forms.py
Caminho: apps/interessados/tests/test_forms.py
Testes de formulários: CadastroInteressadoForm e LoginInteressadoForm
Data: 27 de março de 2026
"""

from django.test import TestCase
from django.utils import timezone
from ..forms import CadastroInteressadoForm, LoginInteressadoForm
from ..models import Interessado, gerar_hash_cpf
from .factories import InteressadoFactory


class TestCadastroInteressadoForm(TestCase):
    """Testes de validação do formulário de cadastro."""

    def test_cadastro_valido_dados_minimos(self):
        """Formulário válido com dados mínimos obrigatórios."""
        form_data = {
            'nome': 'João Silva',
            'cpf': '52998224725',  # CPF válido
            'email': 'joao@example.com',
            'senha': 'SenhaForte123!',
            'confirmar_senha': 'SenhaForte123!',
            'consentimento_lgpd': True,
        }
        form = CadastroInteressadoForm(data=form_data)
        self.assertTrue(form.is_valid(), f"Erros: {form.errors}")

    def test_cadastro_cpf_duplicado(self):
        """Rejeita se CPF já existe no banco."""
        cpf = '52998224725'
        InteressadoFactory.create(cpf=cpf)
        
        form_data = {
            'nome': 'Maria Silva',
            'cpf': cpf,  # Duplicado
            'email': 'maria@example.com',
            'senha': 'SenhaForte123!',
            'confirmar_senha': 'SenhaForte123!',
            'consentimento_lgpd': True,
        }
        form = CadastroInteressadoForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('cpf', form.errors)

    def test_cadastro_email_duplicado(self):
        """Rejeita se email já existe no banco."""
        email = 'existente@example.com'
        InteressadoFactory.create(email=email)
        
        form_data = {
            'nome': 'Pedro Silva',
            'cpf': '11122233344',
            'email': email,  # Duplicado
            'senha': 'SenhaForte123!',
            'confirmar_senha': 'SenhaForte123!',
            'consentimento_lgpd': True,
        }
        form = CadastroInteressadoForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors)

    def test_cadastro_senhas_nao_conferem(self):
        """Rejeita se senhas são diferentes."""
        form_data = {
            'nome': 'Ana Silva',
            'cpf': '55566677788',
            'email': 'ana@example.com',
            'senha': 'SenhaForte123!',
            'confirmar_senha': 'SenhaDiferente456!',  # Diferente
            'consentimento_lgpd': True,
        }
        form = CadastroInteressadoForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('confirmar_senha', form.errors)

    def test_cadastro_cpf_invalido_todos_iguais(self):
        """Rejeita CPF com todos dígitos iguais."""
        form_data = {
            'nome': 'Carlos Silva',
            'cpf': '11111111111',  # Inválido
            'email': 'carlos@example.com',
            'senha': 'SenhaForte123!',
            'confirmar_senha': 'SenhaForte123!',
            'consentimento_lgpd': True,
        }
        form = CadastroInteressadoForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('cpf', form.errors)

    def test_cadastro_sem_consentimento_lgpd(self):
        """Rejeita sem aceitar consentimento LGPD."""
        form_data = {
            'nome': 'Fernanda Silva',
            'cpf': '99988877766',
            'email': 'fernanda@example.com',
            'senha': 'SenhaForte123!',
            'confirmar_senha': 'SenhaForte123!',
            'consentimento_lgpd': False,  # Não aceito
        }
        form = CadastroInteressadoForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('consentimento_lgpd', form.errors)


class TestLoginInteressadoForm(TestCase):
    """Testes de validação do formulário de login."""

    def setUp(self):
        self.cpf = '52998224725'
        self.senha = 'senha123'
        self.interessado = InteressadoFactory.create(
            cpf=self.cpf,
            is_active=True
        )
        # Factory cria com senha padrão 'senha123'

    def test_login_valido(self):
        """Login com CPF e senha corretos."""
        form_data = {
            'cpf': self.cpf,
            'senha': self.senha,
        }
        form = LoginInteressadoForm(data=form_data)
        self.assertTrue(form.is_valid(), f"Erros: {form.errors}")
        # Formulário armazena interessado em form.interessado
        self.assertEqual(form.interessado, self.interessado)

    def test_login_cpf_nao_cadastrado(self):
        """Login com CPF não existente."""
        form_data = {
            'cpf': '99999999999',  # Não existe
            'senha': self.senha,
        }
        form = LoginInteressadoForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('__all__', form.errors)

    def test_login_senha_incorreta(self):
        """Login com senha errada."""
        form_data = {
            'cpf': self.cpf,
            'senha': 'SenhaErrada123',
        }
        form = LoginInteressadoForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('__all__', form.errors)

    def test_login_interessado_inativo(self):
        """Login falha se conta está inativa."""
        self.interessado.is_active = False
        self.interessado.save()
        
        form_data = {
            'cpf': self.cpf,
            'senha': self.senha,
        }
        form = LoginInteressadoForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('__all__', form.errors)

        