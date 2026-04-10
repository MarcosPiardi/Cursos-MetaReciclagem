"""
Arquivo: test_services.py
Caminho: apps/selecao/tests/test_services.py
27/03/2026 - Testes de serviços para o app Selecao
08/04/2026 - Código foi complementado com os 3 novos testes de desempate
"""

from django.test import TestCase
from django.utils import timezone
from datetime import timedelta
from decimal import Decimal

from .factories import (
    InteressadoFactory,
    InscricaoFactory,
    StatusInscricaoFactory,
    ClassificacaoFactory
)
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
        self.status_pendente = StatusInscricaoFactory(nome='Pendente')
        self.status_classificado = StatusInscricaoFactory(nome='Classificado')
        self.status_lista_espera = StatusInscricaoFactory(nome='Lista de Espera')
        
        self.evento = EventoFactory(total_vagas=5)
        self.criterio = CriterioFactory(nome='PCD', tipo_criterio='PONTUACAO', pontos=10)
        self.evento_criterio = EventoCriterioFactory(evento=self.evento, criterio=self.criterio)

    def test_calcular_pontuacao_inscricao_zero(self):
        """Deve retornar 0 pontos para inscrição sem critérios."""
        interessado = InteressadoFactory()
        inscricao = InscricaoFactory(interessado=interessado, evento=self.evento)
        
        pontuacao = ClassificadorService.calcular_pontuacao_inscricao(inscricao)
        self.assertEqual(pontuacao, Decimal('0'))

    def test_calcular_pontuacao_inscricao_com_criterios(self):
        """Deve calcular pontuação com critérios atendidos."""
        interessado = InteressadoFactory()
        inscricao = InscricaoFactory(interessado=interessado, evento=self.evento)
        
        # Simula critérios atendidos
        InscricaoCriterioAtendido.objects.create(
            inscricao=inscricao,
            criterio=self.criterio,
            pontos_atribuidos=10
        )
        
        pontuacao = ClassificadorService.calcular_pontuacao_inscricao(inscricao)
        self.assertEqual(pontuacao, Decimal('10'))

    def test_processar_inscricao_cria_classificacao(self):
        """Deve processar inscrição e criar classificacao."""
        interessado = InteressadoFactory()
        inscricao = InscricaoFactory(interessado=interessado, evento=self.evento)
        
        ClassificadorService.processar_inscricao(inscricao)
        
        classificacao = Classificacao.objects.get(inscricao=inscricao)
        self.assertIsNotNone(classificacao)
        self.assertIsNone(classificacao.posicao)

    def test_classificar_evento_atribui_posicoes(self):
        """Deve classificar evento atribuindo posições corretas."""
        inscricoes = []
        for i in range(7):
            interessado = InteressadoFactory()
            inscricao = InscricaoFactory(
                interessado=interessado,
                evento=self.evento,
                status=self.status_pendente
            )
            inscricoes.append(inscricao)
        
        ClassificadorService.classificar_evento(self.evento)
        
        classificacoes = Classificacao.objects.filter(
            inscricao__evento=self.evento
        ).order_by('posicao')
        
        self.assertEqual(classificacoes.count(), 7)
        for i, classificacao in enumerate(classificacoes):
            self.assertEqual(classificacao.posicao, i + 1)

    def test_classificar_evento_classifica_dentro_vagas(self):
        """Inscrições dentro de vagas devem ser classificadas."""
        for i in range(5):
            interessado = InteressadoFactory()
            InscricaoFactory(
                interessado=interessado,
                evento=self.evento,
                status=self.status_pendente
            )
        
        ClassificadorService.classificar_evento(self.evento)
        
        classificacoes = Classificacao.objects.filter(
            inscricao__evento=self.evento,
            posicao__lte=self.evento.total_vagas
        )
        
        for classificacao in classificacoes:
            self.assertTrue(classificacao.classificado)
            self.assertFalse(classificacao.lista_espera)

    def test_classificar_evento_lista_espera(self):
        """Inscrições acima de vagas devem estar em lista de espera."""
        for i in range(8):
            interessado = InteressadoFactory()
            InscricaoFactory(
                interessado=interessado,
                evento=self.evento,
                status=self.status_pendente
            )
        
        ClassificadorService.classificar_evento(self.evento)
        
        classificacoes = Classificacao.objects.filter(
            inscricao__evento=self.evento,
            posicao__gt=self.evento.total_vagas
        )
        
        for classificacao in classificacoes:
            self.assertFalse(classificacao.classificado)
            self.assertTrue(classificacao.lista_espera)

    def test_classificar_evento_atualiza_status_inscricao(self):
        """Deve atualizar status das inscrições após classificação."""
        interessado = InteressadoFactory()
        inscricao = InscricaoFactory(
            interessado=interessado,
            evento=self.evento,
            status=self.status_pendente
        )
        
        ClassificadorService.classificar_evento(self.evento)
        
        inscricao.refresh_from_db()
        self.assertEqual(inscricao.status.nome, 'Classificado')

    def test_classificar_evento_com_criterios(self):
        """Deve classificar evento respeitando critérios ativos."""
        for i in range(3):
            interessado = InteressadoFactory()
            InscricaoFactory(
                interessado=interessado,
                evento=self.evento,
                status=self.status_pendente
            )
        
        resultado = ClassificadorService.classificar_evento(self.evento)
        self.assertTrue(resultado['sucesso'])
        self.assertEqual(resultado['total_processadas'], 3)

    def test_desempate_por_data_inscricao_igual_pontuacao(self):
        """
        Deve desempatar classificações com mesma pontuação pela data de inscrição
        (mais antiga primeiro).
        """
        # Inscrições com mesma pontuação, mas datas diferentes
        inscricao_a = InscricaoFactory(
            interessado=InteressadoFactory(nome='Interessado A'),
            evento=self.evento,
            status=self.status_pendente,
            data_inscricao=timezone.now() - timedelta(minutes=3)
        )
        InscricaoCriterioAtendido.objects.create(
            inscricao=inscricao_a, criterio=self.criterio, pontos_atribuidos=20
        )

        inscricao_b = InscricaoFactory(
            interessado=InteressadoFactory(nome='Interessado B'),
            evento=self.evento,
            status=self.status_pendente,
            data_inscricao=timezone.now() - timedelta(minutes=2)
        )
        InscricaoCriterioAtendido.objects.create(
            inscricao=inscricao_b, criterio=self.criterio, pontos_atribuidos=20
        )

        inscricao_c = InscricaoFactory(
            interessado=InteressadoFactory(nome='Interessado C'),
            evento=self.evento,
            status=self.status_pendente,
            data_inscricao=timezone.now() - timedelta(minutes=1)
        )
        InscricaoCriterioAtendido.objects.create(
            inscricao=inscricao_c, criterio=self.criterio, pontos_atribuidos=20
        )

        ClassificadorService.classificar_evento(self.evento)

        classificacoes = Classificacao.objects.filter(
            inscricao__evento=self.evento
        ).order_by('posicao')

        self.assertEqual(classificacoes.count(), 3)
        self.assertEqual(classificacoes[0].inscricao, inscricao_a)
        self.assertEqual(classificacoes[0].posicao, 1)
        self.assertEqual(classificacoes[1].inscricao, inscricao_b)
        self.assertEqual(classificacoes[1].posicao, 2)
        self.assertEqual(classificacoes[2].inscricao, inscricao_c)
        self.assertEqual(classificacoes[2].posicao, 3)

    def test_desempate_misto_pontuacoes_diferentes_e_iguais(self):
        """
        Deve classificar corretamente com pontuações diferentes e desempatar
        pela data de inscrição quando as pontuações são iguais.
        """
        # Interessado com maior pontuação
        inscricao_top = InscricaoFactory(
            interessado=InteressadoFactory(nome='Interessado Top'),
            evento=self.evento,
            status=self.status_pendente,
            data_inscricao=timezone.now() - timedelta(minutes=5)
        )
        InscricaoCriterioAtendido.objects.create(
            inscricao=inscricao_top, criterio=self.criterio, pontos_atribuidos=30
        )

        # Inscrições com mesma pontuação, datas diferentes
        inscricao_empate_a = InscricaoFactory(
            interessado=InteressadoFactory(nome='Empate A'),
            evento=self.evento,
            status=self.status_pendente,
            data_inscricao=timezone.now() - timedelta(minutes=4)
        )
        InscricaoCriterioAtendido.objects.create(
            inscricao=inscricao_empate_a, criterio=self.criterio, pontos_atribuidos=20
        )

        inscricao_empate_b = InscricaoFactory(
            interessado=InteressadoFactory(nome='Empate B'),
            evento=self.evento,
            status=self.status_pendente,
            data_inscricao=timezone.now() - timedelta(minutes=3)
        )
        InscricaoCriterioAtendido.objects.create(
            inscricao=inscricao_empate_b, criterio=self.criterio, pontos_atribuidos=20
        )

        # Interessado com pontuação intermediária
        inscricao_meio = InscricaoFactory(
            interessado=InteressadoFactory(nome='Interessado Meio'),
            evento=self.evento,
            status=self.status_pendente,
            data_inscricao=timezone.now() - timedelta(minutes=2)
        )
        InscricaoCriterioAtendido.objects.create(
            inscricao=inscricao_meio, criterio=self.criterio, pontos_atribuidos=25
        )

        ClassificadorService.classificar_evento(self.evento)

        classificacoes = Classificacao.objects.filter(
            inscricao__evento=self.evento
        ).order_by('posicao')

        self.assertEqual(classificacoes.count(), 4)
        self.assertEqual(classificacoes[0].inscricao, inscricao_top)
        self.assertEqual(classificacoes[0].posicao, 1)
        self.assertEqual(classificacoes[1].inscricao, inscricao_meio)
        self.assertEqual(classificacoes[1].posicao, 2)
        self.assertEqual(classificacoes[2].inscricao, inscricao_empate_a)
        self.assertEqual(classificacoes[2].posicao, 3)
        self.assertEqual(classificacoes[3].inscricao, inscricao_empate_b)
        self.assertEqual(classificacoes[3].posicao, 4)

    def test_desempate_com_lista_espera(self):
        """
        Deve aplicar desempate por data de inscrição corretamente
        para classificados e para a lista de espera.
        """
        self.evento.total_vagas = 2  # Apenas 2 vagas para este teste
        self.evento.save()

        # Classificado 1 (maior pontuação)
        inscricao_c1 = InscricaoFactory(
            interessado=InteressadoFactory(nome='Classificado 1'),
            evento=self.evento,
            status=self.status_pendente,
            data_inscricao=timezone.now() - timedelta(minutes=5)
        )
        InscricaoCriterioAtendido.objects.create(
            inscricao=inscricao_c1, criterio=self.criterio, pontos_atribuidos=30
        )

        # Classificado 2 (empate com L1, mas data mais antiga)
        inscricao_c2 = InscricaoFactory(
            interessado=InteressadoFactory(nome='Classificado 2'),
            evento=self.evento,
            status=self.status_pendente,
            data_inscricao=timezone.now() - timedelta(minutes=4)
        )
        InscricaoCriterioAtendido.objects.create(
            inscricao=inscricao_c2, criterio=self.criterio, pontos_atribuidos=20
        )

        # Lista de Espera 1 (empate com C2, mas data mais nova)
        inscricao_l1 = InscricaoFactory(
            interessado=InteressadoFactory(nome='Lista Espera 1'),
            evento=self.evento,
            status=self.status_pendente,
            data_inscricao=timezone.now() - timedelta(minutes=3)
        )
        InscricaoCriterioAtendido.objects.create(
            inscricao=inscricao_l1, criterio=self.criterio, pontos_atribuidos=20
        )

        # Lista de Espera 2 (menor pontuação)
        inscricao_l2 = InscricaoFactory(
            interessado=InteressadoFactory(nome='Lista Espera 2'),
            evento=self.evento,
            status=self.status_pendente,
            data_inscricao=timezone.now() - timedelta(minutes=2)
        )
        InscricaoCriterioAtendido.objects.create(
            inscricao=inscricao_l2, criterio=self.criterio, pontos_atribuidos=10
        )

        ClassificadorService.classificar_evento(self.evento)

        classificacoes = Classificacao.objects.filter(
            inscricao__evento=self.evento
        ).order_by('posicao')

        self.assertEqual(classificacoes.count(), 4)

        # Posição 1: Classificado 1 (maior pontuação)
        self.assertEqual(classificacoes[0].inscricao, inscricao_c1)
        self.assertEqual(classificacoes[0].posicao, 1)
        self.assertTrue(classificacoes[0].classificado)
        self.assertFalse(classificacoes[0].lista_espera)

        # Posição 2: Classificado 2 (empate com L1, mas data mais antiga)
        self.assertEqual(classificacoes[1].inscricao, inscricao_c2)
        self.assertEqual(classificacoes[1].posicao, 2)
        self.assertTrue(classificacoes[1].classificado)
        self.assertFalse(classificacoes[1].lista_espera)

        # Posição 3: Lista Espera 1 (empate com C2, mas data mais nova)
        self.assertEqual(classificacoes[2].inscricao, inscricao_l1)
        self.assertEqual(classificacoes[2].posicao, 3)
        self.assertFalse(classificacoes[2].classificado)
        self.assertTrue(classificacoes[2].lista_espera)

        # Posição 4: Lista Espera 2 (menor pontuação)
        self.assertEqual(classificacoes[3].inscricao, inscricao_l2)
        self.assertEqual(classificacoes[3].posicao, 4)
        self.assertFalse(classificacoes[3].classificado)
        self.assertTrue(classificacoes[3].lista_espera)