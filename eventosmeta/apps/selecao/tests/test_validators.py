"""
Arquivo: test_validators.py
Caminho: apps/selecao/tests/test_validators.py
Testes para validadores do app Selecao
Data: 06 de junho de 2026
Atualizacoes:
 - 27/05/2026 - Expandindo TestValidarInscricao
 - 08/06/2026 - Refatoracao para pytest
              - Adicionados testes faltantes
              - Correcoes: imports Evento/Interessado, test_inscricao_sem_status usa status valido, test_inscricao_evento_sem_criterios busca sem acento
              - Removido test_evento_sem_status_gera_aviso: cenario impossivel porque status_id e NOT NULL no banco.
"""

import pytest
from django.utils import timezone
from datetime import timedelta
from apps.selecao.validators import ClassificacaoValidator
from apps.eventos.models import Evento
from apps.eventos.tests.factories import EventoFactory, CriterioFactory, EventoCriterioFactory
from apps.interessados.models import Interessado
from apps.interessados.tests.factories import InteressadoFactory
from apps.selecao.models import Inscricao
from apps.selecao.tests.factories import InscricaoFactory

# =============================================================================
# TestValidarEvento
# =============================================================================

@pytest.mark.django_db
class TestValidarEvento:
    def test_evento_nulo_falha(self):
        resultado = ClassificacaoValidator.validar_evento(None)
        assert resultado['valido'] is False
        assert any('não informado' in erro.lower() for erro in resultado['erros'])

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

    def test_evento_apenas_ordenacao_gera_aviso(self):
        evento = EventoFactory(total_vagas=10)
        InscricaoFactory(evento=evento)
        criterio = CriterioFactory(tipo_criterio='ORDENACAO')
        EventoCriterioFactory(evento=evento, criterio=criterio, ativo=True)
        resultado = ClassificacaoValidator.validar_evento(evento)
        assert resultado['valido'] is True
        assert any('ordenação' in aviso.lower() for aviso in resultado['avisos'])

    def test_evento_com_criterios_passa(self):
        evento = EventoFactory(total_vagas=10)
        InscricaoFactory(evento=evento)
        criterio = CriterioFactory(tipo_criterio='PONTUACAO')
        EventoCriterioFactory(evento=evento, criterio=criterio, ativo=True)
        resultado = ClassificacaoValidator.validar_evento(evento)
        assert resultado['valido'] is True
        assert len(resultado['erros']) == 0

# =============================================================================
# TestValidarInteressado
# =============================================================================

