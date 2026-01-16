"""
Arquivo: classificar_evento.py
Caminho: apps/selecao/management/commands/classificar_evento.py
Alteração: Corrigido fototipo.upper() para fototipo.nome e tipo_deficiencia
Data: 10/12/2025
"""

"""
Comando para classificar inscrições de um evento
Modelo Simplificado com Pontuação Fixa
"""
from django.core.management.base import BaseCommand
from django.db import transaction
from datetime import date
from apps.eventos.models import Evento, EventoCriterio
from apps.selecao.models import Inscricao, Classificacao, InscricaoCriterioAtendido


class Command(BaseCommand):
    help = 'Classifica as inscrições de um evento baseado em critérios fixos'
    
    def add_arguments(self, parser):
        parser.add_argument(
            '--evento_id',
            type=int,
            required=True,
            help='ID do evento a ser classificado'
        )
    
    def handle(self, *args, **options):
        evento_id = options['evento_id']
        
        try:
            evento = Evento.objects.get(pk=evento_id)
        except Evento.DoesNotExist:
            self.stdout.write(
                self.style.ERROR(f'❌ Evento com ID {evento_id} não encontrado!')
            )
            return
        
        self.stdout.write('='*70)
        self.stdout.write(self.style.SUCCESS(f'🎯 CLASSIFICANDO EVENTO: {evento.nome}'))
        self.stdout.write('='*70)
        
        # Buscar inscrições confirmadas
        inscricoes = Inscricao.objects.filter(
            evento=evento,
            status__nome__in=['CONFIRMADA', 'Confirmada', 'APROVADA', 'Aprovada']
        ).select_related('interessado')
        
        total = inscricoes.count()
        
        if total == 0:
            self.stdout.write(
                self.style.WARNING('⚠️  Nenhuma inscrição CONFIRMADA encontrada!')
            )
            return
        
        self.stdout.write(f'\n📊 Total de inscrições a classificar: {total}\n')
        
        # Buscar critérios ativos
        criterios_ativos = EventoCriterio.objects.filter(
            evento=evento,
            ativo=True
        ).select_related('criterio')
        
        if not criterios_ativos.exists():
            self.stdout.write(
                self.style.WARNING('⚠️  Nenhum critério ativo para este evento!')
            )
            return
        
        self.stdout.write('📋 Critérios ativos:')
        for ec in criterios_ativos:
            if ec.criterio.pontos is not None:
                self.stdout.write(f'   • {ec.criterio.nome} ({ec.criterio.pontos} pts)')
            else:
                self.stdout.write(f'   • {ec.criterio.nome} (Ordenação)')
        
        self.stdout.write('\n' + '-'*70)
        
        # Classificar cada inscrição
        classificados = 0
        
        for inscricao in inscricoes:
            try:
                with transaction.atomic():
                    resultado = self.classificar_inscricao(inscricao, criterios_ativos)
                    self.salvar_classificacao(inscricao, resultado)
                    classificados += 1
                    
                    self.stdout.write(
                        f'✅ {inscricao.interessado.nome}: {resultado["pontuacao"]} pontos'
                    )
            
            except Exception as e:
                self.stdout.write(
                    self.style.ERROR(f'❌ Erro ao classificar {inscricao.interessado.nome}: {str(e)}')
                )
        
        self.stdout.write('-'*70)
        
        # Atualizar posições
        self.stdout.write('\n🔢 Atualizando posições de classificação...')
        self.atualizar_posicoes(evento, criterios_ativos)
        
        self.stdout.write('\n' + '='*70)
        self.stdout.write(self.style.SUCCESS('✅ CLASSIFICAÇÃO CONCLUÍDA!'))
        self.stdout.write(f'   Inscrições classificadas: {classificados}/{total}')
        self.stdout.write('='*70)
    
    def classificar_inscricao(self, inscricao, criterios_ativos):
        """
        Calcula pontuação de uma inscrição
        """
        interessado = inscricao.interessado
        
        pontuacao_total = 0
        criterios_atendidos = []
        
        # Calcular idade
        hoje = date.today()
        idade = (
            hoje.year - interessado.data_nascimento.year -
            ((hoje.month, hoje.day) < (interessado.data_nascimento.month, interessado.data_nascimento.day))
        )
        
        # Verificar cada critério
        for evento_criterio in criterios_ativos:
            criterio = evento_criterio.criterio
            
            # Pular critérios de ORDENACAO (não somam pontos)
            if criterio.tipo_criterio == 'ORDENACAO':
                continue
            
            atendido = False
            observacao = ''
            
            # PCD
            if criterio.codigo == 'PCD':
                if interessado.tem_deficiencia:
                    atendido = True
                    observacao = 'PCD: Sim'
            
            # NIS (Cadastro Único)
            elif criterio.codigo == 'NIS':
                if interessado.num_nis:
                    atendido = True
                    observacao = f'NIS: {interessado.num_nis}'
            
            # JOVEM (16 a 24 anos)
            elif criterio.codigo == 'JOVEM':
                if 16 <= idade <= 24:
                    atendido = True
                    observacao = f'Idade: {idade} anos'
            
            # IDOSO (50+ anos)
            elif criterio.codigo == 'IDOSO':
                if idade >= 50:
                    atendido = True
                    observacao = f'Idade: {idade} anos'
            
            # COTA RACIAL
            elif criterio.codigo == 'COTA_RACIAL':
                racas_cotistas = ['Preta', 'Parda', 'Indígena', 'Preto', 'Pardo', 'Indigena']
                if interessado.fototipo and interessado.fototipo.nome in racas_cotistas:
                    atendido = True
                    observacao = f'Raça/Cor: {interessado.fototipo.nome}'
            
            # ESCOLARIDADE - Fundamental Incompleto
            elif criterio.codigo == 'ESC_FUND_INC':
                if interessado.escolaridade == 'FUNDAMENTAL_INCOMPLETO':
                    atendido = True
                    observacao = 'Escolaridade: Ens. Fundamental Incompleto'
            
            # ESCOLARIDADE - Fundamental Completo
            elif criterio.codigo == 'ESC_FUND_COMP':
                if interessado.escolaridade == 'FUNDAMENTAL_COMPLETO':
                    atendido = True
                    observacao = 'Escolaridade: Ens. Fundamental Completo'
            
            # ESCOLARIDADE - Médio Incompleto
            elif criterio.codigo == 'ESC_MEDIO_INC':
                if interessado.escolaridade == 'MEDIO_INCOMPLETO':
                    atendido = True
                    observacao = 'Escolaridade: Ens. Médio Incompleto'
            
            # ESCOLARIDADE - Médio Completo
            elif criterio.codigo == 'ESC_MEDIO_COMP':
                if interessado.escolaridade == 'MEDIO_COMPLETO':
                    atendido = True
                    observacao = 'Escolaridade: Ens. Médio Completo'
            
            # Se atendeu o critério, adiciona pontos
            if atendido:
                pontos = criterio.pontos or 0
                pontuacao_total += pontos
                criterios_atendidos.append({
                    'criterio': criterio,
                    'pontos': pontos,
                    'observacao': observacao
                })
        
        return {
            'pontuacao': pontuacao_total,
            'criterios_atendidos': criterios_atendidos,
            'idade': idade
        }
    
    def salvar_classificacao(self, inscricao, resultado):
        """
        Salva a classificação no banco
        """
        # Criar/atualizar classificação
        classificacao, created = Classificacao.objects.update_or_create(
            inscricao=inscricao,
            defaults={
                'pontuacao_total': resultado['pontuacao'],
                'processado_em': date.today()
            }
        )
        
        # Limpar critérios antigos
        InscricaoCriterioAtendido.objects.filter(inscricao=inscricao).delete()
        
        # Criar novos registros de critérios atendidos
        for crit in resultado['criterios_atendidos']:
            InscricaoCriterioAtendido.objects.create(
                inscricao=inscricao,
                criterio=crit['criterio'],
                pontos_atribuidos=crit['pontos'],
                observacao_validacao=crit['observacao'],
                validado=True
            )
        
        return classificacao
    
    def atualizar_posicoes(self, evento, criterios_ativos):
        """
        Atualiza as posições de classificação
        Critérios de desempate:
        1. Maior pontuação
        2. Idade (se critério etário ativo: JOVEM=crescente, IDOSO=decrescente)
        3. Data de inscrição (primeiro inscrito)
        """
        # Verificar se tem critério etário ativo
        tem_jovem = criterios_ativos.filter(criterio__codigo='JOVEM').exists()
        tem_idoso = criterios_ativos.filter(criterio__codigo='IDOSO').exists()
        
        # Buscar todas as classificações
        classificacoes = Classificacao.objects.filter(
            inscricao__evento=evento,
            inscricao__status__nome__in=['CONFIRMADA', 'Confirmada', 'APROVADA', 'Aprovada']
        ).select_related('inscricao', 'inscricao__interessado')
        
        # Calcular idade para cada classificação
        classificacoes_list = list(classificacoes)
        hoje = date.today()
        
        for c in classificacoes_list:
            dn = c.inscricao.interessado.data_nascimento
            c.idade_calc = (
                hoje.year - dn.year -
                ((hoje.month, hoje.day) < (dn.month, dn.day))
            )
        
        # Ordenar considerando critérios
        if tem_jovem:
            # Prioriza mais jovens no desempate
            classificacoes_list.sort(
                key=lambda x: (-x.pontuacao_total, x.idade_calc, x.inscricao.data_inscricao)
            )
        elif tem_idoso:
            # Prioriza mais velhos no desempate
            classificacoes_list.sort(
                key=lambda x: (-x.pontuacao_total, -x.idade_calc, x.inscricao.data_inscricao)
            )
        else:
            # Apenas pontuação e data
            classificacoes_list.sort(
                key=lambda x: (-x.pontuacao_total, x.inscricao.data_inscricao)
            )
        
        # Atualizar posições e flags
        total_vagas = evento.total_vagas
        
        for posicao, classificacao in enumerate(classificacoes_list, start=1):
            classificacao.posicao = posicao
            classificacao.classificado = (posicao <= total_vagas)
            classificacao.lista_espera = (posicao > total_vagas)
            classificacao.save(update_fields=['posicao', 'classificado', 'lista_espera'])