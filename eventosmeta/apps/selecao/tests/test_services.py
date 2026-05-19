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
"""

from django.test import TestCase
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


class TestClassificadorService(TestCase):
    """Testes para o serviço ClassificadorService."""

    def setUp(self):
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
        self.assertEqual(pontuacao, Decimal('10.00'))

    def test_calcular_pontuacao_inscricao_zero(self):
        """Deve retornar 0 pontos para inscrição sem critérios."""
        # Criar evento SEM critérios
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
        self.assertEqual(pontuacao, Decimal('0'))

    def test_classificar_evento_atribui_posicoes(self):
        """Deve atribuir posições ordinais corretas."""
        for i in range(3):
            InscricaoFactory(evento=self.evento, status=self.status_pendente)
        
        resultado = ClassificadorService.classificar_evento(self.evento)
        self.assertTrue(resultado['sucesso'])
        
        classificacoes = Classificacao.objects.filter(
            inscricao__evento=self.evento
        ).order_by('posicao')
        
        self.assertEqual(classificacoes[0].posicao, 1)
        self.assertEqual(classificacoes[1].posicao, 2)
        self.assertEqual(classificacoes[2].posicao, 3)

    def test_classificar_evento_classifica_dentro_vagas(self):
        """Candidatos dentro das vagas devem ser classificados."""
        # Evento com 2 vagas
        evento = EventoFactory(total_vagas=2)
        EventoCriterioFactory(evento=evento, criterio=self.criterio)
        
        InscricaoFactory(evento=evento, status=self.status_pendente)
        InscricaoFactory(evento=evento, status=self.status_pendente)
        
        ClassificadorService.classificar_evento(evento)
        
        classificacoes = Classificacao.objects.filter(
            inscricao__evento=evento
        ).order_by('posicao')
        
        self.assertTrue(classificacoes[0].classificado)
        self.assertTrue(classificacoes[1].classificado)

    def test_classificar_evento_lista_espera(self):
        """Candidatos excedentes devem ficar em lista de espera."""
        # Evento com 2 vagas, 3 inscrições
        evento = EventoFactory(total_vagas=2)
        EventoCriterioFactory(evento=evento, criterio=self.criterio)
        
        InscricaoFactory(evento=evento, status=self.status_pendente)
        InscricaoFactory(evento=evento, status=self.status_pendente)
        InscricaoFactory(evento=evento, status=self.status_pendente)
        
        ClassificadorService.classificar_evento(evento)
        
        classificacoes = Classificacao.objects.filter(
            inscricao__evento=evento
        ).order_by('posicao')
        
        self.assertFalse(classificacoes[2].classificado)
        self.assertTrue(classificacoes[2].lista_espera)


    def test_classificar_evento_atualiza_status_inscricao(self):
        """Deve atualizar status de inscrição para 'Classificado'."""
        inscricao = InscricaoFactory(evento=self.evento, status=self.status_pendente)
        
        ClassificadorService.classificar_evento(self.evento)
        
        inscricao.refresh_from_db()
        self.assertEqual(inscricao.status.nome, 'Classificado')

    def test_classificar_evento_com_criterios(self):
        """Deve retornar dict com sucesso e mensagem."""
        InscricaoFactory(evento=self.evento, status=self.status_pendente)
        
        resultado = ClassificadorService.classificar_evento(self.evento)
        
        self.assertTrue(resultado['sucesso'])
        self.assertIn('mensagem', resultado)
        self.assertIn('total_processadas', resultado)

    def test_desempate_por_data_inscricao_igual_pontuacao(self):
        """Desempate deve usar data de inscrição (FIFO) quando pontuações são iguais."""
        evento = EventoFactory(total_vagas=5)
        EventoCriterioFactory(evento=evento, criterio=self.criterio)
        
        # Criar 2 inscrições com mesma pontuação, datas diferentes
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
        
        # Quem se inscreveu primeiro deve ter melhor posição
        self.assertEqual(classificacoes[0].inscricao, inscricao_primeira)
        self.assertEqual(classificacoes[0].posicao, 1)
        self.assertEqual(classificacoes[1].inscricao, inscricao_segunda)
        self.assertEqual(classificacoes[1].posicao, 2)

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
        
        # Primeira deve ser classificada
        self.assertTrue(classificacoes[0].classificado)
        self.assertFalse(classificacoes[0].lista_espera)
        
        # Segunda deve estar em lista de espera
        self.assertFalse(classificacoes[1].classificado)
        self.assertTrue(classificacoes[1].lista_espera)

    def test_desempate_misto_pontuacoes_diferentes_e_iguais(self):
        """
        Deve classificar corretamente com pontuações diferentes e desempatar
        pela data de inscrição quando as pontuações são iguais.
        """
        # Criar novo evento
        evento = EventoFactory(nome='Evento Desempate Misto', total_vagas=4)
        
        # Criar critérios com categorias VÁLIDAS
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
        
        # Adicionar ao evento
        EventoCriterioFactory(evento=evento, criterio=criterio_pcd, prioridade=1, ativo=True)
        EventoCriterioFactory(evento=evento, criterio=criterio_nis, prioridade=2, ativo=True)
        EventoCriterioFactory(evento=evento, criterio=criterio_cota, prioridade=3, ativo=True)
        
        # Interessado TOP: atende PCD (30 pts)
        interessado_top = InteressadoFactory(
            nome='Interessado Top',
            necessidades_especiais=True,  # Atende PCD
            programa_social=False,
            fototipo=None
        )
        inscricao_top = InscricaoFactory(
            interessado=interessado_top,
            evento=evento,
            status=self.status_pendente,
            data_inscricao=timezone.now() - timedelta(minutes=5)
        )
        
        # Interessado MEIO: atende PCD + NIS (30 + 25 = 55 pts)
        interessado_meio = InteressadoFactory(
            nome='Interessado Meio',
            necessidades_especiais=True,  # Atende PCD = +30
            programa_social=True,  # Atende NIS = +25
            fototipo=None
        )
        inscricao_meio = InscricaoFactory(
            interessado=interessado_meio,
            evento=evento,
            status=self.status_pendente,
            data_inscricao=timezone.now() - timedelta(minutes=2)
        )
        
        # Interessado EMPATE A: atende apenas NIS (25 pts, inscrito há 4 min)
        interessado_empate_a = InteressadoFactory(
            nome='Empate A',
            necessidades_especiais=False,
            programa_social=True,  # Atende NIS = +25
            fototipo=None
        )
        inscricao_empate_a = InscricaoFactory(
            interessado=interessado_empate_a,
            evento=evento,
            status=self.status_pendente,
            data_inscricao=timezone.now() - timedelta(minutes=4)
        )
        
        # Interessado EMPATE B: atende apenas NIS (25 pts, inscrito há 3 min)
        interessado_empate_b = InteressadoFactory(
            nome='Empate B',
            necessidades_especiais=False,
            programa_social=True,  # Atende NIS = +25
            fototipo=None
        )
        inscricao_empate_b = InscricaoFactory(
            interessado=interessado_empate_b,
            evento=evento,
            status=self.status_pendente,
            data_inscricao=timezone.now() - timedelta(minutes=3)
        )
        
        # Classificar
        ClassificadorService.classificar_evento(evento)
        
        # Validar resultado esperado
        classificacoes = Classificacao.objects.filter(
            inscricao__evento=evento
        ).order_by('posicao')
        
        self.assertEqual(classificacoes.count(), 4)
        
        # Posição 1: MEIO (55 pts) - PCD + NIS
        self.assertEqual(classificacoes[0].inscricao, inscricao_meio)
        self.assertEqual(classificacoes[0].pontuacao_total, Decimal('55.00'))
        self.assertEqual(classificacoes[0].posicao, 1)

        # Posição 2: TOP (30 pts) - PCD apenas
        self.assertEqual(classificacoes[1].inscricao, inscricao_top)
        self.assertEqual(classificacoes[1].pontuacao_total, Decimal('30.00'))
        self.assertEqual(classificacoes[1].posicao, 2)

        # Posição 3: EMPATE A (25 pts, inscrito há 4 min - chegou primeiro)
        self.assertEqual(classificacoes[2].inscricao, inscricao_empate_a)
        self.assertEqual(classificacoes[2].pontuacao_total, Decimal('25.00'))
        self.assertEqual(classificacoes[2].posicao, 3)

        # Posição 4: EMPATE B (25 pts, inscrito há 3 min - chegou depois)
        self.assertEqual(classificacoes[3].inscricao, inscricao_empate_b)
        self.assertEqual(classificacoes[3].pontuacao_total, Decimal('25.00'))
        self.assertEqual(classificacoes[3].posicao, 4)

    def test_processar_inscricao_cria_classificacao(self):
        """Deve criar Classificacao ao processar inscrição."""
        inscricao = InscricaoFactory(evento=self.evento)
        
        ClassificadorService.processar_inscricao(inscricao)
        
        classificacao = Classificacao.objects.get(inscricao=inscricao)
        self.assertEqual(classificacao.pontuacao_total, Decimal('10.00'))


        
