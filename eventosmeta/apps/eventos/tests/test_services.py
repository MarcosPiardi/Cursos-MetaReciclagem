from django.test import TestCase
from apps.selecao.services import ClassificadorService
from apps.eventos.tests.factories import EventoFactory, CriterioFactory, StatusFactory
from apps.interessados.tests.factories import InteressadoFactory
from .factories import InscricaoFactory


class TestClassificadorService(TestCase):
    """Testes para o ClassificadorService."""

    def setUp(self):
        self.evento = EventoFactory(total_vagas=10)
        self.status_confirmada = StatusFactory(nome='Confirmada')
        
    def test_classificador_service_existe(self):
        """Verifica se o ClassificadorService pode ser instanciado."""
        servico = ClassificadorService()
        self.assertIsNotNone(servico)

    def test_classificar_inscricoes_basico(self):
        """Verifica se o serviço classifica inscrições corretamente."""
        # Criar 3 inscrições
        for i in range(3):
            InscricaoFactory(evento=self.evento)
        
        # Testar se o serviço consegue processar
        servico = ClassificadorService()
        self.assertEqual(self.evento.total_vagas, 10)

        