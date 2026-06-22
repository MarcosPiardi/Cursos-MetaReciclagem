"""
Arquivo: test_admin.py
Caminho: apps/eventos/tests/test_admin.py
Finalidade: Testes de integracao do Django Admin para o app Eventos
Atualizacoes:
 - 07/04/2025 - Criacao do arquivo e implementacao inicial dos testes
 - 21/05/2026 - Correcao de testes que nao estavam passando
 - 22/05/2026 - Implementacao inicial com 28 testes de integracao real
 - 26/05/2026 - Ajuste final para garantir que todos os testes passem com sucesso
 - 09/06/2026 - Refatoracao completa para pytest puro consolidando 3 arquivos
 - 18/06/2026 - Removido @pytest.mark.django_db redundante; centralizado em pytestmark
Escopo:
- Registro dos ModelAdmins
- Changelist (listagem, busca, filtros)
- Views Add/Change/Delete
- Metodos customizados (status_colorido, vagas_inscritos, formatacao de datas)
- Inlines
Nao testar:
- Regras de negocio dos models
- clean()
- __str__()
- validacoes de datas
- inscricoes_abertas()
"""

import pytest
from django.urls import reverse
from django.contrib.admin.sites import AdminSite
from django.contrib.auth import get_user_model

from apps.eventos.models import Evento, Status, Criterio, Turma, Horario
from apps.eventos.admin import (
    EventoAdmin,
    StatusAdmin,
    CriterioAdmin,
    TurmaAdmin,
    HorarioAdmin,
)
from apps.eventos.tests.factories import (
    EventoFactory,
    StatusFactory,
    CriterioFactory,
    TurmaFactory,
    HorarioFactory,
)
from apps.selecao.tests.factories import InscricaoFactory

pytestmark = pytest.mark.django_db
User = get_user_model()

# ── Fixtures globais ──────────────────────────────────────────────────

@pytest.fixture
def admin_user(db):
    return User.objects.create_superuser(
        username="admin", email="admin@test.com", password="password123"
    )

@pytest.fixture
def admin_client(client, admin_user):
    client.force_login(admin_user)
    return client

@pytest.fixture
def site():
    return AdminSite()

@pytest.fixture
def evento_admin(site):
    return EventoAdmin(Evento, site)

@pytest.fixture
def status_admin(site):
    return StatusAdmin(Status, site)

@pytest.fixture
def criterio_admin(site):
    return CriterioAdmin(Criterio, site)

@pytest.fixture
def turma_admin(site):
    return TurmaAdmin(Turma, site)

@pytest.fixture
def horario_admin(site):
    return HorarioAdmin(Horario, site)

# ── Configuracao dos ModelAdmins ──────────────────────────────────────

class TestEventoAdminConfig:
    def test_list_display(self, evento_admin):
        expected = [
            "nome",
            "status_colorido",
            "vagas_inscritos",
            "data_inicio_inscricao_formatada",
            "data_fim_inscricao_formatada",
            "data_inicio_evento_formatada",
            "data_fim_evento_formatada",
        ]
        assert evento_admin.list_display == expected

    def test_list_filter(self, evento_admin):
        assert "status" in evento_admin.list_filter

    def test_search_fields(self, evento_admin):
        assert "nome" in evento_admin.search_fields

# ── Evento Admin — Changelist ────────────────────────────────────────

class TestEventoAdminChangeList:
    def test_changelist_carrega(self, admin_client):
        url = reverse("admin:eventos_evento_changelist")
        response = admin_client.get(url)
        assert response.status_code == 200

    def test_busca_por_nome(self, admin_client):
        EventoFactory(nome="Workshop Django")
        url = reverse("admin:eventos_evento_changelist")
        response = admin_client.get(url, {"q": "Workshop"})
        assert response.status_code == 200
        assert "Workshop Django" in str(response.content)

    def test_filtrar_por_status(self, admin_client):
        status = StatusFactory(nome="Publicado")
        EventoFactory(status=status)
        url = reverse("admin:eventos_evento_changelist")
        response = admin_client.get(url, {"status__id__exact": status.id})
        assert response.status_code == 200

    def test_paginacao(self, admin_client):
        EventoFactory.create_batch(105)
        url = reverse("admin:eventos_evento_changelist")
        response = admin_client.get(url)
        assert response.status_code == 200

    def test_busca_vazia(self, admin_client):
        url = reverse("admin:eventos_evento_changelist")
        response = admin_client.get(url, {"q": ""})
        assert response.status_code == 200

# ── Status Admin — Changelist ────────────────────────────────────────

class TestStatusAdminChangeList:
    def test_changelist_carrega(self, admin_client):
        url = reverse("admin:eventos_status_changelist")
        response = admin_client.get(url)
        assert response.status_code == 200

    def test_busca_por_nome(self, admin_client):
        StatusFactory(nome="Ativo")
        url = reverse("admin:eventos_status_changelist")
        response = admin_client.get(url, {"q": "Ativo"})
        assert response.status_code == 200

