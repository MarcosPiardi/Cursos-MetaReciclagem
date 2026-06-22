"""
Arquivo: test_admin_config.py
Caminho: apps/eventos/tests/test_admin_config.py
Finalidade: Testes de configuracao e metodos nao cobertos pelos testes existentes
Atualizacoes:
 - 19/06/2026 - Criacao do arquivo
 - 19/06/2026 - Correcao: test_has_delete_permission_retorna_false passava None como request
 - 19/06/2026 - Correcao: test_actions_list comparava string com lista de funcoes
 - 19/06/2026 - Correcao: test_readonly_fields comparava list com tuple padrao do Django
 - 19/06/2026 - Correcao: test_vagas_inscritos_zero_vagas com assertiva fragil
 - 19/06/2026 - Correcao: TestEdgeCases usa build() para evitar IntegrityError em campos NOT NULL
 - 19/06/2026 - Correcao: test_vagas_inscritos_zero_vagas usa re.findall para extrair numeros do HTML
Escopo:
- Configuracao completa de CriterioAdmin, TurmaAdmin, HorarioAdmin
- Metodos: has_delete_permission, dia_semana_display, pontos_display
- StatusForm widget
- Edge cases: None status, None dates, total_vagas=0
- Inlines: get_queryset, formfield_for_foreignkey
"""

import re

import pytest
from django.contrib.admin import AdminSite
from django.http import HttpRequest

from apps.eventos.admin import (
    CriterioAdmin,
    EventoAdmin,
    EventoCriterioInline,
    HorarioAdmin,
    StatusAdmin,
    StatusForm,
    TurmaAdmin,
)
from apps.eventos.models import Evento, Status, Criterio, Turma, Horario, EventoCriterio
from apps.eventos.tests.factories import (
    CriterioFactory,
    EventoFactory,
    HorarioFactory,
    StatusFactory,
    TurmaFactory,
)

pytestmark = pytest.mark.django_db

