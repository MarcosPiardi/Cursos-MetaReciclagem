'''
Arquivo: test_popular_dados_iniciais.py
Caminho: apps/scripts_admin/management/commands/tests/test_popular_dados_iniciais.py
Finalidade: Testes unitários para o comando de gestão popular_dados_iniciais.
Data: 01/06/2026 - v1.0 - Criação dos testes (todos os 8 cenários).
Atualizações:

'''


import re
from io import StringIO
from django.core.management import call_command
from django.test import TestCase
from apps.eventos.models import Status
from apps.eventos.models import Criterio
from apps.interessados.models import Fototipo, Sexo
from apps.selecao.models import StatusInscricao
from apps.academico.models import StatusMatricula

def _limpar_ansi(texto):
    return re.sub(r'\x1b\[[0-9;]*m', '', texto)

class BaseCommandTest(TestCase):
    def _rodar_comando(self):
        out = StringIO()
        call_command('popular_dados_iniciais', stdout=out)
        return _limpar_ansi(out.getvalue())

class PopularDadosIniciaisComandoTest(BaseCommandTest):
    def test_comando_executa_sem_erro(self): self._rodar_comando()
    def test_comando_retorna_string(self): self.assertIsInstance(self._rodar_comando(), str)
    def test_comando_nao_vazio(self): self.assertTrue(len(self._rodar_comando()) > 0)

class PopularDadosIniciaisStatusEventosTest(BaseCommandTest):
    def setUp(self): self._rodar_comando()
    def test_status_planejamento(self): self.assertTrue(Status.objects.filter(nome='Planejamento').exists())
    def test_status_inscricoes_abertas(self): self.assertTrue(Status.objects.filter(nome='Inscrições Abertas').exists())
    def test_status_inscricoes_encerradas(self): self.assertTrue(Status.objects.filter(nome='Inscrições Encerradas').exists())
    def test_status_em_classificacao(self): self.assertTrue(Status.objects.filter(nome='Em Classificação').exists())
    def test_status_resultado_divulgado(self): self.assertTrue(Status.objects.filter(nome='Resultado Divulgado').exists())
    def test_status_em_andamento(self): self.assertTrue(Status.objects.filter(nome='Em Andamento').exists())
    def test_status_finalizado(self): self.assertTrue(Status.objects.filter(nome='Finalizado').exists())
    def test_status_cancelado(self): self.assertTrue(Status.objects.filter(nome='Cancelado').exists())
    def test_total_status_eventos(self): self.assertEqual(Status.objects.count(), 8)

class PopularDadosIniciaisStatusInscricoesTest(BaseCommandTest):
    def setUp(self): self._rodar_comando()
    def test_status_pendente(self): self.assertTrue(StatusInscricao.objects.filter(nome='Pendente').exists())
    def test_status_classificado(self): self.assertTrue(StatusInscricao.objects.filter(nome='Classificado').exists())
    def test_status_confirmada(self): self.assertTrue(StatusInscricao.objects.filter(nome='Confirmada').exists())
    def test_status_lista_espera(self): self.assertTrue(StatusInscricao.objects.filter(nome='Lista de Espera').exists())
    def test_status_cancelada(self): self.assertTrue(StatusInscricao.objects.filter(nome='Cancelada').exists())
    def test_status_expirada(self): self.assertTrue(StatusInscricao.objects.filter(nome='Expirada').exists())
    def test_status_desistente(self): self.assertTrue(StatusInscricao.objects.filter(nome='Desistente').exists())
    def test_status_nao_localizado(self): self.assertTrue(StatusInscricao.objects.filter(nome='Não localizado para confirmar matricula').exists())
    def test_total_status_inscricoes(self): self.assertEqual(StatusInscricao.objects.count(), 8)

class PopularDadosIniciaisStatusMatriculasTest(BaseCommandTest):
    def setUp(self): self._rodar_comando()
    def test_status_pendente(self): self.assertTrue(StatusMatricula.objects.filter(nome='Pendente').exists())
    def test_status_ativa(self): self.assertTrue(StatusMatricula.objects.filter(nome='Ativa').exists())
    def test_status_concluida(self): self.assertTrue(StatusMatricula.objects.filter(nome='Concluída').exists())
    def test_status_trancada(self): self.assertTrue(StatusMatricula.objects.filter(nome='Trancada').exists())
    def test_status_cancelada(self): self.assertTrue(StatusMatricula.objects.filter(nome='Cancelada').exists())
    def test_total_status_matriculas(self): self.assertEqual(StatusMatricula.objects.count(), 5)

