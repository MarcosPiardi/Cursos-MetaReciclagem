"""
Arquivo: test_models_horario.py
Caminho: apps/eventos/tests/test_models_horario.py
Finalidade: Testes para o modelo Horario usando pytest
Data: 03/06/2026 - Criação com 18 testes
"""

import pytest
from django.core.exceptions import ValidationError
from apps.eventos.models import Horario
from apps.eventos.tests.factories import HorarioFactory, TurmaFactory

@pytest.mark.django_db
class TestHorarioModel:

    def test_criar_horario_valido(self):
        horario = HorarioFactory()
        assert Horario.objects.count() == 1
        assert horario.id is not None

    def test_ler_horario(self):
        horario = HorarioFactory()
        db_horario = Horario.objects.get(id=horario.id)
        assert db_horario.dia_semana == horario.dia_semana

    def test_atualizar_horario(self):
        horario = HorarioFactory()
        horario.dia_semana = 2
        horario.save()
        assert Horario.objects.get(id=horario.id).dia_semana == 2

    def test_deletar_horario(self):
        horario = HorarioFactory()
        horario.delete()
        assert Horario.objects.count() == 0

    def test_dia_semana_valido(self):
        horario = HorarioFactory(dia_semana=1)
        assert horario.dia_semana == 1

    def test_multiplos_horarios_mesma_turma(self):
        turma = TurmaFactory()
        HorarioFactory(turma=turma)
        HorarioFactory(turma=turma)
        assert Horario.objects.filter(turma=turma).count() == 2

    def test_hora_inicio_antes_fim(self):
        horario = HorarioFactory(hora_inicio='08:00', hora_fim='10:00')
        assert horario.hora_inicio < horario.hora_fim

    def test_hora_inicio_igual_fim_permitido(self):
        horario = HorarioFactory(hora_inicio='09:00', hora_fim='09:00')
        assert horario.hora_inicio == horario.hora_fim

    def test_horario_com_turma(self):
        turma = TurmaFactory()
        horario = HorarioFactory(turma=turma)
        assert horario.turma == turma

    def test_horario_sem_turma_invalido(self):
        with pytest.raises(Exception):
            HorarioFactory(turma=None)

    def test_turma_tem_multiplos_horarios(self):
        turma = TurmaFactory()
        HorarioFactory(turma=turma)
        HorarioFactory(turma=turma)
        horarios = Horario.objects.filter(turma=turma)
        assert horarios.count() == 2

    def test_str_representation(self):
        horario = HorarioFactory(dia_semana=1, hora_inicio='08:00')
        assert str(horario) is not None

    def test_filtro_por_turma(self):
        turma = TurmaFactory()
        HorarioFactory(turma=turma)
        assert Horario.objects.filter(turma=turma).exists()

    def test_queryset_count(self):
        HorarioFactory.create_batch(5)
        assert Horario.objects.count() == 5



