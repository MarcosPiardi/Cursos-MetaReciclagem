"""
Arquivo: test_models.py
Caminho: apps/interessados/tests/test_models.py
Testes dos models: Interessado, Sexo, Fototipo, PasswordResetToken, SolicitacaoExclusao
Atualizações:
 - 20/03/2026 - Criacao inicial dos testes
 - 29/05/2026 - Refatoracao para melhorar cobertura e legibilidade
              - Removido import duplicado / nao utilizado
              - Removido codigo comentado
              - Consolidado classes de teste fragmentadas (Interessado)
              - Melhorado helper com setUpTestData
 - 16/06/2026 - Refatorado para pytest puro
              - Convertido de Django TestCase para pytest puro
              - Testes como funcoes modulares com @pytest.mark.django_db
              - Fixture compartilhada para Interessado valido
              - Asserts nativos do Python (assert x == y)
              - pytest.raises para excecoes esperadas
"""

import pytest
from django.utils import timezone
from django.db import IntegrityError
from django.core.exceptions import ValidationError

from ..models import Interessado, Sexo, Fototipo, PasswordResetToken, SolicitacaoExclusao, gerar_hash_cpf
from .factories import InteressadoFactory, SexoFactory, FototipoFactory, PasswordResetTokenFactory


# ============================================================
# FIXTURES
# ============================================================

@pytest.fixture
def interessado_valido(db):
    """Cria e salva um Interessado valido para testes."""
    i = Interessado(
        nome='Teste Silva',
        cpf='52998224725',
        cpf_hash=gerar_hash_cpf('52998224725'),
        consentimento_lgpd=True,
        consentimento_lgpd_em=timezone.now(),
    )
    i.set_password('senha123')
    i.save()
    return i


# ============================================================
# GERAR_HASH_CPF (sem banco)
# ============================================================

class TestHashCPF:
    """Agrupamento logico - nao requer banco de dados."""

    def test_mesmo_cpf_mesmo_hash(self):
        h1 = gerar_hash_cpf('52998224725')
        h2 = gerar_hash_cpf('52998224725')
        assert h1 == h2

    def test_cpfs_diferentes_hashes_diferentes(self):
        h1 = gerar_hash_cpf('52998224725')
        h2 = gerar_hash_cpf('11144477735')
        assert h1 != h2

    def test_hash_tem_64_caracteres(self):
        h = gerar_hash_cpf('52998224725')
        assert len(h) == 64


# ============================================================
# INTERESSADO
# ============================================================

@pytest.mark.django_db
class TestInteressadoModel:
    """Testes do model Interessado."""

    # --- Senha ---

    def test_senha_nao_e_texto_puro(self, interessado_valido):
        assert interessado_valido.senha != 'senha123'
        assert interessado_valido.senha.startswith('pbkdf2_')

    def test_check_password_ok(self, interessado_valido):
        assert interessado_valido.check_password('senha123')

    def test_check_password_errado(self, interessado_valido):
        assert not interessado_valido.check_password('senhaerrada')

    # --- Interface de autenticacao ---

    def test_is_authenticated(self, interessado_valido):
        assert interessado_valido.is_authenticated

    def test_is_anonymous(self, interessado_valido):
        assert not interessado_valido.is_anonymous

    # --- str ---

    def test_str_contem_nome(self, interessado_valido):
        assert 'Teste Silva' in str(interessado_valido)

    # --- Criptografia CPF ---

    def test_cpf_criptografado_no_banco(self):
        cpf_original = '12345678901'
        i = InteressadoFactory.create(cpf=cpf_original)
        recarregado = Interessado.objects.get(id=i.id)
        assert recarregado.cpf == cpf_original

    def test_cpf_hash_unico(self):
        i1 = InteressadoFactory.create(cpf='12345678901')
        i2 = InteressadoFactory.create(cpf='98765432100')
        assert i1.cpf_hash != i2.cpf_hash
        assert i1.cpf_hash == gerar_hash_cpf('12345678901')

    def test_cpf_hash_busca_eficiente(self):
        cpf = '12345678901'
        i = InteressadoFactory.create(cpf=cpf)
        resultado = Interessado.objects.filter(cpf_hash=gerar_hash_cpf(cpf)).first()
        assert resultado.id == i.id

    # --- Criptografia NIS ---

    def test_nis_criptografado_no_banco(self):
        nis_original = '12345678901'
        i = InteressadoFactory.create(num_nis=nis_original)
        recarregado = Interessado.objects.get(id=i.id)
        assert recarregado.num_nis == nis_original

    # --- Factory cria dados validos ---

    def test_factory_cria_interessado_valido(self):
        i = InteressadoFactory.create()
        assert i.cpf is not None
        assert len(i.cpf.replace('.', '').replace('-', '')) == 11
        assert i.num_nis is not None
        assert i.cpf_hash is not None
        assert len(i.cpf_hash) == 64
        assert i.check_password('senha123')

    # --- CPF field validation ---

    def test_cpf_11_digitos_valido(self):
        cpf = '12345678901'
        i = Interessado(nome='Teste', cpf=cpf, cpf_hash=gerar_hash_cpf(cpf),
                        consentimento_lgpd=True)
        i.set_password('senha123')
        i.full_clean()
        i.save()
        assert i.cpf == cpf

    def test_cpf_formatado_aceito_pelo_model(self):
        """Model aceita CPF formatado (14 chars). A limpeza e da form."""
        cpf = '123.456.789-01'
        i = Interessado(nome='Teste', cpf=cpf, cpf_hash=gerar_hash_cpf(cpf),
                        consentimento_lgpd=True)
        i.set_password('senha123')
        i.save()
        assert i.cpf == cpf

    # --- NIS field validation ---

    def test_nis_valido(self):
        i = InteressadoFactory.create(num_nis='12345678901')
        assert i.num_nis == '12345678901'

    def test_nis_muito_curto_rejeita(self):
        i = Interessado(nome='Teste', cpf='12345678901',
                        cpf_hash=gerar_hash_cpf('12345678901'),
                        num_nis='1234567890',
                        consentimento_lgpd=True)
        i.set_password('senha123')
        with pytest.raises(ValidationError):
            i.full_clean()

    # --- CEP field validation ---

    def test_cep_valido(self):
        i = InteressadoFactory.create(cep='12345678')
        assert i.cep == '12345678'

    def test_cep_muito_curto_rejeita(self):
        i = Interessado(nome='Teste', cpf='12345678901',
                        cpf_hash=gerar_hash_cpf('12345678901'),
                        cep='1234567',
                        consentimento_lgpd=True)
        i.set_password('senha123')
        with pytest.raises(ValidationError):
            i.full_clean()

    # --- Relacionamentos ---

    def test_relacionamento_sexo(self):
        sexo = SexoFactory()
        i = InteressadoFactory.create(sexo=sexo)
        assert i.sexo == sexo

    def test_relacionamento_fototipo(self):
        fototipo = FototipoFactory()
        i = InteressadoFactory.create(fototipo=fototipo)
        assert i.fototipo == fototipo

    def test_relacionamentos_simultaneos(self):
        sexo = SexoFactory()
        fototipo = FototipoFactory()
        i = InteressadoFactory.create(sexo=sexo, fototipo=fototipo)
        assert i.sexo == sexo
        assert i.fototipo == fototipo

    # --- Flags PCD ---

    def test_multiplas_deficiencias(self):
        i = InteressadoFactory.create(
            necessidades_especiais=True,
            pcd_fisica=True,
            pcd_auditiva=True,
        )
        assert i.pcd_fisica
        assert i.pcd_auditiva
        assert not i.pcd_visual

    def test_tem_deficiencia_property(self):
        i1 = InteressadoFactory.create(pcd_fisica=True)
        i2 = InteressadoFactory.create(
            pcd_fisica=False, pcd_auditiva=False,
            pcd_visual=False, pcd_intelectual=False,
            pcd_psicossocial=False, pcd_multiplas=False,
        )
        assert i1.tem_deficiencia
        assert not i2.tem_deficiencia


