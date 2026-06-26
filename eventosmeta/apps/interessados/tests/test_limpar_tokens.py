"""
Arquivo: test_limpar_tokens.py
Caminho: apps/interessados/tests/test_limpar_tokens.py
Finalidade: Testes para o management command limpar_tokens
Atualizações:
 - 24/06/2026 - Criação do arquivo
 - 25/06/2026 - Correcao: criado_em tem auto_now_add=True no model,
                portanto o valor passado no create() eh ignorado.
                Usar update() apos criar para sobrescrever.
"""
import pytest
from io import StringIO
from datetime import timedelta
from django.core.management import call_command
from django.utils import timezone
from apps.interessados.models import PasswordResetToken
from apps.interessados.tests.factories import (
    PasswordResetTokenFactory,
    InteressadoFactory
)

pytestmark = pytest.mark.django_db

class TestLimparTokensCommand:

    def test_remove_tokens_expirados(self):
        PasswordResetTokenFactory(
            expira_em=timezone.now() - timedelta(hours=1)
        )
        call_command('limpar_tokens', stdout=StringIO())
        assert PasswordResetToken.objects.count() == 0

    def test_remove_tokens_usados(self):
        PasswordResetTokenFactory(usado=True)
        call_command('limpar_tokens', stdout=StringIO())
        assert PasswordResetToken.objects.count() == 0

    def test_mantem_tokens_validos(self):
        PasswordResetTokenFactory(
            expira_em=timezone.now() + timedelta(hours=1),
            usado=False
        )
        call_command('limpar_tokens', stdout=StringIO())
        assert PasswordResetToken.objects.count() == 1

    def test_dry_run_nao_remove_tokens(self):
        PasswordResetTokenFactory(
            expira_em=timezone.now() - timedelta(hours=1)
        )
        out = StringIO()
        call_command('limpar_tokens', '--dry-run', stdout=out)
        assert PasswordResetToken.objects.count() == 1
        assert 'SIMULAÇÃO' in out.getvalue()

    def test_dias_remove_token_valido_mas_antigo(self):
        """
        Cria token valido (nao expirado, nao usado) com criado_em
        antigo. Usa update() porque auto_now_add=True no model
        sobrescreve o valor passado no create().
        """
        interessado = InteressadoFactory()
        agora = timezone.now()
        token = PasswordResetToken.objects.create(
            interessado=interessado,
            token='token-teste-antigo',
            expira_em=agora + timedelta(days=30),
            usado=False
        )
        # auto_now_add=True ignora o valor passado no create()
        # Sobrescreve via update() diretamente no banco
        PasswordResetToken.objects.filter(pk=token.pk).update(
            criado_em=agora - timedelta(days=5)
        )
        assert PasswordResetToken.objects.count() == 1

        call_command('limpar_tokens', '--dias', '1', stdout=StringIO())

        assert PasswordResetToken.objects.count() == 0

    def test_dias_nao_remove_tokens_recentes(self):
        PasswordResetTokenFactory(
            criado_em=timezone.now() - timedelta(days=3),
            expira_em=timezone.now() + timedelta(days=1),
            usado=False
        )
        call_command('limpar_tokens', '--dias', '7', stdout=StringIO())
        assert PasswordResetToken.objects.count() == 1

    def test_sem_tokens_nao_gera_erro(self):
        out = StringIO()
        call_command('limpar_tokens', stdout=out)
        assert 'Banco já está limpo' in out.getvalue()

    def test_remove_tokens_expirados_e_usados_simultaneamente(self):
        PasswordResetTokenFactory(expira_em=timezone.now() - timedelta(hours=1))
        PasswordResetTokenFactory(usado=True)
        PasswordResetTokenFactory(
            expira_em=timezone.now() + timedelta(hours=1), usado=False
        )
        call_command('limpar_tokens', stdout=StringIO())
        assert PasswordResetToken.objects.count() == 1

        