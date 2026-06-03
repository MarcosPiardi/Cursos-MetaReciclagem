"""
Arquivo: test_models_turma.py
caminho: apps/eventos/tests/test_models_turma.py
Finalidade: Testes dos modelos do app eventos, focando na model Turma.
Atualizações:   
 - 03/06/2026 - Criação do arquivo com 22 testes básicos para o modelo Turma do app eventos, utilizando pytest e factories.
"""

import pytest
from django.core.exceptions import ValidationError
from django.utils import timezone
from datetime import timedelta
from apps.eventos.models import Turma, Evento, Horario
from apps.eventos.tests.factories import TurmaFactory, EventoFactory, HorarioFactory

@pytest.mark.django_db
class TestTurmaModel:

    def test_criar_turma_valida(self):
        turma = TurmaFactory()
        assert turma.pk is not None

    def test_ler_turma(self):
        turma = TurmaFactory(nome="Turma A")
        db_turma = Turma.objects.get(pk=turma.pk)
        assert db_turma.nome == "Turma A"

    def test_atualizar_turma(self):
        turma = TurmaFactory(nome="Antigo")
        turma.nome = "Novo"
        turma.save()
        assert Turma.objects.get(pk=turma.pk).nome == "Novo"

    def test_deletar_turma(self):
        turma = TurmaFactory()
        turma.delete()
        assert Turma.objects.count() == 0

    def test_multiplas_turmas(self):
        TurmaFactory.create_batch(5)
        assert Turma.objects.count() == 5

    def test_datas_validas_factory(self):
        turma = TurmaFactory()
        assert turma.data_inicio < turma.data_fim

    def test_capacidade_positiva(self):
        turma = TurmaFactory(capacidade=10)
        assert turma.capacidade > 0

    def test_capacidade_grande_numero(self):
        turma = TurmaFactory(capacidade=9999)
        assert turma.capacidade == 9999

    def test_capacidade_zero_permitido(self):
        turma = TurmaFactory(capacidade=0)
        assert turma.capacidade == 0

    def test_turma_com_evento(self):
        evento = EventoFactory()
        turma = TurmaFactory(evento=evento)
        assert turma.evento == evento

    def test_turma_sem_evento_invalido(self):
        turma = Turma(nome="Sem Evento", capacidade=10)
        with pytest.raises(Exception):
            turma.save()

    def test_turma_com_horarios(self):
        turma = TurmaFactory()
        HorarioFactory(turma=turma)
        assert turma.horarios.count() == 1

    def test_turma_multiplos_horarios(self):
        turma = TurmaFactory()
        HorarioFactory.create_batch(3, turma=turma)
        assert turma.horarios.count() == 3

    def test_deletar_turma_deleta_horarios(self):
        turma = TurmaFactory()
        HorarioFactory(turma=turma)
        turma.delete()
        assert Horario.objects.count() == 0

    def test_criado_em_existe(self):
        turma = TurmaFactory()
        assert turma.criado_em is not None

    def test_atualizado_em_atualiza(self):
        turma = TurmaFactory()
        old_updated = turma.atualizado_em
        turma.nome = "Update"
        turma.save()
        assert turma.atualizado_em > old_updated

    def test_str_representation(self):
        turma = TurmaFactory(nome="Python")
        assert "Python" in str(turma)

    def test_nome_obrigatorio(self):
        turma = Turma(nome="", evento=EventoFactory())
        with pytest.raises(ValidationError):
            turma.full_clean()

    def test_filtro_por_evento(self):
        evento = EventoFactory()
        TurmaFactory(evento=evento)
        assert Turma.objects.filter(evento=evento).count() == 1

    def test_filtro_por_turno(self):
        TurmaFactory(turno="Matutino")
        assert Turma.objects.filter(turno="Matutino").count() == 1

    def test_queryset_count(self):
        TurmaFactory.create_batch(10)
        assert Turma.objects.all().count() == 10


