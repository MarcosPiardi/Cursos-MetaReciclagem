from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse
from unittest.mock import patch, MagicMock
import io
import zipfile

from apps.academico.models import Avaliacao
from .factories import MatriculaFactory, InteressadoFactory, StatusMatriculaFactory


class BaseCertificadoTest(TestCase):
    """Base class for certificate view tests."""

    def setUp(self):
        super().setUp()
        self.client = Client()
        self.User = get_user_model()
        
        # Criar usuário staff com CPF único
        self.staff_user = self.User.objects.create_user(
            username='staffuser',
            email='staff@example.com',
            password='password123',
            cpf='11111111111',
            is_staff=True
        )
        
        StatusMatriculaFactory(nome='Ativa')

        # Mock GeradorCertificado
        self.patcher = patch('apps.academico.views.GeradorCertificado')
        self.MockGeradorCertificado = self.patcher.start()
        self.mock_instance = self.MockGeradorCertificado.return_value
        self.mock_instance.gerar_pdf.side_effect = lambda buffer: buffer.write(b"Mock PDF Content")

    def tearDown(self):
        self.patcher.stop()
        super().tearDown()


class TestDownloadCertificadoIndividual(BaseCertificadoTest):
    """Tests for download_certificado_individual view."""

    def test_sem_autenticacao_redireciona(self):
        matricula = MatriculaFactory()
        avaliacao = matricula.avaliacao  # Pega a avaliacao criada pelo signal
        
        response = self.client.get(reverse('academico:download_certificado', args=[avaliacao.pk]))
        self.assertEqual(response.status_code, 302)
        self.assertIn('/admin/login/', response.url)

    def test_aluno_aprovado_gera_pdf(self):
        matricula = MatriculaFactory()
        avaliacao = matricula.avaliacao
        avaliacao.aprovado = True
        avaliacao.save()
        
        self.client.force_login(self.staff_user)
        response = self.client.get(reverse('academico:download_certificado', args=[avaliacao.pk]))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['Content-Type'], 'application/pdf')
        self.assertIn('attachment', response['Content-Disposition'])
        self.MockGeradorCertificado.assert_called_once_with(avaliacao)
        self.mock_instance.gerar_pdf.assert_called_once()

    def test_aluno_reprovado_retorna_400(self):
        matricula = MatriculaFactory()
        avaliacao = matricula.avaliacao
        # avaliacao já vem com aprovado=False por padrão do signal
        
        self.client.force_login(self.staff_user)
        response = self.client.get(reverse('academico:download_certificado', args=[avaliacao.pk]))

        self.assertEqual(response.status_code, 400)
        self.assertIn(b"Certificado dispon", response.content)
        self.MockGeradorCertificado.assert_not_called()

    def test_avaliacao_inexistente_retorna_404(self):
        self.client.force_login(self.staff_user)
        response = self.client.get(reverse('academico:download_certificado', args=[9999]))
        self.assertEqual(response.status_code, 404)


class TestPreviewCertificado(BaseCertificadoTest):
    """Tests for preview_certificado view."""

    def test_sem_autenticacao_redireciona(self):
        matricula = MatriculaFactory()
        avaliacao = matricula.avaliacao
        
        response = self.client.get(reverse('academico:preview_certificado', args=[avaliacao.pk]))
        self.assertEqual(response.status_code, 302)
        self.assertIn('/admin/login/', response.url)

    def test_aluno_aprovado_inline(self):
        matricula = MatriculaFactory()
        avaliacao = matricula.avaliacao
        avaliacao.aprovado = True
        avaliacao.save()
        
        self.client.force_login(self.staff_user)
        response = self.client.get(reverse('academico:preview_certificado', args=[avaliacao.pk]))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['Content-Type'], 'application/pdf')
        self.assertIn('inline', response['Content-Disposition'])
        self.MockGeradorCertificado.assert_called_once_with(avaliacao)
        self.mock_instance.gerar_pdf.assert_called_once()

    def test_aluno_reprovado_retorna_400(self):
        matricula = MatriculaFactory()
        avaliacao = matricula.avaliacao
        
        self.client.force_login(self.staff_user)
        response = self.client.get(reverse('academico:preview_certificado', args=[avaliacao.pk]))

        self.assertEqual(response.status_code, 400)
        self.assertIn(b"Certificado dispon", response.content)


class TestDownloadCertificadosLote(BaseCertificadoTest):
    """Tests for download_certificados_lote view."""

    def test_sem_ids_retorna_400(self):
        self.client.force_login(self.staff_user)
        response = self.client.get(reverse('academico:download_certificados_lote'))
        self.assertEqual(response.status_code, 400)
        self.assertIn(b"Nenhuma avalia", response.content)

    def test_ids_invalidos_retorna_400(self):
        self.client.force_login(self.staff_user)
        response = self.client.get(reverse('academico:download_certificados_lote') + '?ids=abc,123')
        self.assertEqual(response.status_code, 400)
        self.assertIn(b"Nenhum aluno aprovado", response.content)

    def test_apenas_aprovados_no_zip(self):
        interessado1 = InteressadoFactory(cpf='10000000001')
        interessado2 = InteressadoFactory(cpf='10000000002')
        
        matricula1 = MatriculaFactory(interessado=interessado1)
        avaliacao_aprovada = matricula1.avaliacao
        avaliacao_aprovada.aprovado = True
        avaliacao_aprovada.save()
        
        matricula2 = MatriculaFactory(interessado=interessado2)
        avaliacao_reprovada = matricula2.avaliacao
        # avaliacao_reprovada já vem com aprovado=False

        self.client.force_login(self.staff_user)
        response = self.client.get(
            reverse('academico:download_certificados_lote') + f'?ids={avaliacao_aprovada.pk},{avaliacao_reprovada.pk}'
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['Content-Type'], 'application/zip')
        self.assertIn('attachment', response['Content-Disposition'])

        zip_buffer = io.BytesIO(response.content)
        with zipfile.ZipFile(zip_buffer, 'r') as zf:
            self.assertEqual(len(zf.namelist()), 1)

    def test_zip_com_multiplos_certificados(self):
        interessado1 = InteressadoFactory(cpf='10000000003')
        interessado2 = InteressadoFactory(cpf='10000000004')
        
        matricula1 = MatriculaFactory(interessado=interessado1)
        avaliacao1 = matricula1.avaliacao
        avaliacao1.aprovado = True
        avaliacao1.save()
        
        matricula2 = MatriculaFactory(interessado=interessado2)
        avaliacao2 = matricula2.avaliacao
        avaliacao2.aprovado = True
        avaliacao2.save()

        self.client.force_login(self.staff_user)
        response = self.client.get(
            reverse('academico:download_certificados_lote') + f'?ids={avaliacao1.pk},{avaliacao2.pk}'
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['Content-Type'], 'application/zip')
        self.assertIn('attachment', response['Content-Disposition'])

        zip_buffer = io.BytesIO(response.content)
        with zipfile.ZipFile(zip_buffer, 'r') as zf:
            self.assertEqual(len(zf.namelist()), 2)

            