"""
Comando para popular critérios fixos de classificação
"""
from django.core.management.base import BaseCommand
from apps.eventos.models import Criterio


class Command(BaseCommand):
    help = 'Popula critérios fixos de classificação no sistema'
    
    def handle(self, *args, **options):
        self.stdout.write('🔧 Populando critérios fixos...\n')
        
        criterios = [
            # VULNERABILIDADE SOCIAL
            {
                'codigo': 'PCD',
                'nome': 'Pessoa com Deficiência (PCD)',
                'descricao': 'Interessado possui algum tipo de deficiência física, mental, intelectual ou sensorial',
                'pontos': 15,
                'categoria': 'VULNERABILIDADE',
            },
            {
                'codigo': 'NIS',
                'nome': 'Cadastro Único (NIS)',
                'descricao': 'Interessado possui Número de Identificação Social (NIS) ativo',
                'pontos': 10,
                'categoria': 'VULNERABILIDADE',
            },
            
            # FAIXA ETÁRIA
            {
                'codigo': 'JOVEM',
                'nome': 'Jovem (16 a 24 anos)',
                'descricao': 'Interessado tem idade entre 16 e 24 anos',
                'pontos': 5,
                'categoria': 'FAIXA_ETARIA',
            },
            {
                'codigo': 'IDOSO',
                'nome': 'Idoso (50+ anos)',
                'descricao': 'Interessado tem 50 anos ou mais',
                'pontos': 5,
                'categoria': 'FAIXA_ETARIA',
            },
            
            # COTAS RACIAIS
            {
                'codigo': 'COTA_RACIAL',
                'nome': 'Preto, Pardo ou Indígena',
                'descricao': 'Interessado se autodeclara preto, pardo ou indígena',
                'pontos': 5,
                'categoria': 'COTA_RACIAL',
            },
            
            # ESCOLARIDADE
            {
                'codigo': 'ESC_FUND_INC',
                'nome': 'Ensino Fundamental Incompleto',
                'descricao': 'Escolaridade: Ensino Fundamental Incompleto',
                'pontos': 5,
                'categoria': 'ESCOLARIDADE',
            },
            {
                'codigo': 'ESC_FUND_COMP',
                'nome': 'Ensino Fundamental Completo',
                'descricao': 'Escolaridade: Ensino Fundamental Completo',
                'pontos': 3,
                'categoria': 'ESCOLARIDADE',
            },
            {
                'codigo': 'ESC_MEDIO_INC',
                'nome': 'Ensino Médio Incompleto',
                'descricao': 'Escolaridade: Ensino Médio Incompleto',
                'pontos': 2,
                'categoria': 'ESCOLARIDADE',
            },
            {
                'codigo': 'ESC_MEDIO_COMP',
                'nome': 'Ensino Médio Completo',
                'descricao': 'Escolaridade: Ensino Médio Completo',
                'pontos': 1,
                'categoria': 'ESCOLARIDADE',
            },
        ]
        
        criados = 0
        atualizados = 0
        
        for crit_data in criterios:
            criterio, created = Criterio.objects.update_or_create(
                codigo=crit_data['codigo'],
                defaults={
                    'nome': crit_data['nome'],
                    'descricao': crit_data['descricao'],
                    'pontos': crit_data['pontos'],
                    'categoria': crit_data['categoria'],
                    'ativo': True,
                }
            )
            
            if created:
                criados += 1
                self.stdout.write(
                    self.style.SUCCESS(f'✅ Criado: {criterio.nome} ({criterio.pontos} pts)')
                )
            else:
                atualizados += 1
                self.stdout.write(
                    self.style.WARNING(f'🔄 Atualizado: {criterio.nome} ({criterio.pontos} pts)')
                )
        
        self.stdout.write('\n' + '='*60)
        self.stdout.write(self.style.SUCCESS(f'✅ CONCLUÍDO!'))
        self.stdout.write(f'   Criados: {criados}')
        self.stdout.write(f'   Atualizados: {atualizados}')
        self.stdout.write('='*60)

        