"""
Arquivo: popular_dados_iniciais.py
Caminho: apps/scripts_admin/management/commands/popular_dados_iniciais.py
Alteração: Corrigidos campos dos models Status, StatusInscricao e Criterio
Data: 16/01/2026
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
            {'nome': 'Planejamento', 'cor': '#6c757d', 'ordem': 1},
            {'nome': 'Inscrições Abertas', 'cor': '#28a745', 'ordem': 2},
            {'nome': 'Inscrições Encerradas', 'cor': '#ffc107', 'ordem': 3},
            {'nome': 'Em Classificação', 'cor': '#17a2b8', 'ordem': 4},
            {'nome': 'Resultado Divulgado', 'cor': '#007bff', 'ordem': 5},
            {'nome': 'Em Andamento', 'cor': '#20c997', 'ordem': 6},
            {'nome': 'Finalizado', 'cor': '#6f42c1', 'ordem': 7},
            {'nome': 'Cancelado', 'cor': '#dc3545', 'ordem': 8},
        ]
        
        for dados in status_eventos:
            status, created = Status.objects.get_or_create(
                nome=dados['nome'],
                defaults={'cor': dados['cor'], 'ordem': dados['ordem']}
            )
            if created:
                self.stdout.write(f'   ✅ Criado: {status.nome}')
            else:
                self.stdout.write(f'   ⏭️  Já existe: {status.nome}')

        # 2. Status de Inscrições
        self.stdout.write('\n2. Criando Status de Inscrições...')
        status_inscricoes = [
            {'nome': 'Pendente', 'cor': '#ffc107', 'ordem': 1},
            {'nome': 'Classificado', 'cor': '#28a745', 'ordem': 2},
            {'nome': 'Confirmada', 'cor': '#007bff', 'ordem': 3},
            {'nome': 'Lista de Espera', 'cor': '#ffec1f', 'ordem': 4},
            {'nome': 'Cancelada', 'cor': '#dc3545', 'ordem': 5},
            {'nome': 'Expirada', 'cor': '#17a2b8', 'ordem': 6},
            {'nome': 'Desistente', 'cor': '#9b4003', 'ordem': 7},
            {'nome': 'Não localizado para confirmar matricula', 'cor': '#d360e2', 'ordem': 8},
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
                'codigo': 'PCD',
                'nome': 'Pessoa com Deficiência (PCD)',
                'tipo_criterio': 'PCD',
                'categoria': 'VULNERABILIDADE',
                'descricao': 'Possui algum tipo de deficiência',
                'pontos': 15,
                'ativo': True
            },
            {
                'codigo': 'PROGRAMA_SOCIAL',
                'nome': 'Beneficiário de Programa Social',
                'tipo_criterio': 'PROGRAMA_SOCIAL',
                'categoria': 'VULNERABILIDADE',
                'descricao': 'Participa de programas sociais (Bolsa Família, etc.)',
                'pontos': 10,
                'ativo': True
            },
            {
                'codigo': 'JOVEM',
                'nome': 'Idade entre 16 e 24 anos',
                'tipo_criterio': 'FAIXA_ETARIA',
                'categoria': 'FAIXA_ETARIA',
                'descricao': 'Público jovem prioritário',
                'pontos': 5,
                'ativo': True
            },
            {
                'codigo': 'IDOSO',
                'nome': 'Idade acima de 50 anos',
                'tipo_criterio': 'FAIXA_ETARIA',
                'categoria': 'FAIXA_ETARIA',
                'descricao': 'Público idoso prioritário',
                'pontos': 5,
                'ativo': True
            },
            {
                'codigo': 'ENSINO_FUNDAMENTAL',
                'nome': 'Ensino Fundamental Completo',
                'tipo_criterio': 'ESCOLARIDADE',
                'categoria': 'ESCOLARIDADE',
                'descricao': 'Possui ensino fundamental completo',
                'pontos': 3,
                'ativo': True
            },
            {
                'codigo': 'RENDA_BAIXA',
                'nome': 'Renda Familiar até 2 salários mínimos',
                'tipo_criterio': 'RENDA_FAMILIAR',
                'categoria': 'VULNERABILIDADE',
                'descricao': 'Renda familiar de até R$ 2.640,00',
                'pontos': 8,
                'ativo': True
            },
            {
                'codigo': 'COTA_RACIAL',
                'nome': 'Cota Racial',
                'tipo_criterio': 'COTA_RACIAL',
                'categoria': 'COTA_RACIAL',
                'descricao': 'Pessoa preta, parda ou indígena',
                'pontos': 5,
                'ativo': True
            },
        ]
        
        for dados in criterios:
            criterio, created = Criterio.objects.get_or_create(
                codigo=dados['codigo'],
                defaults={
                    'nome': dados['nome'],
                    'tipo_criterio': dados['tipo_criterio'],
                    'categoria': dados['categoria'],
                    'descricao': dados['descricao'],
                    'pontos': dados['pontos'],
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


