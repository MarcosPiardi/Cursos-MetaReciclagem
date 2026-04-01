"""
Arquivo: test_validators.py
Caminho: apps/selecao/tests/test_validators.py
Testes para validadores do app Selecao
Data: 1 de abril de 2026
"""

from django.test import TestCase
from django.utils import timezone
from datetime import timedelta

from apps.selecao.validators import ClassificacaoValidator
from apps.eventos.tests.factories import EventoFactory, CriterioFactory, EventoCriterioFactory
from apps.interessados.tests.factories import InteressadoFactory
from .factories import InscricaoFactory, StatusInscricaoFactory, ClassificacaoFactory


class TestValidarEvento(TestCase):
    """Testes para validar_evento - valida estado do evento."""

    def test_evento_sem_vagas_falha(self):
        """Evento com vagas=0 deve falhar."""
        evento = EventoFactory(total_vagas=0)
        resultado = ClassificacaoValidator.validar_evento(evento)
        self.assertFalse(resultado['valido'])
        self.assertGreater(len(resultado['erros']), 0)

    def test_evento_sem_inscricoes_falha(self):
        """Evento sem inscrições deve falhar."""
        evento = EventoFactory(total_vagas=10)
        resultado = ClassificacaoValidator.validar_evento(evento)
        self.assertFalse(resultado['valido'])
        self.assertGreater(len(resultado['erros']), 0)

    def test_evento_datas_invalidas_falha(self):
        """Evento com data_inicio > data_fim deve falhar."""
        evento = EventoFactory(
            total_vagas=10,
            data_inicio_inscricao=timezone.now() + timedelta(days=10),
            data_fim_inscricao=timezone.now() - timedelta(days=5)
        )
        resultado = ClassificacaoValidator.validar_evento(evento)
        self.assertFalse(resultado['valido'])

    def test_evento_sem_criterios_falha(self):
        """Evento sem critérios ativos deve falhar - usa ordenação por inscrição."""
        evento = EventoFactory(total_vagas=10)
        InscricaoFactory(evento=evento)
        resultado = ClassificacaoValidator.validar_evento(evento)
        self.assertFalse(resultado['valido'])
        self.assertTrue(any('critérios' in erro.lower() for erro in resultado['erros']))

    def test_evento_com_criterios_passa(self):
        """Evento com critérios ativos deve passar."""
        evento = EventoFactory(total_vagas=10)
        InscricaoFactory(evento=evento)
        
        # Criar critério e associar ao evento
        criterio = CriterioFactory(tipo_criterio='PONTUACAO')
        EventoCriterioFactory(evento=evento, criterio=criterio, ativo=True)
        
        resultado = ClassificacaoValidator.validar_evento(evento)
        self.assertTrue(resultado['valido'])
        self.assertEqual(len(resultado['erros']), 0)


class TestValidarInteressado(TestCase):
    """Testes para validar_interessado - valida dados do interessado."""

    def test_interessado_valido_passa(self):
        """Interessado com dados mínimos deve passar."""
        interessado = InteressadoFactory(
            nome='João Silva',
            cpf='12345678901',
            data_nascimento=timezone.localdate() - timedelta(days=365 * 25)
        )
        resultado = ClassificacaoValidator.validar_interessado(interessado)
        self.assertTrue(resultado['valido'])
        self.assertEqual(len(resultado['erros']), 0)

    def test_interessado_sem_nome_falha(self):
        """Interessado sem nome deve gerar erro."""
        interessado = InteressadoFactory.build(nome='')
        resultado = ClassificacaoValidator.validar_interessado(interessado)
        self.assertFalse(resultado['valido'])
        self.assertTrue(any('nome' in erro.lower() for erro in resultado['erros']))

    def test_interessado_cpf_invalido_falha(self):
        """Interessado com CPF muito curto deve gerar erro."""
        interessado = InteressadoFactory.build(cpf='123')
        resultado = ClassificacaoValidator.validar_interessado(interessado)
        # CPF inválido (muito curto) - validador deveria avisar
        self.assertFalse(resultado['valido'])
        self.assertTrue(any('cpf' in erro.lower() for erro in resultado['erros']))

    def test_interessado_data_nascimento_futura_falha(self):
        """Data de nascimento futura deve gerar erro."""
        interessado = InteressadoFactory(
            data_nascimento=timezone.localdate() + timedelta(days=10)
        )
        resultado = ClassificacaoValidator.validar_interessado(interessado)
        self.assertFalse(resultado['valido'])
        self.assertTrue(any('futuro' in erro.lower() for erro in resultado['erros']))

    def test_interessado_sem_sexo_gera_aviso(self):
        """Interessado sem sexo gera aviso, mas passa."""
        interessado = InteressadoFactory(sexo=None)
        resultado = ClassificacaoValidator.validar_interessado(interessado)
        self.assertTrue(resultado['valido'])
        self.assertGreater(len(resultado['avisos']), 0)


class TestValidarInscricao(TestCase):
    """Testes para validar_inscricao - valida inscrição completa."""

    def test_inscricao_valida_passa(self):
        """Inscrição com dados válidos deve passar."""
        evento = EventoFactory(total_vagas=10)
        interessado = InteressadoFactory(nome='Maria')
        inscricao = InscricaoFactory(evento=evento, interessado=interessado)
        
        resultado = ClassificacaoValidator.validar_inscricao(inscricao)
        self.assertTrue(resultado['valido'])
        self.assertEqual(len(resultado['erros']), 0)

    def test_inscricao_evento_invalido_falha(self):
        """Inscrição com evento inválido (total_vagas=0) deve falhar."""
        evento = EventoFactory(total_vagas=0)
        interessado = InteressadoFactory()
        inscricao = InscricaoFactory(evento=evento, interessado=interessado)
        
        resultado = ClassificacaoValidator.validar_inscricao(inscricao)
        # Falha porque valida o evento também
        self.assertFalse(resultado['valido'])
        self.assertGreater(len(resultado['erros']), 0)

    def test_inscricao_interessado_invalido_falha(self):
        """Inscrição com interessado inválido deve falhar."""
        evento = EventoFactory(total_vagas=10)
        interessado = InteressadoFactory.build(nome='')  # Nome vazio
        
        # Não conseguimos fazer .build() com inscrição, então usamos criado
        # mas interessado.build() fará o validador falhar
        inscricao = InscricaoFactory.build(evento=evento, interessado=interessado)
        
        resultado = ClassificacaoValidator.validar_inscricao(inscricao)
        self.assertFalse(resultado['valido'])
        self.assertGreater(len(resultado['erros']), 0)

        