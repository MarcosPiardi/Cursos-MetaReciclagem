"""
Arquivo: test_models.py
Caminho: apps/interessados/tests/test_models.py
Testes dos models: Interessado, Sexo, Fototipo, PasswordResetToken, SolicitacaoExclusao
Data: 20/03/2026
Refatorado: 29/05/2026
  - Removido import duplicado / nao utilizado
  - Removido codigo comentado
  - Consolidado classes de teste fragmentadas (Interessado)
  - Melhorado helper com setUpTestData
"""

from django.test import TestCase
from django.utils import timezone
from django.db import IntegrityError
from django.core.exceptions import ValidationError

from ..models import Interessado, Sexo, Fototipo, PasswordResetToken, SolicitacaoExclusao, gerar_hash_cpf
from .factories import InteressadoFactory, SexoFactory, FototipoFactory, PasswordResetTokenFactory


# ============================================================
# UTILITARIO
# ============================================================

def build_interessado(cpf='52998224725', nome='Teste Silva', senha='senha123'):
    """Cria e salva um Interessado valido para testes."""
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
# GERAR_HASH_CPF
# ============================================================

class TestHashCPF(TestCase):

    def test_mesmo_cpf_mesmo_hash(self):
        h1 = gerar_hash_cpf('52998224725')
        h2 = gerar_hash_cpf('52998224725')
        self.assertEqual(h1, h2)

    def test_cpfs_diferentes_hashes_diferentes(self):
        h1 = gerar_hash_cpf('52998224725')
        h2 = gerar_hash_cpf('11144477735')
        self.assertNotEqual(h1, h2)

    def test_hash_tem_64_caracteres(self):
        h = gerar_hash_cpf('52998224725')
        self.assertEqual(len(h), 64)


# ============================================================
# INTERESSADO (consolidado)
# ============================================================

