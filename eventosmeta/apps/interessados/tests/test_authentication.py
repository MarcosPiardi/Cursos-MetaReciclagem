"""
Arquivo: test_authentication.py
Caminho: apps/interessados/tests/test_authentication.py
Testes para o backend de autenticacao customizado InteressadoBackend
Atualizacoes:
 - 29/05/2026 - Criacao
 - 16/06/2026 - v2.0 - Refatoracao para pytest idiomatico
 - 18/06/2026 - v2.1 - Separacao de fixtures por responsabilidade
"""

import pytest
from django.http import HttpRequest

from apps.interessados.authentication import InteressadoBackend
from .factories import InteressadoFactory

pytestmark = pytest.mark.django_db

# ── Fixtures ──────────────────────────────────────────────────────────

@pytest.fixture
def cpf_valido():
    return "52998224725"

@pytest.fixture
def senha():
    return "senha123"

@pytest.fixture
def interessado_ativo(db, cpf_valido):
    return InteressadoFactory.create(cpf=cpf_valido, is_active=True)

@pytest.fixture
def interessado_inativo(db):
    return InteressadoFactory.create(cpf="98765432100", is_active=False)

@pytest.fixture
def backend():
    return InteressadoBackend()

@pytest.fixture
def request_factory():
    return HttpRequest()

# ── Testes: authenticate ──────────────────────────────────────────────

class TestInteressadoBackendAuthenticate:
    def test_autentica_com_cpf_e_senha_validos(
        self, backend, request_factory, cpf_valido, senha, interessado_ativo
    ):
        result = backend.authenticate(
            request_factory, cpf=cpf_valido, password=senha
        )
        assert result is not None
        assert result.pk == interessado_ativo.pk

    def test_autentica_com_senha_errada_retorna_none(
        self, backend, request_factory, cpf_valido
    ):
        result = backend.authenticate(
            request_factory, cpf=cpf_valido, password="senha_errada"
        )
        assert result is None

    def test_autentica_com_cpf_inexistente_retorna_none(
        self, backend, request_factory, senha
    ):
        result = backend.authenticate(
            request_factory, cpf="00000000000", password=senha
        )
        assert result is None

    def test_autentica_com_cpf_none_retorna_none(
        self, backend, request_factory, senha
    ):
        result = backend.authenticate(
            request_factory, cpf=None, password=senha
        )
        assert result is None

    def test_autentica_com_senha_none_retorna_none(
        self, backend, request_factory, cpf_valido
    ):
        result = backend.authenticate(
            request_factory, cpf=cpf_valido, password=None
        )
        assert result is None

    def test_autentica_interessado_inativo_retorna_none(
        self, backend, request_factory, interessado_inativo
    ):
        result = backend.authenticate(
            request_factory,
            cpf=interessado_inativo.cpf,
            password="senha123",
        )
        assert result is None

    def test_autentica_sem_request_mas_com_cpf_valido(
        self, backend, cpf_valido, senha, interessado_ativo
    ):
        result = backend.authenticate(None, cpf=cpf_valido, password=senha)
        assert result is not None
        assert result.pk == interessado_ativo.pk

# ── Testes: get_user ──────────────────────────────────────────────────

class TestInteressadoBackendGetUser:
    def test_get_user_com_id_valido_retorna_interessado(
        self, backend, interessado_ativo
    ):
        result = backend.get_user(interessado_ativo.pk)
        assert result is not None
        assert result.pk == interessado_ativo.pk

    def test_get_user_com_id_inexistente_retorna_none(self, backend):
        result = backend.get_user(99999)
        assert result is None

    def test_get_user_interessado_inativo_retorna_none(
        self, backend, interessado_inativo
    ):
        result = backend.get_user(interessado_inativo.pk)
        assert result is None

        