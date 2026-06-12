"""
conftest.py - Configuração global do pytest para Sistema MetaReciclagem
Fixtures básicas: usuário staff, interessado teste, cliente autenticado.
Mocks para e-mail e ViaCEP.
Atualizações: 
 - 10/04/2026 - Criação do arquivo - Configuração inicial do pytest com fixtures e mocks
 - 10/06/2026 - Adição de fixture para usuário comum e interessado autenticado
"""


import pytest
from django.test import Client
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
import requests
from unittest.mock import MagicMock
from apps.interessados.tests.factories import InteressadoFactory

User = get_user_model()

@pytest.fixture(autouse=True)
def enable_db_access_for_all_tests(db):
    pass

@pytest.fixture
def client():
    return Client()

@pytest.fixture
def usuario_staff():
    return User.objects.create_superuser(username="staff_teste", email="staff@teste.com", password="senha123")

@pytest.fixture
def usuario_comum():
    return User.objects.create_user(username="usuario_teste", email="usuario@teste.com", password="senha123")

@pytest.fixture
def interessado_teste():
    return InteressadoFactory.create()

@pytest.fixture
def autenticado(client, usuario_staff):
    client.login(username=usuario_staff.username, password="senha123")
    return client

@pytest.fixture
def autenticado_interessado(client, interessado_teste):
    # Assuming the user is linked to the interessado or using a custom auth logic
    # Adjusting to login the user associated with the interessado if applicable
    client.login(username=interessado_teste.user.username, password="senha123")
    return client

@pytest.fixture(autouse=True)
def mock_send_mail(monkeypatch):
    mock = MagicMock()
    monkeypatch.setattr("django.core.mail.send_mail", mock)
    return mock

@pytest.fixture(autouse=True)
def mock_viacep(monkeypatch):
    mock = MagicMock()
    monkeypatch.setattr("requests.get", mock)
    return mock


