"""
Arquivo: test_services.py
Caminho: apps/selecao/tests/test_services.py
Finalidade: Testar os serviços relacionados à classificação de inscrições para eventos
Atualizações:
 - 27/03/2026 - Testes iniciais de serviços
 - 08/04/2026 - Adicionados 3 testes de desempate
 - 15/05/2026 - Inclusão de cabeçalho
 - 18/05/2026 - Refatoração completa de 2 testes
                test_calcular_pontuacao_inscricao_zero (evento sem critérios)
                test_desempate_misto_pontuacoes_diferentes_e_iguais (critérios com pontos diferentes)
 - 27/05/2026 - Refatoração para incluir mais cenários de teste, como classificação sem inscrições, chamada repetida e pontuação com múltiplos critérios acumulados.
 - 08/06/2026 - Refatoração para pytest (unittest → pytest)
 - 10/06/2026 - Refatoração completa para pytest puro com fixtures reutilizáveis
              - Correção: adicionados status_classificado e status_lista_espera aos testes de classificação
"""

import pytest
from django.utils import timezone
from datetime import timedelta
from decimal import Decimal
from apps.selecao.tests.factories import (
    InscricaoFactory,
    StatusInscricaoFactory,
    ClassificacaoFactory
)
from apps.interessados.tests.factories import InteressadoFactory
from apps.interessados.models import Fototipo
from apps.eventos.tests.factories import (
    EventoFactory,
    EventoCriterioFactory,
    CriterioFactory
)
from apps.selecao.models import Inscricao, Classificacao, InscricaoCriterioAtendido
from apps.selecao.services import ClassificadorService

pytestmark = pytest.mark.django_db

@pytest.fixture
def status_pendente():
    return StatusInscricaoFactory(nome='Pendente')

@pytest.fixture
def status_classificado():
    return StatusInscricaoFactory(nome='Classificado')

@pytest.fixture
def status_lista_espera():
    return StatusInscricaoFactory(nome='Lista de Espera')

@pytest.fixture
def criterio():
    return CriterioFactory(nome='PCD', tipo_criterio='PONTUACAO', pontos=10)

@pytest.fixture
def evento(criterio):
    evento = EventoFactory(total_vagas=5)
    EventoCriterioFactory(evento=evento, criterio=criterio)
    return evento

class TestClassificadorServicePontuacao:
    def test_calcular_pontuacao_inscricao_com_criterios(self, evento, status_pendente):
        interessado = InteressadoFactory()
        inscricao = InscricaoFactory(interessado=interessado, evento=evento, status=status_pendente)
        pontuacao = ClassificadorService.calcular_pontuacao_inscricao(inscricao)
        assert pontuacao == Decimal('10.00')

    def test_calcular_pontuacao_inscricao_zero(self, status_pendente):
        evento_sem_criterios = EventoFactory(nome='Evento Sem Critérios', total_vagas=10)
        interessado = InteressadoFactory()
        inscricao = InscricaoFactory(interessado=interessado, evento=evento_sem_criterios, status=status_pendente)
        pontuacao = ClassificadorService.calcular_pontuacao_inscricao(inscricao)
        assert pontuacao == Decimal('0')

    def test_calcular_pontuacao_multiplos_criterios(self, status_pendente):
        evento = EventoFactory(total_vagas=5)
        criterio1 = CriterioFactory(nome='Criterio1', tipo_criterio='PONTUACAO', pontos=10, categoria='OUTRO')
        criterio2 = CriterioFactory(nome='Criterio2', tipo_criterio='PONTUACAO', pontos=20, categoria='OUTRO')
        EventoCriterioFactory(evento=evento, criterio=criterio1)
        EventoCriterioFactory(evento=evento, criterio=criterio2)
        interessado = InteressadoFactory()
        inscricao = InscricaoFactory(evento=evento, interessado=interessado, status=status_pendente)
        InscricaoCriterioAtendido.objects.create(inscricao=inscricao, criterio=criterio1, pontos_atribuidos=Decimal('10.00'), validado=True)
        InscricaoCriterioAtendido.objects.create(inscricao=inscricao, criterio=criterio2, pontos_atribuidos=Decimal('20.00'), validado=True)
        pontuacao = ClassificadorService.calcular_pontuacao_inscricao(inscricao)
        assert pontuacao == Decimal('30.00')

    def test_classificar_sem_eventocriterio_vinculado(self, status_pendente):
        evento = EventoFactory(total_vagas=5)
        CriterioFactory(nome='Criterio', tipo_criterio='PONTUACAO', pontos=10)
        inscricao = InscricaoFactory(evento=evento, status=status_pendente)
        pontuacao = ClassificadorService.calcular_pontuacao_inscricao(inscricao)
        assert pontuacao == Decimal('0.00')

