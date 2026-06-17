"""
Arquivo: test_models.py
Caminho: apps/academico/tests/test_models.py
Atualizacoes:
 - 28/05/2026 - Criacao do arquivo
 - 17/06/2026 - Refatorado de unittest.TestCase para pytest
 - 17/06/2006 - Corrigido test_matricula_unique_together_turma_interessado:
                validacao do model (clean()) levanta ValidationError,
                nao IntegrityError
"""

import pytest
from django.db import IntegrityError
from django.core.exceptions import ValidationError
from django.utils import timezone
from apps.academico.models import StatusMatricula, Matricula
from apps.academico.tests.factories import StatusMatriculaFactory, MatriculaFactory, TurmaFactory
from apps.interessados.tests.factories import InteressadoFactory

pytestmark = pytest.mark.django_db

class TestStatusMatriculaModel:
    """Testes do model StatusMatricula"""

    def test_status_criado_corretamente(self):
        status = StatusMatriculaFactory(nome='Ativo', cor='#00FF00', ordem=1)
        assert status.nome == 'Ativo'
        assert status.cor == '#00FF00'
        assert status.ordem == 1

    def test_status_nome_unique_no_banco(self):
        """Testa a constraint real, nao o comportamento da factory"""
        StatusMatricula.objects.create(nome='Ativo', cor='#000', ordem=1)
        with pytest.raises(IntegrityError):
            StatusMatricula.objects.create(nome='Ativo', cor='#FFF', ordem=2)

class TestMatriculaModel:
    """Testes do model Matricula"""

    def test_matricula_criada_corretamente(self):
        matricula = MatriculaFactory()
        assert matricula.numero_matricula is not None
        assert matricula.turma is not None
        assert matricula.interessado is not None
        assert matricula.status is not None
        assert matricula.data_matricula is not None
        assert matricula.data_matricula <= timezone.now()

    def test_matricula_unique_together_turma_interessado(self):
        """
        unique_together = ['turma', 'interessado']
        Mesma turma + mesmo interessado = violacao.
        O model possui clean() que valida e levanta ValidationError
        antes de chegar na constraint do banco.
        """
        from apps.selecao.models import Inscricao, StatusInscricao

        interessado = InteressadoFactory()
        turma = TurmaFactory()
        status_insc = StatusInscricao.objects.create(nome="Confirmada")
        status_mat = StatusMatricula.objects.create(nome="Ativa", cor="#000", ordem=1)

        inscricao = Inscricao.objects.create(
            interessado=interessado,
            evento=turma.evento,
            status=status_insc,
        )

        primeira = Matricula.objects.create(
            numero_matricula="001",
            turma=turma,
            interessado=interessado,
            inscricao=inscricao,
            status=status_mat,
        )

        with pytest.raises(ValidationError):
            Matricula.objects.create(
                numero_matricula="002",
                turma=turma,
                interessado=interessado,
                inscricao=inscricao,
                status=status_mat,
            )


            