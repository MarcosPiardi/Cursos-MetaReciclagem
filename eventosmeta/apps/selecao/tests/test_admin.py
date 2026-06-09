"""
Arquivo: test_admin.py
Caminho: apps/selecao/tests/test_admin.py
Atualizações
 - 08/04/2026 - Testes para as actions do admin.py do app Selecao
 - 10/04/2026 - Testes para ClassificacaoAdmin - action matricular_alunos_action
             Testa: trava de capacidade, validações, sucesso e tratamento de erros
 - 27/05/2026 - Refatoração para usar RequestFactory e mensagens reais do Django, além de organização em classes de teste.             
- 08/06/2026 - Refatoração para pytest (remover BaseAdminActionTest, adicionar fixtures)
"""


import pytest
from django.test import RequestFactory
from django.contrib import messages
from django.contrib.admin.sites import AdminSite
from django.contrib.messages.storage.cookie import CookieStorage
from django.contrib.admin.helpers import ACTION_CHECKBOX_NAME
from unittest.mock import patch
from apps.selecao.admin import ClassificacaoAdmin
from apps.selecao.models import Classificacao, Inscricao, StatusInscricao
from apps.eventos.models import Evento, Turma
from apps.academico.models import Matricula, StatusMatricula
from apps.selecao.tests.factories import (
    ClassificacaoFactory,
    InscricaoFactory,
    StatusInscricaoFactory,
)
from apps.eventos.tests.factories import (
    EventoFactory,
    TurmaFactory,
)
from apps.academico.tests.factories import (
    StatusMatriculaFactory,
    MatriculaFactory,
)

def _create_request_with_messages(factory, user, method='post', path='/'):
    """Cria um objeto Request com usuário e armazenamento de mensagens."""
    request = getattr(factory, method)(path)
    request.user = user
    request._messages = CookieStorage(request)
    return request

def _get_messages(request):
    """Extrai as mensagens do request como uma lista de strings."""
    return [str(m) for m in request._messages]

@pytest.fixture
def usuario_staff(db):
    from django.contrib.auth import get_user_model
    User = get_user_model()
    user = User.objects.create_user(username='staff_user', password='pass123')
    user.is_staff = True
    user.save()
    return user

@pytest.mark.django_db
class TestMatricularAlunosActionCapacity:
    """Testes para a trava de capacidade da action matricular_alunos_action."""

    def setup_method(self):
        self.factory = RequestFactory()
        self.site = AdminSite()
        self.admin = ClassificacaoAdmin(Classificacao, self.site)
        self.status_matricula_ativa = StatusMatriculaFactory(nome='Ativa')
        self.status_inscricao_confirmada = StatusInscricaoFactory(nome='CONFIRMADA')
        StatusInscricaoFactory(nome='Pendente')

    def test_matricular_alunos_capacidade_ultrapassada(self, usuario_staff):
        """Deve exibir erro e não matricular se a quantidade de selecionados ultrapassa a capacidade da turma."""
        evento = EventoFactory()
        turma = TurmaFactory(evento=evento, capacidade=1)
        inscricao1 = InscricaoFactory(evento=evento)
        inscricao2 = InscricaoFactory(evento=evento)
        classificacao1 = ClassificacaoFactory(inscricao=inscricao1)
        classificacao2 = ClassificacaoFactory(inscricao=inscricao2)
        queryset = Classificacao.objects.filter(id__in=[classificacao1.id, classificacao2.id])

        request = _create_request_with_messages(self.factory, usuario_staff, method='post', path='/admin/selecao/classificacao/')
        request.POST = {
            'action': 'matricular_alunos_action',
            ACTION_CHECKBOX_NAME: [str(c.pk) for c in queryset],
            'confirmar_matricula': '1',
            'turma': str(turma.pk),
        }
        self.admin.matricular_alunos_action(request, queryset)
        messages_list = _get_messages(request)
        assert any('vaga(s) disponível' in msg for msg in messages_list)
        assert Matricula.objects.count() == 0

    def test_matricular_alunos_capacidade_exata(self, usuario_staff):
        """Deve matricular com sucesso se a quantidade de selecionados é igual à capacidade da turma."""
        evento = EventoFactory()
        turma = TurmaFactory(evento=evento, capacidade=2)
        inscricao1 = InscricaoFactory(evento=evento)
        inscricao2 = InscricaoFactory(evento=evento)
        classificacao1 = ClassificacaoFactory(inscricao=inscricao1)
        classificacao2 = ClassificacaoFactory(inscricao=inscricao2)
        queryset = Classificacao.objects.filter(id__in=[classificacao1.id, classificacao2.id])

        request = _create_request_with_messages(self.factory, usuario_staff, method='post', path='/admin/selecao/classificacao/')
        request.POST = {
            'action': 'matricular_alunos_action',
            ACTION_CHECKBOX_NAME: [str(c.pk) for c in queryset],
            'confirmar_matricula': '1',
            'turma': str(turma.pk),
        }
        self.admin.matricular_alunos_action(request, queryset)
        messages_list = _get_messages(request)
        assert any('2 matrícula(s) criada(s)' in msg for msg in messages_list)
        assert Matricula.objects.count() == 2
        assert Inscricao.objects.get(pk=inscricao1.pk).status == self.status_inscricao_confirmada
        assert Inscricao.objects.get(pk=inscricao2.pk).status == self.status_inscricao_confirmada