class TestClassificadorServiceClassificacao:
    def test_classificar_evento_atribui_posicoes(self, evento, status_pendente, status_classificado, status_lista_espera):
        for i in range(3):
            InscricaoFactory(evento=evento, status=status_pendente)
        resultado = ClassificadorService.classificar_evento(evento)
        assert resultado['sucesso'] is True
        classificacoes = Classificacao.objects.filter(inscricao__evento=evento).order_by('posicao')
        assert classificacoes[0].posicao == 1
        assert classificacoes[1].posicao == 2
        assert classificacoes[2].posicao == 3

    def test_classificar_evento_classifica_dentro_vagas(self, status_pendente, status_classificado, status_lista_espera, criterio):
        evento = EventoFactory(total_vagas=2)
        EventoCriterioFactory(evento=evento, criterio=criterio)
        InscricaoFactory(evento=evento, status=status_pendente)
        InscricaoFactory(evento=evento, status=status_pendente)
        ClassificadorService.classificar_evento(evento)
        classificacoes = Classificacao.objects.filter(inscricao__evento=evento).order_by('posicao')
        assert classificacoes[0].classificado is True
        assert classificacoes[1].classificado is True

    def test_classificar_evento_lista_espera(self, status_pendente, status_classificado, status_lista_espera, criterio):
        evento = EventoFactory(total_vagas=2)
        EventoCriterioFactory(evento=evento, criterio=criterio)
        InscricaoFactory(evento=evento, status=status_pendente)
        InscricaoFactory(evento=evento, status=status_pendente)
        InscricaoFactory(evento=evento, status=status_pendente)
        ClassificadorService.classificar_evento(evento)
        classificacoes = Classificacao.objects.filter(inscricao__evento=evento).order_by('posicao')
        assert classificacoes[2].classificado is False
        assert classificacoes[2].lista_espera is True

    def test_classificar_evento_atualiza_status_inscricao(self, evento, status_pendente, status_classificado, status_lista_espera):
        inscricao = InscricaoFactory(evento=evento, status=status_pendente)
        ClassificadorService.classificar_evento(evento)
        inscricao.refresh_from_db()
        assert inscricao.status.nome == 'Classificado'

    def test_classificar_evento_com_criterios(self, evento, status_pendente, status_classificado, status_lista_espera):
        InscricaoFactory(evento=evento, status=status_pendente)
        resultado = ClassificadorService.classificar_evento(evento)
        assert resultado['sucesso'] is True
        assert 'mensagem' in resultado
        assert 'total_processadas' in resultado

    def test_classificar_evento_zero_inscricoes(self, status_classificado, status_lista_espera):
        evento = EventoFactory(total_vagas=5)
        resultado = ClassificadorService.classificar_evento(evento)
        assert resultado['sucesso'] is False
        assert resultado['total_processadas'] == 0
        assert Classificacao.objects.filter(inscricao__evento=evento).count() == 0

    def test_classificar_evento_chamada_repetida(self, status_pendente, status_classificado, status_lista_espera):
        evento = EventoFactory(total_vagas=5)
        for i in range(3):
            InscricaoFactory(evento=evento, status=status_pendente)
        ClassificadorService.classificar_evento(evento)
        ClassificadorService.classificar_evento(evento)
        classificacoes = Classificacao.objects.filter(inscricao__evento=evento).order_by('posicao')
        assert classificacoes.count() == 3
        assert classificacoes[0].posicao == 1
        assert classificacoes[1].posicao == 2
        assert classificacoes[2].posicao == 3

    def test_classificar_evento_exatamente_1_vaga(self, status_pendente, status_classificado, status_lista_espera):
        evento = EventoFactory(total_vagas=1)
        criterio = CriterioFactory(nome='Criterio', tipo_criterio='PONTUACAO', pontos=5)
        EventoCriterioFactory(evento=evento, criterio=criterio)
        inscricoes = []
        for i in range(3):
            insc = InscricaoFactory(evento=evento, status=status_pendente, data_inscricao=timezone.now() + timedelta(hours=i))
            InscricaoCriterioAtendido.objects.create(inscricao=insc, criterio=criterio, pontos_atribuidos=Decimal('5.00'), validado=True)
            inscricoes.append(insc)
        ClassificadorService.classificar_evento(evento)
        classificacoes = Classificacao.objects.filter(inscricao__evento=evento).order_by('posicao')
        assert classificacoes[0].classificado is True
        assert classificacoes[0].lista_espera is False
        assert classificacoes[1].classificado is False
        assert classificacoes[1].lista_espera is True
        assert classificacoes[2].classificado is False
        assert classificacoes[2].lista_espera is True

