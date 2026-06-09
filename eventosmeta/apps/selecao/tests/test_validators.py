"""
Arquivo: test_validators.py
Caminho: apps/selecao/tests/test_validators.py
Testes para validadores do app Selecao
Data: 06 de junho de 2026
Atualizações: 
 - 27/05/2026 - Expandindo TestValidarInscricao para cobrir mais cenários de validação.
 - 08/06/2026 - Refatoração para pytest (unittest → pytest)
"""

import pytest
from django.utils import timezone
from datetime import timedelta
from apps.selecao.validators import ClassificacaoValidator
from apps.eventos.tests.factories import EventoFactory, CriterioFactory, EventoCriterioFactory
from apps.interessados.tests.factories import InteressadoFactory
from apps.selecao.models import Inscricao
from .factories import InscricaoFactory

@pytest.mark.django_db
class TestValidarEvento:
    def test_evento_sem_vagas_falha(self):
        evento = EventoFactory(total_vagas=0)
        resultado = ClassificacaoValidator.validar_evento(evento)
        assert resultado['valido'] is False
        assert len(resultado['erros']) > 0

    def test_evento_sem_inscricoes_falha(self):
        evento = EventoFactory(total_vagas=10)
        resultado = ClassificacaoValidator.validar_evento(evento)
        assert resultado['valido'] is False
        assert len(resultado['erros']) > 0

    def test_evento_datas_invalidas_falha(self):
        evento = EventoFactory(
            total_vagas=10,
            data_inicio_inscricao=timezone.now() + timedelta(days=10),
            data_fim_inscricao=timezone.now() - timedelta(days=5)
        )
        resultado = ClassificacaoValidator.validar_evento(evento)
        assert resultado['valido'] is False

    def test_evento_sem_criterios_falha(self):
        evento = EventoFactory(total_vagas=10)
        InscricaoFactory(evento=evento)
        resultado = ClassificacaoValidator.validar_evento(evento)
        assert resultado['valido'] is False
        assert any('critérios' in erro.lower() for erro in resultado['erros'])

    def test_evento_com_criterios_passa(self):
        evento = EventoFactory(total_vagas=10)
        InscricaoFactory(evento=evento)
        criterio = CriterioFactory(tipo_criterio='PONTUACAO')
        EventoCriterioFactory(evento=evento, criterio=criterio, ativo=True)
        resultado = ClassificacaoValidator.validar_evento(evento)
        assert resultado['valido'] is True
        assert len(resultado['erros']) == 0

@pytest.mark.django_db
class TestValidarInteressado:
    def test_interessado_valido_passa(self):
        interessado = InteressadoFactory(
            nome='João Silva',
            cpf='12345678901',
            data_nascimento=timezone.localdate() - timedelta(days=365 * 25)
        )
        resultado = ClassificacaoValidator.validar_interessado(interessado)
        assert resultado['valido'] is True
        assert len(resultado['erros']) == 0

    def test_interessado_sem_nome_falha(self):
        interessado = InteressadoFactory.build(nome='')
        resultado = ClassificacaoValidator.validar_interessado(interessado)
        assert resultado['valido'] is False
        assert any('nome' in erro.lower() for erro in resultado['erros'])

    def test_interessado_data_nascimento_futura_falha(self):
        interessado = InteressadoFactory(
            data_nascimento=timezone.localdate() + timedelta(days=10)
        )
        resultado = ClassificacaoValidator.validar_interessado(interessado)
        assert resultado['valido'] is False
        assert any('futuro' in erro.lower() for erro in resultado['erros'])

    def test_interessado_sem_sexo_gera_aviso(self):
        interessado = InteressadoFactory(sexo=None)
        resultado = ClassificacaoValidator.validar_interessado(interessado)
        assert resultado['valido'] is True
        assert len(resultado['avisos']) > 0

@pytest.mark.django_db
class TestValidarInscricao:
    def test_inscricao_valida_passa(self):
        evento = EventoFactory(total_vagas=10)
        interessado = InteressadoFactory(nome='Maria')
        inscricao = InscricaoFactory(evento=evento, interessado=interessado)
        resultado = ClassificacaoValidator.validar_inscricao(inscricao)
        assert resultado['valido'] is True
        assert len(resultado['erros']) == 0

    def test_inscricao_sem_evento_falha(self):
        inscricao = InscricaoFactory.build(evento=None)
        resultado = ClassificacaoValidator.validar_inscricao(inscricao)
        assert resultado['valido'] is False
        assert len(resultado['erros']) > 0

    def test_inscricao_sem_interessado_falha(self):
        inscricao = InscricaoFactory.build(interessado=None)
        resultado = ClassificacaoValidator.validar_inscricao(inscricao)
        assert resultado['valido'] is False
        assert len(resultado['erros']) > 0

    def test_inscricao_com_data_futura_falha(self):
        inscricao = InscricaoFactory()
        Inscricao.objects.filter(pk=inscricao.pk).update(
            data_inscricao=timezone.now() + timedelta(days=30)
        )
        inscricao.refresh_from_db()
        resultado = ClassificacaoValidator.validar_inscricao(inscricao)
        assert resultado['valido'] is False
        assert len(resultado['erros']) > 0
        assert any('futur' in erro.lower() for erro in resultado['erros'])


