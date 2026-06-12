"""
Arquivo: test_services.py
Caminho: apps/dashboard/tests/test_services.py
Finalidade: Testes para os serviços de dashboard.

Atualizações:
 - 10/06/2026 - Criação do arquivo - Implementação inicial dos testes de serviços de dashboard
 - 11/06/2026 - Refatorado com setUp() completo, factories corretas, assertions específicas
              - Corrigido: usar Avaliacao criada automaticamente pelo signal, não criar manualmente
 """


from django.test import TestCase
from django.utils import timezone
from datetime import date, timedelta
from apps.interessados.tests.factories import InteressadoFactory
from apps.eventos.tests.factories import EventoFactory, StatusFactory, TurmaFactory
from apps.dashboard.services import (
    DashboardInteressadosService,
    DashboardEventosService,
    DashboardAcademicoService,
    DashboardProcessoSeletivoService,)
import warnings

# Suprimir warning cosmético de naive datetime em testes
warnings.filterwarnings(
    'ignore',
    category=RuntimeWarning,
    message='.*DateTimeField.*naive datetime.*')

class TestDashboardInteressadosService(TestCase):
    """Testes para DashboardInteressadosService"""
    
    def setUp(self):
        """Criar dados de teste para interessados"""
        from apps.interessados.models import Sexo, Fototipo
        
        # Criar dados base
        self.sexo_m = Sexo.objects.create(nome='Masculino')
        self.sexo_f = Sexo.objects.create(nome='Feminino')
        self.fototipo_1 = Fototipo.objects.create(nome='Tipo I')
        self.fototipo_2 = Fototipo.objects.create(nome='Tipo II')
        
        # Criar interessados com factory
        self.interessado_1 = InteressadoFactory.create(
            sexo=self.sexo_m,
            fototipo=self.fototipo_1,
            escolaridade='SUPERIOR_COMPLETO',
            programa_social=True,
            necessidades_especiais=False,
            data_nascimento=date(1990, 5, 15),
        )
        
        self.interessado_2 = InteressadoFactory.create(
            sexo=self.sexo_f,
            fototipo=self.fototipo_2,
            escolaridade='MEDIO_COMPLETO',
            programa_social=False,
            necessidades_especiais=True,
            pcd_fisica=True,
            data_nascimento=date(1995, 8, 20),
        )
    
    def test_calcular_metricas_gerais(self):
        """Testa cálculo de métricas gerais"""
        metricas = DashboardInteressadosService.calcular_metricas_gerais()
        self.assertIsInstance(metricas, dict)
        self.assertEqual(metricas['total_interessados'], 2)
        self.assertIn('interessados_matriculados', metricas)
        self.assertIn('interessados_sem_matricula', metricas)
    
    def test_calcular_distribuicao_sexo(self):
        """Testa distribuição por sexo"""
        distribuicao = DashboardInteressadosService.calcular_distribuicao_sexo()
        self.assertIsInstance(distribuicao, list)
        self.assertGreater(len(distribuicao), 0)
        if distribuicao:
            self.assertIn('sexo__nome', distribuicao[0])
            self.assertIn('total', distribuicao[0])
            self.assertIn('percentual', distribuicao[0])
    
    def test_calcular_distribuicao_fototipo(self):
        """Testa distribuição por fototipo"""
        distribuicao = DashboardInteressadosService.calcular_distribuicao_fototipo()
        self.assertIsInstance(distribuicao, list)
        self.assertGreater(len(distribuicao), 0)
        if distribuicao:
            self.assertIn('fototipo__nome', distribuicao[0])
            self.assertIn('total', distribuicao[0])
            self.assertIn('percentual', distribuicao[0])
    
    def test_calcular_distribuicao_escolaridade(self):
        """Testa distribuição por escolaridade"""
        distribuicao = DashboardInteressadosService.calcular_distribuicao_escolaridade()
        self.assertIsInstance(distribuicao, list)
        self.assertGreater(len(distribuicao), 0)
        if distribuicao:
            self.assertIn('escolaridade', distribuicao[0])
            self.assertIn('escolaridade_label', distribuicao[0])
            self.assertIn('total', distribuicao[0])
    
    def test_calcular_distribuicao_programas_sociais(self):
        """Testa distribuição de programas sociais"""
        distribuicao = DashboardInteressadosService.calcular_distribuicao_programas_sociais()
        self.assertIsInstance(distribuicao, list)
        self.assertEqual(len(distribuicao), 2)
        self.assertIn('participa', distribuicao[0])
        self.assertIn('total', distribuicao[0])
        self.assertIn('percentual', distribuicao[0])
    
    def test_calcular_distribuicao_deficiencias(self):
        """Testa distribuição de deficiências"""
        distribuicao = DashboardInteressadosService.calcular_distribuicao_deficiencias()
        self.assertIsInstance(distribuicao, list)
        self.assertEqual(len(distribuicao), 2)
        self.assertIn('tipo', distribuicao[0])
        self.assertIn('total', distribuicao[0])
        self.assertIn('percentual', distribuicao[0])
    
    def test_calcular_tipos_deficiencia(self):
        """Testa tipos de deficiência"""
        tipos = DashboardInteressadosService.calcular_tipos_deficiencia()
        self.assertIsInstance(tipos, list)
        if tipos:
            self.assertIn('tipo_deficiencia', tipos[0])
            self.assertIn('total', tipos[0])
    
    def test_calcular_faixas_etarias(self):
        """Testa cálculo de faixas etárias"""
        faixas = DashboardInteressadosService.calcular_faixas_etarias()
        self.assertIsInstance(faixas, list)
        if faixas:
            self.assertIn('faixa', faixas[0])
            self.assertIn('total', faixas[0])
            self.assertIn('percentual', faixas[0])
    
    def test_obter_contexto_completo(self):
        """Testa contexto completo"""
        contexto = DashboardInteressadosService.obter_contexto_completo()
        self.assertIsInstance(contexto, dict)
        self.assertIn('total_interessados', contexto)
        self.assertIn('distribuicao_sexo', contexto)
        self.assertIn('distribuicao_fototipo', contexto)
        self.assertIn('distribuicao_escolaridade', contexto)
        self.assertIn('distribuicao_programas', contexto)
        self.assertIn('distribuicao_deficiencia', contexto)
        self.assertIn('tipos_deficiencia', contexto)
        self.assertIn('faixas_etarias', contexto)


