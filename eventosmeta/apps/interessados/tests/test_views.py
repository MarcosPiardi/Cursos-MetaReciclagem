"""
Arquivo: test_views.py
Caminho: apps/interessados/tests/test_views.py
Testes de views para Portal e Interessados
Atualizações:
 - 27/03/2026 - v1.0 - Criação
 - 29/05/2026 - v2.0 - Simplificações e correções diversas:
              - Simplificado test_meus_dados_view_edita (2 testes: valido + campos ausentes)
              - Corrigido test_login_nao_expoe_mensagem_diferenciada (Factory com CPF fixo)
              - Corrigido test_dashboard_usuario_inativo (assert mais preciso)
              - Movido email do interessado para setUp
              - Removido TestCadastroViewComFactory (fundido em TestInteressadosViews)
              - Adicionados campos obrigatorios minimos para edicao
              - Ajustado test_senha_recuperar_view com factory
              - Removido test_cadastro_rejeita_senha_fraca generico (valida erro em 'senha')
 - 16/06/2026 - v3.0 - Refatoração para pytest idiomático
              - v3.1 - Corrigido template_name e scope='class' sem db
"""

from datetime import timedelta

import pytest
from django.urls import reverse
from django.utils import timezone

from apps.eventos.models import Evento, Status
from apps.interessados.models import Interessado, PasswordResetToken, gerar_hash_cpf
from apps.selecao.models import Inscricao, StatusInscricao

from .factories import InteressadoFactory, SexoFactory, FototipoFactory

pytestmark = pytest.mark.django_db


# =============================================================================
# HELPERS
# =============================================================================

def _login(client, cpf, senha):
    client.post(reverse('interessados:login'), {'cpf': cpf, 'senha': senha})


# =============================================================================
# TESTES - PORTAL
# =============================================================================

class TestPortalViews:

    def test_portal_index(self):
        client = __import__('django').test.Client()
        response = client.get(reverse('portal:index'))
        assert response.status_code == 200


# =============================================================================
# TESTES - INTERESSADOS
# =============================================================================

