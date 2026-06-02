"""
Arquivo: test_forms.py
Caminho: apps/portal/tests/test_forms.py
Testes para formularios do app PORTAL
Data: 29/05/2026
"""

from django.test import TestCase
from django.contrib.auth.hashers import make_password

from apps.portal.forms import LoginInteressadoForm, ConsultaPublicaForm
from apps.interessados.models import Interessado, gerar_hash_cpf
from apps.interessados.tests.factories import InteressadoFactory


class TestLoginInteressadoForm(TestCase):
    """Testes para LoginInteressadoForm"""

    @classmethod
    def setUpTestData(cls):
        cls.interessado = InteressadoFactory.create(
            is_active=True,
            cpf='52998224725',
            senha=make_password('senha123'),
        )

    def test_form_valido_com_cpf_e_senha_corretos(self):
        form = LoginInteressadoForm(data={
            'cpf': '52998224725',
            'senha': 'senha123',
        })
        self.assertTrue(form.is_valid())
        self.assertEqual(form.interessado, self.interessado)

    def test_form_valido_com_cpf_formatado(self):
        form = LoginInteressadoForm(data={
            'cpf': '529.982.247-25',
            'senha': 'senha123',
        })
        self.assertTrue(form.is_valid())

    def test_form_invalido_com_cpf_incorreto(self):
        form = LoginInteressadoForm(data={
            'cpf': '00000000000',
            'senha': 'senha123',
        })
        self.assertFalse(form.is_valid())
        self.assertIn('CPF ou senha incorretos', str(form.errors))

    def test_form_invalido_com_senha_incorreta(self):
        form = LoginInteressadoForm(data={
            'cpf': '52998224725',
            'senha': 'senha_errada',
        })
        self.assertFalse(form.is_valid())
        self.assertIn('CPF ou senha incorretos', str(form.errors))

    def test_form_invalido_interessado_inativo(self):
        self.interessado.is_active = False
        self.interessado.save()

        form = LoginInteressadoForm(data={
            'cpf': '52998224725',
            'senha': 'senha123',
        })
        self.assertFalse(form.is_valid())
        self.assertIn('inativa', str(form.errors))

    def test_form_invalido_cpf_com_menos_de_11_digitos(self):
        form = LoginInteressadoForm(data={
            'cpf': '123',
            'senha': 'senha123',
        })
        self.assertFalse(form.is_valid())
        self.assertIn('11 digitos', str(form.errors))

    def test_form_invalido_com_campos_vazios(self):
        form = LoginInteressadoForm(data={})
        self.assertFalse(form.is_valid())
        self.assertIn('cpf', form.errors)
        self.assertIn('senha', form.errors)


class TestConsultaPublicaForm(TestCase):
    """Testes para ConsultaPublicaForm"""

    def test_cpf_valido_sem_formatacao(self):
        form = ConsultaPublicaForm(data={'cpf': '52998224725'})
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data['cpf'], '52998224725')

    def test_cpf_valido_com_formatacao(self):
        form = ConsultaPublicaForm(data={'cpf': '529.982.247-25'})
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data['cpf'], '52998224725')

    def test_cpf_invalido_com_menos_de_11_digitos(self):
        form = ConsultaPublicaForm(data={'cpf': '123456'})
        self.assertFalse(form.is_valid())
        self.assertIn('11 digitos', str(form.errors))

    def test_cpf_invalido_vazio(self):
        form = ConsultaPublicaForm(data={'cpf': ''})
        self.assertFalse(form.is_valid())

        