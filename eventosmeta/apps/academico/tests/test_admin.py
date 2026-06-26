"""
Arquivo: test_admin.py
Caminho: apps/academico/tests/test_admin.py
Descrição: Testes de admin consolidados para StatusMatricula, Matricula e Avaliacao.
           Combina testes baseados em requisições HTTP (Client) com chamadas diretas
           aos métodos do ModelAdmin para máxima cobertura e robustez.
Histórico de Alterações:
 - 28/05/2026 - Criação do arquivo
 - 09/06/2026 - Correção de testes para refletir mudanças no modelo e admin
 - 23/06/2026 - Adicionados testes: get_numero_matricula, get_aluno, _agrupar_por_turma, aprovar_eventos, reprovar_eventos, changelist_view com filtros, download sem aprovados
              - Corrigido acento em test_gerar_certificados_ja_emitido
              - Adicionados testes de cobertura para gerar_relatorio_excel, gerar_relatorio_pdf e changelist_view com IDs inexistentes
              - Consolidação de arquivos, aplicação de DRY com factories/helpers, e expansão de testes de cobertura (múltiplas turmas e simulação de erros).
"""

import pytest
from django.test import Client
from django.urls import reverse
from django.contrib.messages import get_messages
from django.contrib.messages.storage.fallback import FallbackStorage
from django.utils import timezone
from datetime import timedelta, date
from unittest.mock import Mock, patch

from apps.accounts.admin import admin_site
from apps.academico.admin import StatusMatriculaAdmin, MatriculaAdmin, AvaliacaoAdmin
from apps.academico.models import StatusMatricula, Matricula, Avaliacao
from apps.eventos.models import Evento, Turma, Status
from apps.selecao.models import Inscricao, Classificacao, StatusInscricao
from apps.accounts.models import Usuario
from apps.interessados.tests.factories import InteressadoFactory


# =============================================================================
# FIXTURES / HELPERS COMPARTILHADOS
# =============================================================================

def _criar_estrutura_base():
    """Cria a árvore base de entidades: Status, Evento, Turma e StatusMatricula."""
    agora = timezone.now()
    status_evento = Status.objects.create(nome='Ativo')
    status_inscricao = StatusInscricao.objects.create(nome='Confirmada')
    
    evento = Evento.objects.create(
        nome='Evento Teste',
        status=status_evento,
        total_vagas=50,
        data_inicio_inscricao=agora,
        data_fim_inscricao=agora + timedelta(days=30),
        data_inicio_evento=agora.date() + timedelta(days=60),
        data_fim_evento=agora.date() + timedelta(days=61),
    )
    
    turma = Turma.objects.create(
        nome='Turma Teste',
        evento=evento,
        capacidade=40,
        data_inicio=agora.date() + timedelta(days=60),
        data_fim=agora.date() + timedelta(days=61),
    )
    
    status_matricula = StatusMatricula.objects.create(
        nome='Ativa', cor='#00ff00', ordem=1
    )
    
    return {
        'evento': evento,
        'turma': turma,
        'status_evento': status_evento,
        'status_inscricao': status_inscricao,
        'status_matricula': status_matricula,
    }


def _criar_matricula_e_avaliacao(base, interessado=None, numero='100',
                                 nota=8.5, frequencia=90, aprovado=True):
    """Cria de forma encadeada uma inscrição, matrícula e avaliação."""
    if interessado is None:
        interessado = InteressadoFactory()
        
    inscricao = Inscricao.objects.create(
        interessado=interessado,
        evento=base['evento'],
        status=base['status_inscricao'],
    )
    
    matricula = Matricula.objects.create(
        numero_matricula=numero,
        interessado=interessado,
        turma=base['turma'],
        status=base['status_matricula'],
        inscricao=inscricao,
    )
    
    avaliacao, _ = Avaliacao.objects.update_or_create(
        matricula=matricula,
        defaults={
            'nota_final': nota,
            'frequencia': frequencia,
            'aprovado': aprovado,
        },
    )
    return inscricao, matricula, avaliacao


# =============================================================================
# TESTES: STATUS MATRICULA ADMIN
# =============================================================================

