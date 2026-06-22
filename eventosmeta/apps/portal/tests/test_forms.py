"""
Arquivo: test_forms.py
Caminho: apps/portal/tests/test_forms.py
Testes para formularios do app PORTAL
Atualizações:
 - 29/05/2026 - Criacao do arquivo
 - 18/06/2026 - Refatorado para pytest
"""

import pytest
from django.contrib.auth.hashers import make_password

from apps.portal.forms import LoginInteressadoForm, ConsultaPublicaForm
from apps.interessados.tests.factories import InteressadoFactory

pytestmark = pytest.mark.django_db

class TestLoginInteressadoForm:
    """Testes para LoginInteressadoForm"""

    @pytest.fixture(autouse=True)
    def setup(self, db):
        self.interessado = InteressadoFactory.create(
            is_active=True,
            cpf="52998224725",
            senha=make_password("senha123"),
        )

    def test_form_valido_com_cpf_e_senha_corretos(self):
        form = LoginInteressadoForm(
            data={"cpf": "52998224725", "senha": "senha123"}
        )
        assert form.is_valid()
        assert form.interessado == self.interessado

    def test_form_valido_com_cpf_formatado(self):
        form = LoginInteressadoForm(
            data={"cpf": "529.982.247-25", "senha": "senha123"}
        )
        assert form.is_valid()

    def test_form_invalido_com_cpf_incorreto(self):
        form = LoginInteressadoForm(
            data={"cpf": "00000000000", "senha": "senha123"}
        )
        assert not form.is_valid()
        assert "CPF ou senha incorretos" in str(form.errors)

    def test_form_invalido_com_senha_incorreta(self):
        form = LoginInteressadoForm(
            data={"cpf": "52998224725", "senha": "senha_errada"}
        )
        assert not form.is_valid()
        assert "CPF ou senha incorretos" in str(form.errors)

    def test_form_invalido_interessado_inativo(self):
        self.interessado.is_active = False
        self.interessado.save()

        form = LoginInteressadoForm(
            data={"cpf": "52998224725", "senha": "senha123"}
        )
        assert not form.is_valid()
        assert "inativa" in str(form.errors)

    def test_form_invalido_cpf_com_menos_de_11_digitos(self):
        form = LoginInteressadoForm(
            data={"cpf": "123", "senha": "senha123"}
        )
        assert not form.is_valid()
        assert "11 digitos" in str(form.errors)

    def test_form_invalido_com_campos_vazios(self):
        form = LoginInteressadoForm(data={})
        assert not form.is_valid()
        assert "cpf" in form.errors
        assert "senha" in form.errors

class TestConsultaPublicaForm:
    """Testes para ConsultaPublicaForm"""

    def test_cpf_valido_sem_formatacao(self):
        form = ConsultaPublicaForm(data={"cpf": "52998224725"})
        assert form.is_valid()
        assert form.cleaned_data["cpf"] == "52998224725"

    def test_cpf_valido_com_formatacao(self):
        form = ConsultaPublicaForm(data={"cpf": "529.982.247-25"})
        assert form.is_valid()
        assert form.cleaned_data["cpf"] == "52998224725"

    def test_cpf_invalido_com_menos_de_11_digitos(self):
        form = ConsultaPublicaForm(data={"cpf": "123456"})
        assert not form.is_valid()
        assert "11 digitos" in str(form.errors)

    def test_cpf_invalido_vazio(self):
        form = ConsultaPublicaForm(data={"cpf": ""})
        assert not form.is_valid()



