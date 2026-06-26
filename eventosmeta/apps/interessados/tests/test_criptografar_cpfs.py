"""
Arquivo: test_criptografar_cpfs.py
Caminho: apps/interessados/tests/test_criptografar_cpfs.py
Finalidade: Testes para o management command criptografar_cpfs
Atualizações:
 - 24/06/2026 - Criação do arquivo
 - 24/06/2026 - Correção: cpf_hash vazio gera UniqueViolation no PostgreSQL
                Correção: asserção do teste de hash preenchido
"""
import pytest
from io import StringIO
from django.core.management import call_command
from apps.interessados.models import Interessado, gerar_hash_cpf
from apps.interessados.tests.factories import InteressadoFactory

pytestmark = pytest.mark.django_db

class TestCriptografarCpfsCommand:
    """
    Testes para o comando 'python manage.py criptografar_cpfs'.

    O comando percorre todos os Interessado, reatribui o CPF para acionar
    a criptografia do EncryptedCharField e preenche o cpf_hash.
    """

    def test_comando_atualiza_cpf_hash_quando_vazio(self):
        """Deve preencher cpf_hash de registros que estão com hash vazio."""
        interessado = InteressadoFactory(cpf_hash='')

        out = StringIO()
        call_command('criptografar_cpfs', stdout=out)
        output = out.getvalue()

        interessado.refresh_from_db()
        hash_esperado = gerar_hash_cpf(interessado.cpf)

        assert interessado.cpf_hash == hash_esperado
        assert '1 atualizado(s)' in output

    def test_comando_mantem_cpf_hash_quando_ja_preenchido(self):
        """Deve manter o hash existente se ele já estiver preenchido."""
        cpf_original = '12345678901'
        hash_original = gerar_hash_cpf(cpf_original)
        interessado = InteressadoFactory(
            cpf=cpf_original,
            cpf_hash=hash_original
        )

        out = StringIO()
        call_command('criptografar_cpfs', stdout=out)

        interessado.refresh_from_db()
        assert interessado.cpf_hash == hash_original

    def test_comando_processa_multiplos_registros(self):
        """
        Deve processar múltiplos registros com cpf_hash vazio.
        Usa hashes únicos para evitar UniqueViolation no PostgreSQL.
        """
        InteressadoFactory(cpf_hash='')
        InteressadoFactory(cpf_hash='hash_unico_1')
        InteressadoFactory(cpf_hash='hash_unico_2')

        out = StringIO()
        call_command('criptografar_cpfs', stdout=out)
        output = out.getvalue()

        total_com_hash = Interessado.objects.exclude(cpf_hash='').count()

        assert total_com_hash == 3
        assert '3 atualizado(s)' in output

    def test_comando_sem_registros_nao_gera_erro(self):
        """Não deve gerar erro se não houver nenhum Interessado no banco."""
        out = StringIO()
        call_command('criptografar_cpfs', stdout=out)
        output = out.getvalue()

        assert '0 atualizado(s)' in output

    def test_comando_sempre_processa_todos_os_registros(self):
        """
        O comando sempre percorre todos os registros e reatribui o CPF
        para acionar a criptografia. Portanto, sempre reporta N atualizados.
        """
        InteressadoFactory()
        InteressadoFactory()

        out = StringIO()
        call_command('criptografar_cpfs', stdout=out)
        output = out.getvalue()

        assert '2 atualizado(s)' in output

        