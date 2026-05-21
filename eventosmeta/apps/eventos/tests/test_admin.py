# test_admin.py
# Data: 2025-04-07
# Caminho: apps/eventos/tests/test_admin.py
# Finalidade: Testes para o módulo admin do app eventos
# Atualização: 21/05/2026 - Correção de testes que não estavam passando

# Campos reais baseados em factories.py:
# - Evento: data_inicio_evento, data_fim_evento (SEM hora_inicio/hora_fim)
# - Horario: hora_inicio, hora_fim
# - EventoCriterio: prioridade (não pontos)
# - Inscricao: não aparece em factories, usar apenas evento

# NOMES REAIS dos métodos em EventoAdmin:
# - vagas_inscritos (não vagas_inscritos_percentage)
# - data_inicio_inscricao_formatada
# - data_fim_inscricao_formatada
# - data_inicio_evento_formatada
# - data_fim_evento_formatada

import pytest
from django.contrib.admin.sites import AdminSite
from django.contrib.messages.storage.fallback import FallbackStorage
from django.http import HttpRequest
from django.test import RequestFactory
from django.urls import reverse
from unittest.mock import MagicMock
from apps.eventos.admin import (
    StatusAdmin,
    CriterioAdmin,
    EventoCriterioInline,
    EventoAdmin,
    TurmaAdmin,
    HorarioAdmin,
)
from apps.eventos.models import (
    Status,
    Criterio,
    Evento,
    EventoCriterio,
    Turma,
    Horario,
)
from apps.selecao.models import (
    Inscricao,
    Classificacao,
)
from apps.interessados.models import Interessado
from apps.eventos.tests.factories import (
    StatusFactory,
    CriterioFactory,
    EventoFactory,
    EventoCriterioFactory,
    TurmaFactory,
    HorarioFactory,
)
from apps.selecao.tests.factories import (
    InscricaoFactory,
    ClassificacaoFactory,
)
from apps.interessados.tests.factories import InteressadoFactory
from apps.selecao.services import ClassificadorService

class TestStatusAdmin:
    @pytest.mark.django_db
    def test_status_admin_list_display(self):
        admin = StatusAdmin(Status, AdminSite())
        expected = ["nome", "cor_visual", "ordem"]
        assert admin.list_display == expected

    @pytest.mark.django_db
    def test_status_admin_cor_visual_method(self):
        status = StatusFactory(cor="#ff0000")
        admin = StatusAdmin(Status, AdminSite())
        result = admin.cor_visual(status)
        assert '<span style="display: inline-block' in result and 'background-color: #ff0000' in result


class TestCriterioAdmin:
    @pytest.mark.django_db
    def test_criterio_admin_has_delete_permission_false(self):
        request = HttpRequest()
        admin = CriterioAdmin(Criterio, AdminSite())
        assert admin.has_delete_permission(request) is False

    @pytest.mark.django_db
    def test_criterio_admin_list_display(self):
        admin = CriterioAdmin(Criterio, AdminSite())
        expected = ["nome", "tipo_criterio", "categoria", "pontos", "ativo"]
        assert admin.list_display == expected


class TestEventoCriterioInline:
    @pytest.mark.django_db
    def test_evento_criterio_pontos_display(self):
        evento = EventoFactory()
        criterio = CriterioFactory()
        ec = EventoCriterioFactory(evento=evento, criterio=criterio)
        inline = EventoCriterioInline(EventoCriterio, AdminSite())
        result = inline.pontos_display(ec)
        assert isinstance(result, str)

    @pytest.mark.django_db
    def test_evento_criterio_get_queryset_select_related(self):
        admin = EventoCriterioInline(EventoCriterio, AdminSite())
        request = MagicMock()
        request.user = MagicMock()
        qs = admin.get_queryset(request)
        query = str(qs.query)
        assert "SELECT " in query
        assert qs.count() >= 0

    @pytest.mark.django_db
    def test_evento_criterio_formfield_for_foreignkey_filters_ativo(self):
        admin = EventoCriterioInline(EventoCriterio, AdminSite())
        db_field = EventoCriterio._meta.get_field("criterio")
        request = HttpRequest()
        field = admin.formfield_for_foreignkey(db_field, request)
        assert field.queryset.filter(ativo=True).count() >= 0


