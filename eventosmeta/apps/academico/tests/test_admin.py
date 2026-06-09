"""
Arquivo: test_admin.py
Caminho: apps/academico/tests/test_admin.py
Descrição: Testes de admin para StatusMatricula, Matricula e Avaliacao
Histórico de Alterações:
 - 28/05/2026 - Criação do arquivo
 - 09/06/2026 - Correção de testes para refletir mudanças no modelo e admin
"""


import pytest
from django.test import Client
from django.urls import reverse
from django.contrib.messages import get_messages
from django.utils import timezone
from datetime import timedelta

from apps.accounts.admin import admin_site
from apps.academico.admin import StatusMatriculaAdmin, MatriculaAdmin, AvaliacaoAdmin
from apps.academico.models import StatusMatricula, Matricula, Avaliacao
from apps.eventos.models import Evento, Turma, Status
from apps.selecao.models import Inscricao, Classificacao, StatusInscricao
from apps.accounts.models import Usuario
from apps.interessados.tests.factories import InteressadoFactory

@pytest.mark.django_db
class TestStatusMatriculaAdmin:
    """Testes para StatusMatriculaAdmin"""

    def setup_method(self):
        self.admin = StatusMatriculaAdmin(StatusMatricula, admin_site)

    def test_cor_display_com_cor(self):
        """Deve exibir quadrado colorido quando cor está preenchida"""
        obj = StatusMatricula(cor='#ff0000')
        result = self.admin.cor_display(obj)
        assert '#ff0000' in result
        assert 'background-color' in result

    def test_cor_display_sem_cor(self):
        """Deve exibir travessão quando cor está vazia"""
        obj = StatusMatricula(cor='')
        result = self.admin.cor_display(obj)
        assert result == '—'

@pytest.mark.django_db
class TestMatriculaAdmin:
    """Testes para MatriculaAdmin"""

    def setup_method(self):
        self.admin = MatriculaAdmin(Matricula, admin_site)
        self.interessado = InteressadoFactory()
        
        status_evento = Status.objects.create(nome='Ativo')
        status_inscricao = StatusInscricao.objects.create(nome='Confirmada')
        
        agora = timezone.now()
        self.evento = Evento.objects.create(
            nome='Evento Teste',
            status=status_evento,
            total_vagas=50,
            data_inicio_inscricao=agora,
            data_fim_inscricao=agora + timedelta(days=30),
            data_inicio_evento=agora.date() + timedelta(days=60),
            data_fim_evento=agora.date() + timedelta(days=61),
        )
        
        self.turma = Turma.objects.create(
            nome='Turma Teste',
            evento=self.evento,
            capacidade=40,
            data_inicio=agora.date() + timedelta(days=60),
            data_fim=agora.date() + timedelta(days=61),
        )
        
        self.inscricao = Inscricao.objects.create(
            interessado=self.interessado,
            evento=self.evento,
            status=status_inscricao,
        )
        
        self.matricula = Matricula.objects.create(
            numero_matricula='123',
            interessado=self.interessado,
            turma=self.turma,
            status=StatusMatricula.objects.create(
                nome='Ativa', cor='#00ff00', ordem=1
            ),
            inscricao=self.inscricao,
        )

    def test_get_interessado(self):
        """Deve retornar nome do interessado"""
        result = self.admin.get_interessado(self.matricula)
        assert result == self.interessado.nome

    def test_get_evento(self):
        """Deve retornar nome do evento"""
        result = self.admin.get_evento(self.matricula)
        assert result == 'Evento Teste'

