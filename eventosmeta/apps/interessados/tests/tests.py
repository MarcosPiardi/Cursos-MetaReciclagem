"""
Arquivo: tests.py
Caminho: apps/interessados/tests.py
Alteração: Testes automatizados — validação CPF, login, cadastro, LGPD
Data: 20/03/2026
"""

from django.test import TestCase, Client
from django.urls import reverse
from django.utils import timezone

from .models import Interessado, SolicitacaoExclusao, gerar_hash_cpf
from .forms import CadastroInteressadoForm, LoginInteressadoForm


# ============================================================
# HELPERS
# ============================================================

def criar_interessado(cpf='52998224725', nome='Teste Silva', senha='senha123'):
    """Cria um interessado válido para uso nos testes."""
    i = Interessado(
        nome              = nome,
        cpf               = cpf,
        cpf_hash          = gerar_hash_cpf(cpf),
        consentimento_lgpd    = True,
        consentimento_lgpd_em = timezone.now(),
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
        cpf  = '52998224725'
        h1   = gerar_hash_cpf(cpf)
        h2   = gerar_hash_cpf(cpf)
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


# ============================================================
# TESTES — FORMULÁRIO DE CADASTRO (validação CPF)
# ============================================================

class TestValidacaoCPF(TestCase):

    def _dados_base(self, cpf):
        """Retorna dados mínimos para o formulário com o CPF informado."""
        return {
            'nome'              : 'Teste Silva',
            'cpf'               : cpf,
            'senha'             : 'senha123',
            'confirmar_senha'   : 'senha123',
            'consentimento_lgpd': True,
        }

    def test_cpf_valido_aceito(self):
        """CPF válido deve passar na validação."""
        form = CadastroInteressadoForm(data=self._dados_base('529.982.247-25'))
        # Valida apenas o campo cpf isoladamente
        form.is_valid()
        self.assertNotIn('cpf', form.errors)

    def test_cpf_todos_digitos_iguais_rejeitado(self):
        """CPF com todos os dígitos iguais deve ser rejeitado."""
        form = CadastroInteressadoForm(data=self._dados_base('111.111.111-11'))
        form.is_valid()
        self.assertIn('cpf', form.errors)

    def test_cpf_digito_verificador_errado(self):
        """CPF com dígito verificador errado deve ser rejeitado."""
        form = CadastroInteressadoForm(data=self._dados_base('529.982.247-00'))
        form.is_valid()
        self.assertIn('cpf', form.errors)

    def test_cpf_duplicado_rejeitado(self):
        """CPF já cadastrado deve ser rejeitado."""
        criar_interessado(cpf='52998224725')
        form = CadastroInteressadoForm(data=self._dados_base('529.982.247-25'))
        form.is_valid()
        self.assertIn('cpf', form.errors)

    def test_cpf_formatado_aceito(self):
        """CPF formatado deve ser aceito e limpo."""
        form = CadastroInteressadoForm(data=self._dados_base('529.982.247-25'))
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data['cpf'], '52998224725')

    def test_cpf_sem_formatacao_aceito(self):
        """CPF sem formatação também deve ser aceito."""
        form = CadastroInteressadoForm(data=self._dados_base('52998224725'))
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data['cpf'], '52998224725')

# ============================================================
# TESTES — FORMULÁRIO DE LOGIN
# ============================================================

class TestLoginForm(TestCase):

    def setUp(self):
        self.interessado = criar_interessado(cpf='52998224725', senha='senha123')

    def test_login_correto(self):
        """Login com CPF e senha corretos deve ser válido."""
        form = LoginInteressadoForm(data={
            'cpf'  : '529.982.247-25',
            'senha': 'senha123',
        })
        self.assertTrue(form.is_valid())
        self.assertEqual(form.interessado, self.interessado)

    def test_login_senha_errada(self):
        """Login com senha errada deve falhar."""
        form = LoginInteressadoForm(data={
            'cpf'  : '529.982.247-25',
            'senha': 'senhaerrada',
        })
        self.assertFalse(form.is_valid())

    def test_login_cpf_nao_cadastrado(self):
        """Login com CPF não cadastrado deve falhar."""
        form = LoginInteressadoForm(data={
            'cpf'  : '111.444.777-35',
            'senha': 'senha123',
        })
        self.assertFalse(form.is_valid())

    def test_login_conta_inativa(self):
        """Login com conta inativa deve falhar."""
        self.interessado.is_active = False
        self.interessado.save()
        form = LoginInteressadoForm(data={
            'cpf'  : '529.982.247-25',
            'senha': 'senha123',
        })
        self.assertFalse(form.is_valid())


