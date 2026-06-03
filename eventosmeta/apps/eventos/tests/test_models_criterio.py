"""
Arquivo: test_models_criterio.py
Caminho: apps/eventos/tests/test_models_criterio.py
Finalidade: Testes para o modelo Criterio usando pytest
Data: 03/06/2026 - Criação com 15 testes
"""

import pytest
from django.core.exceptions import ValidationError
from django.db import IntegrityError
from apps.eventos.models import Criterio
from apps.eventos.tests.factories import CriterioFactory, EventoCriterioFactory

@pytest.mark.django_db
class TestCriterioModel:

    def test_criar_criterio_valido(self):
        criterio = CriterioFactory()
        assert Criterio.objects.count() == 1

    def test_ler_criterio(self):
        criterio = CriterioFactory(nome="Teste Leitura")
        db_criterio = Criterio.objects.get(id=criterio.id)
        assert db_criterio.nome == "Teste Leitura"

    def test_atualizar_criterio(self):
        criterio = CriterioFactory(nome="Original")
        criterio.nome = "Atualizado"
        criterio.save()
        assert Criterio.objects.get(id=criterio.id).nome == "Atualizado"

    def test_deletar_criterio(self):
        criterio = CriterioFactory()
        criterio.delete()
        assert Criterio.objects.count() == 0

    def test_codigo_unico(self):
        CriterioFactory(codigo="ABC")
        with pytest.raises(IntegrityError):
            CriterioFactory(codigo="ABC")

    def test_codigo_valido(self):
        criterio = CriterioFactory(codigo="XYZ123")
        assert criterio.codigo == "XYZ123"

    def test_pontos_positivo(self):
        criterio = CriterioFactory(pontos=10)
        assert criterio.pontos == 10

    def test_pontos_zero_permitido(self):
        criterio = CriterioFactory(pontos=0)
        assert criterio.pontos == 0

    def test_criterio_ativo_padrao(self):
        criterio = CriterioFactory()
        assert criterio.ativo is True

    def test_criterio_inativo(self):
        criterio = CriterioFactory(ativo=False)
        assert criterio.ativo is False

    def test_criterio_com_eventos(self):
        criterio = CriterioFactory()
        EventoCriterioFactory(criterio=criterio)
        assert criterio.eventocriterio_set.count() == 1

    def test_criterio_sem_eventos(self):
        criterio = CriterioFactory()
        assert criterio.eventocriterio_set.count() == 0

    def test_str_representation(self):
        criterio = CriterioFactory(nome="Criterio Teste")
        assert "Criterio Teste" in str(criterio)

    def test_filtro_por_ativo(self):
        CriterioFactory(ativo=True)
        CriterioFactory(ativo=False)
        assert Criterio.objects.filter(ativo=True).count() == 1

    def test_queryset_count(self):
        CriterioFactory.create_batch(5)
        assert Criterio.objects.count() == 5




        