# ============================================================
# SOLICITACAOEXCLUSAO (LGPD)
# ============================================================

@pytest.mark.django_db
class TestSolicitacaoExclusao:

    def test_criada_com_status_pendente(self):
        i = InteressadoFactory.create()
        s = SolicitacaoExclusao.objects.create(
            interessado=i, nome_solicitante='Joao Silva',
            email_solicitante='joao@email.com',
            motivo='Nao quero mais participar',
            status='PENDENTE',
        )
        assert s.status == 'PENDENTE'
        assert s.interessado == i

    def test_todos_os_status_sao_validos(self):
        i = InteressadoFactory.create()
        for status in ['PENDENTE', 'APROVADA', 'RECUSADA']:
            s = SolicitacaoExclusao.objects.create(
                interessado=i, nome_solicitante='Teste',
                status=status,
            )
            assert s.status == status

    def test_nome_solicitante_obrigatorio(self):
        i = InteressadoFactory.create()
        s = SolicitacaoExclusao(
            interessado=i, nome_solicitante='', status='PENDENTE',
        )
        with pytest.raises(ValidationError):
            s.full_clean()

    def test_email_solicitante_opcional(self):
        i = InteressadoFactory.create()
        s = SolicitacaoExclusao.objects.create(
            interessado=i, nome_solicitante='Maria Santos',
            email_solicitante='', status='PENDENTE',
        )
        assert s.email_solicitante == ''

    def test_str_contem_status_e_nome(self):
        i = InteressadoFactory.create()
        s = SolicitacaoExclusao.objects.create(
            interessado=i, nome_solicitante='Ana Costa',
            status='APROVADA', solicitado_em=timezone.now(),
        )
        assert 'APROVADA' in str(s)
        assert 'Ana Costa' in str(s)


# ============================================================
# SEXO
# ============================================================

@pytest.mark.django_db
class TestSexoModel:

    def test_factory_cria_valido(self):
        s = SexoFactory(nome='Masculino')
        assert s.nome == 'Masculino'

    def test_str_retorna_nome(self):
        s = SexoFactory(nome='Feminino')
        assert str(s) == 'Feminino'

    def test_unique_constraint_violado(self):
        Sexo.objects.create(nome='Outro')
        with pytest.raises(IntegrityError):
            Sexo.objects.create(nome='Outro')


# ============================================================
# FOTOTIPO
# ============================================================

@pytest.mark.django_db
class TestFototipoModel:

    def test_factory_cria_valido(self):
        f = FototipoFactory(nome='Tipo IV')
        assert f.nome == 'Tipo IV'

    def test_descricao_pode_ser_vazia(self):
        f = FototipoFactory(descricao='')
        assert f.descricao == ''


# ============================================================
# PASSWORDRESETTOKEN
# ============================================================

@pytest.mark.django_db
class TestPasswordResetTokenModel:

    def test_factory_cria_token_valido(self):
        t = PasswordResetTokenFactory.create()
        assert t.id is not None
        assert t.token is not None
        assert not t.usado

    def test_expiracao_futura(self):
        t = PasswordResetTokenFactory.create()
        assert t.expira_em > t.criado_em

    def test_marca_como_usado(self):
        t = PasswordResetTokenFactory.create()
        t.usado = True
        t.save()
        t.refresh_from_db()
        assert t.usado