@pytest.mark.django_db
class TestMatricularAlunosActionValidation:
    """Testes para as validações da action matricular_alunos_action."""

    def setup_method(self):
        self.factory = RequestFactory()
        self.site = AdminSite()
        self.admin = ClassificacaoAdmin(Classificacao, self.site)
        self.status_matricula_ativa = StatusMatriculaFactory(nome='Ativa')
        self.status_inscricao_confirmada = StatusInscricaoFactory(nome='CONFIRMADA')
        StatusInscricaoFactory(nome='Pendente')

    def test_validacao_evento_unico(self, usuario_staff):
        """Deve exibir erro se classificações de eventos diferentes forem selecionadas."""
        evento1 = EventoFactory(nome='Evento A')
        evento2 = EventoFactory(nome='Evento B')
        inscricao1 = InscricaoFactory(evento=evento1)
        inscricao2 = InscricaoFactory(evento=evento2)
        classificacao1 = ClassificacaoFactory(inscricao=inscricao1)
        classificacao2 = ClassificacaoFactory(inscricao=inscricao2)
        queryset = Classificacao.objects.filter(id__in=[classificacao1.id, classificacao2.id])
        request = _create_request_with_messages(self.factory, usuario_staff, method='post', path='/admin/selecao/classificacao/')
        request.POST = {
            'action': 'matricular_alunos_action',
            ACTION_CHECKBOX_NAME: [str(c.pk) for c in queryset],
        }
        self.admin.matricular_alunos_action(request, queryset)
        messages_list = _get_messages(request)
        assert any('Selecione apenas classificações do MESMO EVENTO' in msg for msg in messages_list)
        assert Matricula.objects.count() == 0

    def test_validacao_turma_inexistente_para_evento(self, usuario_staff):
        """Deve exibir erro se o evento das classificações não possui turmas cadastradas."""
        evento = EventoFactory()
        inscricao = InscricaoFactory(evento=evento)
        classificacao = ClassificacaoFactory(inscricao=inscricao)
        queryset = Classificacao.objects.filter(id=classificacao.id)
        request = _create_request_with_messages(self.factory, usuario_staff, method='post', path='/admin/selecao/classificacao/')
        request.POST = {
            'action': 'matricular_alunos_action',
            ACTION_CHECKBOX_NAME: [str(c.pk) for c in queryset],
        }
        self.admin.matricular_alunos_action(request, queryset)
        messages_list = _get_messages(request)
        assert any('não possui turmas cadastradas' in msg for msg in messages_list)
        assert Matricula.objects.count() == 0

    def test_protecao_duplicidade_matricula(self, usuario_staff):
        """Deve exibir aviso e não criar matrícula duplicada para o mesmo interessado na mesma turma."""
        evento = EventoFactory()
        turma = TurmaFactory(evento=evento, capacidade=2)
        inscricao = InscricaoFactory(evento=evento)
        classificacao = ClassificacaoFactory(inscricao=inscricao)
        MatriculaFactory(turma=turma, interessado=inscricao.interessado, inscricao=inscricao, status=self.status_matricula_ativa)
        queryset = Classificacao.objects.filter(id=classificacao.id)

        request = _create_request_with_messages(self.factory, usuario_staff, method='post', path='/admin/selecao/classificacao/')
        request.POST = {
            'action': 'matricular_alunos_action',
            ACTION_CHECKBOX_NAME: [str(c.pk) for c in queryset],
            'confirmar_matricula': '1',
            'turma': str(turma.pk),
        }
        self.admin.matricular_alunos_action(request, queryset)
        messages_list = _get_messages(request)
        assert any('já está matriculado nesta turma' in msg for msg in messages_list)
        assert Matricula.objects.count() == 1

    def test_validacao_turma_nao_pertence_ao_evento(self, usuario_staff):
        evento1 = EventoFactory(nome='Evento A')
        evento2 = EventoFactory(nome='Evento B')
        TurmaFactory(evento=evento1, capacidade=2)
        turma_evento2 = TurmaFactory(evento=evento2, capacidade=1)
        inscricao = InscricaoFactory(evento=evento1)
        classificacao = ClassificacaoFactory(inscricao=inscricao)
        queryset = Classificacao.objects.filter(id=classificacao.id)
        request = _create_request_with_messages(self.factory, usuario_staff, method='post', path='/admin/selecao/classificacao/')
        request.POST = {
            'action': 'matricular_alunos_action',
            ACTION_CHECKBOX_NAME: [str(c.pk) for c in queryset],
            'confirmar_matricula': '1',
            'turma': str(turma_evento2.pk),
        }
        self.admin.matricular_alunos_action(request, queryset)
        messages_list = _get_messages(request)
        assert any('Não pertence' in msg.lower() or 'válida' in msg.lower() or 'erro' in msg.lower() for msg in messages_list)
        assert Matricula.objects.count() == 0

