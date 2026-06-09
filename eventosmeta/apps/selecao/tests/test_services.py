"""
Arquivo: test_services.py
Caminho: apps/selecao/tests/test_services.py
Finalidade: Testar os serviços relacionados à classificação de inscrições para eventos.

Histórico de Alterações:
- 27/03/2026 - Testes iniciais de serviços
- 08/04/2026 - Adicionados 3 testes de desempate
- 15/05/2026 - Inclusão de cabeçalho
- 18/05/2026 - Refatoração completa de 2 testes:
               test_calcular_pontuacao_inscricao_zero (evento sem critérios)
               test_desempate_misto_pontuacoes_diferentes_e_iguais (critérios com pontos diferentes)
- 27/05/2026 - Refatoração para incluir mais cenários de teste, como classificação sem inscrições, chamada repetida e pontuação com múltiplos critérios acumulados.
- 08/06/2026 - Refatoração para pytest (unittest → pytest)
"""

import pytest
from django.utils import timezone
from datetime import timedelta
from decimal import Decimal

from .factories import (
    InscricaoFactory,
    StatusInscricaoFactory,
    ClassificacaoFactory
)
from apps.interessados.tests.factories import InteressadoFactory
from apps.eventos.tests.factories import (
    EventoFactory,
    EventoCriterioFactory,
    CriterioFactory
)

from apps.selecao.models import Inscricao, Classificacao, InscricaoCriterioAtendido
from apps.selecao.services import ClassificadorService