@pytest.mark.django_db
class TestStatusMatriculaAdmin:
    """Testes para StatusMatriculaAdmin"""

    def setup_method(self):
        self.admin = StatusMatriculaAdmin(StatusMatricula, admin_site)

    def test_cor_display_com_cor(self):
        """Deve exibir quadrado colorido quando cor esta preenchida"""
        obj = StatusMatricula(cor='#ff0000')
        result = self.admin.cor_display(obj)
        assert '#ff0000' in result
        assert 'background-color' in result

    def test_cor_display_sem_cor(self):
        """Deve exibir travessao quando cor esta vazia"""
        obj = StatusMatricula(cor='')
        result = self.admin.cor_display(obj)
        assert result == '\u2014'


# =============================================================================
# TESTES: MATRICULA ADMIN
# =============================================================================

@pytest.mark.django_db
class TestMatriculaAdmin:
    """Testes para MatriculaAdmin"""

    def setup_method(self):
        self.admin = MatriculaAdmin(Matricula, admin_site)
        self.base = _criar_estrutura_base()
        self.interessado = InteressadoFactory()
        self.inscricao, self.matricula, _ = _criar_matricula_e_avaliacao(
            self.base, self.interessado, numero='123'
        )

    def test_get_interessado(self):
        """Deve retornar nome do interessado"""
        result = self.admin.get_interessado(self.matricula)
        assert result == self.interessado.nome

    def test_get_evento(self):
        """Deve retornar nome do evento"""
        result = self.admin.get_evento(self.matricula)
        assert result == 'Evento Teste'


# =============================================================================
# TESTES: AVALIACAO ADMIN
# =============================================================================