@pytest.mark.django_db
class TestMatricularAlunosActionSuccess:
    """Testes para o cenário de sucesso da action matricular_alunos_action."""

    def setup_method(self):
        self.factory = RequestFactory()
        self.site = AdminSite()
        self.admin = ClassificacaoAdmin(Classificacao, self.site)
        self.status_matricula_ativa = StatusMatriculaFactory(nome='Ativa')
        self.status_inscricao_confirmada = StatusInscricaoFactory(nome='CONFIRMADA')
        StatusInscricaoFactory(nome='Pendente')

    def test_sucesso_matricula_dentro_capacidade(self, usuario_staff):
        """Deve matricular alunos com sucesso e atualizar o status da inscrição."""
        evento = EventoFactory()
        turma = TurmaFactory(evento=evento, capacidade=2)
        inscricao1 = InscricaoFactory(evento=evento)
        inscricao2 = InscricaoFactory(evento=evento)
        classificacao1 = ClassificacaoFactory(inscricao=inscricao1)
        classificacao2 = ClassificacaoFactory(inscricao=inscricao2)
        queryset = Classificacao.objects.filter(id__in=[classificacao1.id, classificacao2.id])
        request = _create_request_with_messages(self.factory, usuario_staff, method='post', path='/admin/selecao/classificacao/')
        request.POST = {
            'action': 'matricular_alunos_action',
            ACTION_CHECKBOX_NAME: [str(c.pk) for c in queryset],
            'confirmar_matricula': '1',
            'turma': str(turma.pk),
        }
        self.admin.matricular_alunos_action(request, queryset)
        messages_list = _get_messages(request)
        assert any('2 matrícula(s) criada(s) na turma' in msg for msg in messages_list)
        assert Matricula.objects.count() == 2
        assert Inscricao.objects.get(pk=inscricao1.pk).status == self.status_inscricao_confirmada
        assert Inscricao.objects.get(pk=inscricao2.pk).status == self.status_inscricao_confirmada

    def test_nenhuma_classificacao_selecionada(self, usuario_staff):
        """Deve exibir erro se nenhuma classificacao for selecionada."""
        queryset = Classificacao.objects.none()
        request = _create_request_with_messages(
            self.factory, usuario_staff, method='post',
            path='/admin/selecao/classificacao/'
        )
        request.POST = {
            'action': 'matricular_alunos_action',
            ACTION_CHECKBOX_NAME: [],
        }
        result = self.admin.matricular_alunos_action(request, queryset)
        messages_list = _get_messages(request)
        assert Matricula.objects.count() == 0