class TestClassificadorServiceDesempate:
    # def setup_method(self):
    #         """Executado antes de CADA teste desta classe."""
    #         # Garante que nenhum lixo de testes anteriores interfira neste cenário sensível de ordenação
    #         Classificacao.objects.all().delete()
    #         Inscricao.objects.all().delete()    

    @pytest.fixture(autouse=True)
    def limpar_inscricoes(self):
        """Executado antes de cada teste: limpa registros que podem interferir na ordenação."""
        Classificacao.objects.all().delete()
        Inscricao.objects.all().delete()
        yield  # teste executa aqui
        # rollback automático pelo pytest-django, não precisa limpar depois
            
    def test_desempate_por_data_inscricao_igual_pontuacao(self, status_pendente, status_classificado, status_lista_espera):
        evento = EventoFactory(total_vagas=5)
        # Categoria permissiva: sempre atende, garantindo pontuacao igual
        criterio = CriterioFactory(
            nome='Criterio Teste',
            tipo_criterio='PONTUACAO',
            pontos=10,
            categoria='OUTRO',
        )
        EventoCriterioFactory(evento=evento, criterio=criterio)
        agora = timezone.now()
        inscricao_primeira = InscricaoFactory(
            evento=evento, status=status_pendente,
            data_inscricao=agora - timedelta(minutes=5),
        )
        inscricao_segunda = InscricaoFactory(
            evento=evento, status=status_pendente,
            data_inscricao=agora,
        )
        ClassificadorService.classificar_evento(evento)
        classificacoes = Classificacao.objects.filter(
            inscricao__evento=evento
        ).order_by('posicao')
        assert classificacoes[0].inscricao == inscricao_primeira
        assert classificacoes[0].posicao == 1
        assert classificacoes[1].inscricao == inscricao_segunda
        assert classificacoes[1].posicao == 2

    def test_desempate_com_lista_espera(self, status_pendente, status_classificado, status_lista_espera, criterio):
        evento = EventoFactory(total_vagas=1)
        EventoCriterioFactory(evento=evento, criterio=criterio)
        inscricao_primeira = InscricaoFactory(evento=evento, status=status_pendente, data_inscricao=timezone.now() - timedelta(minutes=2))
        inscricao_segunda = InscricaoFactory(evento=evento, status=status_pendente, data_inscricao=timezone.now() - timedelta(minutes=1))
        ClassificadorService.classificar_evento(evento)
        classificacoes = Classificacao.objects.filter(inscricao__evento=evento).order_by('posicao')
        assert classificacoes[0].classificado is True
        assert classificacoes[0].lista_espera is False
        assert classificacoes[1].classificado is False
        assert classificacoes[1].lista_espera is True

    def test_desempate_misto_pontuacoes_diferentes_e_iguais(self, status_pendente, status_classificado, status_lista_espera):
        evento = EventoFactory(nome='Evento Desempate Misto', total_vagas=4)
        criterio_pcd = CriterioFactory(nome='Pessoa com Deficiência', pontos=30, tipo_criterio='PONTUACAO', categoria='PCD')
        criterio_nis = CriterioFactory(nome='Programa Social', pontos=25, tipo_criterio='PONTUACAO', categoria='NIS')
        criterio_cota = CriterioFactory(nome='Cota Racial', pontos=10, tipo_criterio='PONTUACAO', categoria='COTA_RACIAL')
        EventoCriterioFactory(evento=evento, criterio=criterio_pcd, prioridade=1, ativo=True)
        EventoCriterioFactory(evento=evento, criterio=criterio_nis, prioridade=2, ativo=True)
        EventoCriterioFactory(evento=evento, criterio=criterio_cota, prioridade=3, ativo=True)
        interessado_top = InteressadoFactory(nome='Interessado Top', necessidades_especiais=True, programa_social=False, fototipo=None)
        inscricao_top = InscricaoFactory(interessado=interessado_top, evento=evento, status=status_pendente, data_inscricao=timezone.now() - timedelta(minutes=5))
        interessado_meio = InteressadoFactory(nome='Interessado Meio', necessidades_especiais=True, programa_social=True, fototipo=None)
        inscricao_meio = InscricaoFactory(interessado=interessado_meio, evento=evento, status=status_pendente, data_inscricao=timezone.now() - timedelta(minutes=2))
        interessado_empate_a = InteressadoFactory(nome='Empate A', necessidades_especiais=False, programa_social=True, fototipo=None)
        inscricao_empate_a = InscricaoFactory(interessado=interessado_empate_a, evento=evento, status=status_pendente, data_inscricao=timezone.now() - timedelta(minutes=4))
        interessado_empate_b = InteressadoFactory(nome='Empate B', necessidades_especiais=False, programa_social=True, fototipo=None)
        inscricao_empate_b = InscricaoFactory(interessado=interessado_empate_b, evento=evento, status=status_pendente, data_inscricao=timezone.now() - timedelta(minutes=3))
        ClassificadorService.classificar_evento(evento)
        classificacoes = Classificacao.objects.filter(inscricao__evento=evento).order_by('posicao')
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


