"""
Arquivo: test_forms.py
Caminho: apps/accounts/tests/test_forms.py
Testes para formularios do app accounts
Atualizacoes:
 - 19/06/2026 - Criacao
              - Correcao: placeholder com acento
              - Correcao: request no authenticate (AxesBackend)
              - Correcao: renderizacao via form, nao admin URL
"""

import pytest
from django.test import RequestFactory
from django.urls import reverse

from apps.accounts.forms import LoginStaffForm

pytestmark = pytest.mark.django_db

class TestLoginStaffForm:
    def test_form_tem_campos_esperados(self):
        form = LoginStaffForm()
        assert "username" in form.fields
        assert "password" in form.fields

    def test_form_placeholder_username(self):
        form = LoginStaffForm()
        attrs = form.fields["username"].widget.attrs
        assert attrs["placeholder"] == "Digite seu usuário"
        assert attrs["class"] == "form-control"

    def test_form_placeholder_password(self):
        form = LoginStaffForm()
        attrs = form.fields["password"].widget.attrs
        assert attrs["placeholder"] == "Digite sua senha"
        assert attrs["class"] == "form-control"

    def test_form_com_dados_validos(self, django_user_model, rf):
        usuario = django_user_model.objects.create_user(
            username="admin", password="senha123"
        )
        request = rf.get("/admin/login/")
        form_data = {"username": "admin", "password": "senha123"}
        form = LoginStaffForm(request=request, data=form_data)
        assert form.is_valid()

    def test_form_com_dados_invalidos(self):
        form_data = {"username": "", "password": ""}
        form = LoginStaffForm(data=form_data)
        assert not form.is_valid()
        assert "username" in form.errors or "password" in form.errors

    def test_form_renderiza_html(self):
        form = LoginStaffForm()
        html = str(form.as_p())
        assert "form-control" in html
        assert "Digite seu" in html

        