class TestInteressadoModel(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.obj = build_interessado()

    # --- Senha ---

    def test_senha_nao_e_texto_puro(self):
        self.assertNotEqual(self.obj.senha, 'senha123')
        self.assertTrue(self.obj.senha.startswith('pbkdf2_'))

    def test_check_password_ok(self):
        self.assertTrue(self.obj.check_password('senha123'))

    def test_check_password_errado(self):
        self.assertFalse(self.obj.check_password('senhaerrada'))

    # --- Interface de autenticacao ---

    def test_is_authenticated(self):
        self.assertTrue(self.obj.is_authenticated)

    def test_is_anonymous(self):
        self.assertFalse(self.obj.is_anonymous)

    # --- str ---

    def test_str_contem_nome(self):
        self.assertIn('Teste Silva', str(self.obj))

    # --- Criptografia CPF ---

    def test_cpf_criptografado_no_banco(self):
        cpf_original = '12345678901'
        i = InteressadoFactory.create(cpf=cpf_original)
        recarregado = Interessado.objects.get(id=i.id)
        self.assertEqual(recarregado.cpf, cpf_original)

    def test_cpf_hash_unico(self):
        i1 = InteressadoFactory.create(cpf='12345678901')
        i2 = InteressadoFactory.create(cpf='98765432100')
        self.assertNotEqual(i1.cpf_hash, i2.cpf_hash)
        self.assertEqual(i1.cpf_hash, gerar_hash_cpf('12345678901'))

    def test_cpf_hash_busca_eficiente(self):
        cpf = '12345678901'
        i = InteressadoFactory.create(cpf=cpf)
        resultado = Interessado.objects.filter(cpf_hash=gerar_hash_cpf(cpf)).first()
        self.assertEqual(resultado.id, i.id)

    # --- Criptografia NIS ---

    def test_nis_criptografado_no_banco(self):
        nis_original = '12345678901'
        i = InteressadoFactory.create(num_nis=nis_original)
        recarregado = Interessado.objects.get(id=i.id)
        self.assertEqual(recarregado.num_nis, nis_original)

    # --- Factory cria dados validos ---

    def test_factory_cria_interessado_valido(self):
        i = InteressadoFactory.create()
        self.assertIsNotNone(i.cpf)
        self.assertEqual(len(i.cpf.replace('.', '').replace('-', '')), 11)
        self.assertIsNotNone(i.num_nis)
        self.assertIsNotNone(i.cpf_hash)
        self.assertEqual(len(i.cpf_hash), 64)
        self.assertTrue(i.check_password('senha123'))

    # --- CPF field validation ---

    def test_cpf_11_digitos_valido(self):
        cpf = '12345678901'
        i = Interessado(nome='Teste', cpf=cpf, cpf_hash=gerar_hash_cpf(cpf),
                        consentimento_lgpd=True)
        i.set_password('senha123')
        i.full_clean()
        i.save()
        self.assertEqual(i.cpf, cpf)

    def test_cpf_formatado_aceito_pelo_model(self):
        """Model aceita CPF formatado (14 chars). A limpeza e da form."""
        cpf = '123.456.789-01'
        i = Interessado(nome='Teste', cpf=cpf, cpf_hash=gerar_hash_cpf(cpf),
                        consentimento_lgpd=True)
        i.set_password('senha123')
        i.save()
        self.assertEqual(i.cpf, cpf)

    # --- NIS field validation ---

    def test_nis_valido(self):
        i = InteressadoFactory.create(num_nis='12345678901')
        self.assertEqual(i.num_nis, '12345678901')

    def test_nis_muito_curto_rejeita(self):
        i = Interessado(nome='Teste', cpf='12345678901',
                        cpf_hash=gerar_hash_cpf('12345678901'),
                        num_nis='1234567890',
                        consentimento_lgpd=True)
        i.set_password('senha123')
        with self.assertRaises(ValidationError):
            i.full_clean()

    # --- CEP field validation ---

    def test_cep_valido(self):
        i = InteressadoFactory.create(cep='12345678')
        self.assertEqual(i.cep, '12345678')

    def test_cep_muito_curto_rejeita(self):
        i = Interessado(nome='Teste', cpf='12345678901',
                        cpf_hash=gerar_hash_cpf('12345678901'),
                        cep='1234567',
                        consentimento_lgpd=True)
        i.set_password('senha123')
        with self.assertRaises(ValidationError):
            i.full_clean()

    # --- Relacionamentos ---

    def test_relacionamento_sexo(self):
        sexo = SexoFactory()
        i = InteressadoFactory.create(sexo=sexo)
        self.assertEqual(i.sexo, sexo)

    def test_relacionamento_fototipo(self):
        fototipo = FototipoFactory()
        i = InteressadoFactory.create(fototipo=fototipo)
        self.assertEqual(i.fototipo, fototipo)

    def test_relacionamentos_simultaneos(self):
        sexo = SexoFactory()
        fototipo = FototipoFactory()
        i = InteressadoFactory.create(sexo=sexo, fototipo=fototipo)
        self.assertEqual(i.sexo, sexo)
        self.assertEqual(i.fototipo, fototipo)

    # --- Flags PCD ---

    def test_multiplas_deficiencias(self):
        i = InteressadoFactory.create(necessidades_especiais=True,
                                      pcd_fisica=True, pcd_auditiva=True)
        self.assertTrue(i.pcd_fisica)
        self.assertTrue(i.pcd_auditiva)
        self.assertFalse(i.pcd_visual)

    def test_tem_deficiencia_property(self):
        i1 = InteressadoFactory.create(pcd_fisica=True)
        i2 = InteressadoFactory.create(pcd_fisica=False, pcd_auditiva=False,
                                        pcd_visual=False, pcd_intelectual=False,
                                        pcd_psicossocial=False, pcd_multiplas=False)
        self.assertTrue(i1.tem_deficiencia)
        self.assertFalse(i2.tem_deficiencia)


# ============================================================
# SOLICITACAOEXCLUSAO (LGPD)
# ============================================================

class TestSolicitacaoExclusao(TestCase):

    def test_criada_com_status_pendente(self):
        i = InteressadoFactory.create()
        s = SolicitacaoExclusao.objects.create(
            interessado=i, nome_solicitante='Joao Silva',
            email_solicitante='joao@email.com',
            motivo='Nao quero mais participar',
            status='PENDENTE',
        )
        self.assertEqual(s.status, 'PENDENTE')
        self.assertEqual(s.interessado, i)

    def test_todos_os_status_sao_validos(self):
        i = InteressadoFactory.create()
        for status in ['PENDENTE', 'APROVADA', 'RECUSADA']:
            s = SolicitacaoExclusao.objects.create(
                interessado=i, nome_solicitante='Teste',
                status=status,
            )
            self.assertEqual(s.status, status)

    def test_nome_solicitante_obrigatorio(self):
        i = InteressadoFactory.create()
        s = SolicitacaoExclusao(interessado=i, nome_solicitante='',
                                status='PENDENTE')
        with self.assertRaises(ValidationError):
            s.full_clean()

    def test_email_solicitante_opcional(self):
        i = InteressadoFactory.create()
        s = SolicitacaoExclusao.objects.create(
            interessado=i, nome_solicitante='Maria Santos',
            email_solicitante='', status='PENDENTE',
        )
        self.assertEqual(s.email_solicitante, '')

    def test_str_contem_status_e_nome(self):
        i = InteressadoFactory.create()
        s = SolicitacaoExclusao.objects.create(
            interessado=i, nome_solicitante='Ana Costa',
            status='APROVADA', solicitado_em=timezone.now(),
        )
        self.assertIn('APROVADA', str(s))
        self.assertIn('Ana Costa', str(s))


# ============================================================
# SEXO
# ============================================================

class TestSexoModel(TestCase):

    def test_factory_cria_valido(self):
        s = SexoFactory(nome='Masculino')
        self.assertEqual(s.nome, 'Masculino')

    def test_str_retorna_nome(self):
        s = SexoFactory(nome='Feminino')
        self.assertEqual(str(s), 'Feminino')

    def test_unique_constraint_violado(self):
        Sexo.objects.create(nome='Outro')
        with self.assertRaises(IntegrityError):
            Sexo.objects.create(nome='Outro')


# ============================================================
# FOTOTIPO
# ============================================================

class TestFototipoModel(TestCase):

    def test_factory_cria_valido(self):
        f = FototipoFactory(nome='Tipo IV')
        self.assertEqual(f.nome, 'Tipo IV')

    def test_descricao_pode_ser_vazia(self):
        f = FototipoFactory(descricao='')
        self.assertEqual(f.descricao, '')


# ============================================================
# PASSWORDRESETTOKEN
# ============================================================

class TestPasswordResetTokenModel(TestCase):

    def test_factory_cria_token_valido(self):
        t = PasswordResetTokenFactory.create()
        self.assertIsNotNone(t.id)
        self.assertIsNotNone(t.token)
        self.assertFalse(t.usado)

    def test_expiracao_futura(self):
        t = PasswordResetTokenFactory.create()
        self.assertTrue(t.expira_em > t.criado_em)

    def test_marca_como_usado(self):
        t = PasswordResetTokenFactory.create()
        t.usado = True
        t.save()
        t.refresh_from_db()
        self.assertTrue(t.usado)


        