class TestClassificadorServiceAtendeCriterio:
    """Testes para o metodo privado _atende_criterio."""

    def test_pcd_atende(self, status_pendente):
        criterio = CriterioFactory(categoria='PCD')
        interessado = InteressadoFactory(necessidades_especiais=True)
        inscricao = InscricaoFactory(interessado=interessado, status=status_pendente)
        assert ClassificadorService._atende_criterio(inscricao, criterio) is True

    def test_pcd_nao_atende(self, status_pendente):
        criterio = CriterioFactory(categoria='PCD')
        interessado = InteressadoFactory(necessidades_especiais=False)
        inscricao = InscricaoFactory(interessado=interessado, status=status_pendente)
        assert ClassificadorService._atende_criterio(inscricao, criterio) is False

    def test_nis_atende(self, status_pendente):
        criterio = CriterioFactory(categoria='NIS')
        interessado = InteressadoFactory(programa_social=True)
        inscricao = InscricaoFactory(interessado=interessado, status=status_pendente)
        assert ClassificadorService._atende_criterio(inscricao, criterio) is True

    def test_nis_nao_atende(self, status_pendente):
        criterio = CriterioFactory(categoria='NIS')
        interessado = InteressadoFactory(programa_social=False)
        inscricao = InscricaoFactory(interessado=interessado, status=status_pendente)
        assert ClassificadorService._atende_criterio(inscricao, criterio) is False

    def test_jovem_atende(self, status_pendente):
        criterio = CriterioFactory(categoria='JOVEM')
        interessado = InteressadoFactory(
            data_nascimento=timezone.localdate() - timedelta(days=365 * 20)
        )
        inscricao = InscricaoFactory(interessado=interessado, status=status_pendente)
        assert ClassificadorService._atende_criterio(inscricao, criterio) is True

    def test_jovem_fora_faixa(self, status_pendente):
        criterio = CriterioFactory(categoria='JOVEM')
        interessado = InteressadoFactory(
            data_nascimento=timezone.localdate() - timedelta(days=365 * 30)
        )
        inscricao = InscricaoFactory(interessado=interessado, status=status_pendente)
        assert ClassificadorService._atende_criterio(inscricao, criterio) is False

    def test_jovem_sem_data(self, status_pendente):
        criterio = CriterioFactory(categoria='JOVEM')
        interessado = InteressadoFactory(data_nascimento=None)
        inscricao = InscricaoFactory(interessado=interessado, status=status_pendente)
        assert ClassificadorService._atende_criterio(inscricao, criterio) is False

    def test_idoso_atende(self, status_pendente):
        criterio = CriterioFactory(categoria='IDOSO')
        interessado = InteressadoFactory(
            data_nascimento=timezone.localdate() - timedelta(days=365 * 60)
        )
        inscricao = InscricaoFactory(interessado=interessado, status=status_pendente)
        assert ClassificadorService._atende_criterio(inscricao, criterio) is True

    def test_idoso_abaixo(self, status_pendente):
        criterio = CriterioFactory(categoria='IDOSO')
        interessado = InteressadoFactory(
            data_nascimento=timezone.localdate() - timedelta(days=365 * 30)
        )
        inscricao = InscricaoFactory(interessado=interessado, status=status_pendente)
        assert ClassificadorService._atende_criterio(inscricao, criterio) is False

    def test_idoso_sem_data(self, status_pendente):
        criterio = CriterioFactory(categoria='IDOSO')
        interessado = InteressadoFactory(data_nascimento=None)
        inscricao = InscricaoFactory(interessado=interessado, status=status_pendente)
        assert ClassificadorService._atende_criterio(inscricao, criterio) is False

    def test_cota_racial_atende(self, status_pendente):
        criterio = CriterioFactory(categoria='COTA_RACIAL')
        # O codigo verifica fototipo.id in [2, 3, 5]
        fototipo = Fototipo.objects.create(id=2, nome='Preta', descricao='Teste')
        interessado = InteressadoFactory(fototipo=fototipo)
        inscricao = InscricaoFactory(interessado=interessado, status=status_pendente)
        assert ClassificadorService._atende_criterio(inscricao, criterio) is True

    def test_cota_racial_nao_atende(self, status_pendente):
        criterio = CriterioFactory(categoria='COTA_RACIAL')
        # id=1 nao esta na lista [2, 3, 5]
        fototipo = Fototipo.objects.create(id=1, nome='Branca', descricao='Teste')
        interessado = InteressadoFactory(fototipo=fototipo)
        inscricao = InscricaoFactory(interessado=interessado, status=status_pendente)
        assert ClassificadorService._atende_criterio(inscricao, criterio) is False

    def test_cota_racial_sem_fototipo(self, status_pendente):
        criterio = CriterioFactory(categoria='COTA_RACIAL')
        interessado = InteressadoFactory(fototipo=None)
        inscricao = InscricaoFactory(interessado=interessado, status=status_pendente)
        assert ClassificadorService._atende_criterio(inscricao, criterio) is False

    def test_escolaridade_fund_inc_atende(self, status_pendente):
        criterio = CriterioFactory(categoria='ESC_FUND_INC')
        interessado = InteressadoFactory(escolaridade='FUNDAMENTAL_INCOMPLETO')
        inscricao = InscricaoFactory(interessado=interessado, status=status_pendente)
        assert ClassificadorService._atende_criterio(inscricao, criterio) is True

    def test_escolaridade_fund_inc_nao_atende(self, status_pendente):
        criterio = CriterioFactory(categoria='ESC_FUND_INC')
        interessado = InteressadoFactory(escolaridade='MEDIO_COMPLETO')
        inscricao = InscricaoFactory(interessado=interessado, status=status_pendente)
        assert ClassificadorService._atende_criterio(inscricao, criterio) is False

    def test_escolaridade_fund_comp_atende(self, status_pendente):
        criterio = CriterioFactory(categoria='ESC_FUND_COMP')
        interessado = InteressadoFactory(escolaridade='FUNDAMENTAL_COMPLETO')
        inscricao = InscricaoFactory(interessado=interessado, status=status_pendente)
        assert ClassificadorService._atende_criterio(inscricao, criterio) is True

    def test_escolaridade_medio_inc_atende(self, status_pendente):
        criterio = CriterioFactory(categoria='ESC_MEDIO_INC')
        interessado = InteressadoFactory(escolaridade='MEDIO_INCOMPLETO')
        inscricao = InscricaoFactory(interessado=interessado, status=status_pendente)
        assert ClassificadorService._atende_criterio(inscricao, criterio) is True

    def test_escolaridade_medio_comp_atende(self, status_pendente):
        criterio = CriterioFactory(categoria='ESC_MEDIO_COMP')
        interessado = InteressadoFactory(escolaridade='MEDIO_COMPLETO')
        inscricao = InscricaoFactory(interessado=interessado, status=status_pendente)
        assert ClassificadorService._atende_criterio(inscricao, criterio) is True

    def test_categoria_desconhecida_atende(self, status_pendente):
        criterio = CriterioFactory(categoria='CATEGORIA_INEXISTENTE')
        interessado = InteressadoFactory()
        inscricao = InscricaoFactory(interessado=interessado, status=status_pendente)
        assert ClassificadorService._atende_criterio(inscricao, criterio) is True

