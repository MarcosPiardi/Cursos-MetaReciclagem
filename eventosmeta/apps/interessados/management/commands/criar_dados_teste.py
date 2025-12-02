

"""
Comando para criar dados de teste completos
Uso: python manage.py criar_dados_teste
"""
from django.core.management.base import BaseCommand
from django.db import transaction
from django.utils import timezone
from datetime import date, timedelta

from apps.interessados.models import Interessado, Sexo, Fototipo
from apps.eventos.models import Evento, Status, Criterio, EventoCriterio, Turma
from apps.selecao.models import Inscricao, StatusInscricao


class Command(BaseCommand):
    help = 'Cria dados de teste completos para o sistema'

    @transaction.atomic
    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('\n=== CRIANDO DADOS DE TESTE ===\n'))

        sexo_m = Sexo.objects.get(nome='Masculino')
        sexo_f = Sexo.objects.get(nome='Feminino')
        fototipo_branca = Fototipo.objects.get(nome='Branca')
        fototipo_preta = Fototipo.objects.get(nome='Preta')
        fototipo_parda = Fototipo.objects.get(nome='Parda')
        status_inscricoes_abertas = Status.objects.get(nome='Inscrições Abertas')
        status_inscricao_aprovada = StatusInscricao.objects.get(nome='Aprovada')

        self.stdout.write('1. Criando Interessados...')
        
        interessados = []
        interessados.append(Interessado.objects.get_or_create(
            cpf='12345678901',
            defaults={'nome': 'Maria Silva Santos', 'data_nascimento': date(2005, 3, 15), 'sexo': sexo_f, 'fototipo': fototipo_parda, 'email': 'maria.silva@email.com', 'telefone': '92987654321', 'celular': '92987654321', 'endereco_residencial': 'Rua das Flores', 'num_endereco': '123', 'bairro': 'Centro', 'cidade_residencia': 'Manaus', 'uf_residencia': 'AM', 'programa_social': True, 'num_nis': '12345678901', 'senha': 'pbkdf2_sha256$260000$test$hash'}
        )[0])
        
        interessados.append(Interessado.objects.get_or_create(
            cpf='23456789012',
            defaults={'nome': 'João Pedro Oliveira', 'data_nascimento': date(2003, 7, 20), 'sexo': sexo_m, 'fototipo': fototipo_preta, 'email': 'joao.pedro@email.com', 'telefone': '92987651234', 'celular': '92987651234', 'endereco_residencial': 'Avenida Brasil', 'num_endereco': '456', 'bairro': 'Adrianópolis', 'cidade_residencia': 'Manaus', 'uf_residencia': 'AM', 'necessidades_especiais': True, 'pcd_fisica': True, 'senha': 'pbkdf2_sha256$260000$test$hash'}
        )[0])
        
        interessados.append(Interessado.objects.get_or_create(
            cpf='34567890123',
            defaults={'nome': 'Ana Paula Costa', 'data_nascimento': date(1998, 11, 5), 'sexo': sexo_f, 'fototipo': fototipo_branca, 'email': 'ana.costa@email.com', 'telefone': '92987655678', 'celular': '92987655678', 'endereco_residencial': 'Rua João Valério', 'num_endereco': '789', 'bairro': 'Nossa Senhora das Graças', 'cidade_residencia': 'Manaus', 'uf_residencia': 'AM', 'programa_social': True, 'num_nis': '34567890123', 'senha': 'pbkdf2_sha256$260000$test$hash'}
        )[0])
        
        for interessado in interessados:
            self.stdout.write(f'   ✅ {interessado.nome}')

        self.stdout.write('\n2. Criando Evento...')
        evento, created = Evento.objects.get_or_create(
            nome='Curso de Manutenção de Computadores e Redes',
            defaults={
                'descricao': 'Curso prático de montagem e manutenção de computadores.',
                'status': status_inscricoes_abertas,
                'total_vagas': 30,
                'data_inicio_inscricao': timezone.make_aware(timezone.datetime(2025, 1, 15, 8, 0)),
                'data_fim_inscricao': timezone.make_aware(timezone.datetime(2025, 2, 15, 23, 59)),
                'data_inicio_evento': date(2025, 3, 1),
                'data_fim_evento': date(2025, 5, 30),
            }
        )
        self.stdout.write(f'   ✅ {evento.nome}')

        self.stdout.write('\n3. Criando Turmas...')
        turma_a, _ = Turma.objects.get_or_create(
            evento=evento,
            nome='Turma A',
            defaults={'turno': 'MATUTINO', 'capacidade': 15, 'local': 'Laboratório 1', 'data_inicio': date(2025, 3, 1), 'data_fim': date(2025, 5, 30)}
        )
        self.stdout.write(f'   ✅ {turma_a.nome}')

        self.stdout.write('\n4. Criando Inscrições...')
        for interessado in interessados:
            Inscricao.objects.get_or_create(
                evento=evento,
                interessado=interessado,
                defaults={'status': status_inscricao_aprovada, 'data_inscricao': timezone.now()}
            )
            self.stdout.write(f'   ✅ {interessado.nome}')

        self.stdout.write(self.style.SUCCESS('\n=== CONCLUÍDO! ===\n'))
        self.stdout.write(f'  • Interessados: {len(interessados)}')
        self.stdout.write(f'  • Eventos: 1')
        self.stdout.write(f'  • Turmas: 1')
        self.stdout.write(f'  • Inscrições: {len(interessados)}\n')

        