class PopularDadosIniciaisCriteriosTest(BaseCommandTest):
    def setUp(self): self._rodar_comando()
    def test_criterio_pcd(self): self.assertTrue(Criterio.objects.filter(codigo='PCD').exists())
    def test_criterio_programa_social(self): self.assertTrue(Criterio.objects.filter(codigo='PROGRAMA_SOCIAL').exists())
    def test_criterio_jovem(self): self.assertTrue(Criterio.objects.filter(codigo='JOVEM').exists())
    def test_criterio_idoso(self): self.assertTrue(Criterio.objects.filter(codigo='IDOSO').exists())
    def test_criterio_ensino_fundamental(self): self.assertTrue(Criterio.objects.filter(codigo='ENSINO_FUNDAMENTAL').exists())
    def test_criterio_renda_baixa(self): self.assertTrue(Criterio.objects.filter(codigo='RENDA_BAIXA').exists())
    def test_criterio_cota_racial(self): self.assertTrue(Criterio.objects.filter(codigo='COTA_RACIAL').exists())

class PopularDadosIniciaisSexoTest(BaseCommandTest):
    def setUp(self): self._rodar_comando()
    def test_sexo_masculino(self): self.assertTrue(Sexo.objects.filter(nome='Masculino').exists())
    def test_sexo_feminino(self): self.assertTrue(Sexo.objects.filter(nome='Feminino').exists())
    def test_sexo_outro(self): self.assertTrue(Sexo.objects.filter(nome='Outro').exists())
    def test_sexo_nao_informar(self): self.assertTrue(Sexo.objects.filter(nome='Prefiro não informar').exists())
    def test_total_sexo(self): self.assertEqual(Sexo.objects.count(), 4)

class PopularDadosIniciaisFototipesTest(BaseCommandTest):
    def setUp(self): self._rodar_comando()
    def test_fototipo_branca(self): self.assertTrue(Fototipo.objects.filter(nome='Branca').exists())
    def test_fototipo_preta(self): self.assertTrue(Fototipo.objects.filter(nome='Preta').exists())
    def test_fototipo_parda(self): self.assertTrue(Fototipo.objects.filter(nome='Parda').exists())
    def test_fototipo_amarela(self): self.assertTrue(Fototipo.objects.filter(nome='Amarela').exists())
    def test_fototipo_indigena(self): self.assertTrue(Fototipo.objects.filter(nome='Indígena').exists())
    def test_total_fototipos(self): self.assertEqual(Fototipo.objects.count(), 5)

class PopularDadosIniciaisIntegracaoTest(BaseCommandTest):
    def test_todos_modelos_populados(self):
        self._rodar_comando()
        self.assertTrue(Status.objects.exists())
        self.assertTrue(StatusInscricao.objects.exists())
        self.assertTrue(StatusMatricula.objects.exists())
    def test_contagem_total_registros(self):
        self._rodar_comando()
        total = Status.objects.count() + StatusInscricao.objects.count() + StatusMatricula.objects.count() + Criterio.objects.count() + Sexo.objects.count() + Fototipo.objects.count()
        self.assertEqual(total, 8 + 8 + 5 + 7 + 4 + 5)
    def test_integridade_dados(self):
        self._rodar_comando()
        self.assertIsNotNone(Status.objects.get(nome='Planejamento'))

class PopularDadosIniciaisIdempotenciaTest(BaseCommandTest):
    def test_execucao_dupla_nao_duplica_dados(self):
        self._rodar_comando()
        self._rodar_comando()
        self.assertEqual(Status.objects.count(), 8)
    def test_execucao_tripla_nao_duplica_dados(self):
        self._rodar_comando()
        self._rodar_comando()
        self._rodar_comando()
        self.assertEqual(Status.objects.count(), 8)

class PopularDadosIniciaisSaidaTest(BaseCommandTest):
    def test_saida_contem_sucesso(self):
        output = self._rodar_comando()
        self.assertIn('sucesso', output.lower())
    def test_saida_contem_nome_comando(self):
        output = self._rodar_comando()
        self.assertIn('populando', output.lower())
    def test_saida_nao_contem_ansi(self):
        output = self._rodar_comando()
        self.assertNotIn('\x1b', output)


