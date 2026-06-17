"""
Arquivo: test_views_exclusao.py
Caminho: apps/accounts/tests/test_views_exclusao.py
Finalidade: Testes para as views de exclusao de dados (LGPD)
Atualizacoes:
 - 28/05/2026 - Criacao do arquivo
 - 17/06/2026 - Refatorado de unittest.TestCase para pytest
"""

import pytest
from django.test import Client
from django.contrib.auth import get_user_model
from django.urls import reverse

from apps.interessados.models import SolicitacaoExclusao, Interessado
from apps.accounts.views_exclusao import _anonimizar_interessado
from apps.interessados.tests.factories import InteressadoFactory

pytestmark = pytest.mark.django_db

class TestListarSolicitacoesView:
    """Testes para listar_solicitacoes_view."""

    def setup_method(self):
        self.client = Client()
        User = get_user_model()

        self.staff_user = User.objects.create_user(
            username='staff',
            email='staff@ex.com',
            password='abc123',
            cpf='11111111111',
            is_staff=True,
            is_active=True,
        )

        self.normal_user = User.objects.create_user(
            username='normal',
            email='normal@ex.com',
            password='abc123',
            cpf='22222222222',
            is_staff=False,
            is_active=True,
        )

        interessado1 = InteressadoFactory()
        interessado2 = InteressadoFactory()
        interessado3 = InteressadoFactory()

        SolicitacaoExclusao.objects.create(
            interessado=interessado1,
            nome_solicitante='Joao',
            status='PENDENTE',
        )
        SolicitacaoExclusao.objects.create(
            interessado=interessado2,
            nome_solicitante='Maria',
            status='APROVADA',
        )
        SolicitacaoExclusao.objects.create(
            interessado=interessado3,
            nome_solicitante='Jose',
            status='RECUSADA',
        )

    def test_listar_solicitacoes_status_200(self):
        self.client.force_login(self.staff_user)
        response = self.client.get(reverse('accounts:listar_solicitacoes_exclusao'))
        assert response.status_code == 200

    def test_listar_solicitacoes_sem_login_redirect(self):
        response = self.client.get(reverse('accounts:listar_solicitacoes_exclusao'))
        assert response.status_code == 302

    def test_listar_solicitacoes_nao_staff_redirect(self):
        self.client.force_login(self.normal_user)
        response = self.client.get(reverse('accounts:listar_solicitacoes_exclusao'))
        assert response.status_code == 302

    def test_listar_solicitacoes_contexto_tem_pendentes(self):
        self.client.force_login(self.staff_user)
        response = self.client.get(reverse('accounts:listar_solicitacoes_exclusao'))
        assert 'pendentes' in response.context

    def test_listar_solicitacoes_contexto_tem_aprovadas(self):
        self.client.force_login(self.staff_user)
        response = self.client.get(reverse('accounts:listar_solicitacoes_exclusao'))
        assert 'aprovadas' in response.context

    def test_listar_solicitacoes_contexto_tem_recusadas(self):
        self.client.force_login(self.staff_user)
        response = self.client.get(reverse('accounts:listar_solicitacoes_exclusao'))
        assert 'recusadas' in response.context

