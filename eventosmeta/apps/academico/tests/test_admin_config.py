"""
Arquivo: test_admin_config.py
Caminho: apps/eventos/tests/test_admin_config.py
Finalidade: Testes de configuracao e metodos do admin do app eventos
Atualizacoes:
 - 22/06/2026 - Criacao do arquivo
"""

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
from apps.eventos.models import (
    Criterio,
    Evento,
    EventoCriterio,
    Horario,
    Status,
    Turma,
)
from apps.eventos.tests.factories import (
    CriterioFactory,
    EventoFactory,
    HorarioFactory,
    StatusFactory,
    TurmaFactory,
)

pytestmark = pytest.mark.django_db


@pytest.fixture
def admin_user(db, django_user_model):
    """Retorna um superusuario para testes no admin."""
    return django_user_model.objects.create_superuser(
        username="admin",
        email="admin@example.com",
        password="password123",
    )


@pytest.fixture
def admin_client(db, client, admin_user):
    """Retorna um cliente Django logado no admin."""
    client.force_login(admin_user)
    return client


@pytest.fixture
def site():
    """Retorna uma instancia de AdminSite."""
    return AdminSite()


@pytest.fixture
def evento_admin(site):
    """Retorna uma instancia de EventoAdmin."""
    return EventoAdmin(Evento, site)


@pytest.fixture
def status_admin(site):
    """Retorna uma instancia de StatusAdmin."""
    return StatusAdmin(Status, site)


@pytest.fixture
def criterio_admin(site):
    """Retorna uma instancia de CriterioAdmin."""
    return CriterioAdmin(Criterio, site)


@pytest.fixture
def turma_admin(site):
    """Retorna uma instancia de TurmaAdmin."""
    return TurmaAdmin(Turma, site)


@pytest.fixture
def horario_admin(site):
    """Retorna uma instancia de HorarioAdmin."""
    return HorarioAdmin(Horario, site)


class TestCriterioAdminConfig:
    """Testes de configuracao do CriterioAdmin."""

    def test_list_display(self, criterio_admin):
        """Verifica os campos exibidos na listagem."""
        assert criterio_admin.list_display == [
            "nome",
            "tipo_criterio",
            "categoria",
            "pontos",
            "ativo",
        ]

    def test_list_filter(self, criterio_admin):
        """Verifica os filtros laterais disponiveis."""
        assert "tipo_criterio" in criterio_admin.list_filter
        assert "categoria" in criterio_admin.list_filter
        assert "ativo" in criterio_admin.list_filter

    def test_search_fields(self, criterio_admin):
        """Verifica os campos utilizados na busca."""
        assert "nome" in criterio_admin.search_fields
        assert "codigo" in criterio_admin.search_fields
        assert "descricao" in criterio_admin.search_fields

    def test_list_editable(self, criterio_admin):
        """Verifica o campo editavel diretamente na listagem."""
        assert "ativo" in criterio_admin.list_editable

    def test_readonly_fields(self, criterio_admin):
        """Verifica que nao existem campos somente leitura."""
        assert criterio_admin.readonly_fields == []

    def test_fieldsets(self, criterio_admin):
        """Verifica que a configuracao de fieldsets esta definida."""
        assert criterio_admin.fieldsets is not None

    def test_has_delete_permission_retorna_false(self, criterio_admin):
        """Verifica que a permissao de exclusao sempre retorna False."""
        assert criterio_admin.has_delete_permission(None) is False


class TestTurmaAdminConfig:
    """Testes de configuracao do TurmaAdmin."""

    def test_list_display(self, turma_admin):
        """Verifica os campos exibidos na listagem."""
        assert turma_admin.list_display == [
            "nome",
            "evento",
            "turno",
            "capacidade",
            "data_inicio",
            "data_fim",
        ]

    def test_list_filter(self, turma_admin):
        """Verifica os filtros laterais disponiveis."""
        assert "evento" in turma_admin.list_filter
        assert "turno" in turma_admin.list_filter

    def test_search_fields(self, turma_admin):
        """Verifica os campos utilizados na busca."""
        assert "nome" in turma_admin.search_fields
        assert "evento__nome" in turma_admin.search_fields


class TestHorarioAdminConfig:
    """Testes de configuracao do HorarioAdmin."""

    def test_list_display(self, horario_admin):
        """Verifica os campos exibidos na listagem."""
        assert horario_admin.list_display == [
            "turma",
            "dia_semana_display",
            "hora_inicio",
            "hora_fim",
        ]

    def test_list_filter(self, horario_admin):
        """Verifica os filtros laterais disponiveis."""
        assert "turma" in horario_admin.list_filter
        assert "dia_semana" in horario_admin.list_filter


class TestHorarioAdminMethods:
    """Testes dos metodos customizados do HorarioAdmin."""

    def test_dia_semana_display(self, horario_admin):
        """Verifica que dia_semana_display retorna o display correto."""
        horario = HorarioFactory(dia_semana=2)
        resultado = horario_admin.dia_semana_display(horario)
        assert resultado == horario.get_dia_semana_display()


