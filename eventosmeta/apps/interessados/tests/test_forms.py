"""
Arquivo: test_forms.py
Caminho: apps/interessados/tests/test_forms.py
Testes de formularios: CadastroInteressadoForm, LoginInteressadoForm, EdicaoInteressadoForm
Data: 07/04/2026
Refatorado: 29/05/2026
  - Removido TestLoginFormComFactory (redundante)
  - Unificado TestCadastroFormCPFValidacao em TestCadastroInteressadoForm
  - Removido import nao utilizado (timezone)
  - Factory imports movidos para nivel da classe
  - Adicionados testes basicos de validacao EdicaoInteressadoForm
"""

from django.test import TestCase

from ..forms import (
    CadastroInteressadoForm,
    LoginInteressadoForm,
    EdicaoInteressadoForm,
)
from ..models import Interessado
from .factories import (
    InteressadoFactory,
    SexoFactory,
    FototipoFactory,
)


# ============================================================
# TESTES: CADASTRO INTERESSADO FORM
# ============================================================

class TestCadastroInteressadoForm(TestCase):
    """Testes de validacao do formulario de cadastro (incluindo CPF)."""

    # --- Dados minimos ---

    def test_cadastro_valido_dados_minimos(self):
        """Formulario valido com dados minimos obrigatorios."""
        form_data = {
            'nome': 'Joao Silva',
            'cpf': '52998224725',
            'email': 'joao@example.com',
            'senha': 'SenhaForte123!',
            'confirmar_senha': 'SenhaForte123!',
            'consentimento_lgpd': True,
        }
        form = CadastroInteressadoForm(data=form_data)
        self.assertTrue(form.is_valid(), f"Erros: {form.errors}")

    # --- Unicidade ---

    def test_cadastro_cpf_duplicado(self):
        """Rejeita se CPF ja existe no banco."""
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
        """Rejeita se email ja existe no banco."""
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

    # --- Senha ---

    def test_cadastro_senhas_nao_conferem(self):
        """Rejeita se senhas sao diferentes."""
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

    # --- CPF ---

    def test_cadastro_cpf_invalido_todos_iguais(self):
        """Rejeita CPF com todos digitos iguais."""
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

    def test_cpf_valido_com_pontuacao(self):
        """Aceita CPF formatado (123.456.789-00)."""
        form_data = {
            'nome': 'Joao',
            'cpf': '529.982.247-25',
            'email': 'joao@test.com',
            'senha': 'Senha123!',
            'confirmar_senha': 'Senha123!',
            'consentimento_lgpd': True,
        }
        form = CadastroInteressadoForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_cpf_invalido_digito_verificador(self):
        """Rejeita CPF com digito verificador invalido."""
        form_data = {
            'nome': 'Joao',
            'cpf': '12345678901',
            'email': 'joao@test.com',
            'senha': 'Senha123!',
            'confirmar_senha': 'Senha123!',
            'consentimento_lgpd': True,
        }
        form = CadastroInteressadoForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_cpf_muito_curto(self):
        """Rejeita CPF com menos de 11 digitos."""
        form_data = {
            'nome': 'Joao',
            'cpf': '1234567890',
            'email': 'joao@test.com',
            'senha': 'Senha123!',
            'confirmar_senha': 'Senha123!',
            'consentimento_lgpd': True,
        }
        form = CadastroInteressadoForm(data=form_data)
        self.assertFalse(form.is_valid())

    # --- LGPD ---

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


# ============================================================
# TESTES: LOGIN INTERESSADO FORM
# ============================================================

class TestLoginInteressadoForm(TestCase):
    """Testes de validacao do formulario de login."""

    def setUp(self):
        self.cpf = '52998224725'
        self.senha = 'senha123'
        self.interessado = InteressadoFactory.create(
            cpf=self.cpf,
            is_active=True,
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
        """Login com CPF nao existente."""
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
        """Login falha se conta esta inativa."""
        self.interessado.is_active = False
        self.interessado.save()
        form_data = {
            'cpf': self.cpf,
            'senha': self.senha,
        }
        form = LoginInteressadoForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('__all__', form.errors)

    def test_login_cpf_formatado_com_pontuacao(self):
        """Login funciona com CPF contendo pontos e tracos."""
        interessado = InteressadoFactory.create(
            cpf='98765432100',
            is_active=True,
        )
        form_data = {
            'cpf': '987.654.321-00',
            'senha': 'senha123',
        }
        form = LoginInteressadoForm(data=form_data)
        self.assertTrue(form.is_valid(), f"Erros: {form.errors}")
        self.assertEqual(form.interessado, interessado)


# ============================================================
# TESTES: EDICAO INTERESSADO FORM
# ============================================================

class TestEdicaoInteressadoForm(TestCase):
    """Testes de validacao do formulario de edicao."""

    @classmethod
    def setUpTestData(cls):
        cls.sexo = SexoFactory()
        cls.fototipo = FototipoFactory()
        cls.interessado = InteressadoFactory.create(
            sexo=cls.sexo,
            fototipo=cls.fototipo,
        )

    def _dados_minimos(self, **kwargs):
        """Retorna dict com dados minimos para edicao valida."""
        dados = {
            'nome': 'Novo Nome',
            'rg': '12.345.678-9',
            'data_nascimento': '1990-05-15',
            'sexo': self.sexo.id,
            'cidade_nascimento': 'Sao Paulo',
            'uf_nascimento': 'SP',
            'nacionalidade': 'Brasileira',
            'fototipo': self.fototipo.id,
            'escolaridade': 'SUPERIOR_COMPLETO',
            'cep': '01234567',
            'endereco_residencial': 'Rua Teste',
            'num_endereco': '123',
            'bairro': 'Centro',
            'cidade_residencia': 'Sao Paulo',
            'uf_residencia': 'SP',
            'email': self.interessado.email,
            'num_nis': '12345678901',
        }
        dados.update(kwargs)
        return dados

    def test_edicao_valida_dados_minimos(self):
        """Formulario valido com dados minimos obrigatorios."""
        form = EdicaoInteressadoForm(
            data=self._dados_minimos(),
            instance=self.interessado,
        )
        self.assertTrue(form.is_valid(), f"Erros: {form.errors}")

    def test_cpf_nao_aparece_na_edicao(self):
        """CPF nao esta nos fields do formulario de edicao."""
        form = EdicaoInteressadoForm(instance=self.interessado)
        self.assertNotIn('cpf', form.fields)

    def test_tentativa_alterar_cpf_ignorada(self):
        """Passar CPF no POST nao altera o cpf_hash do interessado."""
        cpf_hash_original = self.interessado.cpf_hash
        dados = self._dados_minimos(cpf='98765432100')

        form = EdicaoInteressadoForm(
            data=dados,
            instance=self.interessado,
        )
        self.assertTrue(form.is_valid(), f"Erros: {form.errors}")
        saved = form.save()
        self.assertEqual(saved.cpf_hash, cpf_hash_original)

    def test_edicao_sem_nome_rejeita(self):
        """Rejeita edicao sem nome."""
        dados = self._dados_minimos(nome='')
        form = EdicaoInteressadoForm(
            data=dados,
            instance=self.interessado,
        )
        self.assertFalse(form.is_valid())
        self.assertIn('nome', form.errors)

    def test_edicao_email_invalido_rejeita(self):
        """Rejeita edicao com email mal formatado."""
        dados = self._dados_minimos(email='email-invalido')
        form = EdicaoInteressadoForm(
            data=dados,
            instance=self.interessado,
        )
        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors)

        