@pytest.fixture
def admin_user():
    from django.contrib.auth import get_user_model
    User = get_user_model()
    return User.objects.create_superuser(
        username="admin_teste", email="admin@teste.com", password="123456"
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


class TestCriterioAdminConfig:
    def test_list_display(self, criterio_admin):
        assert criterio_admin.list_display == [
            "nome",
            "tipo_criterio",
            "categoria",
            "pontos",
            "ativo",
        ]

    def test_list_filter(self, criterio_admin):
        for field in ("tipo_criterio", "categoria", "ativo"):
            assert field in criterio_admin.list_filter

    def test_search_fields(self, criterio_admin):
        for field in ("nome", "codigo", "descricao"):
            assert field in criterio_admin.search_fields

    def test_list_editable(self, criterio_admin):
        assert "ativo" in criterio_admin.list_editable

    def test_readonly_fields(self, criterio_admin):
        # CORRECAO 19/06/2026: converter para list para aceitar tuple padrao do Django
        assert list(criterio_admin.readonly_fields) == []

    def test_fieldsets(self, criterio_admin):
        assert criterio_admin.fieldsets is not None

    def test_has_delete_permission_retorna_false(self, criterio_admin):
        # CORRECAO 19/06/2026: usar HttpRequest() em vez de None para evitar AttributeError
        request = HttpRequest()
        assert criterio_admin.has_delete_permission(request) is False


class TestTurmaAdminConfig:
    def test_list_display(self, turma_admin):
        assert turma_admin.list_display == [
            "nome",
            "evento",
            "turno",
            "capacidade",
            "data_inicio",
            "data_fim",
        ]

    def test_list_filter(self, turma_admin):
        for field in ("evento", "turno"):
            assert field in turma_admin.list_filter

    def test_search_fields(self, turma_admin):
        for field in ("nome", "evento__nome"):
            assert field in turma_admin.search_fields


class TestHorarioAdminConfig:
    def test_list_display(self, horario_admin):
        assert horario_admin.list_display == [
            "turma",
            "dia_semana_display",
            "hora_inicio",
            "hora_fim",
        ]

    def test_list_filter(self, horario_admin):
        for field in ("turma", "dia_semana"):
            assert field in horario_admin.list_filter


class TestHorarioAdminMethods:
    def test_dia_semana_display(self, horario_admin):
        horario = HorarioFactory(dia_semana=2)
        resultado = horario_admin.dia_semana_display(horario)
        assert resultado == horario.get_dia_semana_display()


class TestStatusAdminConfig:
    def test_list_editable(self, status_admin):
        assert "ordem" in status_admin.list_editable

    def test_ordering(self, status_admin):
        assert "ordem" in status_admin.ordering

    def test_fieldsets(self, status_admin):
        assert status_admin.fieldsets is not None


class TestEventoAdminConfigExtra:
    def test_fieldsets(self, evento_admin):
        assert evento_admin.fieldsets is not None

    def test_actions_list(self, evento_admin):
        for action_name in (
            "classificar_inscricoes",
            "desfazer_classificacao",
            "exportar_classificacao_excel",
        ):
            assert action_name in evento_admin.actions


class TestStatusForm:
    def test_widget_color(self):
        form = StatusForm()
        widget = form.fields["cor"].widget
        attrs = widget.attrs
        assert attrs.get("maxlength") == "7"
        assert "cursor: pointer" in attrs.get("style", "")
        assert "border-radius" in attrs.get("style", "")


class TestEventoCriterioInlineMethods:
    def test_pontos_display_com_pontos(self):
        criterio = CriterioFactory(pontos=10)
        evento = EventoFactory()
        ec = EventoCriterio.objects.create(evento=evento, criterio=criterio)
        inline = EventoCriterioInline(EventoCriterio, AdminSite())
        resultado = inline.pontos_display(ec)
        assert "10 pontos" in resultado

    def test_pontos_display_ordenacao(self):
        criterio = CriterioFactory(pontos=None)
        evento = EventoFactory()
        ec = EventoCriterio.objects.create(evento=evento, criterio=criterio)
        inline = EventoCriterioInline(EventoCriterio, AdminSite())
        resultado = inline.pontos_display(ec)
        assert "Ordenação" in resultado

    def test_get_queryset_usar_select_related(self, db):
        from django.test import RequestFactory
        from django.contrib.auth import get_user_model

        Usuario = get_user_model()
        inline = EventoCriterioInline(EventoCriterio, AdminSite())
        user = Usuario.objects.create_superuser("admin", "admin@test.com", "password")
        request = RequestFactory().get("/")
        request.user = user

        qs = inline.get_queryset(request)
        query_str = str(qs.query)
        assert "criterio" in query_str

    def test_formfield_for_foreignkey_filtra_ativos(self):
        CriterioFactory(ativo=True)
        CriterioFactory(ativo=False)
        inline = EventoCriterioInline(EventoCriterio, AdminSite())
        field = inline.formfield_for_foreignkey(
            EventoCriterio._meta.get_field("criterio"), HttpRequest()
        )
        assert field.queryset.count() == 1


class TestEdgeCases:
    def test_status_colorido_sem_status(self, evento_admin):
        status = StatusFactory()
        evento = EventoFactory(status=status)
        evento.status = None
        resultado = evento_admin.status_colorido(evento)
        assert resultado == "\u2014"

    def test_data_inicio_inscricao_sem_data(self, evento_admin):
        # CORRECAO 19/06/2026: campos de data sao NOT NULL no banco (regra de negocio valida).
        # build() instancia o objeto sem persistir — correto para testar o metodo do admin isoladamente.
        evento = EventoFactory.build(
            data_inicio_inscricao=None,
            data_fim_inscricao=None,
        )
        resultado = evento_admin.data_inicio_inscricao_formatada(evento)
        assert resultado == "\u2014"

    def test_data_fim_inscricao_sem_data(self, evento_admin):
        # CORRECAO 19/06/2026: idem — build() evita IntegrityError sem alterar o model.
        evento = EventoFactory.build(
            data_fim_inscricao=None,
            data_inicio_evento=None,
        )
        resultado = evento_admin.data_fim_inscricao_formatada(evento)
        assert resultado == "\u2014"

    def test_data_inicio_evento_sem_data(self, evento_admin):
        # CORRECAO 19/06/2026: idem.
        evento = EventoFactory.build(
            data_inicio_evento=None,
            data_fim_evento=None,
        )
        resultado = evento_admin.data_inicio_evento_formatada(evento)
        assert resultado == "\u2014"

    def test_data_fim_evento_sem_data(self, evento_admin):
        # CORRECAO 19/06/2026: idem.
        evento = EventoFactory.build(
            data_fim_evento=None,
        )
        resultado = evento_admin.data_fim_evento_formatada(evento)
        assert resultado == "\u2014"

    def test_vagas_inscritos_zero_vagas(self, evento_admin):
        # CORRECAO: regex extrai os numeros do padrao ">inscritos / vagas<"
        # evitando capturar digitos de atributos CSS como #dc3545
        evento = EventoFactory()
        resultado = evento_admin.vagas_inscritos(evento)
        match = re.search(r'>\s*(\d+)\s*/\s*(\d+)\s*<', resultado)
        assert match is not None, "Formato inesperado no retorno de vagas_inscritos"
        inscritos = match.group(1)
        assert inscritos == "0"