@pytest.mark.django_db
class TestAvaliacaoAdmin:
    """Testes para AvaliacaoAdmin"""

    def setup_method(self):
        self.superuser = Usuario.objects.create_user(
            username='admin2',
            email='admin2@ex.com',
            password='123',
            cpf='22222222222',
            is_staff=True,
            is_superuser=True,
        )
        self.client = Client()
        self.client.force_login(self.superuser)
        
        agora = timezone.now()
        status_evento = Status.objects.create(nome='Ativo')
        status_inscricao = StatusInscricao.objects.create(nome='Confirmada')
        
        self.evento = Evento.objects.create(
            nome='Evento Teste',
            status=status_evento,
            total_vagas=50,
            data_inicio_inscricao=agora,
            data_fim_inscricao=agora + timedelta(days=30),
            data_inicio_evento=agora.date() + timedelta(days=60),
            data_fim_evento=agora.date() + timedelta(days=61),
        )
        
        self.turma = Turma.objects.create(
            nome='Turma Teste',
            evento=self.evento,
            capacidade=40,
            data_inicio=agora.date() + timedelta(days=60),
            data_fim=agora.date() + timedelta(days=61),
        )
        
        self.status = StatusMatricula.objects.create(
            nome='Ativa', cor='#00ff00', ordem=1
        )
        
        self.interessado = InteressadoFactory()
        self.inscricao = Inscricao.objects.create(
            interessado=self.interessado,
            evento=self.evento,
            status=status_inscricao,
        )
        
        self.matricula = Matricula.objects.create(
            numero_matricula='456',
            interessado=self.interessado,
            turma=self.turma,
            status=self.status,
            inscricao=self.inscricao,
        )
        
        self.avaliacao, _ = Avaliacao.objects.update_or_create(
            matricula=self.matricula,
            defaults={
                'nota_final': 8.5,
                'frequencia': 90,
                'aprovado': True,
            },
        )
        
        Classificacao.objects.create(
            inscricao=self.inscricao,
            classificado=True,
            pontuacao_total=100,
            posicao=1,
        )
        self.admin = AvaliacaoAdmin(Avaliacao, admin_site)

    def _criar_matricula_extra(self):
        """Helper para criar matrícula extra"""
        interessado2 = InteressadoFactory()
        inscricao2 = Inscricao.objects.create(
            interessado=interessado2,
            evento=self.evento,
            status=StatusInscricao.objects.create(nome='Pendente'),
        )
        matricula2 = Matricula.objects.create(
            numero_matricula='789',
            interessado=interessado2,
            turma=self.turma,
            status=self.status,
            inscricao=inscricao2,
        )
        Classificacao.objects.create(
            inscricao=inscricao2,
            classificado=True,
            pontuacao_total=80,
            posicao=2,
        )
        return matricula2

    def test_acoes_certificado_aprovado(self):
        """Deve exibir botão para certificado aprovado"""
        result = self.admin.acoes_certificado(self.avaliacao)
        assert 'button' in result
        assert str(self.avaliacao.pk) in result

    def test_acoes_certificado_nao_aprovado(self):
        """Deve exibir travessão para não aprovado"""
        matricula2 = self._criar_matricula_extra()
        avaliacao2, _ = Avaliacao.objects.update_or_create(
            matricula=matricula2,
            defaults={
                'nota_final': 5.0,
                'frequencia': 70,
                'aprovado': False,
            },
        )
        result = self.admin.acoes_certificado(avaliacao2)
        assert result == '<span style="color: #999;">-</span>'

    def test_changelist_view_contexto(self):
        """Deve incluir eventos_disponiveis no contexto"""
        response = self.client.get(reverse('admin:academico_avaliacao_changelist'))
        assert response.status_code == 200
        assert 'eventos_disponiveis' in response.context

    def test_gerar_certificados_marca_emitidos(self):
        """Deve marcar certificado como emitido"""
        assert not self.avaliacao.certificado_emitido
        self.client.post(
            reverse('admin:academico_avaliacao_changelist'),
            {
                'action': 'gerar_certificados',
                '_selected_action': [self.avaliacao.pk],
                'index': '0',
            },
        )
        self.avaliacao.refresh_from_db()
        assert self.avaliacao.certificado_emitido
        assert self.avaliacao.data_emissao_certificado == timezone.now().date()

    def test_gerar_certificados_sem_aprovados(self):
        """Deve exibir mensagem quando nenhum aprovado"""
        matricula2 = self._criar_matricula_extra()
        avaliacao2, _ = Avaliacao.objects.update_or_create(
            matricula=matricula2,
            defaults={
                'nota_final': 5.0,
                'frequencia': 70,
                'aprovado': False,
            },
        )
        response = self.client.post(
            reverse('admin:academico_avaliacao_changelist'),
            {
                'action': 'gerar_certificados',
                '_selected_action': [avaliacao2.pk],
                'index': '0',
            },
            follow=True,
        )
        msg_list = list(get_messages(response.wsgi_request))
        assert any('Nenhum aluno aprovado' in str(m) for m in msg_list)

    def test_gerar_certificados_ja_emitido(self):
        """Deve exibir aviso se certificado já emitido"""
        self.avaliacao.certificado_emitido = True
        self.avaliacao.save()
        response = self.client.post(
            reverse('admin:academico_avaliacao_changelist'),
            {
                'action': 'gerar_certificados',
                '_selected_action': [self.avaliacao.pk],
                'index': '0',
            },
            follow=True,
        )
        msg_list = list(get_messages(response.wsgi_request))
        assert any('já possui certificado' in str(m) for m in msg_list)

    def test_download_certificados_lote_action_redirect(self):
        """Deve redirecionar para download em lote"""
        response = self.client.post(
            reverse('admin:academico_avaliacao_changelist'),
            {
                'action': 'download_certificados_lote_action',
                '_selected_action': [self.avaliacao.pk],
                'index': '0',
            },
        )
        assert response.status_code == 302
        assert 'certificados/download-lote' in response.url