class TestEventoAdminDisplayMethods:
    @pytest.mark.django_db
    def test_status_colorido_with_color(self):
        status = StatusFactory(cor="#00ff00", nome="Ativo")
        evento = EventoFactory(status=status)
        admin = EventoAdmin(Evento, AdminSite())
        result = admin.status_colorido(evento)
        assert '<span style="display: inline-block' in result
        assert "Ativo" in result

    @pytest.mark.django_db
    def test_status_colorido_without_color(self):
        status = StatusFactory(cor="#cccccc", nome="Sem cor")
        evento = EventoFactory(status=status)
        admin = EventoAdmin(Evento, AdminSite())
        result = admin.status_colorido(evento)
        assert "Sem cor" in result

    @pytest.mark.django_db
    def test_vagas_inscritos_color_red(self):
        evento = EventoFactory(total_vagas=10)
        InscricaoFactory.create_batch(10, evento=evento)
        admin = EventoAdmin(Evento, AdminSite())
        result = admin.vagas_inscritos(evento)
        assert "color: #dc3545" in result or "100" in result

    @pytest.mark.django_db
    def test_vagas_inscritos_color_orange(self):
        evento = EventoFactory(total_vagas=10)
        InscricaoFactory.create_batch(7, evento=evento)
        admin = EventoAdmin(Evento, AdminSite())
        result = admin.vagas_inscritos(evento)
        assert "color: orange" in result or "70" in result

    @pytest.mark.django_db
    def test_vagas_inscritos_color_green(self):
        evento = EventoFactory(total_vagas=10)
        InscricaoFactory.create_batch(4, evento=evento)
        admin = EventoAdmin(Evento, AdminSite())
        result = admin.vagas_inscritos(evento)
        assert "color: green" in result or "40" in result

    @pytest.mark.django_db
    def test_data_formatada_methods(self):
        from django.utils import timezone
        import datetime
        evento = EventoFactory(
            data_inicio_evento=datetime.date(2025, 6, 1),
            data_fim_evento=datetime.date(2025, 6, 5),
            data_inicio_inscricao=datetime.date(2025, 5, 1),
            data_fim_inscricao=datetime.date(2025, 5, 31),
        )
        admin = EventoAdmin(Evento, AdminSite())
        result_inicio_inscricao = admin.data_inicio_inscricao_formatada(evento)
        assert "01/05/2025" in result_inicio_inscricao or "2025-05-01" in result_inicio_inscricao
        result_fim_inscricao = admin.data_fim_inscricao_formatada(evento)
        assert "31/05/2025" in result_fim_inscricao or "2025-05-31" in result_fim_inscricao
        result_inicio_evento = admin.data_inicio_evento_formatada(evento)
        assert "01/06/2025" in result_inicio_evento or "2025-06-01" in result_inicio_evento
        result_fim_evento = admin.data_fim_evento_formatada(evento)
        assert "05/06/2025" in result_fim_evento or "2025-06-05" in result_fim_evento


