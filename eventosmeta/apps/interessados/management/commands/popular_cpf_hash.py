"""
Script: popular_cpf_hash.py
Caminho: apps/interessados/management/commands/popular_cpf_hash.py
Finalidade: Popula o campo cpf_hash em todos os registros existentes
            que ainda não têm o hash gerado.
Uso: python manage.py popular_cpf_hash
Data: 17/03/2026
"""
from django.core.management.base import BaseCommand
from apps.interessados.models import Interessado, gerar_hash_cpf


class Command(BaseCommand):
    help = 'Popula cpf_hash em todos os Interessados que ainda não têm o hash'

    def handle(self, *args, **kwargs):
        sem_hash = Interessado.objects.filter(cpf_hash='')
        total = sem_hash.count()

        if total == 0:
            self.stdout.write(self.style.SUCCESS('Todos os registros já têm cpf_hash. Nada a fazer.'))
            return

        self.stdout.write(f'Gerando hash para {total} registro(s)...')

        atualizados = 0
        erros = 0

        for interessado in sem_hash:
            try:
                interessado.cpf_hash = gerar_hash_cpf(interessado.cpf)
                interessado.save(update_fields=['cpf_hash'])
                atualizados += 1
            except Exception as e:
                self.stdout.write(
                    self.style.ERROR(f'Erro no registro id={interessado.id}: {e}')
                )
                erros += 1

        self.stdout.write(self.style.SUCCESS(
            f'Concluído. {atualizados} atualizado(s), {erros} erro(s).'
        ))


