"""
Arquivo: test_admin.py
Caminho: apps/interessados/tests/test_admin.py
Testes para o admin de Interessados
Atualizações:
 - 29/05/2026 - Criação do arquivo
"""


"""
Arquivo: test_admin.py
Caminho: apps/interessados/tests/test_admin.py
Testes para admin do app Interessados
SexoAdmin, FototipoAdmin, InteressadoAdmin, PasswordResetTokenAdmin
Data: 29/05/2026
"""

import uuid
from datetime import date, timedelta
from django.test import TestCase
from django.http import HttpRequest
from django.contrib.messages.storage.cookie import CookieStorage
from django.utils import timezone

from apps.accounts.admin import admin_site
from apps.interessados.admin import (
    SexoAdmin,
    FototipoAdmin,
    InteressadoAdmin,
    PasswordResetTokenAdmin,
)
from apps.interessados.models import Interessado, Sexo, Fototipo, PasswordResetToken
from .factories import InteressadoFactory, SexoFactory, FototipoFactory


class TestSexoAdmin(TestCase):

    @classmethod
    def setUpTestData(cls):
        SexoFactory(nome='Masculino')

    def test_list_display(self):
        self.assertEqual(SexoAdmin.list_display, ['nome'])

    def test_search_fields(self):
        self.assertEqual(SexoAdmin.search_fields, ['nome'])


class TestFototipoAdmin(TestCase):

    @classmethod
    def setUpTestData(cls):
        FototipoFactory(nome='Tipo I', descricao='Teste')

    def test_list_display(self):
        self.assertEqual(FototipoAdmin.list_display, ['nome', 'descricao'])

    def test_search_fields(self):
        self.assertEqual(FototipoAdmin.search_fields, ['nome', 'descricao'])


