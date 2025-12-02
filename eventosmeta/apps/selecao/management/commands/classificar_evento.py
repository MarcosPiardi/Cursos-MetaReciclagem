
"""
Comando para classificar inscrições de um evento
Uso: python manage.py classificar_evento --evento_id=1
"""
from django.core.management.base import BaseCommand
from apps.eventos.models import Evento
from apps.selecao.services import ClassificadorService


class Command(BaseCommand):
    help = 'Classifica todas as inscrições de um evento'

    def add_arguments(self, parser):
        parser.add_argument(
            '--evento_id',
            type=int,
            help='ID do evento a ser classificado'
        )

    def handle(self, *args, **options):
        evento_id = options.get('evento_id')
        
        if not evento_id:
            self.stdout.write(self.style.ERROR('❌ Informe o ID do evento: --evento_id=1'))
            return
        
        try:
            evento = Evento.objects.get(pk=evento_id)
        except Evento.DoesNotExist:
            self.stdout.write(self.style.ERROR(f'❌ Evento com ID {evento_id} não encontrado'))
            return
        
        self.stdout.write(self.style.SUCCESS(f'\n🎯 CLASSIFICANDO EVENTO: {evento.nome}\n'))
        
        # Executar classificação
        classificacoes = ClassificadorService.classificar_evento(evento)
        
        # Exibir resultado
        self.stdout.write(self.style.SUCCESS(f'\n✅ CLASSIFICAÇÃO CONCLUÍDA!\n'))
        self.stdout.write(f'Total de inscrições processadas: {classificacoes.count()}\n')
        
        self.stdout.write('\n📊 RESULTADO DA CLASSIFICAÇÃO:\n')
        self.stdout.write('-' * 80)
        
        for classificacao in classificacoes[:10]:  # Mostrar top 10
            status = '✅ CLASSIFICADO' if classificacao.classificado else '⏳ LISTA DE ESPERA'
            self.stdout.write(
                f'{classificacao.posicao}º - {classificacao.inscricao.interessado.nome} '
                f'- {classificacao.pontuacao_total} pontos - {status}'
            )
        
        if classificacoes.count() > 10:
            self.stdout.write(f'\n... e mais {classificacoes.count() - 10} candidatos')
        
        self.stdout.write('')

        