# ============================================================
# TESTES — VIEWS (acesso às páginas)
# ============================================================

class TestViews(TestCase):

    def setUp(self):
        self.client      = Client()
        self.interessado = criar_interessado(cpf='52998224725', senha='senha123')

    def _fazer_login(self):
        """Faz login do interessado via POST."""
        self.client.post(reverse('interessados:login'), {
            'cpf'  : '52998224725',
            'senha': 'senha123',
        })

    def test_pagina_login_acessivel(self):
        """Página de login deve retornar 200."""
        response = self.client.get(reverse('interessados:login'))
        self.assertEqual(response.status_code, 200)

    def test_pagina_cadastro_acessivel(self):
        """Página de cadastro deve retornar 200."""
        response = self.client.get(reverse('interessados:cadastro'))
        self.assertEqual(response.status_code, 200)

    def test_dashboard_sem_login_redireciona(self):
        """Dashboard sem login deve redirecionar."""
        response = self.client.get(reverse('interessados:dashboard'))
        self.assertNotEqual(response.status_code, 200)

    def test_dashboard_com_login_acessivel(self):
        """Dashboard com login deve retornar 200."""
        self._fazer_login()
        response = self.client.get(reverse('interessados:dashboard'))
        self.assertEqual(response.status_code, 200)

    def test_meus_dados_sem_login_redireciona(self):
        """Meus dados sem login deve redirecionar."""
        response = self.client.get(reverse('interessados:meus_dados'))
        self.assertNotEqual(response.status_code, 200)

    def test_solicitar_exclusao_sem_login_redireciona(self):
        """Solicitação de exclusão sem login deve redirecionar."""
        response = self.client.get(reverse('interessados:solicitar_exclusao'))
        self.assertNotEqual(response.status_code, 200)


# ============================================================
# TESTES — SOLICITAÇÃO DE EXCLUSÃO (LGPD)
# ============================================================

class TestSolicitacaoExclusao(TestCase):

    def setUp(self):
        self.client      = Client()
        self.interessado = criar_interessado(cpf='52998224725', senha='senha123')
        # Faz login
        self.client.post(reverse('interessados:login'), {
            'cpf'  : '52998224725',
            'senha': 'senha123',
        })

    def test_solicitacao_criada_com_confirmacao(self):
        """Solicitação com CONFIRMAR deve ser criada."""
        self.client.post(reverse('interessados:solicitar_exclusao'), {
            'confirmacao': 'CONFIRMAR',
            'motivo'     : 'Teste de exclusão',
        })
        self.assertEqual(
            SolicitacaoExclusao.objects.filter(
                interessado=self.interessado,
                status='PENDENTE'
            ).count(),
            1
        )

    def test_solicitacao_nao_criada_sem_confirmacao(self):
        """Solicitação sem CONFIRMAR não deve ser criada."""
        self.client.post(reverse('interessados:solicitar_exclusao'), {
            'confirmacao': 'sim',
            'motivo'     : 'Teste',
        })
        self.assertEqual(
            SolicitacaoExclusao.objects.filter(interessado=self.interessado).count(),
            0
        )

    def test_segunda_solicitacao_bloqueada(self):
        """Segunda solicitação pendente deve ser bloqueada."""
        # Cria a primeira
        SolicitacaoExclusao.objects.create(
            interessado      = self.interessado,
            nome_solicitante = self.interessado.nome,
            status           = 'PENDENTE',
        )
        # Tenta criar a segunda
        response = self.client.post(reverse('interessados:solicitar_exclusao'), {
            'confirmacao': 'CONFIRMAR',
            'motivo'     : 'Segunda tentativa',
        })
        # Deve ter redirecionado para o dashboard (bloqueado)
        self.assertEqual(
            SolicitacaoExclusao.objects.filter(interessado=self.interessado).count(),
            1
        )


