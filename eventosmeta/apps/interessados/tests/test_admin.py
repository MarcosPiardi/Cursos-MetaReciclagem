"""
Arquivo: test_admin.py
Caminho: apps/interessados/tests/test_admin.py
Testes para admin do app Interessados
SexoAdmin, FototipoAdmin, InteressadoAdmin, PasswordResetTokenAdmin
Data: 29/05/2026
Refatorado: 18/06/2006 - unittest.TestCase para pytest
Atualização: 13/07/2026 - CORRIGIDO: import de admin_site customizado
             (removido de apps.accounts.admin). Substituído por
             django.contrib.admin.site, alinhado com a remoção do
             CustomAdminSite (ver config/urls.py, 08/07/2026)
"""

import uuid
from datetime import date, timedelta

import pytest
from django.http import HttpRequest
from django.contrib.messages.storage.cookie import CookieStorage
from django.utils import timezone

from django.contrib.admin import site as admin_site
from apps.interessados.admin import (
    SexoAdmin,
    FototipoAdmin,
    InteressadoAdmin,
    PasswordResetTokenAdmin,
)
from apps.interessados.models import Interessado, Sexo, Fototipo, PasswordResetToken
from .factories import InteressadoFactory, SexoFactory, FototipoFactory
from apps.admin_mixins import CustomTitleMixin

pytestmark = pytest.mark.django_db

# ── Helpers ───────────────────────────────────────────────────────────

def _make_request(is_superuser=True):
    request = HttpRequest()
    request.user = type("User", (), {"is_superuser": is_superuser})()
    setattr(request, "_messages", CookieStorage(request))
    return request

# ── SexoAdmin ─────────────────────────────────────────────────────────

class TestSexoAdmin:
    def test_list_display(self):
        assert SexoAdmin.list_display == ["nome"]

    def test_search_fields(self):
        assert SexoAdmin.search_fields == ["nome"]

# ── FototipoAdmin ─────────────────────────────────────────────────────

class TestFototipoAdmin:
    def test_list_display(self):
        assert FototipoAdmin.list_display == ["nome", "descricao"]

    def test_search_fields(self):
        assert FototipoAdmin.search_fields == ["nome", "descricao"]

# ── InteressadoAdmin Métodos ──────────────────────────────────────────

