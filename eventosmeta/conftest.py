"""
conftest.py - Configuração global do pytest para Sistema MetaReciclagem
Fixtures básicas: usuário staff, interessado teste.
Mocks para e-mail e ViaCEP.
Sem imports problemáticos do pytest-django.
"""

import pytest
from django.contrib.auth import get_user_model
from django.test import Client
from django.utils import timezone
from apps.interessados.models import (
    Interessado,
    gerar_hash_cpf,
)  # Imports básicos do seu models.py


@pytest.fixture(autouse=True)
def enable_db_access_for_all_tests(db):
    """Permite acesso ao banco para todos os testes."""
    pass


@pytest.fixture
def client():
    """Cliente Django para testes de views."""
    return Client()


@pytest.fixture
def usuario_staff():
    """Usuário staff para testes de autenticação admin (de models.txt: Usuario)."""
    Usuario = get_user_model()
    user = Usuario.objects.create_user(
        username="staff_teste",
        email="staff@teste.com",
        password="senha123",
        is_staff=True,
        is_superuser=False,
    )
    return user


@pytest.fixture
def interessado_teste():
    """Interessado básico para testes (de models.txt)."""
    interessado = Interessado.objects.create(
        nome="Teste Silva",
        cpf="52998224725",
        cpf_hash=gerar_hash_cpf("52998224725"),  # Usa a função do seu model
        email="teste@interessado.com",
        consentimento_lgpd=True,
        consentimento_lgpd_em=timezone.now(),
    )
    interessado.set_password("senha123")
    interessado.save()
    return interessado


# Mock para e-mail (de models.txt: usado em recovery)
@pytest.fixture(autouse=True)
def mock_send_mail(monkeypatch):
    def mock_send_mail(subject, message, from_email, recipient_list, **kwargs):
        print(f"Mock e-mail: {subject} para {recipient_list}")
        return 1

    monkeypatch.setattr("django.core.mail.send_mail", mock_send_mail)


# Mock para ViaCEP (de cadastro.html)
@pytest.fixture(autouse=True)
def mock_viacep(monkeypatch):
    class MockResponse:
        def json(self):
            return {
                "logradouro": "Rua Teste",
                "bairro": "Bairro Teste",
                "localidade": "Sorocaba",
                "uf": "SP",
            }

    def mock_get(url, **kwargs):
        return MockResponse()

    monkeypatch.setattr("requests.get", mock_get)