class TestClassificadorServiceProcessamento:
    """Testes para o metodo processar_inscricao."""

    def test_processar_inscricao_cria_classificacao(self, evento):
        inscricao = InscricaoFactory(evento=evento)
        ClassificadorService.processar_inscricao(inscricao)
        classificacao = Classificacao.objects.get(inscricao=inscricao)
        assert classificacao.pontuacao_total == Decimal('10.00')

    def test_processar_inscricao_atualiza_existente(self, evento):
        inscricao = InscricaoFactory(evento=evento)
        ClassificadorService.processar_inscricao(inscricao)
        # Segunda chamada deve atualizar, nao criar duplicata
        ClassificadorService.processar_inscricao(inscricao)
        count = Classificacao.objects.filter(inscricao=inscricao).count()
        assert count == 1

    def test_processar_inscricao_cria_criterio_atendido(self, evento):
        inscricao = InscricaoFactory(evento=evento)
        ClassificadorService.processar_inscricao(inscricao)
        atendidos = InscricaoCriterioAtendido.objects.filter(inscricao=inscricao)
        assert atendidos.count() >= 1

    def test_processar_inscricao_sem_criterios(self, status_pendente):
        evento = EventoFactory(total_vagas=5)
        inscricao = InscricaoFactory(evento=evento, status=status_pendente)
        ClassificadorService.processar_inscricao(inscricao)
        classificacao = Classificacao.objects.get(inscricao=inscricao)
        assert classificacao.pontuacao_total == Decimal('0.00')