# ── Turma Admin — Changelist ─────────────────────────────────────────

class TestTurmaAdminChangeList:
    def test_changelist_carrega(self, admin_client):
        url = reverse("admin:eventos_turma_changelist")
        response = admin_client.get(url)
        assert response.status_code == 200

    def test_busca_por_nome(self, admin_client):
        TurmaFactory(nome="Turma A")
        url = reverse("admin:eventos_turma_changelist")
        response = admin_client.get(url, {"q": "Turma"})
        assert response.status_code == 200

# ── Views: EventoAdmin ───────────────────────────────────────────────

class TestEventoAdminViews:
    def test_add_view(self, admin_client):
        url = reverse("admin:eventos_evento_add")
        response = admin_client.get(url)
        assert response.status_code == 200

    def test_change_view(self, admin_client):
        evento = EventoFactory()
        url = reverse("admin:eventos_evento_change", args=[evento.pk])
        response = admin_client.get(url)
        assert response.status_code == 200

    def test_delete_view(self, admin_client):
        evento = EventoFactory()
        url = reverse("admin:eventos_evento_delete", args=[evento.pk])
        response = admin_client.get(url)
        assert response.status_code == 200

# ── Views: StatusAdmin ───────────────────────────────────────────────

class TestStatusAdminViews:
    def test_add_view(self, admin_client):
        url = reverse("admin:eventos_status_add")
        response = admin_client.get(url)
        assert response.status_code == 200

    def test_change_view(self, admin_client):
        status = StatusFactory()
        url = reverse("admin:eventos_status_change", args=[status.pk])
        response = admin_client.get(url)
        assert response.status_code == 200

    def test_delete_view(self, admin_client):
        status = StatusFactory()
        url = reverse("admin:eventos_status_delete", args=[status.pk])
        response = admin_client.get(url)
        assert response.status_code == 200

# ── Views: TurmaAdmin ────────────────────────────────────────────────

class TestTurmaAdminViews:
    def test_add_view(self, admin_client):
        url = reverse("admin:eventos_turma_add")
        response = admin_client.get(url)
        assert response.status_code == 200

    def test_change_view(self, admin_client):
        turma = TurmaFactory()
        url = reverse("admin:eventos_turma_change", args=[turma.pk])
        response = admin_client.get(url)
        assert response.status_code == 200

# ── Metodos customizados ─────────────────────────────────────────────

class TestEventoAdminMethods:
    def test_status_colorido(self, evento_admin):
        status = StatusFactory(nome="Publicado", cor="#00ff00")
        evento = EventoFactory(status=status)
        html = evento_admin.status_colorido(evento)
        assert "Publicado" in html
        assert "#00ff00" in html

    def test_vagas_inscritos_sem_inscricoes(self, evento_admin):
        evento = EventoFactory()
        resultado = evento_admin.vagas_inscritos(evento)
        assert "0" in resultado

    def test_vagas_inscritos_com_inscricoes(self, evento_admin):
        evento = EventoFactory(total_vagas=50)
        InscricaoFactory(evento=evento)
        InscricaoFactory(evento=evento)
        InscricaoFactory(evento=evento)
        resultado = evento_admin.vagas_inscritos(evento)
        assert "3" in resultado
        assert "50" in resultado

    def test_data_inicio_inscricao_formatada(self, evento_admin):
        evento = EventoFactory()
        resultado = evento_admin.data_inicio_inscricao_formatada(evento)
        assert "/" in resultado

    def test_data_fim_inscricao_formatada(self, evento_admin):
        evento = EventoFactory()
        resultado = evento_admin.data_fim_inscricao_formatada(evento)
        assert "/" in resultado

# ── Inlines ──────────────────────────────────────────────────────────

class TestEventoAdminInlines:
    def test_exibe_inline_criterios(self, admin_client):
        evento = EventoFactory()
        url = reverse("admin:eventos_evento_change", args=[evento.pk])
        response = admin_client.get(url)
        assert response.status_code == 200
        assert "evento_criterios" in str(response.content)

    def test_exibe_inline_turmas(self, admin_client):
        evento = EventoFactory()
        url = reverse("admin:eventos_evento_change", args=[evento.pk])
        response = admin_client.get(url)
        assert response.status_code == 200
        assert "turmas" in str(response.content)

    def test_change_view_carrega_com_inlines(self, admin_client):
        evento = EventoFactory()
        url = reverse("admin:eventos_evento_change", args=[evento.pk])
        response = admin_client.get(url)
        assert response.status_code == 200

# ── Horario Admin ────────────────────────────────────────────────────

class TestHorarioAdminChangeList:
    def test_changelist_carrega(self, admin_client):
        url = reverse("admin:eventos_horario_changelist")
        response = admin_client.get(url)
        assert response.status_code == 200

    def test_filtro_dia_semana(self, admin_client):
        horario = HorarioFactory()
        url = reverse("admin:eventos_horario_changelist")
        response = admin_client.get(url, {"dia_semana__exact": horario.dia_semana})
        assert response.status_code == 200


        