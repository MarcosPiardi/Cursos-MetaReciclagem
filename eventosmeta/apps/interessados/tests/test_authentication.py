"""
Arquivo: test_authentication.py
Caminho: apps/interessados/tests/test_authentication.py
Testes para o backend de autenticacao customizado InteressadoBackend
Atualizações:
 - 29/05/2026 - Criação
 - 16/06/2026 - v2.0 - Refatoração para pytest idiomático
"""

import pytest
from django.http import HttpRequest

from apps.interessados.authentication import InteressadoBackend
from .factories import InteressadoFactory

pytestmark = pytest.mark.django_db


class TestInteressadoBackendAuthenticate:
    """Testes para o metodo authenticate do InteressadoBackend."""

    @pytest.fixture
    def _data(self):
        return {
            'cpf': '52998224725',
            'senha': 'senha123',
            'interessado_ativo': InteressadoFactory.create(cpf='52998224725', is_active=True),
            'interessado_inativo': InteressadoFactory.create(cpf='98765432100', is_active=False),
            'backend': InteressadoBackend(),
            'request': HttpRequest(),
        }

    def test_autentica_com_cpf_e_senha_validos(self, _data):
        result = _data['backend'].authenticate(
            _data['request'],
            cpf=_data['cpf'],
            password=_data['senha'],
        )
        assert result is not None
        assert result.pk == _data['interessado_ativo'].pk

    def test_autentica_com_senha_errada_retorna_none(self, _data):
        result = _data['backend'].authenticate(
            _data['request'],
            cpf=_data['cpf'],
            password='senha_errada',
        )
        assert result is None

    def test_autentica_com_cpf_inexistente_retorna_none(self, _data):
        result = _data['backend'].authenticate(
            _data['request'],
            cpf='00000000000',
            password=_data['senha'],
        )
        assert result is None

    def test_autentica_com_cpf_none_retorna_none(self, _data):
        result = _data['backend'].authenticate(
            _data['request'],
            cpf=None,
            password=_data['senha'],
        )
        assert result is None

    def test_autentica_com_senha_none_retorna_none(self, _data):
        result = _data['backend'].authenticate(
            _data['request'],
            cpf=_data['cpf'],
            password=None,
        )
        assert result is None

    def test_autentica_interessado_inativo_retorna_none(self, _data):
        result = _data['backend'].authenticate(
            _data['request'],
            cpf=_data['interessado_inativo'].cpf,
            password='senha123',
        )
        assert result is None

    def test_autentica_sem_request_mas_com_cpf_valido(self, _data):
        result = _data['backend'].authenticate(
            None,
            cpf=_data['cpf'],
            password=_data['senha'],
        )
        assert result is not None
        assert result.pk == _data['interessado_ativo'].pk


class TestInteressadoBackendGetUser:
    """Testes para o metodo get_user do InteressadoBackend."""

    @pytest.fixture
    def _data(self):
        return {
            'interessado_ativo': InteressadoFactory.create(is_active=True),
            'interessado_inativo': InteressadoFactory.create(is_active=False),
            'backend': InteressadoBackend(),
        }

    def test_get_user_com_id_valido_retorna_interessado(self, _data):
        result = _data['backend'].get_user(_data['interessado_ativo'].pk)
        assert result is not None
        assert result.pk == _data['interessado_ativo'].pk

    def test_get_user_com_id_inexistente_retorna_none(self, _data):
        result = _data['backend'].get_user(99999)
        assert result is None

    def test_get_user_interessado_inativo_retorna_none(self, _data):
        result = _data['backend'].get_user(_data['interessado_inativo'].pk)
        assert result is None



