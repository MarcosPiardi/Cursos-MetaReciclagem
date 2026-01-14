"""
Arquivo: services.py
Caminho: apps/selecao/services.py
Alteração: Adicionadas validações antes da classificação usando ClassificacaoValidator
Data: 11/12/2025
"""

"""
Arquivo: services.py
Caminho: apps/selecao/services.py
Alteração: Implementada nova regra de status após classificação + status do evento "Resultado Divulgado"
Data: 08/01/2026
"""

"""
Arquivo: services.py
Caminho: apps/selecao/services.py
Alteração: Corrigido erro fototipo.upper() para fototipo.nome e ampliado status válidos
Data: 10/12/2025
"""

"""
Arquivo: services.py
Caminho: apps/selecao/services.py
Responsável por: Lógica de classificação e pontuação
Alteração: Adicionado suporte a critérios de ORDENACAO com prioridade
Data: 09/12/2025
"""

from django.db import transaction
from django.utils import timezone
from .models import Inscricao, Classificacao, InscricaoCriterioAtendido, StatusInscricao
from apps.eventos.models import Evento, EventoCriterio
from decimal import Decimal
import logging

# ============================================================================
# 🆕 NOVO: Import do validador
# ============================================================================
from apps.selecao.validators import ClassificacaoValidator

logger = logging.getLogger(__name__)