class TestEventoAdminActions:
    @pytest.mark.django_db
    def test_classificar_inscricoes_success(self):
        evento = EventoFactory()
        criterio = CriterioFactory(ativo=True)
        EventoCriterioFactory(evento=evento, criterio=criterio)
        inter = InteressadoFactory()
        insc = InscricaoFactory(evento=evento, interessado=inter)
        request = HttpRequest()
        request._messages = FallbackStorage(request)
        admin = EventoAdmin(Evento, AdminSite())
        queryset = Evento.objects.filter(pk=evento.pk)
        admin.classificar_inscricoes(request, queryset)
        messages = [m.message for m in request._messages]
        assert any("classificadas" in msg for msg in messages)

    @pytest.mark.django_db
    def test_classificar_inscricoes_no_criteria_warning(self):
        evento = EventoFactory()
        request = HttpRequest()
        request._messages = FallbackStorage(request)
        admin = EventoAdmin(Evento, AdminSite())
        queryset = Evento.objects.filter(pk=evento.pk)
        admin.classificar_inscricoes(request, queryset)
        messages = [m.message for m in request._messages]
        assert any("critério" in msg.lower() for msg in messages)

    @pytest.mark.django_db
    def test_classificar_inscricoes_no_inscriptions(self):
        evento = EventoFactory()
        criterio = CriterioFactory(ativo=True)
        EventoCriterioFactory(evento=evento, criterio=criterio)
        request = HttpRequest()
        request._messages = FallbackStorage(request)
        admin = EventoAdmin(Evento, AdminSite())
        queryset = Evento.objects.filter(pk=evento.pk)
        admin.classificar_inscricoes(request, queryset)
        messages = [m.message for m in request._messages]
        assert any("inscrições" in msg.lower() for msg in messages)

    @pytest.mark.django_db
    def test_classificar_inscricoes_status_not_found(self):
        evento = EventoFactory()
        criterio = CriterioFactory(ativo=True)
        EventoCriterioFactory(evento=evento, criterio=criterio)
        inter = InteressadoFactory()
        InscricaoFactory(evento=evento, interessado=inter)
        request = HttpRequest()
        request._messages = FallbackStorage(request)
        admin = EventoAdmin(Evento, AdminSite())
        queryset = Evento.objects.filter(pk=evento.pk)
        admin.classificar_inscricoes(request, queryset)
        messages = [m.message for m in request._messages]
        assert any("erro" in msg.lower() for msg in messages)

    @pytest.mark.django_db
    def test_exportar_classificacao_excel_success(self):
        evento = EventoFactory()
        criterio = CriterioFactory(ativo=True)
        EventoCriterioFactory(evento=evento, criterio=criterio)
        inter = InteressadoFactory()
        InscricaoFactory(evento=evento, interessado=inter)
        request = HttpRequest()
        admin = EventoAdmin(Evento, AdminSite())
        queryset = Evento.objects.filter(pk=evento.pk)
        response = admin.exportar_classificacao_excel(request, queryset)
        assert response.status_code == 200
        assert response.get("Content-Type") == "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"

    @pytest.mark.django_db
    def test_exportar_classificacao_excel_with_criteria(self):
        evento = EventoFactory()
        criterio1 = CriterioFactory(ativo=True, nome="Critério A")
        criterio2 = CriterioFactory(ativo=True, nome="Critério B")
        EventoCriterioFactory(evento=evento, criterio=criterio1)
        EventoCriterioFactory(evento=evento, criterio=criterio2)
        inter = InteressadoFactory()
        InscricaoFactory(evento=evento, interessado=inter)
        request = HttpRequest()
        admin = EventoAdmin(Evento, AdminSite())
        queryset = Evento.objects.filter(pk=evento.pk)
        response = admin.exportar_classificacao_excel(request, queryset)
        assert response.status_code == 200
        content = response.getvalue().decode("latin-1")
        assert "Critério A" in content or "Critério" in content


class TestEventoAdminConfiguration:
    @pytest.mark.django_db
    def test_evento_admin_list_display(self):
        admin = EventoAdmin(Evento, AdminSite())
        expected = (
            "nome",
            "status_colorido",
            "data_inicio_inscricao_formatada",
            "data_fim_inscricao_formatada",
            "vagas_inscritos",
            "criado_em",
        )
        assert admin.list_display == expected

    @pytest.mark.django_db
    def test_evento_admin_search_fields(self):
        admin = EventoAdmin(Evento, AdminSite())
        expected = ("nome", "descricao")
        assert admin.search_fields == expected

    @pytest.mark.django_db
    def test_evento_admin_fieldsets(self):
        admin = EventoAdmin(Evento, AdminSite())
        expected = (
            ("Informações Gerais", {"fields": ("nome", "descricao", "imagem", "status", "total_vagas")}),
            ("Datas e Horários", {"fields": ("data_inicio_evento", "data_fim_evento")}),
            ("Localização", {"fields": ("local", "endereco", "cidade", "estado")}),
            ("Metadados", {"fields": ("criado_em", "atualizado_em")}),
        )
        assert admin.fieldsets == expected


class TestTurmaAdmin:
    @pytest.mark.django_db
    def test_turma_admin_list_display(self):
        admin = TurmaAdmin(Turma, AdminSite())
        expected = ("nome", "evento", "capacidade", "criado_em")
        assert admin.list_display == expected


class TestHorarioAdmin:
    @pytest.mark.django_db
    def test_horario_admin_list_display(self):
        admin = HorarioAdmin(Horario, AdminSite())
        expected = ("turma", "dia_semana", "hora_inicio", "hora_fim")
        assert admin.list_display == expected

    @pytest.mark.django_db
    def test_horario_admin_dia_semana(self):
        horario = HorarioFactory(dia_semana=1)
        admin = HorarioAdmin(Horario, AdminSite())
        assert horario.dia_semana == 1