class TestDetalheSolicitacaoView:
    """Testes para detalhe_solicitacao_view."""

    def setup_method(self):
        self.client = Client()
        User = get_user_model()

        self.staff_user = User.objects.create_user(
            username='staff',
            email='staff@ex.com',
            password='abc123',
            cpf='11111111111',
            is_staff=True,
            is_active=True,
        )

        self.normal_user = User.objects.create_user(
            username='normal',
            email='normal@ex.com',
            password='abc123',
            cpf='22222222222',
            is_staff=False,
            is_active=True,
        )

        self.interessado = InteressadoFactory()
        self.solicitacao = SolicitacaoExclusao.objects.create(
            interessado=self.interessado,
            nome_solicitante='Teste',
            status='PENDENTE',
        )

    def test_detalhe_solicitacao_status_200(self):
        self.client.force_login(self.staff_user)
        response = self.client.get(
            reverse('accounts:detalhe_solicitacao_exclusao',
                    args=[self.solicitacao.id])
        )
        assert response.status_code == 200

    def test_detalhe_solicitacao_sem_login_redirect(self):
        response = self.client.get(
            reverse('accounts:detalhe_solicitacao_exclusao',
                    args=[self.solicitacao.id])
        )
        assert response.status_code == 302

    def test_detalhe_solicitacao_404(self):
        self.client.force_login(self.staff_user)
        response = self.client.get(
            reverse('accounts:detalhe_solicitacao_exclusao', args=[99999])
        )
        assert response.status_code == 404

    def test_detalhe_solicitacao_aprovar(self):
        self.client.force_login(self.staff_user)
        response = self.client.post(
            reverse('accounts:detalhe_solicitacao_exclusao',
                    args=[self.solicitacao.id]),
            {'acao': 'aprovar', 'parecer': 'Parecer ok'}
        )
        assert response.status_code == 302
        self.solicitacao.refresh_from_db()
        assert self.solicitacao.status == 'APROVADA'
        assert self.solicitacao.parecer_staff == 'Parecer ok'
        assert self.solicitacao.analisado_em is not None
        assert self.solicitacao.analisado_por == self.staff_user

    def test_detalhe_solicitacao_recusar(self):
        self.client.force_login(self.staff_user)
        response = self.client.post(
            reverse('accounts:detalhe_solicitacao_exclusao',
                    args=[self.solicitacao.id]),
            {'acao': 'recusar', 'parecer': 'Motivo X'}
        )
        assert response.status_code == 302
        self.solicitacao.refresh_from_db()
        assert self.solicitacao.status == 'RECUSADA'

    def test_detalhe_solicitacao_acao_invalida(self):
        self.client.force_login(self.staff_user)
        response = self.client.post(
            reverse('accounts:detalhe_solicitacao_exclusao',
                    args=[self.solicitacao.id]),
            {'acao': 'invalida', 'parecer': 'teste'}
        )
        assert response.status_code == 302
        self.solicitacao.refresh_from_db()
        assert self.solicitacao.status == 'PENDENTE'

    def test_detalhe_solicitacao_sem_parecer(self):
        self.client.force_login(self.staff_user)
        response = self.client.post(
            reverse('accounts:detalhe_solicitacao_exclusao',
                    args=[self.solicitacao.id]),
            {'acao': 'aprovar', 'parecer': ''}
        )
        assert response.status_code == 302
        self.solicitacao.refresh_from_db()
        assert self.solicitacao.status == 'PENDENTE'

class TestAnonimizarInteressado:
    """Testes para _anonimizar_interessado."""

    def setup_method(self):
        self.interessado = InteressadoFactory(
            nome='Joao Silva',
            cpf='12345678901',
            rg='MG123456',
            data_nascimento='1990-01-15',
            cidade_nascimento='Belo Horizonte',
            uf_nascimento='MG',
            nacionalidade='Brasileiro',
            endereco_residencial='Rua A',
            num_endereco='100',
            bairro='Centro',
            complemento='Apto 1',
            cep='30000000',
            cidade_residencia='BH',
            uf_residencia='MG',
            telefone='3133333333',
            celular='31999999999',
            email='joao@email.com',
            num_nis='12345678901',
            nome_responsavel='Maria',
            telefone_responsavel='3133333334',
            celular_responsavel='31999999998',
            email_responsavel='maria@email.com',
            observacao='observacao teste',
            is_active=True,
        )

    def test_anonimizar_interessado_limpa_campos(self):
        _anonimizar_interessado(self.interessado)
        self.interessado.refresh_from_db()

        assert self.interessado.nome.startswith('Usuário Removido')
        assert self.interessado.cpf == '00000000000'
        assert self.interessado.rg == ''
        assert self.interessado.data_nascimento is None
        assert self.interessado.cidade_nascimento == ''
        assert self.interessado.uf_nascimento == ''
        assert self.interessado.nacionalidade == ''
        assert self.interessado.endereco_residencial == ''
        assert self.interessado.num_endereco == ''
        assert self.interessado.bairro == ''
        assert self.interessado.complemento == ''
        assert self.interessado.cep == ''
        assert self.interessado.cidade_residencia == ''
        assert self.interessado.uf_residencia == ''
        assert self.interessado.telefone == ''
        assert self.interessado.celular == ''
        assert self.interessado.email is None
        assert self.interessado.num_nis == ''
        assert self.interessado.nome_responsavel == ''
        assert self.interessado.telefone_responsavel == ''
        assert self.interessado.celular_responsavel == ''
        assert self.interessado.email_responsavel == ''
        assert self.interessado.observacao == ''
        assert not self.interessado.is_active

    def test_anonimizar_interessado_mantem_registro(self):
        pk = self.interessado.pk
        _anonimizar_interessado(self.interessado)
        assert Interessado.objects.filter(pk=pk).exists()