@pytest.mark.django_db
class TestAvaliacaoAdmin:
    """Testes para AvaliacaoAdmin"""
    serialized_rollback = True

    def setup_method(self):
        # Configuração do Superusuário e do Client logado
        self.superuser = Usuario.objects.create_user(
            username='admin2',
            email='admin2@ex.com',
            password='123',
            cpf='22222222222',
            is_staff=True,
            is_superuser=True,
        )
        self.client = Client()
        self.client.force_login(self.superuser)

        # Dados estruturais base
        self.base = _criar_estrutura_base()
        self.interessado = InteressadoFactory()
        self.inscricao, self.matricula, self.avaliacao = _criar_matricula_e_avaliacao(
            self.base, self.interessado, numero='456', nota=8.5, frequencia=90, aprovado=True
        )

        Classificacao.objects.create(
            inscricao=self.inscricao,
            classificado=True,
            pontuacao_total=100,
            posicao=1,
        )

        self.admin = AvaliacaoAdmin(Avaliacao, admin_site)

    def _criar_matricula_extra(self, aprovado=False, numero='789'):
        """Helper para criar matricula/avaliacao extra (nao aprovada por padrao)"""
        status_pendente, _ = StatusInscricao.objects.get_or_create(nome='Pendente')
        interessado2 = InteressadoFactory()
        inscricao2 = Inscricao.objects.create(
            interessado=interessado2,
            evento=self.base['evento'],
            status=status_pendente,
        )
        matricula2 = Matricula.objects.create(
            numero_matricula=numero,
            interessado=interessado2,
            turma=self.base['turma'],
            status=self.base['status_matricula'],
            inscricao=inscricao2,
        )
        Classificacao.objects.create(
            inscricao=inscricao2,
            classificado=True,
            pontuacao_total=80,
            posicao=2,
        )
        avaliacao2, _ = Avaliacao.objects.update_or_create(
            matricula=matricula2,
            defaults={
                'nota_final': 5.0,
                'frequencia': 70,
                'aprovado': aprovado,
            },
        )
        return matricula2, avaliacao2

    def _configurar_mock_request(self):
        """Helper para simular uma request interna com suporte a mensagens"""
        request = self.client.get('/').wsgi_request
        setattr(request, 'session', self.client.session)
        setattr(request, '_messages', FallbackStorage(request))
        return request

    # --- Ações de Certificado (Renderização de coluna) ---

    def test_acoes_certificado_aprovado(self):
        """Deve exibir botao para certificado aprovado"""
        result = self.admin.acoes_certificado(self.avaliacao)
        assert 'button' in result
        assert str(self.avaliacao.pk) in result

    def test_acoes_certificado_nao_aprovado(self):
        """Deve exibir travessao para nao aprovado"""
        _, avaliacao2 = self._criar_matricula_extra(aprovado=False)
        result = self.admin.acoes_certificado(avaliacao2)
        assert result == '<span style="color: #999;">-</span>'

    # --- Changelist View & Filtros Contextuais ---

    def test_changelist_view_contexto(self):
        """Deve incluir eventos_disponiveis no contexto"""
        response = self.client.get(reverse('admin:academico_avaliacao_changelist'))
        assert response.status_code == 200
        assert 'eventos_disponiveis' in response.context

    def test_changelist_view_com_evento_filter(self):
        """Deve incluir evento_nome e turmas_disponiveis com evento_filter"""
        response = self.client.get(
            reverse('admin:academico_avaliacao_changelist'),
            {'matricula__turma__evento__id__exact': str(self.base['evento'].pk)}
        )
        assert response.status_code == 200
        assert response.context.get('evento_nome') == self.base['evento'].nome
        assert 'turmas_disponiveis' in response.context

    def test_changelist_view_com_turma_filter(self):
        """Deve incluir turma_nome no contexto com turma_filter"""
        response = self.client.get(
            reverse('admin:academico_avaliacao_changelist'),
            {
                'matricula__turma__evento__id__exact': str(self.base['evento'].pk),
                'matricula__turma__id__exact': str(self.base['turma'].pk),
            }
        )
        assert response.status_code == 200
        assert response.context.get('turma_nome') == self.base['turma'].nome

    def test_changelist_view_evento_inexistente(self):
        """Nao deve quebrar (DoesNotExist) com evento_filter apontando para ID inexistente"""
        response = self.client.get(
            reverse('admin:academico_avaliacao_changelist'),
            {'matricula__turma__evento__id__exact': '99999'}
        )
        assert response.status_code == 200
        assert response.context.get('evento_nome') is None

    def test_changelist_view_turma_inexistente(self):
        """Nao deve quebrar (DoesNotExist) com turma_filter apontando para ID inexistente"""
        response = self.client.get(
            reverse('admin:academico_avaliacao_changelist'),
            {
                'matricula__turma__evento__id__exact': str(self.base['evento'].pk),
                'matricula__turma__id__exact': '99999',
            }
        )
        assert response.status_code == 200
        assert response.context.get('turma_nome') is None

    # --- Action: Gerar Certificados ---

    def test_gerar_certificados_marca_emitidos(self):
        """Deve marcar certificado como emitido com a data atual"""
        assert not self.avaliacao.certificado_emitido
        self.client.post(
            reverse('admin:academico_avaliacao_changelist'),
            {
                'action': 'gerar_certificados',
                '_selected_action': [self.avaliacao.pk],
                'index': '0',
            },
        )
        self.avaliacao.refresh_from_db()
        assert self.avaliacao.certificado_emitido
        assert self.avaliacao.data_emissao_certificado == timezone.now().date()

    def test_gerar_certificados_sem_aprovados(self):
        """Deve exibir mensagem quando nenhum aluno selecionado for aprovado"""
        _, avaliacao2 = self._criar_matricula_extra(aprovado=False)
        response = self.client.post(
            reverse('admin:academico_avaliacao_changelist'),
            {
                'action': 'gerar_certificados',
                '_selected_action': [avaliacao2.pk],
                'index': '0',
            },
            follow=True,
        )
        msg_list = list(get_messages(response.wsgi_request))
        assert any('Nenhum aluno aprovado' in str(m) for m in msg_list)

    def test_gerar_certificados_ja_emitido(self):
        """Deve exibir aviso se o certificado já tiver sido emitido previamente"""
        self.avaliacao.certificado_emitido = True
        self.avaliacao.save()
        response = self.client.post(
            reverse('admin:academico_avaliacao_changelist'),
            {
                'action': 'gerar_certificados',
                '_selected_action': [self.avaliacao.pk],
                'index': '0',
            },
            follow=True,
        )
        msg_list = list(get_messages(response.wsgi_request))
        assert any('já possui certificado emitido' in str(m) for m in msg_list)

    def test_gerar_certificados_erro_ao_salvar(self):
        """Deve capturar exceção genérica e exibir erro em tela se falhar ao salvar no banco"""
        with patch('apps.academico.models.Avaliacao.save', side_effect=Exception('Erro simulado no banco')):
            response = self.client.post(
                reverse('admin:academico_avaliacao_changelist'),
                {
                    'action': 'gerar_certificados',
                    '_selected_action': [self.avaliacao.pk],
                    'index': '0',
                },
                follow=True,
            )
        msg_list = list(get_messages(response.wsgi_request))
        assert any('Erro simulado' in str(m) for m in msg_list)

    # --- Action: Download em Lote ---

    def test_download_certificados_lote_action_redirect(self):
        """Deve redirecionar para a URL de download em lote com sucesso"""
        response = self.client.post(
            reverse('admin:academico_avaliacao_changelist'),
            {
                'action': 'download_certificados_lote_action',
                '_selected_action': [self.avaliacao.pk],
                'index': '0',
            },
        )
        assert response.status_code == 302
        assert 'certificados/download-lote' in response.url

    def test_download_certificados_lote_action_sem_aprovados(self):
        """Deve mostrar erro na listagem se nenhum aprovado for selecionado para download"""
        _, avaliacao2 = self._criar_matricula_extra(aprovado=False)
        response = self.client.post(
            reverse('admin:academico_avaliacao_changelist'),
            {
                'action': 'download_certificados_lote_action',
                '_selected_action': [avaliacao2.pk],
                'index': '0',
            },
            follow=True,
        )
        msg_list = list(get_messages(response.wsgi_request))
        assert any('Nenhum aluno aprovado' in str(m) for m in msg_list)

    # --- Action & Método: Relatório Excel ---

    def test_gerar_relatorio_excel_via_interface(self):
        """Garante compatibilidade de ponta-a-ponta da action Excel via Client POST"""
        hoje = date.today().strftime('%Y%m%d')
        response = self.client.post(
            reverse('admin:academico_avaliacao_changelist'),
            {
                'action': 'gerar_relatorio_excel',
                '_selected_action': [self.avaliacao.pk],
                'index': '0',
            },
        )
        assert response.status_code == 200
        assert 'spreadsheetml' in response['Content-Type']
        assert f'Relatorio_Alunos_{hoje}.xlsx' in response['Content-Disposition']

    def test_gerar_relatorio_excel_retorna_xlsx(self):
        """Testa o método isolado com um QuerySet preenchido"""
        qs = Avaliacao.objects.filter(pk=self.avaliacao.pk)
        request = self._configurar_mock_request()

        response = self.admin.gerar_relatorio_excel(request, qs)
        assert response is not None
        assert 'spreadsheetml' in response['Content-Type']
        assert response['Content-Disposition'].endswith('.xlsx"')

    def test_gerar_relatorio_excel_sem_avaliacoes(self):
        """Deve retornar None (ou exibir erro) quando o QuerySet for vazio"""
        qs = Avaliacao.objects.none()
        request = self._configurar_mock_request()

        response = self.admin.gerar_relatorio_excel(request, qs)
        assert response is None

    def test_gerar_relatorio_excel_via_interface_vazio(self):
        """Garante que a listagem trata o erro elegantemente quando ID não existe no Excel"""
        response = self.client.post(
            reverse('admin:academico_avaliacao_changelist'),
            {
                'action': 'gerar_relatorio_excel',
                '_selected_action': ['99999'],
                'index': '0',
            },
            follow=True,
        )
        msg_list = list(get_messages(response.wsgi_request))
        assert any('Nenhuma avaliação encontrada' in str(m) for m in msg_list)

    # --- Action & Método: Relatório PDF ---

    def test_gerar_relatorio_pdf_via_interface(self):
        """Garante compatibilidade de ponta-a-ponta da action PDF via Client POST"""
        response = self.client.post(
            reverse('admin:academico_avaliacao_changelist'),
            {
                'action': 'gerar_relatorio_pdf',
                '_selected_action': [self.avaliacao.pk],
                'index': '0',
            },
        )
        assert response.status_code == 200
        assert response['Content-Type'] == 'application/pdf'

    def test_gerar_relatorio_pdf_retorna_pdf(self):
        """Testa o método isolado com um QuerySet preenchido"""
        qs = Avaliacao.objects.filter(pk=self.avaliacao.pk)
        request = self._configurar_mock_request()

        response = self.admin.gerar_relatorio_pdf(request, qs)
        assert response is not None
        assert response['Content-Type'] == 'application/pdf'
        assert response['Content-Disposition'].endswith('.pdf"')

    def test_gerar_relatorio_pdf_sem_avaliacoes(self):
        """Deve retornar None quando o QuerySet for vazio no PDF"""
        qs = Avaliacao.objects.none()
        request = self._configurar_mock_request()

        response = self.admin.gerar_relatorio_pdf(request, qs)
        assert response is None

    def test_gerar_relatorio_pdf_via_interface_vazio(self):
        """Garante que a listagem trata o erro elegantemente quando ID não existe no PDF"""
        response = self.client.post(
            reverse('admin:academico_avaliacao_changelist'),
            {
                'action': 'gerar_relatorio_pdf',
                '_selected_action': ['99999'],
                'index': '0',
            },
            follow=True,
        )
        msg_list = list(get_messages(response.wsgi_request))
        assert any('Nenhuma avaliação encontrada' in str(m) for m in msg_list)

    # --- Métodos Auxiliares e Propriedades ---

    def test_get_numero_matricula(self):
        """Deve retornar numero da matricula através do método customizado do admin"""
        result = self.admin.get_numero_matricula(self.avaliacao)
        assert result == '456'

    def test_get_aluno(self):
        """Deve retornar nome do aluno através do método customizado do admin"""
        result = self.admin.get_aluno(self.avaliacao)
        assert result == self.interessado.nome

    def test_agrupar_por_turma_com_avaliacoes(self):
        """Deve agrupar avaliacoes corretamente por turma"""
        qs = Avaliacao.objects.filter(matricula__turma=self.base['turma'])
        resultado = self.admin._agrupar_por_turma(qs)
        assert isinstance(resultado, dict)
        assert self.base['turma'] in resultado
        assert len(resultado[self.base['turma']]) == 1

    def test_agrupar_por_turma_vazio(self):
        """Deve retornar dict vazio quando nao ha avaliacoes para agrupar"""
        qs = Avaliacao.objects.none()
        resultado = self.admin._agrupar_por_turma(qs)
        assert resultado == {}

    def test_agrupar_por_turma_multiplas_turmas(self):
        """Deve segregar e separar corretamente avaliacoes de turmas diferentes"""
        agora = timezone.now()
        turma2 = Turma.objects.create(
            nome='Turma 2',
            evento=self.base['evento'],
            capacidade=20,
            data_inicio=agora.date() + timedelta(days=60),
            data_fim=agora.date() + timedelta(days=61),
        )
        interessado2 = InteressadoFactory()
        status_inscricao = StatusInscricao.objects.get(nome='Confirmada')
        inscricao2 = Inscricao.objects.create(
            interessado=interessado2,
            evento=self.base['evento'],
            status=status_inscricao,
        )
        matricula2 = Matricula.objects.create(
            numero_matricula='999',
            interessado=interessado2,
            turma=turma2,
            status=self.base['status_matricula'],
            inscricao=inscricao2,
        )
        Avaliacao.objects.update_or_create(
            matricula=matricula2,
            defaults={'nota_final': 7.0, 'frequencia': 80, 'aprovado': True},
        )

        qs = Avaliacao.objects.all()
        resultado = self.admin._agrupar_por_turma(qs)
        assert len(resultado) == 2
        assert self.base['turma'] in resultado
        assert turma2 in resultado

    # --- Actions Administrativas Genéricas ---

    def test_aprovar_eventos(self):
        """Deve aprovar eventos selecionados via método direto"""
        request = Mock(_messages=[])
        qs = Mock()
        qs.update = Mock()
        self.admin.aprovar_eventos(request, qs)
        qs.update.assert_called_once_with(status='aprovado')

    def test_reprovar_eventos(self):
        """Deve reprovar eventos selecionados via método direto"""
        request = Mock(_messages=[])
        qs = Mock()
        qs.update = Mock()
        self.admin.reprovar_eventos(request, qs)
        qs.update.assert_called_once_with(status='reprovado')

