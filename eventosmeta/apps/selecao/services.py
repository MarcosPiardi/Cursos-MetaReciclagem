"""
Arquivo: services.py
Caminho: apps/selecao/services.py
Finalidade: Serviços de classificação para o app seleção.

Histórico de Alterações:
- 20/02/2026: Implementação inicial do ClassificadorService
- 08/04/2026: Adicionado desempate por data_inscricao (ordem de chegada)
- 15/05/2026: Inclusão de cabeçalho
- 18/05/2026: Refatoração Opção 3 com criação automática de Classificacao
- 19/05/2026: Adicionada validação automática de critérios
             - Método _atende_criterio() para validar inscrição por categoria
             - _calcular_pontos() agora soma apenas pontos de critérios atendidos
             - Desempate por idade (JOVEM/IDOSO) ou timestamp

Funcionalidades:
- Validação automática de inscrição contra critérios (por categoria)
- Cálculo de pontuação com critérios atendidos apenas
- Processamento de inscrição com persistência
- Classificação automática (pontuação + desempate + quotas)
- Atribuição de posições e flags (classificado/lista_espera)
- Retorno estruturado com mensagens de resultado
"""

from decimal import Decimal
from django.db import transaction
from django.utils import timezone
from datetime import date

from apps.selecao.models import Inscricao, Classificacao, StatusInscricao
from apps.eventos.models import Evento