class TestClassificadorServiceDesfazer:
    """Testes para o metodo desfazer_classificacao_evento."""

    def test_desfazer_classificacao_com_dados(self, evento, status_pendente, status_classificado, status_lista_espera):
        InscricaoFactory(evento=evento, status=status_pendente)
        InscricaoFactory(evento=evento, status=status_pendente)
        ClassificadorService.classificar_evento(evento)
        resultado = ClassificadorService.desfazer_classificacao_evento(evento)
        assert resultado['sucesso'] is True
        assert resultado['total_desfeitas'] == 2
        assert Classificacao.objects.filter(inscricao__evento=evento).count() == 0

    def test_desfazer_classificacao_sem_dados(self, status_pendente):
        evento = EventoFactory(total_vagas=5)
        resultado = ClassificadorService.desfazer_classificacao_evento(evento)
        assert resultado['sucesso'] is True
        assert resultado['total_desfeitas'] == 0

    def test_desfazer_classificacao_reseta_status(self, evento, status_pendente, status_classificado, status_lista_espera):
        inscricao = InscricaoFactory(evento=evento, status=status_pendente)
        ClassificadorService.classificar_evento(evento)
        inscricao.refresh_from_db()
        assert inscricao.status.nome == 'Classificado'
        ClassificadorService.desfazer_classificacao_evento(evento)
        inscricao.refresh_from_db()
        assert inscricao.status.nome == 'Pendente'


        