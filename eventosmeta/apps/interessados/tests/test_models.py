"""
Arquivo: test_models.py
Caminho: apps/interessados/tests/test_models.py
Alteração: Testes automatizados — validação CPF, login, cadastro, LGPD
Data: 20/03/2026
"""

from django.test import TestCase
from django.utils import timezone
from ..models import Interessado, SolicitacaoExclusao, gerar_hash_cpf
from ..forms import CadastroInteressadoForm, LoginInteressadoForm
from .factories import InteressadoFactory, SexoFactory  # Adicionado para factory tests


# ============================================================
# HELPERS
# ============================================================

def criar_interessado(cpf='52998224725', nome='Teste Silva', senha='senha123'):
    """Cria um interessado válido para uso nos testes."""
    i = Interessado(
        nome=nome,
        cpf=cpf,
        cpf_hash=gerar_hash_cpf(cpf),
        consentimento_lgpd=True,
        consentimento_lgpd_em=timezone.now(),
    )
    i.set_password(senha)
    i.save()
    return i


# ============================================================
# TESTES — MODELO / CPF HASH
# ============================================================

class TestHashCPF(TestCase):

    def test_hash_gerado_corretamente(self):
        """O hash do mesmo CPF deve ser sempre igual."""
        cpf = '52998224725'
        h1 = gerar_hash_cpf(cpf)
        h2 = gerar_hash_cpf(cpf)
        self.assertEqual(h1, h2)

    def test_hashes_diferentes_para_cpfs_diferentes(self):
        """CPFs diferentes devem gerar hashes diferentes."""
        h1 = gerar_hash_cpf('52998224725')
        h2 = gerar_hash_cpf('11144477735')
        self.assertNotEqual(h1, h2)

    def test_hash_tem_64_caracteres(self):
        """Hash SHA-256 deve ter 64 caracteres."""
        h = gerar_hash_cpf('52998224725')
        self.assertEqual(len(h), 64)


# ============================================================
# TESTES — MODELO INTERESSADO
# ============================================================

class TestInteressadoModel(TestCase):

    def setUp(self):
        self.interessado = criar_interessado()

    def test_senha_criptografada(self):
        """A senha não deve ser armazenada em texto puro."""
        self.assertNotEqual(self.interessado.senha, 'senha123')
        self.assertTrue(self.interessado.senha.startswith('pbkdf2_'))

    def test_check_password_correto(self):
        """check_password deve retornar True para a senha correta."""
        self.assertTrue(self.interessado.check_password('senha123'))

    def test_check_password_incorreto(self):
        """check_password deve retornar False para senha errada."""
        self.assertFalse(self.interessado.check_password('senhaerrada'))

    def test_is_authenticated(self):
        """Interessado deve ser autenticado."""
        self.assertTrue(self.interessado.is_authenticated)

    def test_is_anonymous_false(self):
        """Interessado não é anônimo."""
        self.assertFalse(self.interessado.is_anonymous)

    def test_str(self):
        """__str__ deve conter o nome."""
        self.assertIn('Teste Silva', str(self.interessado))

    def test_factory_interessado(self):
        """Testa se factory cria Interessado válido."""
        interessado = InteressadoFactory.create()
        self.assertEqual(interessado.cpf, '123.456.789-00')  # max_length=14
        self.assertEqual(interessado.num_nis, '123.45678.90-1')  # max_length=15
        self.assertEqual(interessado.cep, '12345678')  # max_length=8
        self.assertEqual(interessado.rg, '12.345.678-9')  # max_length=20
        self.assertTrue(interessado.consentimento_lgpd)
        self.assertTrue(interessado.check_password('senha123'))






