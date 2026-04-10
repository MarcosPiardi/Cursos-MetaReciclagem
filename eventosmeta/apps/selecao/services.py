
"""
Services do app SELEÇÃO
Arquivo: apps/selecao/services.py

Histórico de Alterações:
- 20/02/2026: Implementação inicial do ClassificadorService
- 08/04/2026: Adicionado desempate por data_inscricao (ordem de chegada) no método classificar_evento

Funcionalidades:
- Verificação de critérios automáticos
- Cálculo de pontuação por inscrição
- Classificação e ordenação de evento (pontuação + desempate por data)
- Atribuição de posições e flags (classificado/lista_espera)
"""

from django.db import transaction
from apps.selecao.models import Inscricao, Evento, Criterio  # Assumindo os modelos necessários


class ClassificadorService:
    """
    Serviço para classificação de inscrições em eventos.
    """

    @staticmethod
    def verificar_criterios_automaticos(inscricao):
        """
        Verifica quais critérios automáticos o interessado atende (fototipo, idade, etc).
        Retorna um dicionário com os critérios atendidos.
        """
        criterios_atendidos = {}
        # Exemplo: Verificar fototipo (assumindo que Inscricao tem campo fototipo)
        if inscricao.fototipo in ['I', 'II']:  # Critérios de exemplo
            criterios_atendidos['fototipo'] = True
        else:
            criterios_atendidos['fototipo'] = False
        
        # Verificar idade (assumindo campo data_nascimento)
        from datetime import date
        idade = date.today().year - inscricao.data_nascimento.year
        if 18 <= idade <= 65:  # Critérios de exemplo
            criterios_atendidos['idade'] = True
        else:
            criterios_atendidos['idade'] = False
        
        # Adicionar outros critérios conforme necessário
        return criterios_atendidos

    @staticmethod
    def processar_inscricao(inscricao):
        """
        Processa uma inscrição individual calculando sua pontuação total baseado nos critérios do evento.
        """
        pontuacao_total = 0
        # Assumindo que Evento tem critérios relacionados
        for criterio in inscricao.evento.criterios.all():
            # Lógica de pontuação baseada no critério (exemplo simples)
            if criterio.nome == 'fototipo' and ClassificadorService.verificar_criterios_automaticos(inscricao)['fototipo']:
                pontuacao_total += criterio.pontos
            elif criterio.nome == 'idade' and ClassificadorService.verificar_criterios_automaticos(inscricao)['idade']:
                pontuacao_total += criterio.pontos
            # Adicionar lógica para outros critérios
        
        inscricao.pontuacao_total = pontuacao_total
        inscricao.save()
        return pontuacao_total

    @staticmethod
    @transaction.atomic
    def classificar_evento(evento):
        """
        Classifica as inscrições do evento:
        - Processa cada inscrição para calcular pontuação
        - Ordena por pontuação_total DESC, depois por data_inscricao ASC
        - Distribui posições
        - Marca classificado=True para dentro das vagas, lista_espera=True para excedentes
        """
        inscricoes = Inscricao.objects.filter(evento=evento).order_by('-pontuacao_total', 'data_inscricao')
        
        # Processar pontuações se necessário (assumindo que já foram calculadas, mas para garantir)
        for inscricao in inscricoes:
            ClassificadorService.processar_inscricao(inscricao)
        
        # Reordenar após processamento
        inscricoes = sorted(inscricoes, key=lambda x: (-x.pontuacao_total, x.data_inscricao))
        
        posicao = 1
        for inscricao in inscricoes:
            inscricao.posicao = posicao
            if posicao <= evento.total_vagas:
                inscricao.classificado = True
                inscricao.lista_espera = False
            else:
                inscricao.classificado = False
                inscricao.lista_espera = True
            inscricao.save()
            posicao += 1