class TestDashboardEventosService(TestCase):
    """Testes para DashboardEventosService"""
    
    def setUp(self):
        """Criar dados de teste para eventos"""
        self.status = StatusFactory.create(nome='Ativo')
        self.evento = EventoFactory.create(status=self.status)
        self.turma = TurmaFactory.create(evento=self.evento)
    
    def test_calcular_metricas_gerais(self):
        """Testa métricas gerais de eventos"""
        metricas = DashboardEventosService.calcular_metricas_gerais()
        self.assertIsInstance(metricas, dict)
        self.assertIn('total_eventos', metricas)
        self.assertIn('total_turmas', metricas)
        self.assertIn('eventos_inscricoes_abertas', metricas)
    
    def test_calcular_turmas_por_status(self):
        """Testa turmas por status"""
        status = DashboardEventosService.calcular_turmas_por_status()
        self.assertIsInstance(status, dict)
        self.assertIn('turmas_futuras', status)
        self.assertIn('turmas_em_andamento', status)
        self.assertIn('turmas_encerradas', status)
    
    def test_calcular_eventos_por_status(self):
        """Testa eventos por status"""
        eventos = DashboardEventosService.calcular_eventos_por_status()
        self.assertIsInstance(eventos, list)
        if eventos:
            self.assertIn('status__nome', eventos[0])
            self.assertIn('total', eventos[0])
    
    def test_calcular_top_eventos_inscricoes(self):
        """Testa top eventos por inscrições"""
        top = DashboardEventosService.calcular_top_eventos_inscricoes()
        self.assertIsInstance(top, list)
    
    def test_obter_contexto_completo(self):
        """Testa contexto completo de eventos"""
        contexto = DashboardEventosService.obter_contexto_completo()
        self.assertIsInstance(contexto, dict)
        self.assertIn('total_eventos', contexto)
        self.assertIn('total_turmas', contexto)
        self.assertIn('eventos_por_status', contexto)
        self.assertIn('top_eventos_inscricoes', contexto)