class TestInteressadoAdminMetodos:
    @pytest.fixture(autouse=True)
    def setup(self, db):
        self.sexo = SexoFactory(nome="Feminino")
        self.fototipo = FototipoFactory(nome="Tipo I")
        self.interessado = InteressadoFactory.create(
            sexo=self.sexo,
            fototipo=self.fototipo,
            data_nascimento=date(1990, 5, 15),
            celular="11987654321",
            telefone="1133334444",
            programa_social=True,
            necessidades_especiais=True,
            pcd_fisica=True,
        )
        self.ma = InteressadoAdmin(model=Interessado, admin_site=admin_site)

    # --- data_nascimento_formatada ---

    def test_data_nascimento_formatada_com_data(self):
        result = self.ma.data_nascimento_formatada(self.interessado)
        assert "15/05/1990" in str(result)

    def test_data_nascimento_formatada_sem_data(self):
        i = InteressadoFactory.create(data_nascimento=None)
        result = self.ma.data_nascimento_formatada(i)
        assert "\u2014" in str(result)

    # --- sexo_display ---

    def test_sexo_display_com_sexo(self):
        result = self.ma.sexo_display(self.interessado)
        assert result == "Feminino"

    def test_sexo_display_sem_sexo(self):
        i = InteressadoFactory.create(sexo=None)
        result = self.ma.sexo_display(i)
        assert result == "\u2014"

    # --- fototipo_display ---

    def test_fototipo_display_com_fototipo(self):
        result = self.ma.fototipo_display(self.interessado)
        assert "Tipo I" in str(result)

    def test_fototipo_display_sem_fototipo(self):
        i = InteressadoFactory.create(fototipo=None)
        result = self.ma.fototipo_display(i)
        assert "\u2014" in str(result)

    # --- programa_social_display ---

    def test_programa_social_display_true(self):
        result = str(self.ma.programa_social_display(self.interessado))
        assert "28a745" in result

    def test_programa_social_display_false(self):
        i = InteressadoFactory.create(programa_social=False)
        result = str(self.ma.programa_social_display(i))
        assert "6c757d" in result

    # --- necessidades_especiais_display ---

    def test_necessidades_especiais_display_true(self):
        result = str(self.ma.necessidades_especiais_display(self.interessado))
        assert "007bff" in result

    def test_necessidades_especiais_display_false(self):
        i = InteressadoFactory.create(
            necessidades_especiais=False,
            pcd_fisica=False, pcd_visual=False, pcd_auditiva=False,
            pcd_intelectual=False, pcd_psicossocial=False, pcd_multiplas=False,
        )
        result = str(self.ma.necessidades_especiais_display(i))
        assert "6c757d" in result

    # --- celular_formatado ---

    def test_celular_formatado_11_digitos(self):
        result = str(self.ma.celular_formatado(self.interessado))
        assert "(11) 98765-4321" in result

    def test_celular_formatado_vazio(self):
        i = InteressadoFactory.create(celular="")
        result = str(self.ma.celular_formatado(i))
        assert "\u2014" in result

    # --- telefone_formatado ---

    def test_telefone_formatado_10_digitos(self):
        result = str(self.ma.telefone_formatado(self.interessado))
        assert "(11) 3333-4444" in result

    def test_telefone_formatado_vazio(self):
        i = InteressadoFactory.create(telefone="")
        result = str(self.ma.telefone_formatado(i))
        assert "\u2014" in result

    # --- is_active_display ---

    def test_is_active_display_ativo(self):
        result = str(self.ma.is_active_display(self.interessado))
        assert "Ativo" in result

    def test_is_active_display_inativo(self):
        i = InteressadoFactory.create(is_active=False)
        result = str(self.ma.is_active_display(i))
        assert "Inativo" in result

    # --- short_description ---

    def test_short_descriptions(self):
        assert (
            self.ma.data_nascimento_formatada.short_description
            == "Data Nascimento"
        )
        assert self.ma.sexo_display.short_description == "Sexo"
        assert self.ma.celular_formatado.short_description == "Celular"
        assert self.ma.telefone_formatado.short_description == "Telefone"

# ── InteressadoAdmin SaveModel ────────────────────────────────────────

class TestInteressadoAdminSaveModel:
    @pytest.fixture(autouse=True)
    def setup(self, db):
        self.interessado = InteressadoFactory.create()
        self.ma = InteressadoAdmin(model=Interessado, admin_site=admin_site)

    def test_save_model_com_senha_nova_aplica_set_password(self):
        class MockForm:
            changed_data = ["senha"]
            cleaned_data = {"senha": "NovaSenha789!"}

        request = HttpRequest()
        self.ma.save_model(request, self.interessado, MockForm(), change=True)
        self.interessado.refresh_from_db()
        assert self.interessado.check_password("NovaSenha789!")

# ── InteressadoAdmin Actions ──────────────────────────────────────────

class TestInteressadoAdminActions:
    @pytest.fixture(autouse=True)
    def setup(self, db):
        self.i1 = InteressadoFactory.create(
            is_active=True, programa_social=True, pcd_fisica=True
        )
        self.i2 = InteressadoFactory.create(is_active=True)
        self.ma = InteressadoAdmin(model=Interessado, admin_site=admin_site)
        self.request = _make_request()

    def test_ativar_interessados(self):
        Interessado.objects.update(is_active=False)
        qs = Interessado.objects.all()
        self.ma.ativar_interessados(self.request, qs)
        for i in Interessado.objects.all():
            assert i.is_active

    def test_desativar_interessados(self):
        qs = Interessado.objects.all()
        self.ma.desativar_interessados(self.request, qs)
        for i in Interessado.objects.all():
            assert not i.is_active

    def test_gerar_senha_provisoria_rejeita_multiplos(self):
        qs = Interessado.objects.all()
        self.ma.gerar_senha_provisoria(self.request, qs)
        self.i1.refresh_from_db()
        assert self.i1.check_password("senha123")

    def test_gerar_senha_provisoria_um_interessado(self):
        qs = Interessado.objects.filter(pk=self.i1.pk)
        self.ma.gerar_senha_provisoria(self.request, qs)
        self.i1.refresh_from_db()
        assert self.i1.must_change_password
        assert not self.i1.check_password("senha123")

    def test_exportar_interessados_retorna_csv(self):
        qs = Interessado.objects.all()
        response = self.ma.exportar_interessados_detalhado(self.request, qs)
        assert response.status_code == 200
        assert "text/csv" in response["Content-Type"]
        assert ".csv" in response["Content-Disposition"]

    def test_exportar_interessados_conteudo_tem_cabecalho(self):
        qs = Interessado.objects.filter(pk=self.i1.pk)
        response = self.ma.exportar_interessados_detalhado(self.request, qs)
        conteudo = response.content.decode("utf-8-sig")
        assert "CPF" in conteudo
        assert "Crit\u00e9rios Atendidos" in conteudo
        assert self.i1.nome in conteudo

