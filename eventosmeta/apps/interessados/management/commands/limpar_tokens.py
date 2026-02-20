"""
Arquivo: limpar_tokens.py
Caminho: apps/interessados/management/commands/limpar_tokens.py
Alteração: Management command para limpeza automática de tokens expirados
Data: 20/02/2026

Uso manual:
    python manage.py limpar_tokens
    python manage.py limpar_tokens --dry-run
    python manage.py limpar_tokens --dias 7
"""

from django.core.management.base import BaseCommand
from django.utils import timezone
from django.db import models


class Command(BaseCommand):
    """
    Remove tokens de recuperação de senha que estão expirados ou já foram usados.
    Projetado para execução automática via agendador (Task Scheduler / cron).
    """

    help = 'Limpa tokens de recuperação de senha expirados ou já utilizados'

    def add_arguments(self, parser):
        parser.add_argument(
            '--dry-run',
            action='store_true',
            help='Simula a limpeza sem deletar nada (apenas mostra o que seria removido)'
        )
        parser.add_argument(
            '--dias',
            type=int,
            default=0,
            help='Remove também tokens válidos mais antigos que N dias (padrão: 0 = não remove)'
        )

    def handle(self, *args, **options):
        from apps.interessados.models import PasswordResetToken

        dry_run = options['dry_run']
        dias    = options['dias']
        agora   = timezone.now()

        # ==========================================
        # IDENTIFICAR TOKENS A REMOVER
        # ==========================================

        # Tokens expirados (prazo vencido) OU já usados
        filtro_invalidos = (
            models.Q(expira_em__lt=agora) |
            models.Q(usado=True)
        )

        tokens_invalidos = PasswordResetToken.objects.filter(filtro_invalidos)

        # Tokens antigos demais (opcional, via --dias)
        tokens_antigos = PasswordResetToken.objects.none()
        if dias > 0:
            corte = agora - timezone.timedelta(days=dias)
            tokens_antigos = PasswordResetToken.objects.filter(
                criado_em__lt=corte
            ).exclude(filtro_invalidos)  # Evita duplicatas

        total_invalidos = tokens_invalidos.count()
        total_antigos   = tokens_antigos.count()
        total_geral     = total_invalidos + total_antigos

        # ==========================================
        # LOG DETALHADO
        # ==========================================

        self.stdout.write('=' * 60)
        self.stdout.write(
            self.style.SUCCESS('🧹 LIMPEZA DE TOKENS DE RECUPERAÇÃO DE SENHA')
        )
        self.stdout.write('=' * 60)
        self.stdout.write(f'📅 Data/Hora: {agora.strftime("%d/%m/%Y %H:%M:%S")}')
        self.stdout.write(f'🔍 Modo: {"SIMULAÇÃO (--dry-run)" if dry_run else "EXECUÇÃO REAL"}')
        self.stdout.write('-' * 60)
        self.stdout.write(f'❌ Tokens expirados/usados encontrados: {total_invalidos}')

        if dias > 0:
            self.stdout.write(
                f'📆 Tokens válidos com mais de {dias} dias encontrados: {total_antigos}'
            )

        self.stdout.write(f'📊 Total a remover: {total_geral}')
        self.stdout.write('-' * 60)

        # ==========================================
        # EXECUÇÃO OU SIMULAÇÃO
        # ==========================================

        if total_geral == 0:
            self.stdout.write(
                self.style.SUCCESS('✅ Banco já está limpo! Nenhum token a remover.')
            )
            self.stdout.write('=' * 60)
            return

        if dry_run:
            # Apenas simula — mostra detalhes sem deletar
            self.stdout.write(
                self.style.WARNING(
                    f'⚠️  SIMULAÇÃO: {total_geral} token(s) SERIAM removidos.'
                )
            )

            if total_invalidos > 0:
                self.stdout.write('\n📋 Tokens expirados/usados que seriam removidos:')
                for token in tokens_invalidos.select_related('interessado')[:10]:
                    status = 'USADO' if token.usado else 'EXPIRADO'
                    self.stdout.write(
                        f'   • {token.interessado.nome} '
                        f'({token.interessado.cpf}) — '
                        f'{status} — '
                        f'Criado: {token.criado_em.strftime("%d/%m/%Y %H:%M")}'
                    )
                if total_invalidos > 10:
                    self.stdout.write(f'   ... e mais {total_invalidos - 10} token(s)')

            self.stdout.write(
                self.style.WARNING(
                    '\n💡 Execute sem --dry-run para deletar de verdade.'
                )
            )

        else:
            # Execução real
            removidos_invalidos = tokens_invalidos.count()
            tokens_invalidos.delete()

            removidos_antigos = 0
            if dias > 0:
                removidos_antigos = tokens_antigos.count()
                tokens_antigos.delete()

            total_removidos = removidos_invalidos + removidos_antigos

            self.stdout.write(
                self.style.SUCCESS(
                    f'✅ {total_removidos} token(s) removido(s) com sucesso!'
                )
            )
            self.stdout.write(
                f'   • Expirados/usados: {removidos_invalidos}'
            )
            if dias > 0:
                self.stdout.write(
                    f'   • Antigos (>{dias} dias): {removidos_antigos}'
                )

        self.stdout.write('=' * 60)

        