@pytest.mark.django_db
class TestClassificadorService:
    """Testes para o serviço ClassificadorService."""

    def setup_method(self):
        """Configuração inicial para todos os testes."""
        self.status_pendente = StatusInscricaoFactory(nome='Pendente')
        self.status_classificado = StatusInscricaoFactory(nome='Classificado')
        self.status_lista_espera = StatusInscricaoFactory(nome='Lista de Espera')
        
        self.evento = EventoFactory(total_vagas=5)
        self.criterio = CriterioFactory(nome='PCD', tipo_criterio='PONTUACAO', pontos=10)
        self.evento_criterio = EventoCriterioFactory(evento=self.evento, criterio=self.criterio)

    def test_calcular_pontuacao_inscricao_com_criterios(self):
        """Deve retornar pontuação correta para inscrição com critérios."""
        interessado = InteressadoFactory()
        inscricao = InscricaoFactory(interessado=interessado, evento=self.evento)
        
        pontuacao = ClassificadorService.calcular_pontuacao_inscricao(inscricao)
        assert pontuacao == Decimal('10.00')

    def test_calcular_pontuacao_inscricao_zero(self):
        """Deve retornar 0 pontos para inscrição sem critérios."""
        evento_sem_criterios = EventoFactory(
            nome='Evento Sem Critérios',
            total_vagas=10
        )
        
        interessado = InteressadoFactory()
        inscricao = InscricaoFactory(
            interessado=interessado,
            evento=evento_sem_criterios,
            status=self.status_pendente
        )
        
        pontuacao = ClassificadorService.calcular_pontuacao_inscricao(inscricao)
        assert pontuacao == Decimal('0')

    def test_classificar_evento_atribui_posicoes(self):
        """Deve atribuir posições ordinais corretas."""
        for i in range(3):
            InscricaoFactory(evento=self.evento, status=self.status_pendente)
        
        resultado = ClassificadorService.classificar_evento(self.evento)
        assert resultado['sucesso'] is True
        
        classificacoes = Classificacao.objects.filter(
            inscricao__evento=self.evento
        ).order_by('posicao')
        
        assert classificacoes[0].posicao == 1
        assert classificacoes[1].posicao == 2
        assert classificacoes[2].posicao == 3

    def test_classificar_evento_classifica_dentro_vagas(self):
        """Candidatos dentro das vagas devem ser classificados."""
        evento = EventoFactory(total_vagas=2)
        EventoCriterioFactory(evento=evento, criterio=self.criterio)
        
        InscricaoFactory(evento=evento, status=self.status_pendente)
        InscricaoFactory(evento=evento, status=self.status_pendente)
        
        ClassificadorService.classificar_evento(evento)
        
        classificacoes = Classificacao.objects.filter(
            inscricao__evento=evento
        ).order_by('posicao')
        
        assert classificacoes[0].classificado is True
        assert classificacoes[1].classificado is True

    def test_classificar_evento_lista_espera(self):
        """Candidatos excedentes devem ficar em lista de espera."""
        evento = EventoFactory(total_vagas=2)
        EventoCriterioFactory(evento=evento, criterio=self.criterio)
        
        InscricaoFactory(evento=evento, status=self.status_pendente)
        InscricaoFactory(evento=evento, status=self.status_pendente)
        InscricaoFactory(evento=evento, status=self.status_pendente)
        
        ClassificadorService.classificar_evento(evento)
        
        classificacoes = Classificacao.objects.filter(
            inscricao__evento=evento
        ).order_by('posicao')
        
        assert classificacoes[2].classificado is False
        assert classificacoes[2].lista_espera is True

    def test_classificar_evento_atualiza_status_inscricao(self):
        """Deve atualizar status de inscrição para 'Classificado'."""
        inscricao = InscricaoFactory(evento=self.evento, status=self.status_pendente)
        
        ClassificadorService.classificar_evento(self.evento)
        
        inscricao.refresh_from_db()
        assert inscricao.status.nome == 'Classificado'

    def test_classificar_evento_com_criterios(self):
        """Deve retornar dict com sucesso e mensagem."""
        InscricaoFactory(evento=self.evento, status=self.status_pendente)
        
        resultado = ClassificadorService.classificar_evento(self.evento)
        
        assert resultado['sucesso'] is True
        assert 'mensagem' in resultado
        assert 'total_processadas' in resultado

    def test_desempate_por_data_inscricao_igual_pontuacao(self):
        """Desempate deve usar data de inscrição (FIFO) quando pontuações são iguais."""
        evento = EventoFactory(total_vagas=5)
        EventoCriterioFactory(evento=evento, criterio=self.criterio)
        
        inscricao_primeira = InscricaoFactory(
            evento=evento,
            status=self.status_pendente,
            data_inscricao=timezone.now() - timedelta(minutes=2)
        )
        
        inscricao_segunda = InscricaoFactory(
            evento=evento,
            status=self.status_pendente,
            data_inscricao=timezone.now() - timedelta(minutes=1)
        )
        
        ClassificadorService.classificar_evento(evento)
        
        classificacoes = Classificacao.objects.filter(
            inscricao__evento=evento
        ).order_by('posicao')
        
        assert classificacoes[0].inscricao == inscricao_primeira
        assert classificacoes[0].posicao == 1
        assert classificacoes[1].inscricao == inscricao_segunda
        assert classificacoes[1].posicao == 2

    def test_desempate_com_lista_espera(self):
        """Desempate por timestamp deve funcionar mesmo em lista de espera."""
        evento = EventoFactory(total_vagas=1)
        EventoCriterioFactory(evento=evento, criterio=self.criterio)
        
        inscricao_primeira = InscricaoFactory(
            evento=evento,
            status=self.status_pendente,
            data_inscricao=timezone.now() - timedelta(minutes=2)
        )
        
        inscricao_segunda = InscricaoFactory(
            evento=evento,
            status=self.status_pendente,
            data_inscricao=timezone.now() - timedelta(minutes=1)
        )
        
        ClassificadorService.classificar_evento(evento)
        
        classificacoes = Classificacao.objects.filter(
            inscricao__evento=evento
        ).order_by('posicao')
        
        assert classificacoes[0].classificado is True
        assert classificacoes[0].lista_espera is False
        
        assert classificacoes[1].classificado is False
        assert classificacoes[1].lista_espera is True

    def test_desempate_misto_pontuacoes_diferentes_e_iguais(self):
        """Deve classificar corretamente com pontuações diferentes e desempatar pela data."""
        evento = EventoFactory(nome='Evento Desempate Misto', total_vagas=4)
        
        criterio_pcd = CriterioFactory(
            nome='Pessoa com Deficiência',
            pontos=30,
            tipo_criterio='PONTUACAO',
            categoria='PCD'
        )
        criterio_nis = CriterioFactory(
            nome='Programa Social',
            pontos=25,
            tipo_criterio='PONTUACAO',
            categoria='NIS'
        )
        criterio_cota = CriterioFactory(
            nome='Cota Racial',
            pontos=10,
            tipo_criterio='PONTUACAO',
            categoria='COTA_RACIAL'
        )
        
        EventoCriterioFactory(evento=evento, criterio=criterio_pcd, prioridade=1, ativo=True)
        EventoCriterioFactory(evento=evento, criterio=criterio_nis, prioridade=2, ativo=True)
        EventoCriterioFactory(evento=evento, criterio=criterio_cota, prioridade=3, ativo=True)
        
        interessado_top = InteressadoFactory(
            nome='Interessado Top',
            necessidades_especiais=True,
            programa_social=False,
            fototipo=None
        )
        inscricao_top = InscricaoFactory(
            interessado=interessado_top,
            evento=evento,
            status=self.status_pendente,
            data_inscricao=timezone.now() - timedelta(minutes=5)
        )
        
        interessado_meio = InteressadoFactory(
            nome='Interessado Meio',
            necessidades_especiais=True,
            programa_social=True,
            fototipo=None
        )
        inscricao_meio = InscricaoFactory(
            interessado=interessado_meio,
            evento=evento,
            status=self.status_pendente,
            data_inscricao=timezone.now() - timedelta(minutes=2)
        )
        
        interessado_empate_a = InteressadoFactory(
            nome='Empate A',
            necessidades_especiais=False,
            programa_social=True,
            fototipo=None
        )
        inscricao_empate_a = InscricaoFactory(
            interessado=interessado_empate_a,
            evento=evento,
            status=self.status_pendente,
            data_inscricao=timezone.now() - timedelta(minutes=4)
        )
        
        interessado_empate_b = InteressadoFactory(
            nome='Empate B',
            necessidades_especiais=False,
            programa_social=True,
            fototipo=None
        )
        inscricao_empate_b = InscricaoFactory(
            interessado=interessado_empate_b,
            evento=evento,
            status=self.status_pendente,
            data_inscricao=timezone.now() - timedelta(minutes=3)
        )
        
        ClassificadorService.classificar_evento(evento)
        
        classificacoes = Classificacao.objects.filter(
            inscricao__evento=evento
        ).order_by('posicao')
        
        assert classificacoes.count() == 4
        
        assert classificacoes[0].inscricao == inscricao_meio
        assert classificacoes[0].pontuacao_total == Decimal('55.00')
        assert classificacoes[0].posicao == 1

        assert classificacoes[1].inscricao == inscricao_top
        assert classificacoes[1].pontuacao_total == Decimal('30.00')
        assert classificacoes[1].posicao == 2

        assert classificacoes[2].inscricao == inscricao_empate_a
        assert classificacoes[2].pontuacao_total == Decimal('25.00')
        assert classificacoes[2].posicao == 3

        assert classificacoes[3].inscricao == inscricao_empate_b
        assert classificacoes[3].pontuacao_total == Decimal('25.00')
        assert classificacoes[3].posicao == 4

    def test_processar_inscricao_cria_classificacao(self):
        """Deve criar Classificacao ao processar inscrição."""
        inscricao = InscricaoFactory(evento=self.evento)
        
        ClassificadorService.processar_inscricao(inscricao)
        
        classificacao = Classificacao.objects.get(inscricao=inscricao)
        assert classificacao.pontuacao_total == Decimal('10.00')

    def test_classificar_evento_zero_inscricoes(self):
        """Testa classificacao de evento sem inscricoes."""
        evento = EventoFactory(total_vagas=5)
        resultado = ClassificadorService.classificar_evento(evento)
        assert resultado['sucesso'] is False
        assert resultado['total_processadas'] == 0
        assert Classificacao.objects.filter(inscricao__evento=evento).count() == 0

    def test_classificar_evento_chamada_repetida(self):
        """Testa que chamar classificar duas vezes nao duplica."""
        evento = EventoFactory(total_vagas=5)
        for i in range(3):
            InscricaoFactory(evento=evento, status=self.status_pendente)
        ClassificadorService.classificar_evento(evento)
        ClassificadorService.classificar_evento(evento)
        classificacoes = Classificacao.objects.filter(inscricao__evento=evento).order_by('posicao')
        assert classificacoes.count() == 3
        assert classificacoes[0].posicao == 1
        assert classificacoes[1].posicao == 2
        assert classificacoes[2].posicao == 3

    def test_calcular_pontuacao_multiplos_criterios(self):
        """Testa pontuacao com 2 criterios acumulados (10+20=30)."""
        evento = EventoFactory(total_vagas=5)
        criterio1 = CriterioFactory(nome='Criterio1', tipo_criterio='PONTUACAO', pontos=10)
        criterio2 = CriterioFactory(nome='Criterio2', tipo_criterio='PONTUACAO', pontos=20)
        EventoCriterioFactory(evento=evento, criterio=criterio1)
        EventoCriterioFactory(evento=evento, criterio=criterio2)
        interessado = InteressadoFactory()
        inscricao = InscricaoFactory(evento=evento, interessado=interessado, status=self.status_pendente)
        InscricaoCriterioAtendido.objects.create(inscricao=inscricao, 
                                                 criterio=criterio1,
                                                 pontos_atribuidos=Decimal('10.00'),
                                                 validado=True)
        InscricaoCriterioAtendido.objects.create(inscricao=inscricao, 
                                                 criterio=criterio2,
                                                 pontos_atribuidos=Decimal('20.00'),
                                                 validado=True)
        
        pontuacao = ClassificadorService.calcular_pontuacao_inscricao(inscricao)
        assert pontuacao == Decimal('30.00')

    def test_classificar_evento_exatamente_1_vaga(self):
        """Testa classificacao com apenas 1 vaga e 3 inscricoes."""
        evento = EventoFactory(total_vagas=1)
        criterio = CriterioFactory(nome='Criterio', tipo_criterio='PONTUACAO', pontos=5)
        EventoCriterioFactory(evento=evento, criterio=criterio)
        inscricoes = []
        for i in range(3):
            insc = InscricaoFactory(
                evento=evento,
                status=self.status_pendente,
                data_inscricao=timezone.now() + timedelta(hours=i)
            )
            InscricaoCriterioAtendido.objects.create(inscricao=insc, 
                                                     criterio=criterio, 
                                                     pontos_atribuidos=Decimal('5.00'),
                                                     validado=True)
            
            inscricoes.append(insc)
        ClassificadorService.classificar_evento(evento)
        classificacoes = Classificacao.objects.filter(inscricao__evento=evento).order_by('posicao')
        assert classificacoes[0].classificado is True
        assert classificacoes[0].lista_espera is False
        assert classificacoes[1].classificado is False
        assert classificacoes[1].lista_espera is True
        assert classificacoes[2].classificado is False
        assert classificacoes[2].lista_espera is True

    def test_classificar_sem_eventocriterio_vinculado(self):
        """Testa pontuacao zero quando criterio existe mas nao vinculado."""
        evento = EventoFactory(total_vagas=5)
        CriterioFactory(nome='Criterio', tipo_criterio='PONTUACAO', pontos=10)
        inscricao = InscricaoFactory(evento=evento, status=self.status_pendente)
        pontuacao = ClassificadorService.calcular_pontuacao_inscricao(inscricao)
        assert pontuacao == Decimal('0.00')





