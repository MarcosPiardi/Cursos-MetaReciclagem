

"""
Comando para popular dados iniciais do sistema
Uso: python manage.py popular_dados_iniciais
"""
from django.core.management.base import BaseCommand
from django.db import transaction
from apps.eventos.models import Status, Criterio
from apps.selecao.models import StatusInscricao
from apps.academico.models import StatusMatricula
from apps.interessados.models import Sexo, Fototipo


class Command(BaseCommand):
    help = 'Popula dados iniciais necessários para o sistema funcionar'

    @transaction.atomic
    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('========================================'))
        self.stdout.write(self.style.SUCCESS('POPULANDO DADOS INICIAIS'))
        self.stdout.write(self.style.SUCCESS('========================================\n'))

        # 1. Status de Eventos
        self.stdout.write('1. Criando Status de Eventos...')
        status_eventos = [
            {'nome': 'Planejamento', 'ordem': 1, 'ativo': True},
            {'nome': 'Inscrições Abertas', 'ordem': 2, 'ativo': True},
            {'nome': 'Inscrições Encerradas', 'ordem': 3, 'ativo': True},
            {'nome': 'Em Classificação', 'ordem': 4, 'ativo': True},
            {'nome': 'Resultado Divulgado', 'ordem': 5, 'ativo': True},
            {'nome': 'Em Andamento', 'ordem': 6, 'ativo': True},
            {'nome': 'Finalizado', 'ordem': 7, 'ativo': True},
            {'nome': 'Cancelado', 'ordem': 8, 'ativo': False},
        ]
        
        for dados in status_eventos:
            status, created = Status.objects.get_or_create(
                nome=dados['nome'],
                defaults={'ordem': dados['ordem'], 'ativo': dados['ativo']}
            )
            if created:
                self.stdout.write(f'   ✅ Criado: {status.nome}')
            else:
                self.stdout.write(f'   ⏭️  Já existe: {status.nome}')

        # 2. Status de Inscrições
        self.stdout.write('\n2. Criando Status de Inscrições...')
        status_inscricoes = [
            {'nome': 'Pendente', 'cor': '#FFA500', 'ordem': 1},
            {'nome': 'Em Análise', 'cor': '#1E90FF', 'ordem': 2},
            {'nome': 'Aprovada', 'cor': '#32CD32', 'ordem': 3},
            {'nome': 'Reprovada', 'cor': '#DC143C', 'ordem': 4},
            {'nome': 'Cancelada', 'cor': '#808080', 'ordem': 5},
        ]
        
        for dados in status_inscricoes:
            status, created = StatusInscricao.objects.get_or_create(
                nome=dados['nome'],
                defaults={'cor': dados['cor'], 'ordem': dados['ordem']}
            )
            if created:
                self.stdout.write(f'   ✅ Criado: {status.nome}')
            else:
                self.stdout.write(f'   ⏭️  Já existe: {status.nome}')

        # 3. Status de Matrículas
        self.stdout.write('\n3. Criando Status de Matrículas...')
        status_matriculas = [
            {'nome': 'Pendente', 'cor': '#FFA500', 'ordem': 1},
            {'nome': 'Ativa', 'cor': '#32CD32', 'ordem': 2},
            {'nome': 'Concluída', 'cor': '#1E90FF', 'ordem': 3},
            {'nome': 'Trancada', 'cor': '#FFD700', 'ordem': 4},
            {'nome': 'Cancelada', 'cor': '#DC143C', 'ordem': 5},
        ]
        
        for dados in status_matriculas:
            status, created = StatusMatricula.objects.get_or_create(
                nome=dados['nome'],
                defaults={'cor': dados['cor'], 'ordem': dados['ordem']}
            )
            if created:
                self.stdout.write(f'   ✅ Criado: {status.nome}')
            else:
                self.stdout.write(f'   ⏭️  Já existe: {status.nome}')

        # 4. Critérios de Seleção
        self.stdout.write('\n4. Criando Critérios de Seleção...')
        criterios = [
            {
                'nome': 'Morador de Manaus',
                'tipo': 'MORADOR_MANAUS',
                'descricao': 'Reside em Manaus/AM',
                'pontos': 10,
                'requer_validacao_manual': False,
                'ativo': True
            },
            {
                'nome': 'Pessoa com Deficiência (PCD)',
                'tipo': 'PCD',
                'descricao': 'Possui algum tipo de deficiência',
                'pontos': 15,
                'requer_validacao_manual': False,
                'ativo': True
            },
            {
                'nome': 'Beneficiário de Programa Social',
                'tipo': 'PROGRAMA_SOCIAL',
                'descricao': 'Participa de programas sociais (Bolsa Família, etc.)',
                'pontos': 10,
                'requer_validacao_manual': False,
                'ativo': True
            },
            {
                'nome': 'Idade entre 16 e 24 anos',
                'tipo': 'FAIXA_ETARIA',
                'descricao': 'Público jovem prioritário',
                'pontos': 5,
                'ordem_idade': 1,
                'requer_validacao_manual': True,
                'ativo': True
            },
            {
                'nome': 'Idade acima de 50 anos',
                'tipo': 'FAIXA_ETARIA',
                'descricao': 'Público idoso prioritário',
                'pontos': 5,
                'ordem_idade': 2,
                'requer_validacao_manual': True,
                'ativo': True
            },
            {
                'nome': 'Ensino Fundamental Completo',
                'tipo': 'ESCOLARIDADE',
                'descricao': 'Possui ensino fundamental completo',
                'pontos': 3,
                'requer_validacao_manual': True,
                'ativo': True
            },
            {
                'nome': 'Renda Familiar até 2 salários mínimos',
                'tipo': 'RENDA_FAMILIAR',
                'descricao': 'Renda familiar de até R$ 2.640,00',
                'pontos': 8,
                'requer_validacao_manual': True,
                'ativo': True
            },
        ]
        
        for dados in criterios:
            criterio, created = Criterio.objects.get_or_create(
                tipo=dados['tipo'],
                nome=dados['nome'],
                defaults={
                    'descricao': dados['descricao'],
                    'pontos': dados['pontos'],
                    'ordem_idade': dados.get('ordem_idade'),
                    'requer_validacao_manual': dados['requer_validacao_manual'],
                    'ativo': dados['ativo']
                }
            )
            if created:
                self.stdout.write(f'   ✅ Criado: {criterio.nome}')
            else:
                self.stdout.write(f'   ⏭️  Já existe: {criterio.nome}')

        # 5. Sexo
        self.stdout.write('\n5. Criando opções de Sexo...')
        sexos = ['Masculino', 'Feminino', 'Outro', 'Prefiro não informar']
        
        for nome in sexos:
            sexo, created = Sexo.objects.get_or_create(nome=nome)
            if created:
                self.stdout.write(f'   ✅ Criado: {sexo.nome}')
            else:
                self.stdout.write(f'   ⏭️  Já existe: {sexo.nome}')

        # 6. Fototipos (Padrão IBGE - Cor/Raça)
        self.stdout.write('\n6. Criando Fototipos (Padrão IBGE)...')
        fototipos = [
            {
                'nome': 'Branca',
                'descricao': 'Pessoa que se autodeclara branca (Padrão IBGE)'
            },
            {
                'nome': 'Preta',
                'descricao': 'Pessoa que se autodeclara preta (Padrão IBGE)'
            },
            {
                'nome': 'Parda',
                'descricao': 'Pessoa que se autodeclara parda (Padrão IBGE)'
            },
            {
                'nome': 'Amarela',
                'descricao': 'Pessoa que se autodeclara amarela - descendência asiática (Padrão IBGE)'
            },
            {
                'nome': 'Indígena',
                'descricao': 'Pessoa que se autodeclara indígena (Padrão IBGE)'
            },
        ]
        
        for dados in fototipos:
            fototipo, created = Fototipo.objects.get_or_create(
                nome=dados['nome'],
                defaults={'descricao': dados['descricao']}
            )
            if created:
                self.stdout.write(f'   ✅ Criado: {fototipo.nome}')
            else:
                self.stdout.write(f'   ⏭️  Já existe: {fototipo.nome}')

        # Resumo
        self.stdout.write(self.style.SUCCESS('\n========================================'))
        self.stdout.write(self.style.SUCCESS('✅ DADOS INICIAIS POPULADOS COM SUCESSO!'))
        self.stdout.write(self.style.SUCCESS('========================================\n'))
        
        self.stdout.write('Resumo:')
        self.stdout.write(f'  • Status de Eventos: {Status.objects.count()}')
        self.stdout.write(f'  • Status de Inscrições: {StatusInscricao.objects.count()}')
        self.stdout.write(f'  • Status de Matrículas: {StatusMatricula.objects.count()}')
        self.stdout.write(f'  • Critérios de Seleção: {Criterio.objects.count()}')
        self.stdout.write(f'  • Sexo: {Sexo.objects.count()}')
        self.stdout.write(f'  • Fototipos (IBGE): {Fototipo.objects.count()}')
        self.stdout.write('')

        