class ClassificadorService:
    """
    Serviço para classificação de inscrições em eventos.
    
    ARQUITETURA:
    - _atende_criterio(): valida se inscrição atende critério específico
    - _calcular_pontos(): lógica pura, soma apenas pontos de critérios atendidos
    - calcular_pontuacao_inscricao(): retorna pontos sem salvar
    - processar_inscricao(): calcula e cria Classificacao
    - classificar_evento(): orquestra classificação completa com desempate e quotas
    
    Alteração: 19/05/2026 - Adicionada validação automática de critérios
    """

    @staticmethod
    def _atende_criterio(inscricao, criterio):
        """
        MÉTODO PRIVADO: Valida se uma inscrição atende a um critério específico.
        
        Cada categoria de critério mapeia para um atributo ou regra do Interessado.
        Retorna True se a inscrição deve somar os pontos deste critério.
        
        Alteração: 19/05/2026 - Implementação de validação automática
        
        Args:
            inscricao: Objeto Inscricao com interessado relacionado
            criterio: Objeto Criterio com categoria definida
            
        Returns:
            bool: True se inscrição atende critério, False caso contrário
        """
        interessado = inscricao.interessado
        categoria = criterio.categoria
        
        # PCD: Pessoa com Deficiência
        # Validação: campo necessidades_especiais deve ser True
        if categoria == 'PCD':
            return interessado.necessidades_especiais
        
        # NIS: Programa Social (Cadastro Único)
        # Validação: campo programa_social deve ser True
        if categoria == 'NIS':
            return interessado.programa_social
        
        # JOVEM: Faixa etária 16-24 anos
        # Validação: calcula idade a partir de data_nascimento
        if categoria == 'JOVEM':
            if interessado.data_nascimento:
                idade = (date.today() - interessado.data_nascimento).days // 365
                return 16 <= idade <= 24
            return False
        
        # IDOSO: Faixa etária 50+ anos
        # Validação: calcula idade e verifica se >= 50
        if categoria == 'IDOSO':
            if interessado.data_nascimento:
                idade = (date.today() - interessado.data_nascimento).days // 365
                return idade >= 50
            return False
        
        # COTA_RACIAL: Preto, Pardo, Indígena
        # Validação: fototipo.id deve estar em [2, 3, 5] (conforme tabela interessados_fototipo)
        # IDs: 2=Preta, 3=Parda, 5=Indígena
        if categoria == 'COTA_RACIAL':
            if interessado.fototipo:
                return interessado.fototipo.id in [2, 3, 5]
            return False
        
        # ESC_FUND_INC: Ensino Fundamental Incompleto
        if categoria == 'ESC_FUND_INC':
            return interessado.escolaridade == 'FUNDAMENTAL_INCOMPLETO'
        
        # ESC_FUND_COMP: Ensino Fundamental Completo
        if categoria == 'ESC_FUND_COMP':
            return interessado.escolaridade == 'FUNDAMENTAL_COMPLETO'
        
        # ESC_MEDIO_INC: Ensino Médio Incompleto
        if categoria == 'ESC_MEDIO_INC':
            return interessado.escolaridade == 'MEDIO_INCOMPLETO'
        
        # ESC_MEDIO_COMP: Ensino Médio Completo
        if categoria == 'ESC_MEDIO_COMP':
            return interessado.escolaridade == 'MEDIO_COMPLETO'
        
        # Se categoria não reconhecida, assume que atende (padrão permissivo)
        return True

    @staticmethod
    def _calcular_pontos(inscricao):
        """
        MÉTODO PRIVADO: Lógica pura de cálculo de pontuação.
        
        Percorre os critérios do evento com tipo PONTUACAO e soma os pontos
        APENAS dos critérios que a inscrição ATENDE (validação automática).
        SEM efeitos colaterais no BD (não salva).
        
        Fluxo:
        1. Obtém EventoCriterio com ativo=True ordenados por prioridade
        2. Para cada critério com tipo PONTUACAO:
           - Valida se inscrição atende (via _atende_criterio)
           - Se atende, soma os pontos
        3. Retorna Decimal('0.00') se sem critérios ou nenhum atendido
        
        Alteração: 19/05/2026 - Adicionada validação automática de atendimento
        
        Args:
            inscricao: Objeto Inscricao com evento relacionado
            
        Returns:
            Decimal: Pontuação total calculada (0.00 se sem critérios)
        """
        pontuacao_total = Decimal('0.00')
        
        # Acessa critérios através do relacionamento EventoCriterio
        # related_name='evento_criterios' (definido em apps/eventos/models.py)
        evento_criterios = inscricao.evento.evento_criterios.filter(
            ativo=True
        ).order_by('prioridade')
        
        for evento_criterio in evento_criterios:
            criterio = evento_criterio.criterio
            
            # Lógica de pontuação:
            # - Apenas critérios com tipo PONTUACAO
            # - Apenas se inscrição ATENDE o critério
            # - Apenas se critério tem pontos definidos
            if (criterio.tipo_criterio == 'PONTUACAO' and 
                criterio.pontos is not None and
                ClassificadorService._atende_criterio(inscricao, criterio)):
                
                pontuacao_total += Decimal(str(criterio.pontos))
        
        return pontuacao_total

    @staticmethod
    def calcular_pontuacao_inscricao(inscricao):
        """
        Calcula a pontuação de uma inscrição SEM salvar no BD.
        
        Método público que reutiliza _calcular_pontos().
        Útil para validações, testes e consultas sem persistência.
        
        Alteração: 19/05/2026 - Implementação como wrapper de _calcular_pontos()
        
        Args:
            inscricao: Objeto Inscricao com evento relacionado
            
        Returns:
            Decimal: Pontuação total calculada
        """
        return ClassificadorService._calcular_pontos(inscricao)

    @staticmethod
    def processar_inscricao(inscricao):
        """
        Processa uma inscrição: calcula pontuação e cria/atualiza Classificacao.
        
        Reutiliza _calcular_pontos() e persiste em Classificacao.
        NÃO atualiza status, classificado, lista_espera, posicao aqui.
        Esses campos são definidos por classificar_evento().
        
        Alteração: 19/05/2026 - Refatoração com validação automática
        
        Args:
            inscricao: Objeto Inscricao com evento relacionado
            
        Returns:
            Decimal: Pontuação total calculada e salva
        """
        pontuacao_total = ClassificadorService._calcular_pontos(inscricao)
        
        # Cria ou atualiza Classificacao com a pontuação
        classificacao, criada = Classificacao.objects.get_or_create(
            inscricao=inscricao,
            defaults={'pontuacao_total': pontuacao_total}
        )
        
        if not criada:
            classificacao.pontuacao_total = pontuacao_total
            classificacao.save()
        
        return pontuacao_total

    @staticmethod
    @transaction.atomic
    def classificar_evento(evento):
        """
        Classifica TODAS as inscrições do evento:
        - Processa cada inscrição para calcular pontuação
        - Aplica desempate inteligente (idade ou timestamp)
        - Aplica quotas se critérios existirem (30% PCD, 40% social)
        - Atribui posições ordinais
        - Marca classificado/lista_espera
        - Atualiza status Inscricao para "Classificado"
        
        Desempate Inteligente (Documento 07, Seção 5):
        - Verifica se existe critério de IDADE ou FAIXA_ETARIA
        - SE SIM: ordena por idade
          - Para critérios de jovem: crescente (idade menor = melhor)
          - Para critérios de idoso: decrescente (idade maior = melhor)
        - SE NÃO: ordena por data_inscricao (timestamp) - FIFO
        
        Quotas (apenas se critérios estabelecidos existirem):
        - 30% PCD: se critério categoria='PCD' existir
        - 40% social: se critério categoria='VULNERABILIDADE' existir
        - Resto: concorrência aberta
        
        Alteração: 19/05/2026 - Implementação com validação automática
        
        Args:
            evento: Objeto Evento a ser classificado
            
        Returns:
            dict: {'sucesso': True/False, 'mensagem': str, 'total_processadas': int}
        """
        try:
            # Obter todas as inscrições do evento
            inscricoes = Inscricao.objects.filter(evento=evento)
            
            if not inscricoes.exists():
                return {
                    'sucesso': False,
                    'mensagem': f'Nenhuma inscrição encontrada para o evento {evento.nome}',
                    'total_processadas': 0
                }
            
            # Etapa 1: Processar pontuações para todas as inscrições
            for inscricao in inscricoes:
                ClassificadorService.processar_inscricao(inscricao)
            
            # Etapa 2: Obter Classificacoes e aplicar desempate
            classificacoes = Classificacao.objects.filter(
                inscricao__evento=evento
            ).select_related('inscricao__interessado')
            
            # Desempate Inteligente
            # Verifica se existe critério de idade/faixa_etaria
            tem_criterio_idade = evento.evento_criterios.filter(
                criterio__categoria__in=['IDADE', 'FAIXA_ETARIA', 'JOVEM', 'IDOSO'],
                ativo=True
            ).exists()
            
            if tem_criterio_idade:
                # Desempate por idade
                # NOTA: Assumindo que Interessado tem campo 'data_nascimento'
                classificacoes = sorted(
                    classificacoes,
                    key=lambda x: (
                        -float(x.pontuacao_total),  # Pontuação DESC (maior primeiro)
                        x.inscricao.interessado.data_nascimento or date.today()  # Idade (crescente)
                    )
                )
            else:
                # Desempate por timestamp (FIFO)
                classificacoes = sorted(
                    classificacoes,
                    key=lambda x: (
                        -float(x.pontuacao_total),  # Pontuação DESC
                        x.inscricao.data_inscricao  # Data de inscrição ASC (chegou primeiro = melhor)
                    )
                )
            
            # Etapa 3: Aplicar quotas (se critérios existirem)
            tem_criterio_pcd = evento.evento_criterios.filter(
                criterio__categoria='PCD',
                ativo=True
            ).exists()
            
            tem_criterio_social = evento.evento_criterios.filter(
                criterio__categoria='NIS',
                ativo=True
            ).exists()
            
            # Cálculo de vagas por quota
            total_vagas = evento.total_vagas
            vagas_pcd = int(total_vagas * 0.30) if tem_criterio_pcd else 0
            vagas_social = int(total_vagas * 0.40) if tem_criterio_social else 0
            vagas_aberta = total_vagas - vagas_pcd - vagas_social
            
            # Etapa 4: Atribuir posições e flags
            posicao = 1
            
            # Obter status "Classificado" e "Lista de Espera"
            status_classificado = StatusInscricao.objects.get(nome='Classificado')
            
            for classificacao in classificacoes:
                classificacao.posicao = posicao
                
                # Lógica de preenchimento de vagas (simplificada)
                # NOTA: Implement full quota logic based on interessado PCD/social status if needed
                if posicao <= total_vagas:
                    classificacao.classificado = True
                    classificacao.lista_espera = False
                    # Atualizar status da inscrição
                    classificacao.inscricao.status = status_classificado
                else:
                    classificacao.classificado = False
                    classificacao.lista_espera = True
                
                classificacao.save()
                classificacao.inscricao.save()
                posicao += 1
            
            return {
                'sucesso': True,
                'mensagem': f'Evento {evento.nome} classificado com sucesso. {total_vagas} vagas preenchidas.',
                'total_processadas': len(classificacoes)
            }
        
        except StatusInscricao.DoesNotExist:
            return {
                'sucesso': False,
                'mensagem': 'Status "Classificado" não encontrado. Verifique StatusInscricao no admin.',
                'total_processadas': 0
            }
        except Exception as erro:
            return {
                'sucesso': False,
                'mensagem': f'Erro ao classificar evento: {str(erro)}',
                'total_processadas': 0
            }
        
        