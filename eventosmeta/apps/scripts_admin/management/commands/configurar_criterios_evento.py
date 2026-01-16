"""
Comando para configurar critérios de um evento
Uso: python manage.py configurar_criterios_evento --evento_id=1
"""
from django.core.management.base import BaseCommand
from apps.eventos.models import Evento, Criterio, EventoCriterio


class Command(BaseCommand):
    help = 'Configura critérios de seleção de um evento'

    def add_arguments(self, parser):
        parser.add_argument('--evento_id', type=int, help='ID do evento')

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
        
        self.stdout.write(self.style.SUCCESS(f'\n📋 CONFIGURANDO CRITÉRIOS DO EVENTO: {evento.nome}\n'))
        
        # Listar critérios disponíveis
        criterios = Criterio.objects.exclude(tipo='RENDA_FAMILIAR').order_by('tipo', 'nome')
        
        self.stdout.write('CRITÉRIOS DISPONÍVEIS:\n')
        for c in criterios:
            # Verificar se já está vinculado
            vinculado = EventoCriterio.objects.filter(evento=evento, criterio=c).exists()
            status = '✅' if vinculado else '⬜'
            self.stdout.write(f'{status} ID {c.id}: {c.nome} ({c.tipo}) - {c.pontos} pontos')
        
        self.stdout.write('\n' + '='*80)
        self.stdout.write('\nDIGITE OS IDs DOS CRITÉRIOS QUE DESEJA VINCULAR (separados por vírgula)')
        self.stdout.write('Exemplo: 2,3,4  (para vincular PCD, Programa Social e Faixa Etária 16-24)')
        self.stdout.write('Digite "limpar" para remover todos os critérios\n')
        
        escolha = input('Sua escolha: ').strip()
        
        if escolha.lower() == 'limpar':
            EventoCriterio.objects.filter(evento=evento).delete()
            self.stdout.write(self.style.SUCCESS('\n✅ Todos os critérios foram removidos!'))
            return
        
        if not escolha:
            self.stdout.write(self.style.WARNING('\n⚠️  Nenhuma alteração realizada'))
            return
        
        # Processar IDs
        try:
            ids = [int(x.strip()) for x in escolha.split(',')]
        except ValueError:
            self.stdout.write(self.style.ERROR('\n❌ IDs inválidos! Use apenas números separados por vírgula'))
            return
        
        # Limpar critérios existentes
        EventoCriterio.objects.filter(evento=evento).delete()
        
        # Vincular novos critérios
        ordem = 1
        vinculados = []
        
        for criterio_id in ids:
            try:
                criterio = Criterio.objects.get(pk=criterio_id)
                EventoCriterio.objects.create(
                    evento=evento,
                    criterio=criterio,
                    ordem=ordem,
                    ativo=True
                )
                vinculados.append(f'{criterio.nome} ({criterio.pontos} pts)')
                ordem += 1
            except Criterio.DoesNotExist:
                self.stdout.write(self.style.WARNING(f'⚠️  Critério ID {criterio_id} não encontrado'))
        
        if vinculados:
            self.stdout.write(self.style.SUCCESS(f'\n✅ CRITÉRIOS VINCULADOS COM SUCESSO!\n'))
            for i, nome in enumerate(vinculados, 1):
                self.stdout.write(f'   {i}. {nome}')
            
            self.stdout.write('\n💡 Execute agora: python manage.py classificar_evento --evento_id=1\n')
        else:
            self.stdout.write(self.style.ERROR('\n❌ Nenhum critério foi vinculado'))

            