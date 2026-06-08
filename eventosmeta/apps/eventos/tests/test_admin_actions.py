"""
Arquivo: test_admin_actions.py
Caminho: apps/eventos/tests/test_admin_actions.py
Finalidade: Testes para actions, métodos de display e inlines do admin.py
Data: 08/06/2026 - Criação com 12 testes
"""

import pytest
from django.test import TestCase
from django.contrib.auth import get_user_model
from django.utils import timezone
from datetime import datetime
from apps.eventos.models import Evento, Status
from apps.eventos.admin import EventoAdmin, StatusAdmin
from apps.eventos.tests.factories import EventoFactory, StatusFactory
from apps.selecao.tests.factories import InscricaoFactory
from django.contrib.admin.sites import AdminSite

User = get_user_model()

@pytest.mark.django_db
class TestAdminActions(TestCase):
    def setUp(self):
        self.site = AdminSite()
        self.evento_admin = EventoAdmin(Evento, self.site)
        self.status_admin = StatusAdmin(Status, self.site)

    def test_cor_visual_retorna_html_com_cor(self):
        status = StatusFactory(cor="#FF0000")
        result = self.status_admin.cor_visual(status)
        assert "#FF0000" in result and "span" in result

    def test_vagas_inscritos_cor_vermelho(self):
        evento = EventoFactory(total_vagas=100)
        InscricaoFactory.create_batch(70, evento=evento)
        result = self.evento_admin.vagas_inscritos(evento)
        assert "#dc3545" in result

    def test_vagas_inscritos_cor_laranja(self):
        evento = EventoFactory(total_vagas=100)
        InscricaoFactory.create_batch(90, evento=evento)
        result = self.evento_admin.vagas_inscritos(evento)
        assert "#ffc107" in result

    def test_vagas_inscritos_cor_verde(self):
        evento = EventoFactory(total_vagas=100)
        InscricaoFactory.create_batch(110, evento=evento)
        result = self.evento_admin.vagas_inscritos(evento)
        assert "#28a745" in result

    def test_data_inicio_inscricao_formatada(self):
        evento = EventoFactory(data_inicio_inscricao=timezone.make_aware(datetime(2026, 6, 8)))
        result = self.evento_admin.data_inicio_inscricao_formatada(evento)
        assert "08/06/2026" in result

    def test_data_fim_inscricao_formatada(self):
        evento = EventoFactory(data_fim_inscricao=timezone.make_aware(datetime(2026, 6, 13)))
        result = self.evento_admin.data_fim_inscricao_formatada(evento)
        assert "13/06/2026" in result

    def test_data_inicio_evento_formatada(self):
        evento = EventoFactory(data_inicio_evento=timezone.make_aware(datetime(2026, 7, 1)))
        result = self.evento_admin.data_inicio_evento_formatada(evento)
        assert "01/07/2026" in result

    def test_data_fim_evento_formatada(self):
        evento = EventoFactory(data_fim_evento=timezone.make_aware(datetime(2026, 7, 5)))
        result = self.evento_admin.data_fim_evento_formatada(evento)
        assert "05/07/2026" in result

    def test_classificar_inscricoes_action_existe(self):
        assert 'classificar_inscricoes' in self.evento_admin.actions

    def test_desfazer_classificacao_action_existe(self):
        assert 'desfazer_classificacao' in self.evento_admin.actions

    def test_exportar_classificacao_excel_action_existe(self):
        assert 'exportar_classificacao_excel' in self.evento_admin.actions

    def test_status_admin_list_display(self):
        assert all(item in self.status_admin.list_display for item in ['nome', 'cor_visual', 'ordem'])


        








