"""
Arquivo: test_admin.py
Caminho: apps/academico/tests/test_admin.py
Atualizações
28/05/2026 - Criação do arquivo 
"""

from datetime import date, timedelta
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.messages import get_messages

from apps.accounts.admin import admin_site
from apps.academico.admin import (
    StatusMatriculaAdmin,
    MatriculaAdmin,
    AvaliacaoAdmin,
)
from apps.academico.models import StatusMatricula, Matricula, Avaliacao
from apps.eventos.models import Evento, Turma, Status
from apps.selecao.models import Inscricao, Classificacao, StatusInscricao
from apps.accounts.models import Usuario
from apps.interessados.tests.factories import InteressadoFactory


class TestStatusMatriculaAdmin(TestCase):
    def setUp(self):
        self.model_admin = StatusMatriculaAdmin(StatusMatricula, admin_site)

    def test_cor_display_com_cor(self):
        obj = StatusMatricula(cor="#ff0000")
        result = self.model_admin.cor_display(obj)
        self.assertIn("#ff0000", result)
        self.assertIn("background-color", result)

    def test_cor_display_sem_cor(self):
        obj = StatusMatricula(cor="")
        result = self.model_admin.cor_display(obj)
        self.assertEqual(result, "\u2014")


class TestMatriculaAdmin(TestCase):
    def setUp(self):
        self.interessado = InteressadoFactory()

        status_evento = Status.objects.create(nome="Ativo")
        status_inscricao = StatusInscricao.objects.create(nome="Confirmada")

        self.evento = Evento.objects.create(
            nome="Evento Teste",
            status=status_evento,
            total_vagas=50,
            data_inicio_inscricao=date.today(),
            data_fim_inscricao=date.today() + timedelta(days=30),
            data_inicio_evento=date.today() + timedelta(days=60),
            data_fim_evento=date.today() + timedelta(days=61),
        )
        self.turma = Turma.objects.create(
            nome="Turma Teste",
            evento=self.evento,
            capacidade=40,
            data_inicio=date.today() + timedelta(days=60),
            data_fim=date.today() + timedelta(days=61),
        )
        self.inscricao = Inscricao.objects.create(
            interessado=self.interessado,
            evento=self.evento,
            status=status_inscricao,
        )
        self.matricula = Matricula.objects.create(
            numero_matricula="123",
            interessado=self.interessado,
            turma=self.turma,
            status=StatusMatricula.objects.create(
                nome="Ativa", cor="#00ff00", ordem=1
            ),
            inscricao=self.inscricao,
        )
        self.model_admin = MatriculaAdmin(Matricula, admin_site)

    def test_get_interessado(self):
        result = self.model_admin.get_interessado(self.matricula)
        self.assertEqual(result, self.interessado.nome)

    def test_get_evento(self):
        result = self.model_admin.get_evento(self.matricula)
        self.assertEqual(result, "Evento Teste")