class TestDashboardAcademicoService(TestCase):
    """Testes para DashboardAcademicoService"""
    
    def setUp(self):
        """Criar dados de teste para avaliações"""
        from apps.academico.models import Matricula, StatusMatricula
        from apps.eventos.models import Evento, Status
        from apps.selecao.models import Inscricao, StatusInscricao
        
        # Criar dados base
        self.status_evento = Status.objects.create(nome='Ativo')
        self.evento = Evento.objects.create(
            nome='Curso Teste',
            status=self.status_evento,
            total_vagas=30,
            data_inicio_inscricao=timezone.now(),
            data_fim_inscricao=timezone.now() + timedelta(days=7),
            data_inicio_evento=timezone.now().date() + timedelta(days=8),
            data_fim_evento=timezone.now().date() + timedelta(days=15),
        )
        
        self.turma = TurmaFactory.create(evento=self.evento)
        self.interessado = InteressadoFactory.create()
        
        # Criar matrícula
        self.status_matricula = StatusMatricula.objects.create(nome='Ativa')
        self.status_inscricao = StatusInscricao.objects.create(nome='Confirmada')
        self.inscricao = Inscricao.objects.create(
            interessado=self.interessado,
            evento=self.evento,
            status=self.status_inscricao,
        )
        
        self.matricula = Matricula.objects.create(
            turma=self.turma,
            interessado=self.interessado,
            inscricao=self.inscricao,
            status=self.status_matricula,
        )
        
        # Avaliacao é criada automaticamente pelo signal
        # Apenas atualizar seus valores
        self.avaliacao = self.matricula.avaliacao
        self.avaliacao.nota_final = 8.5
        self.avaliacao.frequencia = 85.0
        self.avaliacao.aprovado = True
        self.avaliacao.certificado_emitido = True
        self.avaliacao.save()
    
    def test_calcular_metricas_avaliacoes(self):
        """Testa métricas de avaliações"""
        metricas = DashboardAcademicoService.calcular_metricas_avaliacoes()
        self.assertIsInstance(metricas, dict)
        self.assertEqual(metricas['total_avaliacoes'], 1)
        self.assertEqual(metricas['total_aprovados'], 1)
        self.assertEqual(metricas['total_reprovados'], 0)
        self.assertIn('media_notas', metricas)
        self.assertIn('media_frequencia', metricas)
        self.assertIn('certificados_emitidos', metricas)
    
    def test_calcular_taxa_aprovacao(self):
        """Testa taxa de aprovação"""
        taxa = DashboardAcademicoService.calcular_taxa_aprovacao()
        self.assertEqual(taxa, 100.0)
    
    def test_calcular_top_cursos_aprovados(self):
        """Testa top cursos aprovados"""
        top = DashboardAcademicoService.calcular_top_cursos_aprovados()
        self.assertIsInstance(top, list)
    
    def test_obter_contexto_completo(self):
        """Testa contexto completo acadêmico"""
        contexto = DashboardAcademicoService.obter_contexto_completo()
        self.assertIsInstance(contexto, dict)
        self.assertIn('total_avaliacoes', contexto)
        self.assertIn('taxa_aprovacao', contexto)
        self.assertIn('top_cursos_aprovados', contexto)


class TestDashboardProcessoSeletivoService(TestCase):
    """Testes para DashboardProcessoSeletivoService"""
    
    def setUp(self):
        """Criar dados de teste para processo seletivo"""
        from apps.selecao.models import Inscricao, Classificacao, StatusInscricao
        from apps.eventos.models import Evento, Status
        
        # Criar dados base
        self.status_evento = Status.objects.create(nome='Ativo')
        self.evento = Evento.objects.create(
            nome='Seleção 2026',
            status=self.status_evento,
            total_vagas=30,
            data_inicio_inscricao=timezone.now(),
            data_fim_inscricao=timezone.now() + timedelta(days=7),
            data_inicio_evento=timezone.now().date() + timedelta(days=8),
            data_fim_evento=timezone.now().date() + timedelta(days=15),
        )
        
        self.status_inscricao = StatusInscricao.objects.create(nome='Confirmada')
        self.interessado = InteressadoFactory.create()
        
        # Criar inscrição - NÃO passar data_inscricao (auto_now_add faz isso)
        self.inscricao = Inscricao.objects.create(
            evento=self.evento,
            interessado=self.interessado,
            status=self.status_inscricao,
            # data_inscricao=timezone.now(), retirar para evitar warning de naive datetime em testes
        )
        
        # Criar classificação
        self.classificacao = Classificacao.objects.create(
            inscricao=self.inscricao,
            pontuacao_total=85.5,
            classificado=True,
        )
    
    def test_calcular_metricas_inscricoes(self):
        """Testa métricas de inscrições"""
        metricas = DashboardProcessoSeletivoService.calcular_metricas_inscricoes()
        self.assertIsInstance(metricas, dict)
        self.assertIn('total_inscricoes', metricas)
        self.assertIn('inscricoes_recentes', metricas)
    
    def test_calcular_metricas_classificacoes(self):
        """Testa métricas de classificações"""
        metricas = DashboardProcessoSeletivoService.calcular_metricas_classificacoes()
        self.assertIsInstance(metricas, dict)
        self.assertEqual(metricas['total_classificacoes'], 1)
        self.assertEqual(metricas['classificados'], 1)
        self.assertIn('taxa_classificacao', metricas)
    
    def test_calcular_top_eventos_inscricoes(self):
        """Testa top eventos por inscrições"""
        top = DashboardProcessoSeletivoService.calcular_top_eventos_inscricoes()
        self.assertIsInstance(top, list)
    
    def test_obter_contexto_completo(self):
        """Testa contexto completo de processo seletivo"""
        contexto = DashboardProcessoSeletivoService.obter_contexto_completo()
        self.assertIsInstance(contexto, dict)
        self.assertIn('total_inscricoes', contexto)
        self.assertIn('total_classificacoes', contexto)
        self.assertIn('top_eventos_inscricoes', contexto)