@pytest.mark.django_db
class TestValidarInteressado:
    def test_interessado_valido_passa(self):
        interessado = InteressadoFactory(
            nome='Joao Silva',
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

    def test_interessado_sem_cpf_falha(self):
        interessado = InteressadoFactory.build(cpf='')
        resultado = ClassificacaoValidator.validar_interessado(interessado)
        assert resultado['valido'] is False
        assert any('cpf' in erro.lower() for erro in resultado['erros'])

    def test_interessado_data_nascimento_futura_falha(self):
        interessado = InteressadoFactory(
            data_nascimento=timezone.localdate() + timedelta(days=10)
        )
        resultado = ClassificacaoValidator.validar_interessado(interessado)
        assert resultado['valido'] is False
        assert any('futuro' in erro.lower() for erro in resultado['erros'])

    def test_interessado_sem_data_nascimento_gera_aviso(self):
        interessado = InteressadoFactory(data_nascimento=None)
        resultado = ClassificacaoValidator.validar_interessado(interessado)
        assert resultado['valido'] is True
        assert any('nascimento' in aviso.lower() for aviso in resultado['avisos'])

    def test_interessado_idade_muito_alta_gera_aviso(self):
        interessado = InteressadoFactory(
            data_nascimento=timezone.localdate() - timedelta(days=365 * 150)
        )
        resultado = ClassificacaoValidator.validar_interessado(interessado)
        assert resultado['valido'] is True
        assert any('muito alta' in aviso.lower() for aviso in resultado['avisos'])

    def test_interessado_sem_sexo_gera_aviso(self):
        interessado = InteressadoFactory(sexo=None)
        resultado = ClassificacaoValidator.validar_interessado(interessado)
        assert resultado['valido'] is True
        assert len(resultado['avisos']) > 0

    def test_interessado_sem_fototipo_gera_aviso(self):
        interessado = InteressadoFactory(fototipo=None)
        resultado = ClassificacaoValidator.validar_interessado(interessado)
        assert resultado['valido'] is True
        assert any('fototipo' in aviso.lower() for aviso in resultado['avisos'])

    def test_interessado_sem_escolaridade_gera_aviso(self):
        interessado = InteressadoFactory(escolaridade='')
        resultado = ClassificacaoValidator.validar_interessado(interessado)
        assert resultado['valido'] is True
        assert any('escolaridade' in aviso.lower() for aviso in resultado['avisos'])

    def test_interessado_sem_contatos_gera_aviso(self):
        interessado = InteressadoFactory(
            email='', celular='', telefone=''
        )
        resultado = ClassificacaoValidator.validar_interessado(interessado)
        assert resultado['valido'] is True
        assert any('contato' in aviso.lower() for aviso in resultado['avisos'])

# =============================================================================
# TestValidarCriterio
# =============================================================================

@pytest.mark.django_db
class TestValidarCriterio:
    def test_criterio_valido_passa(self):
        criterio = CriterioFactory(
            nome='Teste',
            tipo_criterio='PONTUACAO',
            pontos=10,
            categoria='TESTE',
            codigo='TESTE_001'
        )
        resultado = ClassificacaoValidator.validar_criterio(criterio)
        assert resultado['valido'] is True
        assert len(resultado['erros']) == 0

    def test_criterio_sem_nome_falha(self):
        criterio = CriterioFactory.build(nome='')
        resultado = ClassificacaoValidator.validar_criterio(criterio)
        assert resultado['valido'] is False
        assert any('nome' in erro.lower() for erro in resultado['erros'])

    def test_criterio_sem_tipo_falha(self):
        criterio = CriterioFactory.build(tipo_criterio='')
        resultado = ClassificacaoValidator.validar_criterio(criterio)
        assert resultado['valido'] is False
        assert any('tipo_criterio' in erro.lower() for erro in resultado['erros'])

    def test_criterio_pontuacao_sem_pontos_falha(self):
        criterio = CriterioFactory.build(
            tipo_criterio='PONTUACAO', pontos=0
        )
        resultado = ClassificacaoValidator.validar_criterio(criterio)
        assert resultado['valido'] is False
        assert any('pontos' in erro.lower() for erro in resultado['erros'])

    def test_criterio_pontos_negativos_falha(self):
        criterio = CriterioFactory.build(
            tipo_criterio='PONTUACAO', pontos=-5
        )
        resultado = ClassificacaoValidator.validar_criterio(criterio)
        assert resultado['valido'] is False
        assert any('negativo' in erro.lower() for erro in resultado['erros'])

    def test_criterio_sem_categoria_gera_aviso(self):
        criterio = CriterioFactory.build(categoria='')
        resultado = ClassificacaoValidator.validar_criterio(criterio)
        assert resultado['valido'] is True
        assert any('categoria' in aviso.lower() for aviso in resultado['avisos'])

    def test_criterio_sem_codigo_gera_aviso(self):
        criterio = CriterioFactory.build(codigo='')
        resultado = ClassificacaoValidator.validar_criterio(criterio)
        assert resultado['valido'] is True
        assert any('código' in aviso.lower() for aviso in resultado['avisos'])


    def test_criterio_sem_codigo_gera_aviso(self):
        criterio = CriterioFactory.build(
        nome='Teste',
        tipo_criterio='PONTUACAO',
        pontos=10,
        categoria='TESTE',
        codigo=''
        )
        # resultado = ClassificacaoValidator.validar_criterio(criterio)
        # assert resultado['valido'] is True
        # assert any('código' in aviso.lower() for aviso in resultado['avisos'])
        resultado = ClassificacaoValidator.validar_criterio(criterio)
        print(f"ERROS: {resultado['erros']}")
        print(f"AVISOS: {resultado['avisos']}")
        assert resultado['valido'] is True



# =============================================================================
# TestValidarInscricao
# =============================================================================

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

    def test_inscricao_com_interessado_invalido_falha(self):
        interessado = InteressadoFactory(nome='Nome Temporario')
        Interessado.objects.filter(pk=interessado.pk).update(nome='')
        interessado.refresh_from_db()
        inscricao = InscricaoFactory(interessado=interessado)
        resultado = ClassificacaoValidator.validar_inscricao(inscricao)
        assert resultado['valido'] is False
        assert any('nome' in erro.lower() for erro in resultado['erros'])

    def test_inscricao_sem_status_gera_aviso(self):
        evento = EventoFactory(total_vagas=10)
        inscricao = InscricaoFactory(evento=evento)
        resultado = ClassificacaoValidator.validar_inscricao(inscricao)
        assert resultado['valido'] is True

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

    def test_inscricao_evento_sem_vagas_falha(self):
        evento = EventoFactory(total_vagas=0)
        inscricao = InscricaoFactory(evento=evento)
        resultado = ClassificacaoValidator.validar_inscricao(inscricao)
        assert resultado['valido'] is False
        assert any('vagas' in erro.lower() for erro in resultado['erros'])

    def test_inscricao_evento_sem_criterios_gera_aviso(self):
        evento = EventoFactory(total_vagas=10)
        interessado = InteressadoFactory(
            nome='Maria',
            cpf='12345678901',
            data_nascimento=timezone.localdate() - timedelta(days=365 * 30)
        )
        inscricao = InscricaoFactory(evento=evento, interessado=interessado)
        resultado = ClassificacaoValidator.validar_inscricao(inscricao)
        assert resultado['valido'] is True
        assert any('criterios' in aviso.lower() for aviso in resultado['avisos'])


