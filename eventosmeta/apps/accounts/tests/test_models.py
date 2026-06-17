"""
Arquivo: test_models.py
Caminho: apps/accounts/tests/test_models.py
Testes dos models: User e UserManager do app Accounts.
Atualizações:
 - 10/02/2026 - Criacao inicial dos testes
 - 16/06/2026 - Refatorado para pytest puro
"""

import pytest
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.db.utils import IntegrityError


@pytest.fixture
def user_model():
    return get_user_model()


@pytest.mark.django_db
def test_criar_usuario_com_cpf_valido(user_model):
    cpf_valido = "12345678901"

    usuario = user_model.objects.create_user(
        username="testuser",
        email="test@example.com",
        password="password123",
        cpf=cpf_valido,
    )

    assert usuario is not None
    assert usuario.username == "testuser"
    assert usuario.email == "test@example.com"
    assert usuario.cpf == cpf_valido
    assert usuario.check_password("password123")


@pytest.mark.django_db
@pytest.mark.parametrize(
    "cpf",
    [
        "1234567890",      # 10 dígitos
        "123456789012",    # 12 dígitos
    ],
)
def test_criar_usuario_com_cpf_invalido(user_model, cpf):
    usuario = user_model(
        username="usuario_teste",
        email="teste@example.com",
        cpf=cpf,
    )

    with pytest.raises(ValidationError):
        usuario.full_clean()


@pytest.mark.django_db
def test_cpf_unico(user_model):
    cpf_duplicado = "98765432109"

    user_model.objects.create_user(
        username="firstuser",
        email="first@example.com",
        password="password123",
        cpf=cpf_duplicado,
    )

    with pytest.raises(IntegrityError):
        user_model.objects.create_user(
            username="seconduser",
            email="second@example.com",
            password="password456",
            cpf=cpf_duplicado,
        )


@pytest.mark.django_db
def test_usuario_staff_pode_login(user_model):
    usuario = user_model.objects.create_user(
        username="staffuser",
        email="staff@example.com",
        password="staffpassword",
        cpf="11122233344",
        is_staff=True,
    )

    assert usuario.is_staff is True


@pytest.mark.django_db
def test_usuario_nao_staff_nao_pode_login_staff(user_model):
    usuario = user_model.objects.create_user(
        username="normaluser",
        email="normal@example.com",
        password="normalpassword",
        cpf="55566677788",
        is_staff=False,
    )

    assert usuario.is_staff is False


@pytest.mark.django_db
def test_criar_usuario_sem_username_falha(user_model):
    with pytest.raises(ValueError):
        user_model.objects.create_user(
            username=None,
            email="semusername@example.com",
            password="password123",
            cpf="11122233344",
        )


@pytest.mark.django_db
def test_criar_usuario_sem_password_falha(user_model):
    usuario = user_model.objects.create_user(
        username="sempassword",
        email="sempassword@example.com",
        password=None,
        cpf="22233344455",
    )

    assert not usuario.check_password("qualquercoisa")


@pytest.mark.django_db
def test_criar_superuser_is_staff(user_model):
    usuario = user_model.objects.create_superuser(
        username="admin",
        email="admin@ex.com",
        password="admin123",
        cpf="99988877766",
    )

    assert usuario.is_staff is True


@pytest.mark.django_db
def test_criar_superuser_is_superuser(user_model):
    usuario = user_model.objects.create_superuser(
        username="admin2",
        email="admin2@ex.com",
        password="admin123",
        cpf="88877766655",
    )

    assert usuario.is_superuser is True


@pytest.mark.django_db
def test_usuario_str_retorna_username(user_model):
    usuario = user_model.objects.create_user(
        username="joaosilva",
        email="joao@example.com",
        password="password123",
        cpf="33344455566",
    )

    assert str(usuario) == "joaosilva - CPF: 33344455566"


