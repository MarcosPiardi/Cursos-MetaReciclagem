"""
Arquivo: test_context_processors.py
caminho: apps/eventos/tests/test_context_processors.py
Finalidade: Testar os context processors do app eventos.
Atualizacoes:
 - 29/05/2026 - Criacao do arquivo
 - 18/06/2026 - Refatorado de unittest.TestCase para pytest
 - 18/06/2026 - Corrigido warnings de datetime naive: usar timezone.now()
                em DateTimeField (data_inicio_inscricao, data_fim_inscricao)
"""

from datetime import date, timedelta

import pytest
from django.test import RequestFactory
from django.contrib.auth import get_user_model
from django.utils import timezone

from apps.eventos.models import Evento, Status
from apps.eventos.context_processors import notificacoes_eventos

pytestmark = pytest.mark.django_db

@pytest.fixture
def rf():
    return RequestFactory()

@pytest.fixture
def staff_user(db):
    User = get_user_model()
    return User.objects.create_user(
        username="staff",
        email="staff@test.com",
        password="test123",
        cpf="11111111111",
        is_staff=True,
    )

@pytest.fixture
def normal_user(db):
    User = get_user_model()
    return User.objects.create_user(
        username="user",
        email="user@test.com",
        password="test123",
        cpf="22222222222",
        is_staff=False,
    )

@pytest.fixture
def status(db):
    return {
        "inscricoes_abertas": Status.objects.create(
            nome="Inscri\u00e7\u00f5es Abertas"
        ),
        "em_andamento": Status.objects.create(nome="Em Andamento"),
        "finalizado": Status.objects.create(nome="Finalizado"),
        "cancelado": Status.objects.create(nome="Cancelado"),
        "inscricoes_encerradas": Status.objects.create(
            nome="Inscri\u00e7\u00f5es Encerradas"
        ),
        "rascunho": Status.objects.create(nome="Rascunho"),
    }

def _get_result(request, user):
    request.user = user
    return notificacoes_eventos(request)

