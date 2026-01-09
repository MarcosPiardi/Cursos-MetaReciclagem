"""
Arquivo: gerar_dados_teste.py
Caminho: apps/selecao/management/commands/gerar_dados_teste.py
Alteração: Melhorado com nomes reais, mais campos preenchidos, garantia de PCD e programa social
Data: 11/12/2025
"""

from django.core.management.base import BaseCommand
from django.utils import timezone
from datetime import date, timedelta
import random

from apps.eventos.models import Evento, Status, Criterio, EventoCriterio
from apps.interessados.models import Interessado, Fototipo, Sexo
from apps.selecao.models import Inscricao, StatusInscricao


class Command(BaseCommand):
    help = 'Gera massa de dados de teste para o sistema'
    
    def add_arguments(self, parser):
        parser.add_argument(
            '--eventos',
            type=int,
            default=5,
            help='Quantidade de eventos a criar (padrão: 5)'
        )
        parser.add_argument(
            '--interessados',
            type=int,
            default=50,
            help='Quantidade de interessados a criar (padrão: 50)'
        )
        parser.add_argument(
            '--inscricoes-por-evento',
            type=int,
            default=30,
            help='Quantidade de inscrições por evento (padrão: 30)'
        )
    
    def handle(self, *args, **options):
        self.stdout.write(self.style.WARNING('🚀 Iniciando geração de dados de teste...'))
        
        qtd_eventos = options['eventos']
        qtd_interessados = options['interessados']
        qtd_inscricoes = options['inscricoes_por_evento']
        
        # Busca ou cria dados base
        self.stdout.write('📋 Verificando dados base...')
        status_evento = self._garantir_status_evento()
        status_inscricao = self._garantir_status_inscricao()
        fototipos = self._garantir_fototipos()
        escolaridades = self._obter_escolaridades()
        sexos = self._garantir_sexos()
        criterios = self._garantir_criterios()
        
        # Cria eventos
        self.stdout.write(f'🎓 Criando {qtd_eventos} eventos...')
        eventos = self._criar_eventos(qtd_eventos, status_evento, criterios)
        
        # Cria interessados
        self.stdout.write(f'👥 Criando {qtd_interessados} interessados...')
        interessados = self._criar_interessados(
            qtd_interessados,
            fototipos,
            escolaridades,
            sexos
        )
        
        # Cria inscrições
        self.stdout.write(f'📝 Criando inscrições ({qtd_inscricoes} por evento)...')
        total_inscricoes = self._criar_inscricoes(
            eventos,
            interessados,
            status_inscricao,
            qtd_inscricoes
        )
        
        # Resumo
        total_pcd = sum(1 for i in interessados if i.tem_deficiencia)
        total_programa_social = sum(1 for i in interessados if i.programa_social)
        
        self.stdout.write(self.style.SUCCESS('✅ DADOS CRIADOS COM SUCESSO!'))
        self.stdout.write(self.style.SUCCESS(f'   📊 {len(eventos)} eventos'))
        self.stdout.write(self.style.SUCCESS(f'   👥 {len(interessados)} interessados'))
        self.stdout.write(self.style.SUCCESS(f'   ♿ {total_pcd} com PCD'))
        self.stdout.write(self.style.SUCCESS(f'   🏠 {total_programa_social} em programa social'))
        self.stdout.write(self.style.SUCCESS(f'   📝 {total_inscricoes} inscrições'))
    
    def _garantir_status_evento(self):
        """Garante que status de evento existem"""
        status, _ = Status.objects.get_or_create(
            nome='Inscrições Abertas',
            defaults={'cor': '#28a745', 'ordem': 2}
        )
        return status
    
    def _garantir_status_inscricao(self):
        """Garante que status Pendente existe"""
        status, _ = StatusInscricao.objects.get_or_create(
            nome='Pendente',
            defaults={'codigo': 1}
        )
        return status
    
    def _garantir_fototipos(self):
        """Garante que fototipos existem"""
        nomes = ['Branco', 'Preto', 'Pardo', 'Amarelo', 'Indígena']
        fototipos = []
        for nome in nomes:
            fototipo, _ = Fototipo.objects.get_or_create(nome=nome)
            fototipos.append(fototipo)
        return fototipos
    
    def _obter_escolaridades(self):
        """Retorna lista de escolaridades (choices do modelo)"""
        return [
            'FUNDAMENTAL_INCOMPLETO',
            'FUNDAMENTAL_COMPLETO',
            'MEDIO_INCOMPLETO',
            'MEDIO_COMPLETO',
            'SUPERIOR_INCOMPLETO',
            'SUPERIOR_COMPLETO',
            'POS_GRADUACAO'
        ]
    
    def _garantir_sexos(self):
        """Garante que sexos existem"""
        nomes = ['Masculino', 'Feminino']
        sexos = []
        for nome in nomes:
            sexo, _ = Sexo.objects.get_or_create(nome=nome)
            sexos.append(sexo)
        return sexos
    
    def _garantir_criterios(self):
        """Garante que critérios básicos existem"""
        criterios_base = [
            {'codigo': 'PCD', 'nome': 'Pessoa com Deficiência', 'pontos': 10, 'categoria': 'VULNERABILIDADE'},
            {'codigo': 'JOVEM', 'nome': 'Jovem 16-24 anos', 'pontos': 5, 'categoria': 'FAIXA_ETARIA'},
            {'codigo': 'COTA_RACIAL', 'nome': 'Cota Racial', 'pontos': 5, 'categoria': 'COTA_RACIAL'},
        ]
        
        criterios = []
        for dados in criterios_base:
            criterio, _ = Criterio.objects.get_or_create(
                codigo=dados['codigo'],
                defaults={
                    'nome': dados['nome'],
                    'pontos': dados['pontos'],
                    'categoria': dados['categoria'],
                    'tipo_criterio': 'PONTUACAO'
                }
            )
            criterios.append(criterio)
        
        return criterios
    
    def _criar_eventos(self, quantidade, status, criterios):
        """Cria eventos de teste"""
        cursos = [
            'Informática Básica', 'Manutenção de Computadores', 'Excel Avançado',
            'Programação Python', 'Design Gráfico', 'Edição de Vídeo',
            'Marketing Digital', 'Redes de Computadores', 'Segurança da Informação',
            'Desenvolvimento Web', 'Banco de Dados', 'Inglês Instrumental'
        ]
        
        eventos = []
        hoje = timezone.now()
        
        for i in range(quantidade):
            nome_curso = random.choice(cursos)
            
            evento = Evento.objects.create(
                nome=f'{nome_curso} - Turma {i+1}',
                descricao=f'Curso de {nome_curso} para capacitação profissional',
                status=status,
                total_vagas=random.randint(20, 40),
                data_inicio_inscricao=hoje - timedelta(days=30),
                data_fim_inscricao=hoje + timedelta(days=30),
                data_inicio_evento=hoje.date() + timedelta(days=60),
                data_fim_evento=hoje.date() + timedelta(days=150)
            )
            
            # Associa critérios ao evento
            for idx, criterio in enumerate(criterios, start=1):
                EventoCriterio.objects.create(
                    evento=evento,
                    criterio=criterio,
                    prioridade=idx,
                    ativo=True
                )
            
            eventos.append(evento)
        
        return eventos
    
    def _criar_interessados(self, quantidade, fototipos, escolaridades, sexos):
        """Cria interessados de teste com dados completos"""
        
        # Nomes completos realistas
        nomes_masc = [
            'João Pedro Silva', 'José Carlos Santos', 'Carlos Eduardo Oliveira', 'Paulo Roberto Souza',
            'Pedro Henrique Alves', 'Lucas Gabriel Costa', 'Fernando José Lima', 'Rafael Augusto Pereira',
            'Gabriel Luiz Rodrigues', 'Bruno César Fernandes', 'Matheus Vinícius Carvalho',
            'Thiago Alexandre Martins', 'Felipe Henrique Ribeiro', 'André Luiz Gomes', 'Leonardo Antônio Dias',
            'Rodrigo Fernando Silva', 'Marcelo José Santos', 'Ricardo Paulo Oliveira', 'Diego Lucas Souza',
            'Gustavo Henrique Alves'
        ]
        
        nomes_fem = [
            'Maria Eduarda Silva', 'Ana Paula Santos', 'Paula Cristina Oliveira', 'Juliana Aparecida Souza',
            'Carla Fernanda Alves', 'Fernanda Cristina Costa', 'Patrícia Regina Lima', 'Aline Maria Pereira',
            'Camila Aparecida Rodrigues', 'Beatriz Helena Fernandes', 'Amanda Cristina Carvalho',
            'Mariana Vitória Martins', 'Larissa Fernanda Ribeiro', 'Débora Cristina Gomes', 'Renata Maria Dias',
            'Vanessa Aparecida Silva', 'Tatiane Cristina Santos', 'Simone Regina Oliveira', 'Jéssica Maria Souza',
            'Cláudia Fernanda Alves'
        ]
        
        sobrenomes = ['Silva', 'Santos', 'Oliveira', 'Souza', 'Costa', 'Ferreira', 'Rodrigues', 
                     'Almeida', 'Nascimento', 'Lima', 'Araújo', 'Fernandes', 'Carvalho', 'Gomes',
                     'Martins', 'Rocha', 'Ribeiro', 'Alves', 'Pereira', 'Melo']
        
        ruas = ['Rua das Flores', 'Avenida Brasil', 'Rua São Paulo', 'Travessa do Comércio',
                'Rua Santa Maria', 'Avenida Central', 'Rua do Progresso', 'Rua da Paz']
        
        bairros = ['Centro', 'Jardim Primavera', 'Vila Nova', 'Parque Industrial',
                   'Bela Vista', 'Santa Cruz', 'São José', 'Boa Esperança']
        
        cidades = ['São Paulo', 'Rio de Janeiro', 'Belo Horizonte', 'Salvador',
                   'Brasília', 'Curitiba', 'Porto Alegre', 'Recife']
        
        ufs = ['SP', 'RJ', 'MG', 'BA', 'DF', 'PR', 'RS', 'PE']
        
        interessados = []
        
        # GARANTE que pelo menos 30% terão PCD e 40% programa social
        qtd_pcd = int(quantidade * 0.3)
        qtd_programa_social = int(quantidade * 0.4)
        
        indices_pcd = set(random.sample(range(quantidade), qtd_pcd))
        indices_programa_social = set(random.sample(range(quantidade), qtd_programa_social))
        
        for i in range(quantidade):
            # Escolhe sexo e nome correspondente
            sexo = random.choice(sexos)
            if sexo.nome == 'Masculino':
                nome_completo = random.choice(nomes_masc)
            else:
                nome_completo = random.choice(nomes_fem)
            
            # Adiciona sobrenome extra para mais variedade
            if random.random() < 0.3:
                nome_completo += ' ' + random.choice(sobrenomes)
            
            # Gera CPF fictício único
            cpf = ''.join([str(random.randint(0, 9)) for _ in range(11)])
            while Interessado.objects.filter(cpf=cpf).exists():
                cpf = ''.join([str(random.randint(0, 9)) for _ in range(11)])
            
            # Data de nascimento (18 a 60 anos)
            idade = random.randint(18, 60)
            data_nascimento = date.today() - timedelta(days=idade*365 + random.randint(0, 364))
            
            # GARANTE PCD para alguns
            tem_pcd = i in indices_pcd
            
            # GARANTE Programa Social para alguns
            tem_programa_social = i in indices_programa_social
            num_nis = ''.join([str(random.randint(0, 9)) for _ in range(11)]) if tem_programa_social else ''
            
            # Escolhe cidade/UF
            idx_cidade = random.randint(0, len(cidades)-1)
            cidade = cidades[idx_cidade]
            uf = ufs[idx_cidade]
            
            # Telefones
            celular = f'{random.randint(11, 99)}9{random.randint(10000000, 99999999)}'
            telefone = f'{random.randint(11, 99)}{random.randint(20000000, 39999999)}'
            
            interessado = Interessado.objects.create(
                nome=nome_completo,
                cpf=cpf,
                rg=f'{random.randint(1000000, 9999999)}{random.choice(["X", "0", "1", "2"])}',
                data_nascimento=data_nascimento,
                sexo=sexo,
                fototipo=random.choice(fototipos),
                escolaridade=random.choice(escolaridades),
                
                # Endereço completo
                endereco_residencial=random.choice(ruas),
                num_endereco=str(random.randint(1, 9999)),
                bairro=random.choice(bairros),
                complemento=random.choice(['', 'Apto 101', 'Casa', 'Bloco A']) if random.random() < 0.3 else '',
                cidade_residencia=cidade,
                uf_residencia=uf,
                cidade_nascimento=random.choice(cidades),
                uf_nascimento=random.choice(ufs),
                nacionalidade='Brasileira',
                
                # Contatos
                celular=celular,
                telefone=telefone if random.random() < 0.5 else '',
                email=f'{nome_completo.lower().replace(" ", ".")}@email.com',
                
                # PCD - GARANTIDO para alguns
                necessidades_especiais=tem_pcd,
                pcd_fisica=tem_pcd and random.random() < 0.6,
                pcd_visual=tem_pcd and random.random() < 0.3,
                pcd_auditiva=tem_pcd and random.random() < 0.2,
                pcd_intelectual=tem_pcd and random.random() < 0.1,
                
                # Programa Social - GARANTIDO para alguns
                programa_social=tem_programa_social,
                num_nis=num_nis,
                
                # Campo obrigatório
                senha=''
            )
            
            interessados.append(interessado)
        
        return interessados
    
    def _criar_inscricoes(self, eventos, interessados, status, qtd_por_evento):
        """Cria inscrições de teste"""
        total = 0
        
        for evento in eventos:
            # Seleciona interessados aleatórios para este evento
            selecionados = random.sample(
                interessados,
                min(qtd_por_evento, len(interessados))
            )
            
            for interessado in selecionados:
                # Evita inscrição duplicada
                if not Inscricao.objects.filter(evento=evento, interessado=interessado).exists():
                    Inscricao.objects.create(
                        evento=evento,
                        interessado=interessado,
                        status=status,
                        data_inscricao=timezone.now() - timedelta(days=random.randint(1, 30))
                    )
                    total += 1
        
        return total
    