class TestInteressadoAdminMetodos(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.sexo = SexoFactory(nome='Feminino')
        cls.fototipo = FototipoFactory(nome='Tipo I')
        cls.interessado = InteressadoFactory.create(
            sexo=cls.sexo,
            fototipo=cls.fototipo,
            data_nascimento=date(1990, 5, 15),
            celular='11987654321',
            telefone='1133334444',
            programa_social=True,
            necessidades_especiais=True,
            pcd_fisica=True,
        )

    def setUp(self):
        self.ma = InteressadoAdmin(model=Interessado, admin_site=admin_site)

    # --- data_nascimento_formatada ---

    def test_data_nascimento_formatada_com_data(self):
        result = self.ma.data_nascimento_formatada(self.interessado)
        self.assertIn('15/05/1990', str(result))

    def test_data_nascimento_formatada_sem_data(self):
        i = InteressadoFactory.create(data_nascimento=None)
        result = self.ma.data_nascimento_formatada(i)
        self.assertIn('\u2014', str(result))

    # --- sexo_display ---

    def test_sexo_display_com_sexo(self):
        result = self.ma.sexo_display(self.interessado)
        self.assertEqual(result, 'Feminino')

    def test_sexo_display_sem_sexo(self):
        i = InteressadoFactory.create(sexo=None)
        result = self.ma.sexo_display(i)
        self.assertEqual(result, '\u2014')

    # --- fototipo_display ---

    def test_fototipo_display_com_fototipo(self):
        result = self.ma.fototipo_display(self.interessado)
        self.assertIn('Tipo I', str(result))

    def test_fototipo_display_sem_fototipo(self):
        i = InteressadoFactory.create(fototipo=None)
        result = self.ma.fototipo_display(i)
        self.assertIn('\u2014', str(result))

    # --- programa_social_display ---

    def test_programa_social_display_true(self):
        result = str(self.ma.programa_social_display(self.interessado))
        self.assertIn('28a745', result)

    def test_programa_social_display_false(self):
        i = InteressadoFactory.create(programa_social=False)
        result = str(self.ma.programa_social_display(i))
        self.assertIn('6c757d', result)

    # --- necessidades_especiais_display ---

    def test_necessidades_especiais_display_true(self):
        result = str(self.ma.necessidades_especiais_display(self.interessado))
        self.assertIn('007bff', result)

    def test_necessidades_especiais_display_false(self):
        i = InteressadoFactory.create(
            necessidades_especiais=False,
            pcd_fisica=False, pcd_visual=False, pcd_auditiva=False,
            pcd_intelectual=False, pcd_psicossocial=False, pcd_multiplas=False,
        )
        result = str(self.ma.necessidades_especiais_display(i))
        self.assertIn('6c757d', result)

    # --- celular_formatado ---

    def test_celular_formatado_11_digitos(self):
        result = str(self.ma.celular_formatado(self.interessado))
        self.assertIn('(11) 98765-4321', result)

    def test_celular_formatado_vazio(self):
        i = InteressadoFactory.create(celular='')
        result = str(self.ma.celular_formatado(i))
        self.assertIn('\u2014', result)

    # --- telefone_formatado ---

    def test_telefone_formatado_10_digitos(self):
        result = str(self.ma.telefone_formatado(self.interessado))
        self.assertIn('(11) 3333-4444', result)

    def test_telefone_formatado_vazio(self):
        i = InteressadoFactory.create(telefone='')
        result = str(self.ma.telefone_formatado(i))
        self.assertIn('\u2014', result)

    # --- is_active_display ---

    def test_is_active_display_ativo(self):
        result = str(self.ma.is_active_display(self.interessado))
        self.assertIn('Ativo', result)

    def test_is_active_display_inativo(self):
        i = InteressadoFactory.create(is_active=False)
        result = str(self.ma.is_active_display(i))
        self.assertIn('Inativo', result)

    # --- short_description ---

    def test_short_descriptions(self):
        self.assertEqual(
            self.ma.data_nascimento_formatada.short_description,
            'Data Nascimento',
        )
        self.assertEqual(self.ma.sexo_display.short_description, 'Sexo')
        self.assertEqual(self.ma.celular_formatado.short_description, 'Celular')
        self.assertEqual(self.ma.telefone_formatado.short_description, 'Telefone')


class TestInteressadoAdminSaveModel(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.interessado = InteressadoFactory.create()

    def setUp(self):
        self.ma = InteressadoAdmin(model=Interessado, admin_site=admin_site)

    def test_save_model_com_senha_nova_aplica_set_password(self):
        class MockForm:
            changed_data = ['senha']
            cleaned_data = {'senha': 'NovaSenha789!'}

        request = HttpRequest()
        self.ma.save_model(request, self.interessado, MockForm(), change=True)
        self.interessado.refresh_from_db()
        self.assertTrue(self.interessado.check_password('NovaSenha789!'))


class TestInteressadoAdminActions(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.i1 = InteressadoFactory.create(is_active=True, programa_social=True, pcd_fisica=True)
        cls.i2 = InteressadoFactory.create(is_active=True)

    def setUp(self):
        self.ma = InteressadoAdmin(model=Interessado, admin_site=admin_site)
        self.request = HttpRequest()
        self.request.user = type('User', (), {'is_superuser': True})()
        # CookieStorage nao precisa de middleware de sessao
        setattr(self.request, '_messages', CookieStorage(self.request))

    def test_ativar_interessados(self):
        Interessado.objects.update(is_active=False)
        qs = Interessado.objects.all()
        self.ma.ativar_interessados(self.request, qs)
        for i in Interessado.objects.all():
            self.assertTrue(i.is_active)

    def test_desativar_interessados(self):
        qs = Interessado.objects.all()
        self.ma.desativar_interessados(self.request, qs)
        for i in Interessado.objects.all():
            self.assertFalse(i.is_active)

    def test_gerar_senha_provisoria_rejeita_multiplos(self):
        qs = Interessado.objects.all()
        self.ma.gerar_senha_provisoria(self.request, qs)
        self.i1.refresh_from_db()
        self.assertTrue(self.i1.check_password('senha123'))

    def test_gerar_senha_provisoria_um_interessado(self):
        qs = Interessado.objects.filter(pk=self.i1.pk)
        self.ma.gerar_senha_provisoria(self.request, qs)
        self.i1.refresh_from_db()
        self.assertTrue(self.i1.must_change_password)
        self.assertFalse(self.i1.check_password('senha123'))

    def test_exportar_interessados_retorna_csv(self):
        qs = Interessado.objects.all()
        response = self.ma.exportar_interessados_detalhado(self.request, qs)
        self.assertEqual(response.status_code, 200)
        self.assertIn('text/csv', response['Content-Type'])
        self.assertIn('.csv', response['Content-Disposition'])

    def test_exportar_interessados_conteudo_tem_cabecalho(self):
        qs = Interessado.objects.filter(pk=self.i1.pk)
        response = self.ma.exportar_interessados_detalhado(self.request, qs)
        conteudo = response.content.decode('utf-8-sig')
        self.assertIn('CPF', conteudo)
        self.assertIn('Crit\u00e9rios Atendidos', conteudo)
        self.assertIn(self.i1.nome, conteudo)


class TestPasswordResetTokenAdmin(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.interessado = InteressadoFactory.create()
        # Token com uuid para respeitar unique constraint
        cls.token_valido = PasswordResetToken.objects.create(
            interessado=cls.interessado,
            token=str(uuid.uuid4()),
            usado=False,
            criado_em=timezone.now(),
            expira_em=timezone.now() + timedelta(hours=24),
        )
        cls.token_expirado = PasswordResetToken.objects.create(
            interessado=cls.interessado,
            token=str(uuid.uuid4()),
            usado=False,
            criado_em=timezone.now() - timedelta(days=2),
            expira_em=timezone.now() - timedelta(days=1),
        )
        cls.token_usado = PasswordResetToken.objects.create(
            interessado=cls.interessado,
            token=str(uuid.uuid4()),
            usado=True,
            criado_em=timezone.now() - timedelta(days=1),
            expira_em=timezone.now() + timedelta(hours=24),
        )

    def setUp(self):
        self.ma = PasswordResetTokenAdmin(
            model=PasswordResetToken,
            admin_site=admin_site,
        )
        self.request = HttpRequest()
        self.request.user = type('User', (), {'is_superuser': True})()
        setattr(self.request, '_messages', CookieStorage(self.request))

    def test_get_interessado_retorna_nome(self):
        result = self.ma.get_interessado(self.token_valido)
        self.assertEqual(result, self.interessado.nome)

    def test_get_status_valido(self):
        result = str(self.ma.get_status(self.token_valido))
        self.assertIn('V\u00e1lido', result)

    def test_get_status_expirado(self):
        result = str(self.ma.get_status(self.token_expirado))
        self.assertIn('Expirado', result)

    def test_get_status_usado(self):
        result = str(self.ma.get_status(self.token_usado))
        self.assertIn('Usado', result)

    def test_limpar_tokens_expirados(self):
        qs = PasswordResetToken.objects.all()
        self.ma.limpar_tokens_expirados(self.request, qs)
        self.assertFalse(PasswordResetToken.objects.filter(pk=self.token_expirado.pk).exists())
        self.assertTrue(PasswordResetToken.objects.filter(pk=self.token_valido.pk).exists())
        self.assertTrue(PasswordResetToken.objects.filter(pk=self.token_usado.pk).exists())

    def test_limpar_tokens_usados(self):
        qs = PasswordResetToken.objects.all()
        self.ma.limpar_tokens_usados(self.request, qs)
        self.assertFalse(PasswordResetToken.objects.filter(pk=self.token_usado.pk).exists())
        self.assertTrue(PasswordResetToken.objects.filter(pk=self.token_valido.pk).exists())
        self.assertTrue(PasswordResetToken.objects.filter(pk=self.token_expirado.pk).exists())

    def test_limpar_todos_invalidos(self):
        qs = PasswordResetToken.objects.all()
        self.ma.limpar_todos_invalidos(self.request, qs)
        self.assertTrue(PasswordResetToken.objects.filter(pk=self.token_valido.pk).exists())
        self.assertFalse(PasswordResetToken.objects.filter(pk=self.token_expirado.pk).exists())
        self.assertFalse(PasswordResetToken.objects.filter(pk=self.token_usado.pk).exists())

    def test_has_add_permission_false(self):
        self.assertFalse(self.ma.has_add_permission(self.request))

    def test_has_change_permission_false(self):
        self.assertFalse(self.ma.has_change_permission(self.request))

    def test_has_delete_permission_superuser_true(self):
        self.assertTrue(self.ma.has_delete_permission(self.request))

    def test_has_delete_permission_normal_user_false(self):
        req = HttpRequest()
        req.user = type('User', (), {'is_superuser': False})()
        self.assertFalse(self.ma.has_delete_permission(req))


        