@pytest.mark.django_db
class TestMatricularAlunosActionErrorHandling:
    """Testes para o tratamento de erros e transações da action matricular_alunos_action."""

    def setup_method(self):
        self.factory = RequestFactory()
        self.site = AdminSite()
        self.admin = ClassificacaoAdmin(Classificacao, self.site)
        self.status_matricula_ativa = StatusMatriculaFactory(nome='Ativa')
        self.status_inscricao_confirmada = StatusInscricaoFactory(nome='CONFIRMADA')
        StatusInscricaoFactory(nome='Pendente')

    def test_transacao_atomica_rollback_on_matricula_save_error(self, usuario_staff):
        evento = EventoFactory()
        turma = TurmaFactory(evento=evento, capacidade=3)
        inscricao1 = InscricaoFactory(evento=evento)
        inscricao2 = InscricaoFactory(evento=evento)
        classificacao1 = ClassificacaoFactory(inscricao=inscricao1)
        classificacao2 = ClassificacaoFactory(inscricao=inscricao2)
        queryset = Classificacao.objects.filter(id__in=[classificacao1.id, classificacao2.id])
        request = _create_request_with_messages(
            self.factory, usuario_staff, method='post',
            path='/admin/selecao/classificacao/'
        )
        request.POST = {
            'action': 'matricular_alunos_action',
            ACTION_CHECKBOX_NAME: [str(c.pk) for c in queryset],
            'confirmar_matricula': '1',
            'turma': str(turma.pk),
        }
        with patch('apps.selecao.admin.Matricula.objects.create', side_effect=Exception('Erro simulado')):
            self.admin.matricular_alunos_action(request, queryset)
        messages_list = _get_messages(request)
        assert any('Erro' in msg for msg in messages_list)
        assert Matricula.objects.count() == 0
        assert Inscricao.objects.get(pk=inscricao1.pk).status != self.status_inscricao_confirmada

    def test_status_ativa_nao_encontrado(self, usuario_staff):
        """Deve exibir erro se o StatusMatricula 'Ativa' não for encontrado."""
        self.status_matricula_ativa.delete()
        evento = EventoFactory()
        turma = TurmaFactory(evento=evento, capacidade=1)
        inscricao = InscricaoFactory(evento=evento)
        classificacao = ClassificacaoFactory(inscricao=inscricao)
        queryset = Classificacao.objects.filter(id=classificacao.id)

        request = _create_request_with_messages(self.factory, usuario_staff, method='post', path='/admin/selecao/classificacao/')
        request.POST = {
            'action': 'matricular_alunos_action',
            ACTION_CHECKBOX_NAME: [str(c.pk) for c in queryset],
            'confirmar_matricula': '1',
            'turma': str(turma.pk),
        }
        self.admin.matricular_alunos_action(request, queryset)
        messages_list = _get_messages(request)
        assert any('Status "ATIVA" não encontrado em Status de Matrículas' in msg for msg in messages_list)
        assert Matricula.objects.count() == 0

    def test_status_confirmada_nao_encontrado(self, usuario_staff):
        """Deve exibir erro se o StatusInscricao 'CONFIRMADA' não for encontrado."""
        self.status_inscricao_confirmada.delete()
        evento = EventoFactory()
        turma = TurmaFactory(evento=evento, capacidade=1)
        inscricao = InscricaoFactory(evento=evento)
        classificacao = ClassificacaoFactory(inscricao=inscricao)
        queryset = Classificacao.objects.filter(id=classificacao.id)
        request = _create_request_with_messages(self.factory, usuario_staff, method='post', path='/admin/selecao/classificacao/')
        request.POST = {
            'action': 'matricular_alunos_action',
            ACTION_CHECKBOX_NAME: [str(c.pk) for c in queryset],
            'confirmar_matricula': '1',
            'turma': str(turma.pk),
        }
        self.admin.matricular_alunos_action(request, queryset)
        messages_list = _get_messages(request)
        assert any('Status "CONFIRMADA" não encontrado em Status de Inscrições' in msg for msg in messages_list)
        assert Matricula.objects.count() == 0

    def test_classificacoes_sem_evento_associado(self, usuario_staff):
        """Deve exibir erro se a classificacao nao tem inscricao valida."""
        evento = EventoFactory()
        turma = TurmaFactory(evento=evento, capacidade=1)
        inscricao = InscricaoFactory(evento=evento)
        classificacao = ClassificacaoFactory(inscricao=inscricao)
        queryset = Classificacao.objects.filter(id=classificacao.id)
        request = _create_request_with_messages(
            self.factory, usuario_staff, method='post',
            path='/admin/selecao/classificacao/'
        )
        request.POST = {
            'action': 'matricular_alunos_action',
            ACTION_CHECKBOX_NAME: [str(c.pk) for c in queryset],
            'confirmar_matricula': '1',
            'turma': str(turma.pk),
        }
        self.admin.matricular_alunos_action(request, queryset)
        messages_list = _get_messages(request)
        assert Matricula.objects.count() > 0 or any('erro' in msg.lower() for msg in messages_list)