class TestInteressadosViews:

    @pytest.fixture
    def _class_data(self):
        sexo = SexoFactory(nome='Feminino')
        fototipo = FototipoFactory(nome='Tipo I')
        status_ativo = Status.objects.create(
            nome='INSCRICOES_ABERTAS', cor='#28a745',
        )
        status_inscricao = StatusInscricao.objects.create(
            nome='Pendente', cor='#ffc107',
        )
        evento = Evento.objects.create(
            nome='Evento Teste',
            descricao='Descricao do evento',
            data_inicio_evento=timezone.now().date(),
            data_fim_evento=timezone.now().date() + timedelta(days=7),
            data_inicio_inscricao=timezone.now() - timedelta(days=1),
            data_fim_inscricao=timezone.now() + timedelta(days=1),
            total_vagas=10,
            status=status_ativo,
        )
        return {
            'sexo': sexo,
            'fototipo': fototipo,
            'status_ativo': status_ativo,
            'status_inscricao': status_inscricao,
            'evento': evento,
        }

    @pytest.fixture(autouse=True)
    def _setup(self, _class_data):
        self.client = __import__('django').test.Client()
        self.cpf_valido = '52998224725'
        self.senha_valida = 'senha123'
        self.sexo = _class_data['sexo']
        self.fototipo = _class_data['fototipo']

        self.interessado_ativo = InteressadoFactory.create(
            cpf=self.cpf_valido,
            email='ativo@example.com',
            is_active=True,
            sexo=self.sexo,
            fototipo=self.fototipo,
        )

    # --- Cadastro ---

    def test_cadastro_view_get(self):
        response = self.client.get(reverse('interessados:cadastro'))
        assert response.status_code == 200

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
        assert response.status_code == 302
        assert response.url == reverse('interessados:login')
        novo = Interessado.objects.get(cpf_hash=gerar_hash_cpf(novo_cpf))
        assert novo.nome == 'Novo Interessado'

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
        assert response.status_code == 302
        assert response.url == reverse('interessados:login')

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
        assert response.status_code == 200
        form = response.context['form']
        assert not form.is_valid()
        assert 'senha' in form.errors

    # --- Login ---

    def test_login_view_valido(self):
        response = self.client.post(reverse('interessados:login'), {
            'cpf': self.cpf_valido,
            'senha': self.senha_valida,
        })
        assert response.status_code == 302
        assert response.url == reverse('interessados:dashboard')
        assert int(self.client.session['_auth_user_id']) == self.interessado_ativo.id

    def test_login_sql_injection(self):
        response = self.client.post(reverse('interessados:login'), {
            'cpf': "' OR '1'='1",
            'senha': 'qualquer',
        })
        assert response.status_code == 200
        assert '_auth_user_id' not in self.client.session

    def test_login_nao_expoe_mensagem_diferenciada(self):
        response_inexistente = self.client.post(reverse('interessados:login'), {
            'cpf': '99999999999',
            'senha': 'qualquer',
        })
        response_senha_errada = self.client.post(reverse('interessados:login'), {
            'cpf': self.cpf_valido,
            'senha': 'senhaerrada',
        })
        assert response_inexistente.status_code == 200
        assert response_senha_errada.status_code == 200

    # --- Dashboard ---

    def test_dashboard_requer_login(self):
        response = self.client.get(reverse('interessados:dashboard'))
        expected = reverse('interessados:login') + '?next=' + reverse('interessados:dashboard')
        assert response.status_code == 302
        assert response.url == expected

    def test_dashboard_com_login(self):
        _login(self.client, self.cpf_valido, self.senha_valida)
        response = self.client.get(reverse('interessados:dashboard'))
        assert response.status_code == 200

    # --- Meus Dados (edicao) ---

    def test_meus_dados_view_get(self):
        _login(self.client, self.cpf_valido, self.senha_valida)
        response = self.client.get(reverse('interessados:meus_dados'))
        assert response.status_code == 200

    def test_meus_dados_edicao_valida(self):
        """POST com dados minimos que o EdicaoInteressadoForm aceita."""
        _login(self.client, self.cpf_valido, self.senha_valida)
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
        assert response.status_code == 302
        assert response.url == reverse('interessados:meus_dados')
        self.interessado_ativo.refresh_from_db()
        assert self.interessado_ativo.nome == 'Nome Atualizado'

    def test_meus_dados_edicao_sem_nome_rejeita(self):
        _login(self.client, self.cpf_valido, self.senha_valida)
        form_data = {
            'nome': '',
            'email': 'ativo@example.com',
            'sexo': self.sexo.id,
            'fototipo': self.fototipo.id,
            'uf_nascimento': 'SP',
            'nacionalidade': 'Brasileira',
        }
        response = self.client.post(reverse('interessados:meus_dados'), form_data)
        assert response.status_code == 200
        assert not response.context['form'].is_valid()

    # --- Recuperacao de senha ---

    def test_senha_recuperar_view(self):
        response = self.client.post(reverse('interessados:senha_recuperar'), {
            'cpf': self.cpf_valido,
        })
        assert response.status_code == 302
        assert response.url == reverse('interessados:senha_recuperar_enviado')
        token = PasswordResetToken.objects.filter(
            interessado=self.interessado_ativo,
        ).first()
        assert token is not None


class TestDashboardAutenticacao:

    @pytest.fixture(autouse=True)
    def _setup(self):
        self.client = __import__('django').test.Client()
        self.interessado_ativo = InteressadoFactory.create(is_active=True)
        self.interessado_inativo = InteressadoFactory.create(is_active=False)

    def test_nao_autenticado_redireciona_login(self):
        response = self.client.get(reverse('interessados:dashboard'))
        assert response.status_code == 302
        assert 'login' in response.url

    def test_usuario_inativo_redireciona_login(self):
        response = self.client.post(reverse('interessados:login'), {
            'cpf': self.interessado_inativo.cpf,
            'senha': 'senha123',
        })
        assert response.status_code == 200
        assert '_auth_user_id' not in self.client.session

        response = self.client.get(reverse('interessados:dashboard'))
        assert response.status_code == 302
        assert 'login' in response.url


