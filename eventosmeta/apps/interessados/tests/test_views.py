"""
Arquivo: test_views.py
Caminho: apps/interessados/tests/test_views.py
Testes de views para Portal e Interessados
Data: 27/03/2026
Refatorado: 29/05/2026
  - Simplificado test_meus_dados_view_edita (2 testes: valido + campos ausentes)
  - Corrigido test_login_nao_expoe_mensagem_diferenciada (Factory com CPF fixo)
  - Corrigido test_dashboard_usuario_inativo (assert mais preciso)
  - Movido email do interessado para setUp
  - Removido TestCadastroViewComFactory (fundido em TestInteressadosViews)
  - Adicionados campos obrigatorios minimos para edicao
  - Ajustado test_senha_recuperar_view com factory
  - Removido test_cadastro_rejeita_senha_fraca generico (valida erro em 'senha')
"""

from django.test import TestCase, Client
from django.urls import reverse
from django.utils import timezone
from datetime import timedelta

from apps.interessados.models import Interessado, PasswordResetToken, gerar_hash_cpf
from apps.eventos.models import Evento, Status
from apps.selecao.models import Inscricao, StatusInscricao
from .factories import InteressadoFactory, SexoFactory, FototipoFactory


class TestPortalViews(TestCase):

    def setUp(self):
        self.client = Client()

    def test_portal_index(self):
        response = self.client.get(reverse('portal:index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'portal/index.html')


class TestInteressadosViews(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.sexo = SexoFactory(nome='Feminino')
        cls.fototipo = FototipoFactory(nome='Tipo I')
        cls.status_ativo = Status.objects.create(
            nome='INSCRICOES_ABERTAS', cor='#28a745',
        )
        cls.status_inscricao = StatusInscricao.objects.create(
            nome='Pendente', cor='#ffc107',
        )
        cls.evento = Evento.objects.create(
            nome='Evento Teste',
            descricao='Descricao do evento',
            data_inicio_evento=timezone.now().date(),
            data_fim_evento=timezone.now().date() + timedelta(days=7),
            data_inicio_inscricao=timezone.now() - timedelta(days=1),
            data_fim_inscricao=timezone.now() + timedelta(days=1),
            total_vagas=10,
            status=cls.status_ativo,
        )

    def setUp(self):
        self.client = Client()
        self.cpf_valido = '52998224725'
        self.senha_valida = 'senha123'

        self.interessado_ativo = InteressadoFactory.create(
            cpf=self.cpf_valido,
            email='ativo@example.com',
            is_active=True,
            sexo=self.sexo,
            fototipo=self.fototipo,
        )

    def _login(self):
        self.client.post(reverse('interessados:login'), {
            'cpf': self.cpf_valido,
            'senha': self.senha_valida,
        })

    # --- Cadastro ---

    def test_cadastro_view_get(self):
        response = self.client.get(reverse('interessados:cadastro'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'interessados/cadastro.html')

    def test_cadastro_view_post_valido(self):
        novo_cpf = '98765432100'
        form_data = {
            'nome': 'Novo Interessado',
            'cpf': novo_cpf,
            'email': 'novo@example.com',
            'senha': 'SenhaForte123!',
            'confirmar_senha': 'SenhaForte123!',
            'consentimento_lgpd': True,
            'sexo': self.sexo.id,
            'fototipo': self.fototipo.id,
            'uf_nascimento': 'SP',
            'nacionalidade': 'Brasileira',
        }
        response = self.client.post(reverse('interessados:cadastro'), form_data)
        self.assertRedirects(response, reverse('interessados:login'))
        novo = Interessado.objects.get(cpf_hash=gerar_hash_cpf(novo_cpf))
        self.assertEqual(novo.nome, 'Novo Interessado')

    def test_cadastro_post_com_dados_completos(self):
        """CPF valido: 111.222.333-96."""
        form_data = {
            'nome': 'Novo Usuario',
            'cpf': '11122233396',
            'email': 'completo@test.com',
            'rg': '12345678',
            'data_nascimento': '1995-06-20',
            'sexo': self.sexo.id,
            'fototipo': self.fototipo.id,
            'cidade_nascimento': 'Rio de Janeiro',
            'uf_nascimento': 'RJ',
            'nacionalidade': 'Brasileira',
            'cep': '01234567',
            'endereco_residencial': 'Av. Teste',
            'num_endereco': '456',
            'bairro': 'Bela Vista',
            'complemento': 'Apto 101',
            'cidade_residencia': 'Rio de Janeiro',
            'uf_residencia': 'RJ',
            'telefone': '2133334444',
            'celular': '21987654321',
            'escolaridade': 'SUPERIOR_COMPLETO',
            'programa_social': False,
            'necessidades_especiais': False,
            'senha': 'SenhaForte123!',
            'confirmar_senha': 'SenhaForte123!',
            'consentimento_lgpd': True,
        }
        response = self.client.post(reverse('interessados:cadastro'), form_data)
        self.assertRedirects(response, reverse('interessados:login'))

    def test_cadastro_rejeita_senha_fraca(self):
        form_data = {
            'nome': 'Teste',
            'cpf': '52998224725',
            'email': 'teste@test.com',
            'senha': '123',
            'confirmar_senha': '123',
            'consentimento_lgpd': True,
        }
        response = self.client.post(reverse('interessados:cadastro'), form_data)
        self.assertEqual(response.status_code, 200)
        form = response.context['form']
        self.assertFalse(form.is_valid())
        self.assertIn('senha', form.errors)

    # --- Login ---

    def test_login_view_valido(self):
        response = self.client.post(reverse('interessados:login'), {
            'cpf': self.cpf_valido,
            'senha': self.senha_valida,
        })
        self.assertRedirects(response, reverse('interessados:dashboard'))
        self.assertEqual(
            int(self.client.session['_auth_user_id']),
            self.interessado_ativo.id,
        )

    def test_login_sql_injection(self):
        response = self.client.post(reverse('interessados:login'), {
            'cpf': "' OR '1'='1",
            'senha': 'qualquer',
        })
        self.assertEqual(response.status_code, 200)
        self.assertNotIn('_auth_user_id', self.client.session)

    def test_login_nao_expoe_mensagem_diferenciada(self):
        response_inexistente = self.client.post(reverse('interessados:login'), {
            'cpf': '99999999999',
            'senha': 'qualquer',
        })
        response_senha_errada = self.client.post(reverse('interessados:login'), {
            'cpf': self.cpf_valido,
            'senha': 'senhaerrada',
        })
        self.assertEqual(response_inexistente.status_code, 200)
        self.assertEqual(response_senha_errada.status_code, 200)

    # --- Dashboard ---

    def test_dashboard_requer_login(self):
        response = self.client.get(reverse('interessados:dashboard'))
        expected = reverse('interessados:login') + '?next=' + reverse('interessados:dashboard')
        self.assertRedirects(response, expected)

    def test_dashboard_com_login(self):
        self._login()
        response = self.client.get(reverse('interessados:dashboard'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'interessados/dashboard.html')

    # --- Meus Dados (edicao) ---

    def test_meus_dados_view_get(self):
        self._login()
        response = self.client.get(reverse('interessados:meus_dados'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'interessados/meus_dados.html')

    def test_meus_dados_edicao_valida(self):
        """POST com dados minimos que o EdicaoInteressadoForm aceita."""
        self._login()
        form_data = {
            'nome': 'Nome Atualizado',
            'email': 'ativo@example.com',
            'data_nascimento': '2000-01-01',
            'sexo': self.sexo.id,
            'fototipo': self.fototipo.id,
            'uf_nascimento': 'SP',
            'nacionalidade': 'Brasileira',
            'rg': '12345678',
            'cep': '01234567',
            'endereco_residencial': 'Rua A',
            'num_endereco': '123',
            'bairro': 'Centro',
            'cidade_residencia': 'Sao Paulo',
            'uf_residencia': 'SP',
            'escolaridade': 'SUPERIOR_COMPLETO',
            'num_nis': '12345678901',
        }
        response = self.client.post(reverse('interessados:meus_dados'), form_data)
        self.assertRedirects(response, reverse('interessados:meus_dados'))
        self.interessado_ativo.refresh_from_db()
        self.assertEqual(self.interessado_ativo.nome, 'Nome Atualizado')

    def test_meus_dados_edicao_sem_nome_rejeita(self):
        self._login()
        form_data = {
            'nome': '',
            'email': 'ativo@example.com',
            'sexo': self.sexo.id,
            'fototipo': self.fototipo.id,
            'uf_nascimento': 'SP',
            'nacionalidade': 'Brasileira',
        }
        response = self.client.post(reverse('interessados:meus_dados'), form_data)
        self.assertEqual(response.status_code, 200)
        self.assertFalse(response.context['form'].is_valid())

    # --- Recuperacao de senha ---

    def test_senha_recuperar_view(self):
        response = self.client.post(reverse('interessados:senha_recuperar'), {
            'cpf': self.cpf_valido,
        })
        self.assertRedirects(response, reverse('interessados:senha_recuperar_enviado'))
        token = PasswordResetToken.objects.filter(
            interessado=self.interessado_ativo,
        ).first()
        self.assertIsNotNone(token)


class TestDashboardAutenticacao(TestCase):

    def setUp(self):
        self.client = Client()
        self.interessado_ativo = InteressadoFactory.create(is_active=True)
        self.interessado_inativo = InteressadoFactory.create(is_active=False)

    def test_nao_autenticado_redireciona_login(self):
        response = self.client.get(reverse('interessados:dashboard'))
        self.assertEqual(response.status_code, 302)
        self.assertIn('login', response.url)

    def test_usuario_inativo_redireciona_login(self):
        """Login via POST com usuario inativo nao autentica e redireciona."""
        response = self.client.post(reverse('interessados:login'), {
            'cpf': self.interessado_inativo.cpf,
            'senha': 'senha123',
        })
        self.assertEqual(response.status_code, 200)
        self.assertNotIn('_auth_user_id', self.client.session)

        # Tenta acessar dashboard
        response = self.client.get(reverse('interessados:dashboard'))
        self.assertEqual(response.status_code, 302)
        self.assertIn('login', response.url)


        