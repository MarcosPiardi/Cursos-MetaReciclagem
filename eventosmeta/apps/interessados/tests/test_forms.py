"""
Arquivo: test_forms.py
Caminho: apps/interessados/tests/test_forms.py
Testes de formulários: CadastroInteressadoForm, LoginInteressadoForm, EdicaoInteressadoForm
Data: 07/04/2026
"""

from django.test import TestCase
from django.utils import timezone

from ..forms import (
    CadastroInteressadoForm,
    LoginInteressadoForm,
    EdicaoInteressadoForm
)
from ..models import Interessado, gerar_hash_cpf
from .factories import InteressadoFactory, SexoFactory, FototipoFactory


# ============================================================
# TESTES: CADASTRO INTERESSADO FORM
# ============================================================

class TestCadastroInteressadoForm(TestCase):
    """Testes de validação do formulário de cadastro."""

    def test_cadastro_valido_dados_minimos(self):
        """Formulário válido com dados mínimos obrigatórios."""
        form_data = {
            'nome': 'João Silva',
            'cpf': '52998224725',
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
            'cpf': cpf,
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
            'email': email,
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
            'confirmar_senha': 'SenhaDiferente456!',
            'consentimento_lgpd': True,
        }
        form = CadastroInteressadoForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('confirmar_senha', form.errors)

    def test_cadastro_cpf_invalido_todos_iguais(self):
        """Rejeita CPF com todos dígitos iguais."""
        form_data = {
            'nome': 'Carlos Silva',
            'cpf': '11111111111',
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
            'consentimento_lgpd': False,
        }
        form = CadastroInteressadoForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('consentimento_lgpd', form.errors)


class TestCadastroFormCPFValidacao(TestCase):
    """Testes específicos para validação de CPF no cadastro."""

    def test_cpf_valido_com_pontuacao(self):
        """Aceita CPF formatado (123.456.789-00)."""
        form_data = {
            'nome': 'João',
            'cpf': '529.982.247-25',
            'email': 'joao@test.com',
            'senha': 'Senha123!',
            'confirmar_senha': 'Senha123!',
            'consentimento_lgpd': True,
        }
        form = CadastroInteressadoForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_cpf_invalido_digito_verificador(self):
        """Rejeita CPF com dígito verificador inválido."""
        form_data = {
            'nome': 'João',
            'cpf': '12345678901',
            'email': 'joao@test.com',
            'senha': 'Senha123!',
            'confirmar_senha': 'Senha123!',
            'consentimento_lgpd': True,
        }
        form = CadastroInteressadoForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_cpf_muito_curto(self):
        """Rejeita CPF com menos de 11 dígitos."""
        form_data = {
            'nome': 'João',
            'cpf': '1234567890',
            'email': 'joao@test.com',
            'senha': 'Senha123!',
            'confirmar_senha': 'Senha123!',
            'consentimento_lgpd': True,
        }
        form = CadastroInteressadoForm(data=form_data)
        self.assertFalse(form.is_valid())


# ============================================================
# TESTES: LOGIN INTERESSADO FORM
# ============================================================

class TestLoginInteressadoForm(TestCase):
    """Testes de validação do formulário de login."""

    def setUp(self):
        self.cpf = '52998224725'
        self.senha = 'senha123'
        self.interessado = InteressadoFactory.create(
            cpf=self.cpf,
            is_active=True
        )

    def test_login_valido(self):
        """Login com CPF e senha corretos."""
        form_data = {
            'cpf': self.cpf,
            'senha': self.senha,
        }
        form = LoginInteressadoForm(data=form_data)
        self.assertTrue(form.is_valid(), f"Erros: {form.errors}")
        self.assertEqual(form.interessado, self.interessado)

    def test_login_cpf_nao_cadastrado(self):
        """Login com CPF não existente."""
        form_data = {
            'cpf': '99999999999',
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


class TestLoginFormComFactory(TestCase):
    """Testes de login usando Factory."""

    def setUp(self):
        from .factories import InteressadoFactory
        self.interessado = InteressadoFactory.create(
            cpf='529.982.247-25',
            is_active=True
        )

    def test_login_com_factory_interessado(self):
        """Login funciona com interessado criado por factory."""
        form_data = {
            'cpf': '52998224725',
            'senha': 'senha123',
        }
        form = LoginInteressadoForm(data=form_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.interessado, self.interessado)


# ============================================================
# TESTES: EDIÇÃO INTERESSADO FORM
# ============================================================

class TestEdicaoFormCPFReadonly(TestCase):
    """Testes para garantir que CPF não pode ser alterado na edição."""

    def setUp(self):
        from .factories import InteressadoFactory, SexoFactory, FototipoFactory
        self.sexo = SexoFactory()
        self.fototipo = FototipoFactory()
        self.interessado = InteressadoFactory.create(
            sexo=self.sexo,
            fototipo=self.fototipo
        )

    def test_cpf_nao_aparece_na_edicao(self):
        """CPF não está nos fields da forma de edição."""
        form = EdicaoInteressadoForm(instance=self.interessado)
        self.assertNotIn('cpf', form.fields)

    def test_tentativa_alterar_cpf_ignora(self):
        """Tentativa de alterar CPF é ignorada."""
        novo_cpf = '98765432100'
        original_cpf_hash = self.interessado.cpf_hash

        # ✅ TODOS os campos obrigatórios preenchidos
        form_data = {
            'nome': 'Novo Nome',
            'rg': self.interessado.rg or '12.345.678-9',
            'data_nascimento': self.interessado.data_nascimento or '1990-05-15',
            'sexo': self.sexo.id,
            'cidade_nascimento': self.interessado.cidade_nascimento or 'São Paulo',
            'uf_nascimento': 'SP',
            'nacionalidade': 'Brasileira',
            'fototipo': self.fototipo.id,
            'escolaridade': self.interessado.escolaridade or 'SUPERIOR_COMPLETO',
            'cep': self.interessado.cep or '01234567',
            'endereco_residencial': self.interessado.endereco_residencial or 'Rua Teste',
            'num_endereco': self.interessado.num_endereco or '123',
            'bairro': self.interessado.bairro or 'Centro',
            'cidade_residencia': self.interessado.cidade_residencia or 'São Paulo',
            'uf_residencia': 'SP',
            'email': self.interessado.email,
            'num_nis': self.interessado.num_nis or '12345678901',  # ✅ ADICIONADO AQUI
            'cpf': novo_cpf,  # Será ignorado (não está em fields)
        }

        form = EdicaoInteressadoForm(
            data=form_data,
            instance=self.interessado
        )

        self.assertTrue(form.is_valid(), f"Form errors: {form.errors}")
        saved = form.save()
        self.assertEqual(saved.cpf_hash, original_cpf_hash)

        