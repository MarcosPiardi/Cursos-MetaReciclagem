"""
Foi o primeiro que usei para popular dados.
Não usar mais, tem um melhor: gerar_dados_teste.py
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
        fototipo_amarela = Fototipo.objects.get(nome='Amarela')
        fototipo_indigena = Fototipo.objects.get(nome='Indígena')
        status_inscricoes_abertas = Status.objects.get(nome='Inscrições Abertas')
        status_inscricao_aprovada = StatusInscricao.objects.get(nome='Aprovada')

        self.stdout.write('1. Criando 10 Interessados variados...')
        
        interessados_data = [
            # 1. Jovem, Parda, NIS, Ensino Médio Completo
            {'cpf': '12345678901', 'rg': '1234567', 'nome': 'Maria Silva Santos', 
             'data_nascimento': date(2005, 3, 15), 'sexo': sexo_f, 'fototipo': fototipo_parda,
             'escolaridade': 'MEDIO_COMPLETO', 'email': 'maria.silva@email.com', 
             'telefone': '92987654321', 'celular': '92987654321', 'endereco_residencial': 'Rua das Flores',
             'num_endereco': '123', 'bairro': 'Centro', 'cidade_residencia': 'Manaus', 'uf_residencia': 'AM',
             'programa_social': True, 'num_nis': '12345678901', 'senha': 'pbkdf2_sha256$260000$test$hash'},
            
            # 2. Jovem, Preto, PCD Física, Ensino Fundamental Completo
            {'cpf': '23456789012', 'rg': '2345678', 'nome': 'João Pedro Oliveira', 
             'data_nascimento': date(2003, 7, 20), 'sexo': sexo_m, 'fototipo': fototipo_preta,
             'escolaridade': 'FUNDAMENTAL_COMPLETO', 'email': 'joao.pedro@email.com',
             'telefone': '92987651234', 'celular': '92987651234', 'endereco_residencial': 'Avenida Brasil',
             'num_endereco': '456', 'bairro': 'Adrianópolis', 'cidade_residencia': 'Manaus', 'uf_residencia': 'AM',
             'necessidades_especiais': True, 'pcd_fisica': True, 'senha': 'pbkdf2_sha256$260000$test$hash'},
            
            # 3. Adulta, Branca, NIS, Ensino Superior Completo
            {'cpf': '34567890123', 'rg': '3456789', 'nome': 'Ana Paula Costa', 
             'data_nascimento': date(1998, 11, 5), 'sexo': sexo_f, 'fototipo': fototipo_branca,
             'escolaridade': 'SUPERIOR_COMPLETO', 'email': 'ana.costa@email.com',
             'telefone': '92987655678', 'celular': '92987655678', 'endereco_residencial': 'Rua João Valério',
             'num_endereco': '789', 'bairro': 'Nossa Senhora das Graças', 'cidade_residencia': 'Manaus', 'uf_residencia': 'AM',
             'programa_social': True, 'num_nis': '34567890123', 'senha': 'pbkdf2_sha256$260000$test$hash'},
            
            # 4. Idoso, Pardo, sem benefícios, Ensino Médio Completo
            {'cpf': '45678901234', 'rg': '4567890', 'nome': 'Carlos Eduardo Ferreira', 
             'data_nascimento': date(1970, 2, 10), 'sexo': sexo_m, 'fototipo': fototipo_parda,
             'escolaridade': 'MEDIO_COMPLETO', 'email': 'carlos.ferreira@email.com',
             'telefone': '92987659012', 'celular': '92987659012', 'endereco_residencial': 'Avenida Torquato Tapajós',
             'num_endereco': '321', 'bairro': 'Flores', 'cidade_residencia': 'Manaus', 'uf_residencia': 'AM',
             'senha': 'pbkdf2_sha256$260000$test$hash'},
            
            # 5. Jovem, Preta, NIS, Ensino Médio Incompleto
            {'cpf': '56789012345', 'rg': '5678901', 'nome': 'Juliana Souza Ramos', 
             'data_nascimento': date(2006, 9, 25), 'sexo': sexo_f, 'fototipo': fototipo_preta,
             'escolaridade': 'MEDIO_INCOMPLETO', 'email': 'juliana.ramos@email.com',
             'telefone': '92987653456', 'celular': '92987653456', 'endereco_residencial': 'Rua Rio Negro',
             'num_endereco': '654', 'bairro': 'Parque 10', 'cidade_residencia': 'Manaus', 'uf_residencia': 'AM',
             'programa_social': True, 'num_nis': '56789012345', 'senha': 'pbkdf2_sha256$260000$test$hash'},
            
            # 6. Jovem, Pardo, PCD Auditiva, NIS, Ensino Fundamental Completo
            {'cpf': '67890123456', 'rg': '6789012', 'nome': 'Rafael Almeida Dias', 
             'data_nascimento': date(2004, 4, 12), 'sexo': sexo_m, 'fototipo': fototipo_parda,
             'escolaridade': 'FUNDAMENTAL_COMPLETO', 'email': 'rafael.dias@email.com',
             'telefone': '92987657890', 'celular': '92987657890', 'endereco_residencial': 'Avenida Constantino Nery',
             'num_endereco': '987', 'bairro': 'Chapada', 'cidade_residencia': 'Manaus', 'uf_residencia': 'AM',
             'necessidades_especiais': True, 'pcd_auditiva': True, 'programa_social': True, 'num_nis': '67890123456',
             'senha': 'pbkdf2_sha256$260000$test$hash'},
            
            # 7. Adulta, Branca, sem benefícios, Ensino Superior Incompleto
            {'cpf': '78901234567', 'rg': '7890123', 'nome': 'Fernanda Lima Pereira', 
             'data_nascimento': date(2000, 12, 30), 'sexo': sexo_f, 'fototipo': fototipo_branca,
             'escolaridade': 'SUPERIOR_INCOMPLETO', 'email': 'fernanda.pereira@email.com',
             'telefone': '92987652345', 'celular': '92987652345', 'endereco_residencial': 'Rua Acre',
             'num_endereco': '111', 'bairro': 'Cidade Nova', 'cidade_residencia': 'Manaus', 'uf_residencia': 'AM',
             'senha': 'pbkdf2_sha256$260000$test$hash'},
            
            # 8. Jovem, Preto, NIS, Ensino Médio Completo
            {'cpf': '89012345678', 'rg': '8901234', 'nome': 'Pedro Henrique Barbosa', 
             'data_nascimento': date(2005, 6, 18), 'sexo': sexo_m, 'fototipo': fototipo_preta,
             'escolaridade': 'MEDIO_COMPLETO', 'email': 'pedro.barbosa@email.com',
             'telefone': '92987656789', 'celular': '92987656789', 'endereco_residencial': 'Avenida Max Teixeira',
             'num_endereco': '222', 'bairro': 'Cidade Nova', 'cidade_residencia': 'Manaus', 'uf_residencia': 'AM',
             'programa_social': True, 'num_nis': '89012345678', 'senha': 'pbkdf2_sha256$260000$test$hash'},
            
            # 9. Idosa, Parda, NIS, Ensino Fundamental Incompleto
            {'cpf': '90123456789', 'rg': '9012345', 'nome': 'Camila Rodrigues Martins', 
             'data_nascimento': date(1968, 8, 8), 'sexo': sexo_f, 'fototipo': fototipo_parda,
             'escolaridade': 'FUNDAMENTAL_INCOMPLETO', 'email': 'camila.martins@email.com',
             'telefone': '92987658901', 'celular': '92987658901', 'endereco_residencial': 'Rua Barreirinha',
             'num_endereco': '333', 'bairro': 'Aleixo', 'cidade_residencia': 'Manaus', 'uf_residencia': 'AM',
             'programa_social': True, 'num_nis': '90123456789', 'senha': 'pbkdf2_sha256$260000$test$hash'},
            
            # 10. Jovem, Amarela, PCD Visual, Ensino Médio Completo
            {'cpf': '01234567890', 'rg': '0123456', 'nome': 'Lucas Gabriel Teixeira', 
             'data_nascimento': date(2002, 1, 22), 'sexo': sexo_m, 'fototipo': fototipo_amarela,
             'escolaridade': 'MEDIO_COMPLETO', 'email': 'lucas.teixeira@email.com',
             'telefone': '92987650123', 'celular': '92987650123', 'endereco_residencial': 'Avenida Autaz Mirim',
             'num_endereco': '444', 'bairro': 'São José', 'cidade_residencia': 'Manaus', 'uf_residencia': 'AM',
             'necessidades_especiais': True, 'pcd_visual': True, 'senha': 'pbkdf2_sha256$260000$test$hash'},
        ]
        
        interessados = []
        for data in interessados_data:
            interessado, created = Interessado.objects.get_or_create(
                cpf=data['cpf'],
                defaults=data
            )
            interessados.append(interessado)
            if created:
                self.stdout.write(f'   ✅ {interessado.nome}')
            else:
                self.stdout.write(f'   ⏭️  {interessado.nome}')

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
        if created:
            self.stdout.write(f'   ✅ {evento.nome}')
        else:
            self.stdout.write(f'   ⏭️  {evento.nome}')

        self.stdout.write('\n3. Criando Turmas...')
        turma_a, _ = Turma.objects.get_or_create(
            evento=evento, nome='Turma A',
            defaults={'turno': 'MATUTINO', 'capacidade': 15, 'local': 'Laboratório 1',
                     'data_inicio': date(2025, 3, 1), 'data_fim': date(2025, 5, 30)}
        )
        turma_b, _ = Turma.objects.get_or_create(
            evento=evento, nome='Turma B',
            defaults={'turno': 'VESPERTINO', 'capacidade': 15, 'local': 'Laboratório 2',
                     'data_inicio': date(2025, 3, 1), 'data_fim': date(2025, 5, 30)}
        )
        self.stdout.write(f'   ✅ {turma_a.nome}')
        self.stdout.write(f'   ✅ {turma_b.nome}')

        self.stdout.write('\n4. Criando Inscrições...')
        for i, interessado in enumerate(interessados):
            inscricao, created = Inscricao.objects.get_or_create(
                evento=evento, interessado=interessado,
                defaults={'status': status_inscricao_aprovada,
                         'data_inscricao': timezone.now() - timedelta(days=(len(interessados)-i))}
            )
            if created:
                self.stdout.write(f'   ✅ {interessado.nome}')
            else:
                self.stdout.write(f'   ⏭️  {interessado.nome}')

        self.stdout.write(self.style.SUCCESS('\n=== CONCLUÍDO! ===\n'))
        self.stdout.write(f'  • Interessados: {len(interessados)}')
        self.stdout.write(f'  • Eventos: 1')
        self.stdout.write(f'  • Turmas: 2')
        self.stdout.write(f'  • Inscrições: {len(interessados)}\n')

        