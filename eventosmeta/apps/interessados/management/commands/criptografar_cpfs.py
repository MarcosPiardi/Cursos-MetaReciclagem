"""
Script: criptografar_cpfs.py
Caminho: apps/interessados/management/commands/criptografar_cpfs.py
Finalidade: Criptografa CPFs que ainda estão em texto plano no banco.
            Lê o CPF atual, salva de volta — o EncryptedCharField
            criptografa automaticamente ao salvar.
            Também atualiza o cpf_hash caso esteja vazio.
Uso: python manage.py criptografar_cpfs
Data: 17/03/2026
"""
from django.core.management.base import BaseCommand
from apps.interessados.models import Interessado, gerar_hash_cpf


class Command(BaseCommand):
    help = 'Criptografa CPFs em texto plano e garante cpf_hash preenchido'

    def handle(self, *args, **kwargs):
        todos = Interessado.objects.all()
        total = todos.count()

        self.stdout.write(f'Processando {total} registro(s)...')

        atualizados = 0
        erros       = 0

        for interessado in todos:
            try:
                cpf_atual = interessado.cpf

                # Garante que o cpf_hash está preenchido
                hash_atual = gerar_hash_cpf(cpf_atual)

                # Salva de volta — EncryptedCharField criptografa automaticamente
                interessado.cpf      = cpf_atual
                interessado.cpf_hash = hash_atual
                interessado.save(update_fields=['cpf', 'cpf_hash'])

                atualizados += 1

            except Exception as e:
                self.stdout.write(
                    self.style.ERROR(f'Erro no registro id={interessado.id}: {e}')
                )
                erros += 1

        self.stdout.write(self.style.SUCCESS(
            f'Concluído. {atualizados} atualizado(s), {erros} erro(s).'
        ))

        