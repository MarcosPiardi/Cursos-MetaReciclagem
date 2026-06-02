from django.test import TestCase
from django.core.exceptions import ValidationError
from django.db.utils import IntegrityError
from django.contrib.auth import get_user_model


class TestUsuarioModel(TestCase):
    """Testes para o modelo customizado de usuário (Usuario)."""

    def setUp(self):
        self.User = get_user_model()

    def test_criar_usuario_com_cpf_valido(self):
        """Verifica se um usuário pode ser criado com um CPF válido de 11 dígitos."""
        cpf_valido = '12345678901'
        usuario = self.User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='password123',
            cpf=cpf_valido
        )
        self.assertIsNotNone(usuario)
        self.assertEqual(usuario.username, 'testuser')
        self.assertEqual(usuario.email, 'test@example.com')
        self.assertEqual(usuario.cpf, cpf_valido)
        self.assertTrue(usuario.check_password('password123'))

    def test_criar_usuario_com_cpf_invalido(self):
        """Verifica se a criação falha com CPF que não tem 11 dígitos."""
        cpf_curto = '1234567890'
        cpf_longo = '123456789012'

        with self.assertRaises(ValidationError):
            usuario = self.User(
                username='usercurto',
                email='curto@example.com',
                cpf=cpf_curto
            )
            usuario.full_clean()
            usuario.save()

        with self.assertRaises(ValidationError):
            usuario = self.User(
                username='userlongo',
                email='longo@example.com',
                cpf=cpf_longo
            )
            usuario.full_clean()
            usuario.save()

    def test_cpf_unico(self):
        """Verifica se CPF duplicado falha."""
        cpf_duplicado = '98765432109'
        self.User.objects.create_user(
            username='firstuser',
            email='first@example.com',
            password='password123',
            cpf=cpf_duplicado
        )

        with self.assertRaises(IntegrityError):
            self.User.objects.create_user(
                username='seconduser',
                email='second@example.com',
                password='password456',
                cpf=cpf_duplicado
            )

    def test_usuario_staff_pode_login(self):
        """Verifica se um usuário staff é criado com is_staff=True."""
        staff_cpf = '11122233344'
        staff_user = self.User.objects.create_user(
            username='staffuser',
            email='staff@example.com',
            password='staffpassword',
            cpf=staff_cpf,
            is_staff=True
        )
        self.assertTrue(staff_user.is_staff)

    def test_usuario_nao_staff_nao_pode_login_staff(self):
        """Verifica se um usuário não staff é criado com is_staff=False."""
        normal_cpf = '55566677788'
        normal_user = self.User.objects.create_user(
            username='normaluser',
            email='normal@example.com',
            password='normalpassword',
            cpf=normal_cpf,
            is_staff=False
        )
        self.assertFalse(normal_user.is_staff)

    def test_criar_usuario_sem_username_falha(self):
        with self.assertRaises((ValueError)):
            self.User.objects.create_user(
                username=None,
                email='semusername@example.com',
                password='password123',
                cpf='11122233344'
            )

    def test_criar_usuario_sem_password_falha(self):
        usuario = self.User.objects.create_user(
            username='sempassword',
            email='sempassword@example.com',
            password=None,
            cpf='22233344455'
        )
        self.assertFalse(usuario.check_password('qualquercoisa'))

    def test_criar_superuser_is_staff(self):
        usuario = self.User.objects.create_superuser(
            username='admin',
            email='admin@ex.com',
            password='admin123',
            cpf='99988877766'
        )
        self.assertTrue(usuario.is_staff)

    def test_criar_superuser_is_superuser(self):
        usuario = self.User.objects.create_superuser(
            username='admin2',
            email='admin2@ex.com',
            password='admin123',
            cpf='88877766655'
        )
        self.assertTrue(usuario.is_superuser)

    def test_usuario_str_retorna_username(self):
        usuario = self.User.objects.create_user(
            username='joaosilva',
            email='joao@example.com',
            password='password123',
            cpf='33344455566'
        )
        self.assertEqual(str(usuario), 'joaosilva - CPF: 33344455566')



        