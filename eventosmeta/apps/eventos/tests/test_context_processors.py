"""
Arquivo: test_context_processors.py
caminho: apps/eventos/tests/test_context_processors.py
Finalidade: Testar os context processors do app eventos.
Atualizações:
- 29/05/2026 - Criação do arquivo
"""

from datetime import date, timedelta
from django.test import RequestFactory, TestCase
from django.contrib.auth import get_user_model
from apps.eventos.models import Evento, Status


class TestNotificacoesEventos(TestCase):
    """Testes do context processor notificacoes_eventos"""

    @classmethod
    def setUpTestData(cls):
        User = get_user_model()
        cls.staff = User.objects.create_user(
            username="staff",
            email="staff@test.com",
            password="test123",
            cpf="11111111111",
            is_staff=True,
        )
        cls.user = User.objects.create_user(
            username="user",
            email="user@test.com",
            password="test123",
            cpf="22222222222",
            is_staff=False,
        )

        cls.status_inscricoes_abertas = Status.objects.create(
            nome="Inscri\u00e7\u00f5es Abertas"
        )
        cls.status_em_andamento = Status.objects.create(
            nome="Em Andamento"
        )
        cls.status_finalizado = Status.objects.create(
            nome="Finalizado"
        )
        cls.status_cancelado = Status.objects.create(
            nome="Cancelado"
        )
        cls.status_inscricoes_encerradas = Status.objects.create(
            nome="Inscri\u00e7\u00f5es Encerradas"
        )
        cls.status_rascunho = Status.objects.create(
            nome="Rascunho"
        )

    def setUp(self):
        self.factory = RequestFactory()
        from apps.eventos.context_processors import notificacoes_eventos
        self.processor = notificacoes_eventos

    def _get_result(self, user):
        request = self.factory.get("/")
        request.user = user
        return self.processor(request)

    # --- Autenticacao ---

    def test_usuario_anonimo_retorna_lista_vazia(self):
        result = self._get_result(
            type("AnonUser", (), {"is_authenticated": False, "is_staff": False})
        )
        self.assertEqual(result, {"eventos_notificacao": []})

    def test_usuario_nao_staff_retorna_lista_vazia(self):
        result = self._get_result(self.user)
        self.assertEqual(result, {"eventos_notificacao": []})

    def test_sem_eventos_retorna_lista_vazia(self):
        result = self._get_result(self.staff)
        self.assertEqual(result, {"eventos_notificacao": []})

    # --- Verificacao 1 ---

    def test_verificacao1_status_correto_sem_alerta(self):
        hoje = date.today()
        Evento.objects.create(
            nome="Evento Teste",
            total_vagas=30,
            data_inicio_inscricao=hoje - timedelta(days=1),
            data_fim_inscricao=hoje + timedelta(days=1),
            data_inicio_evento=hoje + timedelta(days=10),
            data_fim_evento=hoje + timedelta(days=15),
            status=self.status_inscricoes_abertas,
        )
        result = self._get_result(self.staff)
        self.assertEqual(len(result["eventos_notificacao"]), 0)

    def test_verificacao1_status_errado_gera_alerta(self):
        hoje = date.today()
        evento = Evento.objects.create(
            nome="Evento Teste",
            total_vagas=30,
            data_inicio_inscricao=hoje - timedelta(days=1),
            data_fim_inscricao=hoje + timedelta(days=1),
            data_inicio_evento=hoje + timedelta(days=10),
            data_fim_evento=hoje + timedelta(days=15),
            status=self.status_rascunho,
        )
        result = self._get_result(self.staff)
        self.assertEqual(len(result["eventos_notificacao"]), 1)
        self.assertEqual(result["eventos_notificacao"][0].pk, evento.pk)
        self.assertEqual(result["eventos_notificacao"][0].tipo_alerta, "inscricao")

    # --- Verificacao 2 ---

    def test_verificacao2_status_valido_sem_alerta(self):
        hoje = date.today()
        Evento.objects.create(
            nome="Evento Teste",
            total_vagas=30,
            data_inicio_inscricao=hoje - timedelta(days=10),
            data_fim_inscricao=hoje - timedelta(days=1),
            data_inicio_evento=hoje + timedelta(days=5),
            data_fim_evento=hoje + timedelta(days=10),
            status=self.status_inscricoes_encerradas,
        )
        result = self._get_result(self.staff)
        self.assertEqual(len(result["eventos_notificacao"]), 0)

    def test_verificacao2_status_invalido_gera_alerta(self):
        hoje = date.today()
        evento = Evento.objects.create(
            nome="Evento Teste",
            total_vagas=30,
            data_inicio_inscricao=hoje - timedelta(days=10),
            data_fim_inscricao=hoje - timedelta(days=1),
            data_inicio_evento=hoje + timedelta(days=5),
            data_fim_evento=hoje + timedelta(days=10),
            status=self.status_rascunho,
        )
        result = self._get_result(self.staff)
        self.assertEqual(len(result["eventos_notificacao"]), 1)
        self.assertEqual(result["eventos_notificacao"][0].pk, evento.pk)
        self.assertEqual(result["eventos_notificacao"][0].tipo_alerta, "pos_inscricao")

    # --- Verificacao 3 ---

    def test_verificacao3_status_correto_sem_alerta(self):
        hoje = date.today()
        Evento.objects.create(
            nome="Evento Teste",
            total_vagas=30,
            data_inicio_inscricao=hoje - timedelta(days=20),
            data_fim_inscricao=hoje - timedelta(days=10),
            data_inicio_evento=hoje - timedelta(days=1),
            data_fim_evento=hoje + timedelta(days=5),
            status=self.status_em_andamento,
        )
        result = self._get_result(self.staff)
        self.assertEqual(len(result["eventos_notificacao"]), 0)

    def test_verificacao3_status_errado_gera_alerta(self):
        hoje = date.today()
        evento = Evento.objects.create(
            nome="Evento Teste",
            total_vagas=30,
            data_inicio_inscricao=hoje - timedelta(days=20),
            data_fim_inscricao=hoje - timedelta(days=10),
            data_inicio_evento=hoje - timedelta(days=1),
            data_fim_evento=hoje + timedelta(days=5),
            status=self.status_rascunho,
        )
        result = self._get_result(self.staff)
        self.assertEqual(len(result["eventos_notificacao"]), 1)
        self.assertEqual(result["eventos_notificacao"][0].pk, evento.pk)
        self.assertEqual(result["eventos_notificacao"][0].tipo_alerta, "evento")

    # --- Verificacao 4 ---

    def test_verificacao4_status_valido_sem_alerta(self):
        hoje = date.today()
        Evento.objects.create(
            nome="Evento Teste",
            total_vagas=30,
            data_inicio_inscricao=hoje - timedelta(days=30),
            data_fim_inscricao=hoje - timedelta(days=20),
            data_inicio_evento=hoje - timedelta(days=15),
            data_fim_evento=hoje - timedelta(days=1),
            status=self.status_finalizado,
        )
        result = self._get_result(self.staff)
        self.assertEqual(len(result["eventos_notificacao"]), 0)

    def test_verificacao4_status_invalido_gera_alerta(self):
        hoje = date.today()
        evento = Evento.objects.create(
            nome="Evento Teste",
            total_vagas=30,
            data_inicio_inscricao=hoje - timedelta(days=30),
            data_fim_inscricao=hoje - timedelta(days=20),
            data_inicio_evento=hoje - timedelta(days=15),
            data_fim_evento=hoje - timedelta(days=1),
            status=self.status_rascunho,
        )
        result = self._get_result(self.staff)
        self.assertEqual(len(result["eventos_notificacao"]), 1)
        self.assertEqual(result["eventos_notificacao"][0].pk, evento.pk)
        self.assertEqual(result["eventos_notificacao"][0].tipo_alerta, "pos_evento")

    def test_verificacao4_cancelado_sem_alerta(self):
        hoje = date.today()
        Evento.objects.create(
            nome="Evento Cancelado",
            total_vagas=30,
            data_inicio_inscricao=hoje - timedelta(days=30),
            data_fim_inscricao=hoje - timedelta(days=20),
            data_inicio_evento=hoje - timedelta(days=15),
            data_fim_evento=hoje - timedelta(days=1),
            status=self.status_cancelado,
        )
        result = self._get_result(self.staff)
        self.assertEqual(len(result["eventos_notificacao"]), 0)

    # --- Multiplos eventos ---

    def test_multiplos_eventos_com_alerta(self):
        hoje = date.today()
        Evento.objects.create(
            nome="Alerta Inscricao",
            total_vagas=30,
            data_inicio_inscricao=hoje - timedelta(days=1),
            data_fim_inscricao=hoje + timedelta(days=1),
            data_inicio_evento=hoje + timedelta(days=10),
            data_fim_evento=hoje + timedelta(days=15),
            status=self.status_rascunho,
        )
        Evento.objects.create(
            nome="Alerta Pos-Evento",
            total_vagas=30,
            data_inicio_inscricao=hoje - timedelta(days=30),
            data_fim_inscricao=hoje - timedelta(days=20),
            data_inicio_evento=hoje - timedelta(days=15),
            data_fim_evento=hoje - timedelta(days=1),
            status=self.status_rascunho,
        )
        result = self._get_result(self.staff)
        self.assertEqual(len(result["eventos_notificacao"]), 2)

        