class TestAvaliacaoAdmin(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.superuser = Usuario.objects.create_user(
            username="admin2",
            email="admin2@ex.com",
            password="123",
            cpf="22222222222",
            is_staff=True,
            is_superuser=True,
        )

    def setUp(self):
        self.client = Client()
        self.client.force_login(self.superuser)

        hoj = date.today()
        status_evento = Status.objects.create(nome="Ativo")
        status_inscricao = StatusInscricao.objects.create(nome="Confirmada")

        self.evento = Evento.objects.create(
            nome="Evento Teste",
            status=status_evento,
            total_vagas=50,
            data_inicio_inscricao=hoj,
            data_fim_inscricao=hoj + timedelta(days=30),
            data_inicio_evento=hoj + timedelta(days=60),
            data_fim_evento=hoj + timedelta(days=61),
        )
        self.turma = Turma.objects.create(
            nome="Turma Teste",
            evento=self.evento,
            capacidade=40,
            data_inicio=hoj + timedelta(days=60),
            data_fim=hoj + timedelta(days=61),
        )
        self.status = StatusMatricula.objects.create(
            nome="Ativa", cor="#00ff00", ordem=1
        )
        self.interessado = InteressadoFactory()
        self.inscricao = Inscricao.objects.create(
            interessado=self.interessado,
            evento=self.evento,
            status=status_inscricao,
        )
        self.matricula = Matricula.objects.create(
            numero_matricula="456",
            interessado=self.interessado,
            turma=self.turma,
            status=self.status,
            inscricao=self.inscricao,
        )

        # CORRECAO: update_or_create garante aprovado=True mesmo se Matricula.save() criou com False
        self.avaliacao, _ = Avaliacao.objects.update_or_create(
            matricula=self.matricula,
            defaults={
                "nota_final": 8.5,
                "frequencia": 90,
                "aprovado": True,
            },
        )

        Classificacao.objects.create(
            inscricao=self.inscricao,
            classificado=True,
            pontuacao_total=100,
            posicao=1,
        )
        self.model_admin = AvaliacaoAdmin(Avaliacao, admin_site)

    def _criar_matricula_extra(self):
        """Helper para criar matricula extra para testes que precisam de outro Avaliacao"""
        hoj = date.today()
        interessado2 = InteressadoFactory()
        inscricao2 = Inscricao.objects.create(
            interessado=interessado2,
            evento=self.evento,
            status=StatusInscricao.objects.create(nome="Pendente"),
        )
        matricula2 = Matricula.objects.create(
            numero_matricula="789",
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
        result = self.model_admin.acoes_certificado(self.avaliacao)
        self.assertIn("button", result)
        self.assertIn(str(self.avaliacao.pk), result)

    def test_acoes_certificado_nao_aprovado(self):
        matricula2 = self._criar_matricula_extra()
        avaliacao2, _ = Avaliacao.objects.update_or_create(
            matricula=matricula2,
            defaults={
                "nota_final": 5.0,
                "frequencia": 70,
                "aprovado": False,
            },
        )
        result = self.model_admin.acoes_certificado(avaliacao2)
        self.assertEqual(result, '<span style="color: #999;">-</span>')

    def test_changelist_view_contexto(self):
        response = self.client.get(
            reverse("admin:academico_avaliacao_changelist")
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn("eventos_disponiveis", response.context)

    def test_gerar_certificados_marca_emitidos(self):
        self.assertFalse(self.avaliacao.certificado_emitido)
        self.client.post(
            reverse("admin:academico_avaliacao_changelist"),
            {
                "action": "gerar_certificados",
                "_selected_action": [self.avaliacao.pk],
                "index": "0",
            },
        )
        self.avaliacao.refresh_from_db()
        self.assertTrue(self.avaliacao.certificado_emitido)
        self.assertEqual(
            self.avaliacao.data_emissao_certificado, date.today()
        )

    def test_gerar_certificados_sem_aprovados(self):
        matricula2 = self._criar_matricula_extra()
        avaliacao2, _ = Avaliacao.objects.update_or_create(
            matricula=matricula2,
            defaults={
                "nota_final": 5.0,
                "frequencia": 70,
                "aprovado": False,
            },
        )
        response = self.client.post(
            reverse("admin:academico_avaliacao_changelist"),
            {
                "action": "gerar_certificados",
                "_selected_action": [avaliacao2.pk],
                "index": "0",
            },
            follow=True,
        )
        msg_list = list(get_messages(response.wsgi_request))
        self.assertTrue(
            any("Nenhum aluno aprovado" in str(m) for m in msg_list)
        )

    def test_gerar_certificados_ja_emitido(self):
        self.avaliacao.certificado_emitido = True
        self.avaliacao.save()
        response = self.client.post(
            reverse("admin:academico_avaliacao_changelist"),
            {
                "action": "gerar_certificados",
                "_selected_action": [self.avaliacao.pk],
                "index": "0",
            },
            follow=True,
        )
        msg_list = list(get_messages(response.wsgi_request))
        self.assertTrue(
            any("já possui certificado" in str(m) for m in msg_list)
        )

    def test_download_certificados_lote_action_redirect(self):
        response = self.client.post(
            reverse("admin:academico_avaliacao_changelist"),
            {
                "action": "download_certificados_lote_action",
                "_selected_action": [self.avaliacao.pk],
                "index": "0",
            },
        )
        self.assertEqual(response.status_code, 302)
        self.assertIn("certificados/download-lote", response.url)