class TestNotificacoesEventos:
    """Testes do context processor notificacoes_eventos"""

    # --- Autenticacao ---

    def test_usuario_anonimo_retorna_lista_vazia(self, rf):
        request = rf.get("/")
        result = _get_result(
            request,
            type("AnonUser", (), {"is_authenticated": False, "is_staff": False})(),
        )
        assert result == {"eventos_notificacao": []}

    def test_usuario_nao_staff_retorna_lista_vazia(self, rf, normal_user):
        request = rf.get("/")
        result = _get_result(request, normal_user)
        assert result == {"eventos_notificacao": []}

    def test_sem_eventos_retorna_lista_vazia(self, rf, staff_user):
        request = rf.get("/")
        result = _get_result(request, staff_user)
        assert result == {"eventos_notificacao": []}

    # --- Verificacao 1 ---

    def test_verificacao1_status_correto_sem_alerta(self, rf, staff_user, status):
        agora = timezone.now()
        Evento.objects.create(
            nome="Evento Teste",
            total_vagas=30,
            data_inicio_inscricao=agora - timedelta(days=1),
            data_fim_inscricao=agora + timedelta(days=1),
            data_inicio_evento=date.today() + timedelta(days=10),
            data_fim_evento=date.today() + timedelta(days=15),
            status=status["inscricoes_abertas"],
        )
        request = rf.get("/")
        result = _get_result(request, staff_user)
        assert len(result["eventos_notificacao"]) == 0

    def test_verificacao1_status_errado_gera_alerta(self, rf, staff_user, status):
        agora = timezone.now()
        evento = Evento.objects.create(
            nome="Evento Teste",
            total_vagas=30,
            data_inicio_inscricao=agora - timedelta(days=1),
            data_fim_inscricao=agora + timedelta(days=1),
            data_inicio_evento=date.today() + timedelta(days=10),
            data_fim_evento=date.today() + timedelta(days=15),
            status=status["rascunho"],
        )
        request = rf.get("/")
        result = _get_result(request, staff_user)
        assert len(result["eventos_notificacao"]) == 1
        assert result["eventos_notificacao"][0].pk == evento.pk
        assert result["eventos_notificacao"][0].tipo_alerta == "inscricao"

    # --- Verificacao 2 ---

    def test_verificacao2_status_valido_sem_alerta(self, rf, staff_user, status):
        agora = timezone.now()
        Evento.objects.create(
            nome="Evento Teste",
            total_vagas=30,
            data_inicio_inscricao=agora - timedelta(days=10),
            data_fim_inscricao=agora - timedelta(days=1),
            data_inicio_evento=date.today() + timedelta(days=5),
            data_fim_evento=date.today() + timedelta(days=10),
            status=status["inscricoes_encerradas"],
        )
        request = rf.get("/")
        result = _get_result(request, staff_user)
        assert len(result["eventos_notificacao"]) == 0

    def test_verificacao2_status_invalido_gera_alerta(self, rf, staff_user, status):
        agora = timezone.now()
        evento = Evento.objects.create(
            nome="Evento Teste",
            total_vagas=30,
            data_inicio_inscricao=agora - timedelta(days=10),
            data_fim_inscricao=agora - timedelta(days=1),
            data_inicio_evento=date.today() + timedelta(days=5),
            data_fim_evento=date.today() + timedelta(days=10),
            status=status["rascunho"],
        )
        request = rf.get("/")
        result = _get_result(request, staff_user)
        assert len(result["eventos_notificacao"]) == 1
        assert result["eventos_notificacao"][0].pk == evento.pk
        assert result["eventos_notificacao"][0].tipo_alerta == "pos_inscricao"

    # --- Verificacao 3 ---

    def test_verificacao3_status_correto_sem_alerta(self, rf, staff_user, status):
        agora = timezone.now()
        Evento.objects.create(
            nome="Evento Teste",
            total_vagas=30,
            data_inicio_inscricao=agora - timedelta(days=20),
            data_fim_inscricao=agora - timedelta(days=10),
            data_inicio_evento=date.today() - timedelta(days=1),
            data_fim_evento=date.today() + timedelta(days=5),
            status=status["em_andamento"],
        )
        request = rf.get("/")
        result = _get_result(request, staff_user)
        assert len(result["eventos_notificacao"]) == 0

    def test_verificacao3_status_errado_gera_alerta(self, rf, staff_user, status):
        agora = timezone.now()
        evento = Evento.objects.create(
            nome="Evento Teste",
            total_vagas=30,
            data_inicio_inscricao=agora - timedelta(days=20),
            data_fim_inscricao=agora - timedelta(days=10),
            data_inicio_evento=date.today() - timedelta(days=1),
            data_fim_evento=date.today() + timedelta(days=5),
            status=status["rascunho"],
        )
        request = rf.get("/")
        result = _get_result(request, staff_user)
        assert len(result["eventos_notificacao"]) == 1
        assert result["eventos_notificacao"][0].pk == evento.pk
        assert result["eventos_notificacao"][0].tipo_alerta == "evento"

    # --- Verificacao 4 ---

    def test_verificacao4_status_valido_sem_alerta(self, rf, staff_user, status):
        agora = timezone.now()
        Evento.objects.create(
            nome="Evento Teste",
            total_vagas=30,
            data_inicio_inscricao=agora - timedelta(days=30),
            data_fim_inscricao=agora - timedelta(days=20),
            data_inicio_evento=date.today() - timedelta(days=15),
            data_fim_evento=date.today() - timedelta(days=1),
            status=status["finalizado"],
        )
        request = rf.get("/")
        result = _get_result(request, staff_user)
        assert len(result["eventos_notificacao"]) == 0

    def test_verificacao4_status_invalido_gera_alerta(self, rf, staff_user, status):
        agora = timezone.now()
        evento = Evento.objects.create(
            nome="Evento Teste",
            total_vagas=30,
            data_inicio_inscricao=agora - timedelta(days=30),
            data_fim_inscricao=agora - timedelta(days=20),
            data_inicio_evento=date.today() - timedelta(days=15),
            data_fim_evento=date.today() - timedelta(days=1),
            status=status["rascunho"],
        )
        request = rf.get("/")
        result = _get_result(request, staff_user)
        assert len(result["eventos_notificacao"]) == 1
        assert result["eventos_notificacao"][0].pk == evento.pk
        assert result["eventos_notificacao"][0].tipo_alerta == "pos_evento"

    def test_verificacao4_cancelado_sem_alerta(self, rf, staff_user, status):
        agora = timezone.now()
        Evento.objects.create(
            nome="Evento Cancelado",
            total_vagas=30,
            data_inicio_inscricao=agora - timedelta(days=30),
            data_fim_inscricao=agora - timedelta(days=20),
            data_inicio_evento=date.today() - timedelta(days=15),
            data_fim_evento=date.today() - timedelta(days=1),
            status=status["cancelado"],
        )
        request = rf.get("/")
        result = _get_result(request, staff_user)
        assert len(result["eventos_notificacao"]) == 0

    # --- Multiplos eventos ---

    def test_multiplos_eventos_com_alerta(self, rf, staff_user, status):
        agora = timezone.now()
        Evento.objects.create(
            nome="Alerta Inscricao",
            total_vagas=30,
            data_inicio_inscricao=agora - timedelta(days=1),
            data_fim_inscricao=agora + timedelta(days=1),
            data_inicio_evento=date.today() + timedelta(days=10),
            data_fim_evento=date.today() + timedelta(days=15),
            status=status["rascunho"],
        )
        Evento.objects.create(
            nome="Alerta Pos-Evento",
            total_vagas=30,
            data_inicio_inscricao=agora - timedelta(days=30),
            data_fim_inscricao=agora - timedelta(days=20),
            data_inicio_evento=date.today() - timedelta(days=15),
            data_fim_evento=date.today() - timedelta(days=1),
            status=status["rascunho"],
        )
        request = rf.get("/")
        result = _get_result(request, staff_user)
        assert len(result["eventos_notificacao"]) == 2

        