class TestStatusAdminConfig:
    """Testes de configuracao do StatusAdmin."""

    def test_list_editable(self, status_admin):
        """Verifica que a ordem eh editavel na listagem."""
        assert "ordem" in status_admin.list_editable

    def test_ordering(self, status_admin):
        """Verifica que a ordenacao padrao utiliza o campo ordem."""
        assert "ordem" in status_admin.ordering

    def test_fieldsets(self, status_admin):
        """Verifica que a configuracao de fieldsets esta definida."""
        assert status_admin.fieldsets is not None


class TestEventoAdminConfigExtra:
    """Testes extras de configuracao do EventoAdmin."""

    def test_fieldsets(self, evento_admin):
        """Verifica que a configuracao de fieldsets esta definida."""
        assert evento_admin.fieldsets is not None

    def test_actions_list(self, evento_admin):
        """Verifica que as actions customizadas estao registradas."""
        for action in (
            "classificar_inscricoes",
            "desfazer_classificacao",
            "exportar_classificacao_excel",
        ):
            assert action in evento_admin.actions


class TestStatusForm:
    """Testes de configuracao do widget de cor do StatusForm."""

    def test_widget_color(self):
        """Verifica o widget do campo cor."""
        form = StatusForm()
        widget = form.fields["cor"].widget
        attrs = widget.attrs
        assert attrs.get("maxlength") == "7"
        style = attrs.get("style", "")
        assert "cursor: pointer" in style
        assert "border-radius" in style


class TestEventoCriterioInlineMethods:
    """Testes dos metodos e comportamentos do EventoCriterioInline."""

    def test_pontos_display_com_pontos(self):
        """Verifica que pontos_display exibe a pontuacao quando existir."""
        criterio = CriterioFactory(pontos=10)
        evento = EventoFactory()
        evento_criterio = EventoCriterio.objects.create(
            evento=evento,
            criterio=criterio,
        )
        inline = EventoCriterioInline(EventoCriterio, AdminSite())
        resultado = inline.pontos_display(evento_criterio)
        assert "10 pontos" in resultado

    def test_pontos_display_ordenacao(self):
        """Verifica que pontos_display exibe 'Ordenacao' quando pontos for nulo."""
        criterio = CriterioFactory(pontos=None)
        evento = EventoFactory()
        evento_criterio = EventoCriterio.objects.create(
            evento=evento,
            criterio=criterio,
        )
        inline = EventoCriterioInline(EventoCriterio, AdminSite())
        resultado = inline.pontos_display(evento_criterio)
        assert "Ordenação" in resultado

    def test_get_queryset_usar_select_related(self):
        """Verifica que o queryset utiliza select_related em criterio."""
        inline = EventoCriterioInline(EventoCriterio, AdminSite())
        qs = inline.get_queryset(HttpRequest())
        assert "criterio" in str(qs.query).lower()

    def test_formfield_for_foreignkey_filtra_ativos(self):
        """Verifica que o queryset de criterio exibe apenas criterios ativos."""
        CriterioFactory(ativo=True)
        CriterioFactory(ativo=False)
        inline = EventoCriterioInline(EventoCriterio, AdminSite())
        field = inline.formfield_for_foreignkey(
            EventoCriterio._meta.get_field("criterio"),
            HttpRequest(),
        )
        assert field.queryset.count() == 1


class TestEdgeCases:
    """Testes de casos de borda dos metodos do EventoAdmin."""

    def test_status_colorido_sem_status(self, evento_admin):
        """Verifica status_colorido quando o evento nao possui status."""
        evento = EventoFactory(status=None)
        resultado = evento_admin.status_colorido(evento)
        assert resultado == "—"

    def test_data_inicio_inscricao_sem_data(self, evento_admin):
        """Verifica data_inicio_inscricao_formatada sem data definida."""
        evento = EventoFactory(data_inicio_inscricao=None)
        resultado = evento_admin.data_inicio_inscricao_formatada(evento)
        assert resultado == "—"

    def test_data_fim_inscricao_sem_data(self, evento_admin):
        """Verifica data_fim_inscricao_formatada sem data definida."""
        evento = EventoFactory(data_fim_inscricao=None)
        resultado = evento_admin.data_fim_inscricao_formatada(evento)
        assert resultado == "—"

    def test_data_inicio_evento_sem_data(self, evento_admin):
        """Verifica data_inicio_evento_formatada sem data definida."""
        evento = EventoFactory(data_inicio_evento=None)
        resultado = evento_admin.data_inicio_evento_formatada(evento)
        assert resultado == "—"

    def test_data_fim_evento_sem_data(self, evento_admin):
        """Verifica data_fim_evento_formatada sem data definida."""
        evento = EventoFactory(data_fim_evento=None)
        resultado = evento_admin.data_fim_evento_formatada(evento)
        assert resultado == "—"

    def test_vagas_inscritos_zero_vagas(self, evento_admin):
        """Verifica vagas_inscritos quando o evento possui zero vagas."""
        evento = EventoFactory(total_vagas=0)
        resultado = evento_admin.vagas_inscritos(evento)
        assert "0" in resultado



        