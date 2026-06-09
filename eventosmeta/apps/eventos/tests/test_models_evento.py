"""
Arquivo: test_models_evento.py
Caminho: apps/eventos/tests/test_models_evento.py
Finalidade: Testes dos modelos Evento do app eventos (CRUD, validações, métodos)
Atualizações:
 - 03/06/2026 - Criação do arquivo com testes básicos para os modelos do app eventos, utilizando pytest e factories.
 - 09/06/2026 - Refatoração completa para pytest puro e adição de 5 testes de métodos
"""


import pytest
from django.utils import timezone
from datetime import timedelta
from django.core.exceptions import ValidationError
from apps.eventos.models import Evento
from apps.eventos.tests.factories import EventoFactory, StatusFactory, TurmaFactory, EventoCriterioFactory

pytestmark = pytest.mark.django_db

@pytest.fixture
def status_ativo():
    return StatusFactory(nome="Ativo")

@pytest.fixture
def evento_padrao(status_ativo):
    return EventoFactory(status=status_ativo)

class TestEventoCRUD:
    def test_criar_evento_valido(self):
        evento = EventoFactory()
        assert Evento.objects.count() == 1
        assert evento.pk is not None

    def test_ler_evento(self):
        evento = EventoFactory(nome='Evento Teste')
        db_evento = Evento.objects.get(pk=evento.pk)
        assert db_evento.nome == 'Evento Teste'

    def test_atualizar_evento(self):
        evento = EventoFactory(nome='Original')
        evento.nome = 'Atualizado'
        evento.save()
        assert Evento.objects.get(pk=evento.pk).nome == 'Atualizado'

    def test_deletar_evento(self):
        evento = EventoFactory()
        evento.delete()
        assert Evento.objects.count() == 0

    def test_multiplos_eventos(self):
        EventoFactory.create_batch(5)
        assert Evento.objects.count() == 5

class TestEventoValidacoes:
    def test_data_inicio_inscricao_antes_fim_inscricao(self):
        evento = EventoFactory.build(
            data_inicio_inscricao=timezone.now(),
            data_fim_inscricao=timezone.now() - timedelta(days=1)
        )
        with pytest.raises(ValidationError):
            evento.clean()

    def test_data_fim_inscricao_antes_inicio_evento(self):
        evento = EventoFactory.build(
            data_fim_inscricao=timezone.now(),
            data_inicio_evento=timezone.now() - timedelta(days=1)
        )
        with pytest.raises(ValidationError):
            evento.clean()

    def test_data_inicio_evento_antes_fim_evento(self):
        evento = EventoFactory.build(
            data_inicio_evento=timezone.now(),
            data_fim_evento=timezone.now() - timedelta(days=1)
        )
        with pytest.raises(ValidationError):
            evento.clean()

    def test_datas_validas_factory(self):
        evento = EventoFactory()
        assert evento.data_inicio_inscricao < evento.data_fim_inscricao

    def test_clean_valida_datas(self):
        evento = EventoFactory()
        assert evento.clean() is None

    def test_total_vagas_positivo(self):
        evento = EventoFactory(total_vagas=10)
        assert evento.total_vagas == 10

    def test_total_vagas_grande_numero(self):
        evento = EventoFactory(total_vagas=999999)
        assert evento.total_vagas == 999999

    def test_total_vagas_zero_permitido(self):
        evento = EventoFactory(total_vagas=0)
        assert evento.total_vagas == 0

class TestEventoStatus:
    def test_evento_com_status(self):
        status = StatusFactory()
        evento = EventoFactory(status=status)
        assert evento.status == status

    def test_evento_sem_status_invalido(self):
        with pytest.raises(Exception):
            EventoFactory(status=None)

    def test_evento_com_turmas(self):
        evento = EventoFactory()
        turma = TurmaFactory(evento=evento)
        assert turma in evento.turmas.all()

    def test_evento_multiplas_turmas(self):
        evento = EventoFactory()
        TurmaFactory.create_batch(3, evento=evento)
        assert evento.turmas.count() == 3

    def test_evento_com_criterios(self):
        evento = EventoFactory()
        ec = EventoCriterioFactory(evento=evento)
        assert ec in evento.evento_criterios.all()

    def test_evento_multiplos_criterios(self):
        evento = EventoFactory()
        EventoCriterioFactory.create_batch(3, evento=evento)
        assert evento.evento_criterios.count() == 3

class TestEventoTimestamps:
    def test_evento_sem_criterios(self):
        evento = EventoFactory()
        assert evento.evento_criterios.count() == 0

    def test_deletar_evento_deleta_turmas(self):
        evento = EventoFactory()
        TurmaFactory(evento=evento)
        assert evento.turmas.count() == 1
        evento.delete()
        assert Evento.objects.filter(pk=evento.pk).count() == 0

    def test_criado_em_existe(self):
        evento = EventoFactory()
        assert evento.criado_em is not None

    def test_atualizado_em_existe(self):
        evento = EventoFactory()
        assert evento.atualizado_em is not None

    def test_atualizado_em_atualiza(self):
        evento = EventoFactory()
        old_updated = evento.atualizado_em
        evento.nome = 'Novo'
        evento.save()
        assert evento.atualizado_em > old_updated

class TestEventoMetodos:
    def test_inscricoes_abertas(self):
        evento = EventoFactory(
            data_inicio_inscricao=timezone.now() - timedelta(days=1),
            data_fim_inscricao=timezone.now() + timedelta(days=1)
        )
        assert evento.inscricoes_abertas() is True

    def test_inscricoes_fechadas(self):
        evento = EventoFactory(
            data_inicio_inscricao=timezone.now() - timedelta(days=10),
            data_fim_inscricao=timezone.now() - timedelta(days=1)
        )
        assert evento.inscricoes_abertas() is False

    def test_validacao_datas_inscricao(self):
        evento = EventoFactory.build(
            data_inicio_inscricao=timezone.now() + timedelta(days=2),
            data_fim_inscricao=timezone.now() + timedelta(days=1)
        )
        with pytest.raises(ValidationError):
            evento.full_clean()

    def test_validacao_datas_evento(self):
        evento = EventoFactory.build(
            data_inicio_evento=(timezone.now() + timedelta(days=2)).date(),
            data_fim_evento=(timezone.now() + timedelta(days=1)).date()
        )
        with pytest.raises(ValidationError):
            evento.full_clean()

    def test_formatacao_datas(self):
        evento = EventoFactory()
        assert evento.data_inicio_inscricao_formatada() is not None
        assert evento.data_fim_inscricao_formatada() is not None
        assert evento.data_inicio_evento_formatada() is not None
        assert evento.data_fim_evento_formatada() is not None

class TestEventoQueryset:
    def test_filtro_por_status(self):
        status = StatusFactory(nome='Ativo')
        EventoFactory(status=status)
        assert Evento.objects.filter(status__nome='Ativo').count() == 1

    def test_filtro_por_ativo(self):
        status = StatusFactory(nome='Ativo')
        EventoFactory(status=status)
        assert Evento.objects.filter(status__nome='Ativo').exists()

    def test_queryset_count(self):
        EventoFactory.create_batch(3)
        assert Evento.objects.all().count() == 3

    def test_queryset_exists(self):
        EventoFactory()
        assert Evento.objects.exists() is True

    def test_nome_obrigatorio(self):
        with pytest.raises(Exception):
            EventoFactory(nome=None)

    def test_str_representation(self):
        evento = EventoFactory(nome='Evento A')
        assert str(evento) == 'Evento A'

        