class ClassificadorService:
    """
    Service responsável por classificar inscrições com base em critérios
    
    REGRA DE NEGÓCIO (11/12/2025):
    - Apenas inscrições com status: Pendente, Classificado, Lista de Espera participam
    - Após classificação, status da inscrição é atualizado para:
      * Classificado (se posição <= total_vagas)
      * Lista de Espera (se posição > total_vagas)
    - Status do evento é alterado para "Resultado Divulgado" (ID=5)
    """
    
    # Status válidos para participar da classificação
    STATUS_VALIDOS_CLASSIFICACAO = ['Pendente', 'Classificado', 'Lista de Espera']
    
    @staticmethod
    def calcular_pontuacao_inscricao(inscricao):
        """
        Calcula pontuação total de uma inscrição baseado nos critérios atendidos
        
        Args:
            inscricao: Objeto Inscricao
            
        Returns:
            Decimal: Pontuação total
        """
        criterios_atendidos = InscricaoCriterioAtendido.objects.filter(
            inscricao=inscricao
        )
        
        total = sum(
            criterio.pontos_atribuidos 
            for criterio in criterios_atendidos
        )
        
        return Decimal(str(total))
    
    @staticmethod
    def verificar_criterios_automaticos(inscricao):
        """
        Verifica automaticamente quais critérios o interessado atende
        
        Args:
            inscricao: Objeto Inscricao
            
        Returns:
            list: Lista de criterios atendidos
        """
        interessado = inscricao.interessado
        evento = inscricao.evento
        criterios_evento = EventoCriterio.objects.filter(evento=evento, ativo=True)
        
        criterios_atendidos = []
        
        for evento_criterio in criterios_evento:
            criterio = evento_criterio.criterio
            
            if criterio.tipo_criterio == 'ORDENACAO':
                continue
            
            atende = False
            pontos = criterio.pontos or 0
            
            if criterio.codigo == 'PCD':
                if interessado.tem_deficiencia:
                    atende = True
            
            elif criterio.codigo == 'PROGRAMA_SOCIAL' or criterio.codigo == 'NIS':
                if interessado.programa_social and interessado.num_nis:
                    atende = True
            
            elif criterio.codigo.startswith('JOVEM') or criterio.codigo.startswith('IDOSO') or criterio.categoria == 'FAIXA_ETARIA':
                if interessado.data_nascimento:
                    hoje = timezone.now().date()
                    idade = hoje.year - interessado.data_nascimento.year
                    
                    if (hoje.month, hoje.day) < (interessado.data_nascimento.month, interessado.data_nascimento.day):
                        idade -= 1
                    
                    if '16' in criterio.nome and '24' in criterio.nome:
                        if 16 <= idade <= 24:
                            atende = True
                    elif '50' in criterio.nome or 'Idoso' in criterio.nome:
                        if idade >= 50:
                            atende = True
                    elif '60' in criterio.nome:
                        if idade >= 60:
                            atende = True
            
            elif criterio.categoria == 'ESCOLARIDADE':
                if interessado.escolaridade:
                    niveis_ordem = [
                        'FUNDAMENTAL_INCOMPLETO',
                        'FUNDAMENTAL_COMPLETO',
                        'MEDIO_INCOMPLETO',
                        'MEDIO_COMPLETO',
                        'SUPERIOR_INCOMPLETO',
                        'SUPERIOR_COMPLETO',
                        'POS_GRADUACAO'
                    ]
                    
                    nivel_minimo = None
                    if 'Fundamental Completo' in criterio.nome:
                        nivel_minimo = 'FUNDAMENTAL_COMPLETO'
                    elif 'Médio Completo' in criterio.nome or 'Medio Completo' in criterio.nome:
                        nivel_minimo = 'MEDIO_COMPLETO'
                    elif 'Superior' in criterio.nome:
                        nivel_minimo = 'SUPERIOR_COMPLETO'
                    
                    if nivel_minimo and interessado.escolaridade in niveis_ordem:
                        idx_interessado = niveis_ordem.index(interessado.escolaridade)
                        idx_minimo = niveis_ordem.index(nivel_minimo)
                        
                        if idx_interessado >= idx_minimo:
                            atende = True
            
            elif criterio.codigo == 'RENDA_FAMILIAR':
                atende = False
            
            elif criterio.categoria == 'COTA_RACIAL':
                if interessado.fototipo:
                    racas_cotistas = ['Preta', 'Parda', 'Indígena', 'Preto', 'Pardo', 'Indigena']
                    if interessado.fototipo.nome in racas_cotistas:
                        atende = True
            
            if atende:
                criterios_atendidos.append({
                    'criterio': criterio,
                    'pontos': pontos,
                    'validado': True
                })
        
        return criterios_atendidos
    
    @staticmethod
    @transaction.atomic
    def processar_inscricao(inscricao):
        """
        Processa uma inscrição: verifica critérios e calcula pontuação
        
        Args:
            inscricao: Objeto Inscricao
        """
        criterios_atendidos = ClassificadorService.verificar_criterios_automaticos(inscricao)
        
        for item in criterios_atendidos:
            InscricaoCriterioAtendido.objects.update_or_create(
                inscricao=inscricao,
                criterio=item['criterio'],
                defaults={
                    'pontos_atribuidos': item['pontos'],
                    'validado': item['validado']
                }
            )
        
        pontuacao_total = ClassificadorService.calcular_pontuacao_inscricao(inscricao)
        
        Classificacao.objects.update_or_create(
            inscricao=inscricao,
            defaults={
                'pontuacao_total': pontuacao_total,
                'processado_em': timezone.now()
            }
        )
        
        logger.info(f"Inscrição {inscricao.id} processada. Pontuação: {pontuacao_total}")
    
    @staticmethod
    @transaction.atomic
    def classificar_evento(evento):
        """
        Classifica todas as inscrições de um evento
        
        LÓGICA:
        - Critérios são aplicados conforme prioridade definida no evento
        - Pode ser: ORDENACAO primeiro, PONTUACAO primeiro, ou misturado
        
        NOVA REGRA (11/12/2025):
        - Apenas inscrições com status: Pendente, Classificado, Lista de Espera participam
        - Após classificação:
          * Inscrições classificadas recebem status "Classificado"
          * Inscrições em lista de espera recebem status "Lista de Espera"
          * Evento recebe status "Resultado Divulgado"
        
        Args:
            evento: Objeto Evento
            
        Returns:
            dict: Resultado da classificação com estatísticas
            
        Raises:
            ValueError: Se validações falharem
        """
        logger.info(f"Iniciando classificação do evento: {evento.nome} (ID: {evento.id})")
        
        # ============================================================================
        # 🆕 NOVO: VALIDAÇÕES ANTES DE CLASSIFICAR
        # ============================================================================
        
        # 1. Validar evento
        validacao_evento = ClassificacaoValidator.validar_evento(evento)
        
        if not validacao_evento['valido']:
            erros_formatados = '\n• '.join(validacao_evento['erros'])
            mensagem_erro = f'❌ VALIDAÇÃO FALHOU:\n• {erros_formatados}'
            logger.error(mensagem_erro)
            raise ValueError(mensagem_erro)
        
        # Exibir avisos (não bloqueiam, mas informam no log)
        if validacao_evento['avisos']:
            logger.warning(f"⚠️  AVISOS para evento {evento.nome}:")
            for aviso in validacao_evento['avisos']:
                logger.warning(f"   • {aviso}")
        
        # ============================================================================
        # FIM DAS VALIDAÇÕES - Código original continua abaixo
        # ============================================================================
        
        # Busca status válidos para classificação
        status_validos = StatusInscricao.objects.filter(
            nome__in=ClassificadorService.STATUS_VALIDOS_CLASSIFICACAO
        )
        
        # Validação: status devem existir
        if not status_validos.exists():
            mensagem = f"ERRO: Nenhum status válido encontrado. Verifique se existem os status: {ClassificadorService.STATUS_VALIDOS_CLASSIFICACAO}"
            logger.error(mensagem)
            raise ValueError(mensagem)
        
        logger.info(f"Status válidos para classificação: {[s.nome for s in status_validos]}")
        
        # Filtra inscrições elegíveis
        inscricoes = Inscricao.objects.filter(
            evento=evento,
            status__in=status_validos
        ).select_related('interessado')
        
        total_inscricoes = inscricoes.count()
        logger.info(f"Total de inscrições elegíveis: {total_inscricoes}")
        
        if total_inscricoes == 0:
            logger.warning("Nenhuma inscrição elegível para classificar")
            return {
                'sucesso': True,
                'total_processadas': 0,
                'total_classificadas': 0,
                'total_lista_espera': 0,
                'mensagem': 'Nenhuma inscrição elegível para classificar'
            }
        
        # Processa cada inscrição (calcula pontuação)
        for inscricao in inscricoes:
            ClassificadorService.processar_inscricao(inscricao)
        
        logger.info("Pontuações calculadas para todas as inscrições")
        
        # Busca critérios de ordenação do evento
        criterios_evento = EventoCriterio.objects.filter(
            evento=evento,
            ativo=True
        ).select_related('criterio').order_by('prioridade')
        
        # Monta ordem de classificação baseada nos critérios
        order_fields = []
        
        for evento_criterio in criterios_evento:
            criterio = evento_criterio.criterio
            
            if criterio.tipo_criterio == 'PONTUACAO':
                if '-pontuacao_total' not in order_fields:
                    order_fields.append('-pontuacao_total')
            
            elif criterio.tipo_criterio == 'ORDENACAO':
                codigo = criterio.codigo
                
                if codigo == 'ORDEM_INSCRICAO':
                    order_fields.append('inscricao__data_inscricao')
                
                elif codigo == 'IDADE_CRESCENTE':
                    order_fields.append('-inscricao__interessado__data_nascimento')
                
                elif codigo == 'IDADE_DECRESCENTE':
                    order_fields.append('inscricao__interessado__data_nascimento')
        
        # Garante ordem padrão se não houver critérios
        if not order_fields:
            order_fields = ['-pontuacao_total', 'inscricao__data_inscricao']
        
        # Adiciona data de inscrição como desempate final
        if 'inscricao__data_inscricao' not in order_fields and '-inscricao__data_inscricao' not in order_fields:
            order_fields.append('inscricao__data_inscricao')
        
        logger.info(f"Ordem de classificação: {order_fields}")
        
        # Ordena classificações
        classificacoes = Classificacao.objects.filter(
            inscricao__evento=evento,
            inscricao__status__in=status_validos
        ).select_related('inscricao__interessado').order_by(*order_fields)
        
        # Busca status "Classificado" e "Lista de Espera" para atualização
        try:
            status_classificado = StatusInscricao.objects.get(nome='Classificado')
        except StatusInscricao.DoesNotExist:
            mensagem = "ERRO: Status 'Classificado' não encontrado no banco de dados"
            logger.error(mensagem)
            raise ValueError(mensagem)
        
        try:
            status_lista_espera = StatusInscricao.objects.get(nome='Lista de Espera')
        except StatusInscricao.DoesNotExist:
            mensagem = "ERRO: Status 'Lista de Espera' não encontrado no banco de dados"
            logger.error(mensagem)
            raise ValueError(mensagem)
        
        # Atualiza posições e status das inscrições
        total_vagas = evento.total_vagas
        posicao = 1
        total_classificadas = 0
        total_lista_espera = 0
        
        for classificacao in classificacoes:
            # Atualiza posição na tabela Classificacao
            classificacao.posicao = posicao
            classificacao.classificado = (posicao <= total_vagas)
            classificacao.lista_espera = (posicao > total_vagas)
            classificacao.atualizado_em = timezone.now()
            classificacao.save()
            
            # NOVA REGRA: Atualiza status da inscrição
            inscricao = classificacao.inscricao
            
            if posicao <= total_vagas:
                inscricao.status = status_classificado
                total_classificadas += 1
                logger.debug(f"Posição {posicao}: {inscricao.interessado.nome} - CLASSIFICADO")
            else:
                inscricao.status = status_lista_espera
                total_lista_espera += 1
                logger.debug(f"Posição {posicao}: {inscricao.interessado.nome} - LISTA DE ESPERA")
            
            inscricao.save()
            
            posicao += 1
        
        # NOVA REGRA: Atualiza status do evento para "Resultado Divulgado"
        try:
            from apps.eventos.models import Status
            
            status_resultado_divulgado = Status.objects.get(id=5)
            evento.status = status_resultado_divulgado
            evento.save()
            
            logger.info(f"Status do evento alterado para: {status_resultado_divulgado.nome}")
        except Status.DoesNotExist:
            logger.error("ERRO: Status 'Resultado Divulgado' (ID=5) não encontrado")
        except Exception as e:
            logger.warning(f"Não foi possível atualizar status do evento: {e}")
        
        # Log final
        logger.info(
            f"Classificação concluída! "
            f"Evento: {evento.nome} | "
            f"Critérios: {order_fields} | "
            f"Total: {total_inscricoes} | "
            f"Classificadas: {total_classificadas} | "
            f"Lista de Espera: {total_lista_espera}"
        )
        
        # Retorna resultado
        return {
            'sucesso': True,
            'total_processadas': total_inscricoes,
            'total_classificadas': total_classificadas,
            'total_lista_espera': total_lista_espera,
            'criterios_ordenacao': order_fields,
            'mensagem': f'Classificação concluída com sucesso! {total_classificadas} classificados, {total_lista_espera} em lista de espera.'
        }
    
    