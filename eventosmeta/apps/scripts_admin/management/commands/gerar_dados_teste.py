"""
Arquivo: gerar_dados_teste.py
Caminho: apps/selecao/management/commands/gerar_dados_teste.py
Alteração: Corrigido geração de nomes únicos e adicionado senha padrão '123'
Data: 12/01/2026
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
        total_pcd = sum(1 for i in interessados if i.necessidades_especiais)
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
    
    def _gerar_nome_unico(self, sexo, nomes_usados):
        """Gera um nome completo único combinando nomes e sobrenomes aleatoriamente"""
        
        # Listas expandidas de nomes
        primeiros_nomes_masc = [
            'João', 'José', 'Carlos', 'Paulo', 'Pedro', 'Lucas', 'Fernando', 'Rafael',
            'Gabriel', 'Bruno', 'Matheus', 'Thiago', 'Felipe', 'André', 'Leonardo',
            'Rodrigo', 'Marcelo', 'Ricardo', 'Diego', 'Gustavo', 'Daniel', 'Eduardo',
            'Fábio', 'Vinícius', 'Alexandre', 'Leandro', 'Renato', 'Sérgio', 'Marcos',
            'Antônio', 'Júlio', 'César', 'Henrique', 'Márcio', 'Roberto', 'Jorge'
        ]
        
        primeiros_nomes_fem = [
            'Maria', 'Ana', 'Paula', 'Juliana', 'Carla', 'Fernanda', 'Patrícia', 'Aline',
            'Camila', 'Beatriz', 'Amanda', 'Mariana', 'Larissa', 'Débora', 'Renata',
            'Vanessa', 'Tatiane', 'Simone', 'Jéssica', 'Cláudia', 'Sandra', 'Cristina',
            'Adriana', 'Priscila', 'Luciana', 'Daniela', 'Carolina', 'Bianca', 'Letícia',
            'Viviane', 'Elaine', 'Mônica', 'Andreia', 'Raquel', 'Silvia', 'Rosana'
        ]
        
        nomes_meio = [
            'da Silva', 'dos Santos', 'de Oliveira', 'de Souza', 'da Costa', 'Ferreira',
            'Rodrigues', 'de Almeida', 'do Nascimento', 'Lima', 'de Araújo', 'Fernandes',
            'de Carvalho', 'Gomes', 'Martins', 'Rocha', 'Ribeiro', 'Alves', 'Pereira',
            'de Melo', 'Barbosa', 'Cardoso', 'Teixeira', 'Reis', 'Correia', 'da Silva',
            'Moreira', 'Pinto', 'Castro', 'Ramos', 'Monteiro', 'Nunes', 'Mendes'
        ]
        
        sobrenomes_finais = [
            'Junior', 'Neto', 'Filho', 'Silva', 'Santos', 'Oliveira', 'Souza', 'Costa',
            'Lima', 'Alves', 'Pereira', 'Rocha', 'Dias', 'Moura', 'Cunha', 'Pires',
            'Farias', 'Lopes', 'Soares', 'Duarte', 'Coelho', 'Freitas', 'Barros'
        ]
        
        # Escolhe lista de nomes baseado no sexo
        if sexo.nome == 'Masculino':
            primeiros_nomes = primeiros_nomes_masc
        else:
            primeiros_nomes = primeiros_nomes_fem
        
        # Tenta gerar nome único (máximo 100 tentativas)
        for _ in range(100):
            # Gera combinação aleatória
            primeiro = random.choice(primeiros_nomes)
            meio = random.choice(nomes_meio)
            final = random.choice(sobrenomes_finais) if random.random() < 0.5 else ''
            
            # Monta nome completo
            if final:
                nome_completo = f'{primeiro} {meio} {final}'
            else:
                nome_completo = f'{primeiro} {meio}'
            
            # Verifica se é único
            if nome_completo not in nomes_usados:
                # Verifica também no banco de dados
                if not Interessado.objects.filter(nome=nome_completo).exists():
                    nomes_usados.add(nome_completo)
                    return nome_completo
        
        # Se não conseguiu, adiciona número ao final
        base = f'{random.choice(primeiros_nomes)} {random.choice(nomes_meio)}'
        contador = 1
        while True:
            nome_completo = f'{base} {contador}'
            if nome_completo not in nomes_usados and not Interessado.objects.filter(nome=nome_completo).exists():
                nomes_usados.add(nome_completo)
                return nome_completo
            contador += 1
    
    def _criar_interessados(self, quantidade, fototipos, escolaridades, sexos):
        """Cria interessados de teste com dados completos e nomes únicos"""
        
        ruas = ['Rua das Flores', 'Avenida Brasil', 'Rua São Paulo', 'Travessa do Comércio',
                'Rua Santa Maria', 'Avenida Central', 'Rua do Progresso', 'Rua da Paz',
                'Rua 7 de Setembro', 'Avenida Paulista', 'Rua XV de Novembro', 'Rua Dom Pedro']
        
        bairros = ['Centro', 'Jardim Primavera', 'Vila Nova', 'Parque Industrial',
                   'Bela Vista', 'Santa Cruz', 'São José', 'Boa Esperança', 'Jardim das Rosas',
                   'Vila Mariana', 'Cidade Nova', 'Alto da Glória']
        
        cidades = ['São Paulo', 'Rio de Janeiro', 'Belo Horizonte', 'Salvador',
                   'Brasília', 'Curitiba', 'Porto Alegre', 'Recife', 'Fortaleza', 'Manaus']
        
        ufs = ['SP', 'RJ', 'MG', 'BA', 'DF', 'PR', 'RS', 'PE', 'CE', 'AM']
        
        interessados = []
        nomes_usados = set()
        
        # GARANTE que pelo menos 30% terão PCD e 40% programa social
        qtd_pcd = int(quantidade * 0.3)
        qtd_programa_social = int(quantidade * 0.4)
        
        indices_pcd = set(random.sample(range(quantidade), qtd_pcd))
        indices_programa_social = set(random.sample(range(quantidade), qtd_programa_social))
        
        for i in range(quantidade):
            # Escolhe sexo
            sexo = random.choice(sexos)
            
            # Gera nome único
            nome_completo = self._gerar_nome_unico(sexo, nomes_usados)
            
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
            
            # Email único baseado no nome
            email_base = nome_completo.lower().replace(' ', '.').replace('á', 'a').replace('é', 'e').replace('í', 'i').replace('ó', 'o').replace('ú', 'u').replace('ã', 'a').replace('õ', 'o').replace('ç', 'c')
            email = f'{email_base}@email.com'
            contador_email = 1
            while Interessado.objects.filter(email=email).exists():
                email = f'{email_base}{contador_email}@email.com'
                contador_email += 1
            
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
                complemento=random.choice(['', 'Apto 101', 'Casa', 'Bloco A', 'Fundos']) if random.random() < 0.3 else '',
                cidade_residencia=cidade,
                uf_residencia=uf,
                cidade_nascimento=random.choice(cidades),
                uf_nascimento=random.choice(ufs),
                nacionalidade='Brasileira',
                
                # Contatos
                celular=celular,
                telefone=telefone if random.random() < 0.5 else '',
                email=email,
                
                # PCD - GARANTIDO para alguns
                necessidades_especiais=tem_pcd,
                pcd_fisica=tem_pcd and random.random() < 0.6,
                pcd_visual=tem_pcd and random.random() < 0.3,
                pcd_auditiva=tem_pcd and random.random() < 0.2,
                pcd_intelectual=tem_pcd and random.random() < 0.1,
                
                # Programa Social - GARANTIDO para alguns
                programa_social=tem_programa_social,
                num_nis=num_nis,
                
                # Senha padrão: 123
                senha='123'
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
    
    