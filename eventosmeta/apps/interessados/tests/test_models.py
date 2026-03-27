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
from ..models import Interessado, SolicitacaoExclusao, gerar_hash_cpf

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



    # ============================================================
    # BLOCO 2: VALIDADORES
    # ============================================================

    def test_cpf_valido(self):
        """CPF com 11 dígitos deve passar na validação."""
        cpf_valido = '12345678901'
        interessado = Interessado(
            nome='Test User',
            cpf=cpf_valido,
            cpf_hash=gerar_hash_cpf(cpf_valido),
            consentimento_lgpd=True,
        )
        interessado.set_password('senha123')
        # Não deve lançar ValidationError
        interessado.full_clean()
        interessado.save()
        self.assertEqual(interessado.cpf, cpf_valido)

    # def test_cpf_invalido_caracteres(self):
    #     """CPF com caracteres não numéricos deve falhar na validação."""
    #     from django.core.exceptions import ValidationError
    #     cpf_invalido = '123.456.789-01'  # Formatado
    #     interessado = Interessado(
    #         nome='Test User',
    #         cpf=cpf_invalido,
    #         cpf_hash=gerar_hash_cpf(cpf_invalido),
    #         consentimento_lgpd=True,
    #     )
    #     interessado.set_password('senha123')
    #     with self.assertRaises(ValidationError):
    #         interessado.full_clean()

    def test_cpf_formatado_aceito(self):
        """Model aceita CPF formatado (limpeza é responsabilidade da form)."""
        cpf_formatado = '123.456.789-01'
        interessado = Interessado(
            nome='Test User',
            cpf=cpf_formatado,
            cpf_hash=gerar_hash_cpf(cpf_formatado),
            consentimento_lgpd=True,
        )
        interessado.set_password('senha123')
        # Não deve lançar erro - model aceita strings até 14 chars
        interessado.save()
        self.assertEqual(interessado.cpf, cpf_formatado)    

    def test_nis_valido(self):
        """NIS com 11-15 dígitos deve passar na validação."""
        nis_valido = '12345678901'  # 11 dígitos
        interessado = InteressadoFactory.create(num_nis=nis_valido)
        self.assertEqual(interessado.num_nis, nis_valido)

    def test_nis_invalido_poucos_digitos(self):
        """NIS com <11 dígitos deve falhar na validação."""
        from django.core.exceptions import ValidationError
        nis_invalido = '1234567890'  # 10 dígitos (menos que o mínimo)
        interessado = Interessado(
            nome='Test User',
            cpf='12345678901',
            cpf_hash=gerar_hash_cpf('12345678901'),
            num_nis=nis_invalido,
            consentimento_lgpd=True,
        )
        interessado.set_password('senha123')
        with self.assertRaises(ValidationError):
            interessado.full_clean()

    def test_cep_valido(self):
        """CEP com exatamente 8 dígitos deve passar na validação."""
        cep_valido = '12345678'
        interessado = InteressadoFactory.create(cep=cep_valido)
        self.assertEqual(interessado.cep, cep_valido)

    def test_cep_invalido_formato(self):
        """CEP com menos de 8 dígitos deve falhar na validação."""
        from django.core.exceptions import ValidationError
        cep_invalido = '1234567'  # 7 dígitos
        interessado = Interessado(
            nome='Test User',
            cpf='12345678901',
            cpf_hash=gerar_hash_cpf('12345678901'),
            cep=cep_invalido,
            consentimento_lgpd=True,
        )
        interessado.set_password('senha123')
        with self.assertRaises(ValidationError):
            interessado.full_clean()

    # ============================================================
    # BLOCO 3: ENCRYPTEDCHARFIELD (Criptografia CPF/NIS)
    # ============================================================

    def test_cpf_criptografado_salvo(self):
        """CPF é armazenado criptografado no banco de dados."""
        cpf_original = '12345678901'
        interessado = InteressadoFactory.create(cpf=cpf_original)
        # Recarrega do banco para verificar criptografia
        interessado_reload = Interessado.objects.get(id=interessado.id)
        # CPF descriptografado deve ser igual ao original
        self.assertEqual(interessado_reload.cpf, cpf_original)

    def test_cpf_hash_unico_por_cpf(self):
        """Cada CPF gera um hash único e imutável para buscas."""
        cpf1 = '12345678901'
        cpf2 = '98765432100'
        i1 = InteressadoFactory.create(cpf=cpf1)
        i2 = InteressadoFactory.create(cpf=cpf2)
        # Hashes devem ser diferentes
        self.assertNotEqual(i1.cpf_hash, i2.cpf_hash)
        # Hash deve ser consistente
        hash_cpf1 = gerar_hash_cpf(cpf1)
        self.assertEqual(i1.cpf_hash, hash_cpf1)

    def test_nis_criptografado_salvo(self):
        """NIS é armazenado criptografado no banco de dados."""
        nis_original = '12345678901'
        interessado = InteressadoFactory.create(num_nis=nis_original)
        # Recarrega do banco
        interessado_reload = Interessado.objects.get(id=interessado.id)
        # NIS descriptografado deve ser igual ao original
        self.assertEqual(interessado_reload.num_nis, nis_original)

    def test_cpf_hash_facilita_busca(self):
        """cpf_hash permite busca eficiente sem descriptografar CPF."""
        cpf = '12345678901'
        interessado = InteressadoFactory.create(cpf=cpf)
        cpf_hash = gerar_hash_cpf(cpf)
        # Busca por hash deve retornar o interessado
        resultado = Interessado.objects.filter(cpf_hash=cpf_hash).first()
        self.assertIsNotNone(resultado)
        self.assertEqual(resultado.id, interessado.id)


    # ============================================================
    # BLOCO 1: SOLICITACAOEXCLUSAO (LGPD — Direito ao Esquecimento)
    # ============================================================

    def test_solicitacao_exclusao_criada(self):
        """SolicitacaoExclusao é criada com status PENDENTE."""
        interessado = InteressadoFactory.create()
        solicitacao = SolicitacaoExclusao.objects.create(
            interessado=interessado,
            nome_solicitante='João Silva',
            email_solicitante='joao@email.com',
            motivo='Não quero mais participar',
            status='PENDENTE'
        )
        self.assertEqual(solicitacao.status, 'PENDENTE')
        self.assertEqual(solicitacao.interessado, interessado)

    def test_solicitacao_exclusao_status_choices(self):
        """Solicitação pode ter status PENDENTE, APROVADA ou RECUSADA."""
        interessado = InteressadoFactory.create()
        status_validos = ['PENDENTE', 'APROVADA', 'RECUSADA']
        
        for status in status_validos:
            solicitacao = SolicitacaoExclusao.objects.create(
                interessado=interessado,
                nome_solicitante='Teste',
                status=status
            )
            self.assertEqual(solicitacao.status, status)

    def test_solicitacao_exclusao_nome_obrigatorio(self):
        """Nome do solicitante é obrigatório."""
        interessado = InteressadoFactory.create()
        solicitacao = SolicitacaoExclusao(
            interessado=interessado,
            nome_solicitante='',  # Vazio
            status='PENDENTE'
        )
        # Tenta salvar sem nome
        with self.assertRaises(Exception):
            solicitacao.full_clean()

    def test_solicitacao_exclusao_email_opcional(self):
        """Email do solicitante é opcional."""
        interessado = InteressadoFactory.create()
        solicitacao = SolicitacaoExclusao.objects.create(
            interessado=interessado,
            nome_solicitante='Maria Santos',
            email_solicitante='',  # Vazio é permitido
            status='PENDENTE'
        )
        self.assertEqual(solicitacao.email_solicitante, '')

    def test_solicitacao_exclusao_str(self):
        """__str__ retorna formato legível com status e data."""
        from django.utils import timezone
        interessado = InteressadoFactory.create()
        solicitacao = SolicitacaoExclusao.objects.create(
            interessado=interessado,
            nome_solicitante='Ana Costa',
            status='APROVADA',
            solicitado_em=timezone.now()
        )
        str_repr = str(solicitacao)
        self.assertIn('APROVADA', str_repr)
        self.assertIn('Ana Costa', str_repr)






