"""
Arquivo: test_models.py
Caminho: apps/selecao/tests/test_models.py
Atualizações:
 - 27/03/2026 - Testes de modelos para o app Selecao
 - 08/04/2026 - Testes de modelos para o app Seleção com validações e desempate
 - 27/05/2026 - Refatoração dos testes de modelos para incluir validações adicionais e teste de desempate por data de inscrição.
 - 08/06/2026 - Refatoração para pytest (remover BaseAdminActionTest, adicionar fixtures)
"""

import pytest
from django.db.utils import IntegrityError
from django.core.exceptions import ValidationError
from django.utils import timezone
from datetime import timedelta

from apps.selecao.models import StatusInscricao, Inscricao, Classificacao
from apps.selecao.tests.factories import (
    StatusInscricaoFactory,
    InscricaoFactory,
    ClassificacaoFactory
)
from apps.eventos.tests.factories import EventoFactory
from apps.interessados.tests.factories import InteressadoFactory


@pytest.mark.django_db
class TestStatusInscricaoModel:
    """Testes para o modelo StatusInscricao."""

    def setup_method(self):
        """Configuração inicial para todos os testes."""
        self.status = StatusInscricaoFactory(nome='Pendente', cor='#FF0000')

    def test_create_status_inscricao(self):
        """Deve criar um StatusInscricao com sucesso."""
        assert self.status.pk is not None
        assert self.status.nome == 'Pendente'
        assert self.status.cor == '#FF0000'

    def test_status_inscricao_str(self):
        """O método __str__ deve retornar o nome do status."""
        status = StatusInscricaoFactory(nome='Aprovado')
        assert str(status) == 'Aprovado'

    def test_status_inscricao_unique_name(self):
        """Não deve permitir dois status com o mesmo nome."""
        StatusInscricaoFactory(nome='Unico')
        with pytest.raises(IntegrityError):
            StatusInscricao.objects.create(nome='Unico', cor='#FF0000')


@pytest.mark.django_db
class TestInscricaoModel:
    """Testes para o modelo Inscricao."""

    def setup_method(self):
        """Configuração inicial para todos os testes."""
        self.interessado = InteressadoFactory()
        self.evento = EventoFactory()
        self.status_pendente = StatusInscricaoFactory(nome='Pendente')

    def test_create_inscricao(self):
        """Deve criar uma Inscricao com sucesso."""
        inscricao = InscricaoFactory(
            interessado=self.interessado,
            evento=self.evento,
            status=self.status_pendente
        )
        assert inscricao.pk is not None
        assert inscricao.interessado == self.interessado
        assert inscricao.evento == self.evento

    def test_inscricao_str(self):
        """O método __str__ deve retornar formato legível."""
        inscricao = InscricaoFactory(
            interessado=self.interessado,
            evento=self.evento,
            status=self.status_pendente
        )
        assert self.interessado.nome in str(inscricao)
        assert self.evento.nome in str(inscricao)

    def test_inscricao_unique_together(self):
        """Não deve permitir duas inscrições do mesmo interessado no mesmo evento."""
        InscricaoFactory(
            interessado=self.interessado,
            evento=self.evento,
            status=self.status_pendente
        )
        with pytest.raises(IntegrityError):
            InscricaoFactory(
                interessado=self.interessado,
                evento=self.evento,
                status=self.status_pendente
            )

    def test_inscricao_relacionamentos(self):
        """Deve verificar os relacionamentos corretos."""
        inscricao = InscricaoFactory(
            interessado=self.interessado,
            evento=self.evento,
            status=self.status_pendente
        )
        assert inscricao.interessado.nome == self.interessado.nome
        assert inscricao.evento.nome == self.evento.nome
        assert inscricao.status.nome == self.status_pendente.nome


@pytest.mark.django_db
class TestClassificacaoModel:
    """Testes para o modelo Classificacao."""

    def setup_method(self):
        """Configuração inicial para todos os testes."""
        self.inscricao = InscricaoFactory()

    def test_create_classificacao(self):
        """Deve criar uma Classificacao com sucesso."""
        classificacao = ClassificacaoFactory(
            inscricao=self.inscricao,
            pontuacao_total=50,
            posicao=1,
            classificado=True
        )
        assert classificacao.pk is not None
        assert classificacao.inscricao == self.inscricao
        assert classificacao.pontuacao_total == 50
        assert classificacao.posicao == 1
        assert classificacao.classificado is True
        assert classificacao.lista_espera is False

    def test_classificacao_str(self):
        """O método __str__ deve retornar formato legível."""
        classificacao = ClassificacaoFactory(
            inscricao=self.inscricao,
            pontuacao_total=75,
            posicao=3
        )
        resultado_str = str(classificacao)
        assert '3º' in resultado_str
        assert self.inscricao.interessado.nome in resultado_str

    def test_classificacao_posicao_null_default(self):
        """A posição deve ser nula por padrão."""
        classificacao = ClassificacaoFactory(
            inscricao=self.inscricao,
            pontuacao_total=60,
            posicao=None,
            lista_espera=False
        )
        assert classificacao.posicao is None
        assert classificacao.classificado is False
        assert classificacao.lista_espera is False

    def test_classificacao_unique_inscricao(self):
        """Cada inscrição deve ter apenas uma classificacao."""
        ClassificacaoFactory(inscricao=self.inscricao)
        with pytest.raises(IntegrityError):
            ClassificacaoFactory(inscricao=self.inscricao)

    def test_pontuacao_total_validacao_range(self):
        """A pontuação total não deve ser menor que 0 ou maior que 100."""
        classificacao = ClassificacaoFactory(inscricao=self.inscricao)
        
        classificacao.pontuacao_total = -1
        with pytest.raises(ValidationError):
            classificacao.full_clean()
            
        classificacao.pontuacao_total = 101
        with pytest.raises(ValidationError):
            classificacao.full_clean()

    def test_flags_classificacao_mutuamente_exclusivas(self):
        """classificado e lista_espera nao podem ser True juntos."""
        classificacao = ClassificacaoFactory(inscricao=self.inscricao)
        classificacao.classificado = True
        classificacao.lista_espera = True
        with pytest.raises(ValidationError):
            classificacao.full_clean()    
        
    def test_desempate_por_data_inscricao(self):
        """Ordenacao respeita data de inscricao (FIFO) para pontuacoes iguais."""
        interessado2 = InteressadoFactory()
        inscricao2 = InscricaoFactory(interessado=interessado2)

        ClassificacaoFactory(
            inscricao=self.inscricao,
            pontuacao_total=50
        )
        ClassificacaoFactory(
            inscricao=inscricao2,
            pontuacao_total=50
        )

        agora = timezone.now()
        Inscricao.objects.filter(pk=self.inscricao.pk).update(
            data_inscricao=agora - timedelta(hours=2)
        )
        Inscricao.objects.filter(pk=inscricao2.pk).update(
            data_inscricao=agora - timedelta(hours=1)
        )

        queryset = Classificacao.objects.all().order_by(
            '-pontuacao_total', 'inscricao__data_inscricao'
        )

        assert queryset.first().inscricao == self.inscricao
        assert queryset.last().inscricao == inscricao2

