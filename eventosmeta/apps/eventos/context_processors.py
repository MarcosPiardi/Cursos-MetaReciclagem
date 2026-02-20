# Arquivo: context_processors.py
# Caminho: apps/eventos/context_processors.py
# Alteração: Context processor com 4 verificações de status - Expandido
# Data: 19/02/2026
# Alteração: Removidos prints de debug
# Data: 20/02/2026

from datetime import date, datetime


def notificacoes_eventos(request):
    """
    Adiciona eventos que precisam de notificação ao contexto do template.

    Exibe banner para admin/staff quando:
    1. Data atual está no período de inscrições E status ≠ "Inscrições Abertas"
    2. Data atual está entre fim inscrições e início evento E status não é um dos esperados
    3. Data atual está no período do evento E status ≠ "Em Andamento"
    4. Data atual é posterior ao fim do evento E status não é um dos esperados
    """
    eventos_para_notificar = []

    # Só processa para usuários staff autenticados
    if not (request.user.is_authenticated and request.user.is_staff):
        return {'eventos_notificacao': eventos_para_notificar}

    try:
        from apps.eventos.models import Evento

        hoje = date.today()

        eventos = Evento.objects.select_related('status').all()

        for evento in eventos:

            # Converter datas datetime para date
            def converter_data(data):
                if data is None:
                    return None
                return data.date() if isinstance(data, datetime) else data

            data_inicio_insc = converter_data(evento.data_inicio_inscricao)
            data_fim_insc    = converter_data(evento.data_fim_inscricao)
            data_inicio_ev   = converter_data(evento.data_inicio_evento)
            data_fim_ev      = converter_data(evento.data_fim_evento)

            evento_ja_adicionado = False

            # ==========================================
            # VERIFICAÇÃO 1: PERÍODO DE INSCRIÇÕES
            # ==========================================
            if data_inicio_insc and data_fim_insc:
                if data_inicio_insc <= hoje <= data_fim_insc:
                    status_correto = (
                        evento.status and
                        evento.status.nome == 'Inscrições Abertas'
                    )
                    if not status_correto:
                        evento.tipo_alerta = 'inscricao'
                        eventos_para_notificar.append(evento)
                        evento_ja_adicionado = True

            # ==========================================
            # VERIFICAÇÃO 2: ENTRE FIM INSCRIÇÕES E INÍCIO EVENTO
            # ==========================================
            if data_fim_insc and data_inicio_ev and not evento_ja_adicionado:
                if data_fim_insc < hoje < data_inicio_ev:
                    status_validos = [
                        'Inscrições Encerradas',
                        'Em Classificação',
                        'Resultado Divulgado',
                        'Cancelado'
                    ]
                    status_correto = (
                        evento.status and
                        evento.status.nome in status_validos
                    )
                    if not status_correto:
                        evento.tipo_alerta = 'pos_inscricao'
                        eventos_para_notificar.append(evento)
                        evento_ja_adicionado = True

            # ==========================================
            # VERIFICAÇÃO 3: PERÍODO DO EVENTO
            # ==========================================
            if data_inicio_ev and data_fim_ev and not evento_ja_adicionado:
                if data_inicio_ev <= hoje <= data_fim_ev:
                    status_correto = (
                        evento.status and
                        evento.status.nome == 'Em Andamento'
                    )
                    if not status_correto:
                        evento.tipo_alerta = 'evento'
                        eventos_para_notificar.append(evento)
                        evento_ja_adicionado = True

            # ==========================================
            # VERIFICAÇÃO 4: POSTERIOR AO FIM DO EVENTO
            # ==========================================
            if data_fim_ev and not evento_ja_adicionado:
                if hoje > data_fim_ev:
                    status_validos = ['Finalizado', 'Cancelado']
                    status_correto = (
                        evento.status and
                        evento.status.nome in status_validos
                    )
                    if not status_correto:
                        evento.tipo_alerta = 'pos_evento'
                        eventos_para_notificar.append(evento)

    except Exception:
        eventos_para_notificar = []

    return {
        'eventos_notificacao': eventos_para_notificar
    }

