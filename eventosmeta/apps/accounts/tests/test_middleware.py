"""
Arquivo: test_middleware.py
Caminho: apps/accounts/tests/test_middleware.py
Finalidade: Testar o middleware de autenticação.
Atualizações:
 - 01/06/2026 - Criação do arquivo e implementação dos testes iniciais    
 - 15/06/2026 - Correção de testes para refletir a nova estrutura de URLs (ex: /staff/senha/trocar-obrigatorio/) 
 - 17/06/2026 - Adição de testes para URLs estáticas e de mídia, além de URLs de login/logout do admin
              - Refatoração para pytest, utilizando fixtures para criar usuários e interessados de teste, e um helper para aplicar o middleware nos requests.
 - 22/07/2026 - Corrigidos paths do RequestFactory para incluir prefixo /eventosmeta/
                e expected URLs nos redirects, alinhando com o middleware refatorado.
"""

import pytest
from django.test import RequestFactory
from django.contrib.sessions.middleware import SessionMiddleware
from django.contrib.auth.middleware import AuthenticationMiddleware
from apps.accounts.middleware import TrocarSenhaObrigatorioMiddleware
from apps.accounts.models import Usuario
from apps.interessados.tests.factories import InteressadoFactory

# ── Fixtures ──────────────────────────────────────────────────────────

@pytest.fixture
def rf():
    return RequestFactory()

@pytest.fixture
def usuario_staff(db):
    return Usuario.objects.create_user(
        username='staff', email='staff@ex.com', password='123',
        cpf='11111111111', is_staff=True, is_active=True,
        must_change_password=False,
    )

@pytest.fixture
def usuario_comum(db):
    return Usuario.objects.create_user(
        username='comum', email='comum@ex.com', password='123',
        cpf='22222222222', is_staff=False, is_active=True,
        must_change_password=False,
    )

@pytest.fixture
def interessado(db):
    return InteressadoFactory(
        is_active=True, must_change_password=False,
    )

# ── Helper ────────────────────────────────────────────────────────────

def _aplicar_middleware(request, user=None):
    """Aplica SessionMiddleware + AuthenticationMiddleware + TrocarSenhaObrigatorioMiddleware"""
    # Session
    SessionMiddleware(lambda r: None).process_request(request)
    request.session.save()

    # Auth
    AuthenticationMiddleware(lambda r: None).process_request(request)

    # Force login se user foi passado
    if user:
        request.user = user

    # Nosso middleware
    return TrocarSenhaObrigatorioMiddleware(lambda r: None)(request)

# ── Testes ────────────────────────────────────────────────────────────

def test_usuario_nao_autenticado_passa(rf):
    request = rf.get('/eventosmeta/admin/')
    response = _aplicar_middleware(request)
    assert response is None

def test_usuario_sem_must_change_password_passa(rf, usuario_comum):
    request = rf.get('/eventosmeta/admin/')
    response = _aplicar_middleware(request, user=usuario_comum)
    assert response is None

def test_usuario_com_must_change_password_url_liberada_staff(rf, usuario_staff):
    usuario_staff.must_change_password = True
    usuario_staff.save()
    request = rf.get('/eventosmeta/staff/logout/')
    response = _aplicar_middleware(request, user=usuario_staff)
    assert response is None

def test_usuario_com_must_change_password_url_restrita_staff(rf, usuario_staff):
    usuario_staff.must_change_password = True
    usuario_staff.save()
    request = rf.get('/eventosmeta/admin/')
    response = _aplicar_middleware(request, user=usuario_staff)
    assert response.status_code == 302
    # 22/07/2026 - Corrigido: prefixo /eventosmeta/ incluido
    assert response.url == '/eventosmeta/staff/senha/trocar-obrigatorio/'

def test_interessado_com_must_change_password_url_restrita(rf, interessado):
    interessado.must_change_password = True
    interessado.save()
    request = rf.get('/eventosmeta/inscricao/')
    response = _aplicar_middleware(request, user=interessado)
    assert response.status_code == 302
    # 22/07/2026 - Corrigido: prefixo /eventosmeta/ incluido
    assert response.url == '/eventosmeta/inscricao/senha/trocar-obrigatorio/'

def test_static_url_liberada_mesmo_com_must_change_password(rf, usuario_staff):
    usuario_staff.must_change_password = True
    usuario_staff.save()
    request = rf.get('/static/css/style.css')
    response = _aplicar_middleware(request, user=usuario_staff)
    assert response is None

def test_media_url_liberada_mesmo_com_must_change_password(rf, usuario_staff):
    usuario_staff.must_change_password = True
    usuario_staff.save()
    request = rf.get('/media/fotos/foto.jpg')
    response = _aplicar_middleware(request, user=usuario_staff)
    assert response is None

def test_url_admin_login_liberada(rf, usuario_staff):
    usuario_staff.must_change_password = True
    usuario_staff.save()
    # 22/07/2026 - Corrigido: path com prefixo para resolve() encontrar a URL
    request = rf.get('/eventosmeta/admin/login/')
    response = _aplicar_middleware(request, user=usuario_staff)
    assert response is None

def test_url_admin_logout_liberada(rf, usuario_staff):
    usuario_staff.must_change_password = True
    usuario_staff.save()
    request = rf.get('/eventosmeta/admin/logout/')
    response = _aplicar_middleware(request, user=usuario_staff)
    assert response is None

    