# ── PasswordResetTokenAdmin ───────────────────────────────────────────

class TestPasswordResetTokenAdmin:
    @pytest.fixture(autouse=True)
    def setup(self, db):
        self.interessado = InteressadoFactory.create()
        self.ma = PasswordResetTokenAdmin(
            model=PasswordResetToken, admin_site=admin_site
        )
        self.request = _make_request()

        self.token_valido = PasswordResetToken.objects.create(
            interessado=self.interessado,
            token=str(uuid.uuid4()),
            usado=False,
            criado_em=timezone.now(),
            expira_em=timezone.now() + timedelta(hours=24),
        )
        self.token_expirado = PasswordResetToken.objects.create(
            interessado=self.interessado,
            token=str(uuid.uuid4()),
            usado=False,
            criado_em=timezone.now() - timedelta(days=2),
            expira_em=timezone.now() - timedelta(days=1),
        )
        self.token_usado = PasswordResetToken.objects.create(
            interessado=self.interessado,
            token=str(uuid.uuid4()),
            usado=True,
            criado_em=timezone.now() - timedelta(days=1),
            expira_em=timezone.now() + timedelta(hours=24),
        )

    def test_get_interessado_retorna_nome(self):
        result = self.ma.get_interessado(self.token_valido)
        assert result == self.interessado.nome

    def test_get_status_valido(self):
        result = str(self.ma.get_status(self.token_valido))
        assert "V\u00e1lido" in result

    def test_get_status_expirado(self):
        result = str(self.ma.get_status(self.token_expirado))
        assert "Expirado" in result

    def test_get_status_usado(self):
        result = str(self.ma.get_status(self.token_usado))
        assert "Usado" in result

    def test_limpar_tokens_expirados(self):
        qs = PasswordResetToken.objects.all()
        self.ma.limpar_tokens_expirados(self.request, qs)
        assert not PasswordResetToken.objects.filter(pk=self.token_expirado.pk).exists()
        assert PasswordResetToken.objects.filter(pk=self.token_valido.pk).exists()
        assert PasswordResetToken.objects.filter(pk=self.token_usado.pk).exists()

    def test_limpar_tokens_usados(self):
        qs = PasswordResetToken.objects.all()
        self.ma.limpar_tokens_usados(self.request, qs)
        assert not PasswordResetToken.objects.filter(pk=self.token_usado.pk).exists()
        assert PasswordResetToken.objects.filter(pk=self.token_valido.pk).exists()
        assert PasswordResetToken.objects.filter(pk=self.token_expirado.pk).exists()

    def test_limpar_todos_invalidos(self):
        qs = PasswordResetToken.objects.all()
        self.ma.limpar_todos_invalidos(self.request, qs)
        assert PasswordResetToken.objects.filter(pk=self.token_valido.pk).exists()
        assert not PasswordResetToken.objects.filter(pk=self.token_expirado.pk).exists()
        assert not PasswordResetToken.objects.filter(pk=self.token_usado.pk).exists()

    def test_has_add_permission_false(self):
        assert not self.ma.has_add_permission(self.request)

    def test_has_change_permission_false(self):
        assert not self.ma.has_change_permission(self.request)

    def test_has_delete_permission_superuser_true(self):
        assert self.ma.has_delete_permission(self.request)

    def test_has_delete_permission_normal_user_false(self):
        req = _make_request(is_superuser=False)
        assert not self.ma.has_delete_permission(req)

        