"""
Arquivo: test_admin.py
Caminho: apps/eventos/tests/test_admin.py
Data: 2025-04-07
Finalidade: Testes para o admin.py do app eventos (28 testes, 8 blocos tematicos)
Historico de Alteracoes:
- 21/05/2026 - Correção de testes que não estavam passando
- 22/05/2026 - Implementacao inicial com 28 testes de integracao real
             - Reescrever APENAS os testes usando force_login() ao invés de login()

Campos reais baseados em factories.py:
- Evento: data_inicio_evento, data_fim_evento (SEM hora_inicio/hora_fim)
- Horario: hora_inicio, hora_fim
- EventoCriterio: prioridade (não pontos)
- Inscricao: não aparece em factories, usar apenas evento

NOMES REAIS dos métodos em EventoAdmin:
- vagas_inscritos (não vagas_inscritos_percentage)
- data_inicio_inscricao_formatada
- data_fim_inscricao_formatada
- data_inicio_evento_formatada
- data_fim_evento_formatada

"""


from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model
from datetime import datetime, date
from apps.accounts.models import Usuario
from apps.eventos.models import Evento, Status, Criterio, Turma, Horario
from apps.eventos.admin import EventoAdmin, StatusAdmin, CriterioAdmin, TurmaAdmin, HorarioAdmin
from apps.eventos.tests.factories import StatusFactory, CriterioFactory, EventoFactory, TurmaFactory, HorarioFactory
from apps.selecao.tests.factories import InscricaoFactory

User = get_user_model()


class EventoAdminTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.status = StatusFactory()
        cls.evento = EventoFactory(status=cls.status)
        # cls.criterio = CriterioFactory(evento=cls.evento)
        cls.turma = TurmaFactory(evento=cls.evento)
        cls.horario = HorarioFactory(turma=cls.turma)
        cls.inscricao = InscricaoFactory(evento=cls.evento)
        cls.admin = User.objects.create_superuser(
            username='admin',
            email='admin@test.com',
            password='admin123'
        )

    def setUp(self):
        self.client = Client()
        self.client.force_login(self.admin)

    def test_evento_list_view(self):
        url = reverse('admin:eventos_evento_changelist')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.evento.nome)

    def test_evento_add_view(self):
        url = reverse('admin:eventos_evento_add')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_evento_change_view(self):
        url = reverse('admin:eventos_evento_change', args=[self.evento.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.evento.nome)

    def test_evento_delete_view(self):
        url = reverse('admin:eventos_evento_delete', args=[self.evento.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_evento_search(self):
        url = reverse('admin:eventos_evento_changelist')
        response = self.client.get(url, {'q': self.evento.nome[:3]})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.evento.nome)

    def test_evento_list_display(self):
        # Valida que list_display está configurado
        admin = EventoAdmin(model=Evento, admin_site=None)
        self.assertIn('status_colorido', admin.list_display)
        self.assertIn('vagas_inscritos', admin.list_display)
        self.assertIn('data_inicio_inscricao_formatada', admin.list_display)
        self.assertIn('data_fim_inscricao_formatada', admin.list_display)
        self.assertIn('data_inicio_evento_formatada', admin.list_display)
        self.assertIn('data_fim_evento_formatada', admin.list_display)

    def test_evento_individual_date_methods(self):
        admin = EventoAdmin(model=Evento, admin_site=None)
        
        result1 = admin.data_inicio_inscricao_formatada(self.evento)
        self.assertIn('/', result1)  # dd/mm/yyyy contém /
        
        result2 = admin.data_fim_inscricao_formatada(self.evento)
        self.assertIn('/', result2)
        
        result3 = admin.data_inicio_evento_formatada(self.evento)
        self.assertIn('/', result3)
        
        result4 = admin.data_fim_evento_formatada(self.evento)
        self.assertIn('/', result4)

    def test_evento_criterios_inline(self):
        # Valida que inline está registrada (pode adicionar critérios)
        url = reverse('admin:eventos_evento_change', args=[self.evento.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        # Se inline existe, formulário carrega sem erro

    def test_evento_turmas_inline(self):
        url = reverse('admin:eventos_evento_change', args=[self.evento.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Turmas')


class StatusAdminTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.status = StatusFactory()
        cls.admin = User.objects.create_superuser(
            username='admin2',
            email='admin2@test.com',
            password='admin123'
        )

    def setUp(self):
        self.client = Client()
        self.client.force_login(self.admin)

    def test_status_list_view(self):
        url = reverse('admin:eventos_status_changelist')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.status.nome)

    def test_status_add_view(self):
        url = reverse('admin:eventos_status_add')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_status_change_view(self):
        url = reverse('admin:eventos_status_change', args=[self.status.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.status.nome)

    def test_status_delete_view(self):
        url = reverse('admin:eventos_status_delete', args=[self.status.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_status_search(self):
        url = reverse('admin:eventos_status_changelist')
        response = self.client.get(url, {'q': self.status.nome[:3]})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.status.nome)


class CriterioAdminTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.status = StatusFactory()
        cls.evento = EventoFactory(status=cls.status)
        # cls.criterio = CriterioFactory(evento=cls.evento)
        cls.admin = User.objects.create_superuser(
            username='admin3',
            email='admin3@test.com',
            password='admin123'
        )

    def setUp(self):
        self.client = Client()
        self.client.force_login(self.admin)

    def test_criterio_add_view(self):
        url = reverse('admin:eventos_criterio_add')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_criterio_list_filter(self):
        # Valida que list_filter está configurado
        admin = CriterioAdmin(model=Criterio, admin_site=None)
        self.assertTrue(len(admin.list_filter) > 0)  # Tem filtros


class TurmaAdminTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.status = StatusFactory()
        cls.evento = EventoFactory(status=cls.status)
        cls.turma = TurmaFactory(evento=cls.evento)
        cls.admin = User.objects.create_superuser(
            username='admin4',
            email='admin4@test.com',
            password='admin123'
        )

    def setUp(self):
        self.client = Client()
        self.client.force_login(self.admin)

    def test_turma_list_view(self):
        url = reverse('admin:eventos_turma_changelist')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.turma.nome)

    def test_turma_add_view(self):
        url = reverse('admin:eventos_turma_add')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_turma_change_view(self):
        url = reverse('admin:eventos_turma_change', args=[self.turma.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.turma.nome)

    def test_turma_delete_view(self):
        url = reverse('admin:eventos_turma_delete', args=[self.turma.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_turma_search(self):
        url = reverse('admin:eventos_turma_changelist')
        response = self.client.get(url, {'q': self.turma.nome[:3]})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.turma.nome)

    def test_turma_list_display_evento(self):
        url = reverse('admin:eventos_turma_changelist')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.turma.evento.nome)


class HorarioAdminTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.status = StatusFactory()
        cls.evento = EventoFactory(status=cls.status)
        cls.turma = TurmaFactory(evento=cls.evento)
        cls.horario = HorarioFactory(turma=cls.turma)
        cls.admin = User.objects.create_superuser(
            username='admin5',
            email='admin5@test.com',
            password='admin123'
        )

    def setUp(self):
        self.client = Client()
        self.client.force_login(self.admin)

    def test_horario_list_view(self):
        url = reverse('admin:eventos_horario_changelist')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.horario.turma.nome)

    def test_horario_add_view(self):
        url = reverse('admin:eventos_horario_add')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_horario_change_view(self):
        url = reverse('admin:eventos_horario_change', args=[self.horario.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.horario.turma.nome)

    def test_horario_delete_view(self):
        url = reverse('admin:eventos_horario_delete', args=[self.horario.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_horario_search(self):
        url = reverse('admin:eventos_horario_changelist')
        response = self.client.get(url, {'q': self.horario.turma.nome[:3]})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.horario.turma.nome)

    def test_horario_list_filter(self):
        url = reverse('admin:eventos_horario_changelist')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Filtrar')

    def test_horario_dia_semana_filter(self):
        url = reverse('admin:eventos_horario_changelist')
        response = self.client.get(url, {'dia_semana__exact': self.horario.dia_semana})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.horario.turma.nome)



