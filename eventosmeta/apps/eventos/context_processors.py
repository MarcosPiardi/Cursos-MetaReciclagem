# Arquivo: context_processors.py
# Caminho: apps/eventos/context_processors.py
# Alteração: Context processor com 4 verificações de status - Expandido
# Data: 19/02/2026

from datetime import date, datetime
from django.conf import settings

# DEBUG mode - controla se exibe prints
DEBUG_NOTIFICACOES = settings.DEBUG

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
    if request.user.is_authenticated and request.user.is_staff:
        try:
            if DEBUG_NOTIFICACOES:
                print("\n" + "="*80)
                print("🚀 INICIANDO CONTEXT PROCESSOR - NOTIFICAÇÕES DE EVENTOS")
                print("="*80)
                print(f"👤 Usuário: {request.user.username}")
                print(f"🔐 É staff: {request.user.is_staff}")
                print(f"🔐 É superuser: {request.user.is_superuser}")
                print(f"📅 Data Atual: {date.today().strftime('%d/%m/%Y')}")
                print("="*80)
            
            # Import dentro da função para evitar erros de importação circular
            from apps.eventos.models import Evento
            
            hoje = date.today()
            
            # Busca TODOS os eventos ativos
            eventos = Evento.objects.select_related('status').all()
            
            if DEBUG_NOTIFICACOES:
                print(f"\n📊 TOTAL DE EVENTOS NO BANCO: {eventos.count()}")
                print("="*80)
                print("🔎 VERIFICANDO EVENTO POR EVENTO")
                print("="*80)
            
            for evento in eventos:
                if DEBUG_NOTIFICACOES:
                    print(f"\n📌 EVENTO: {evento.nome}")
                    print(f"   Status Atual: {evento.status.nome if evento.status else 'SEM STATUS'}")
                    if evento.status:
                        print(f"   Cor Status: {evento.status.cor}")
                
                # Converter datas datetime para date
                def converter_data(data):
                    if data is None:
                        return None
                    return data.date() if isinstance(data, datetime) else data
                
                data_inicio_insc = converter_data(evento.data_inicio_inscricao)
                data_fim_insc = converter_data(evento.data_fim_inscricao)
                data_inicio_ev = converter_data(evento.data_inicio_evento)
                data_fim_ev = converter_data(evento.data_fim_evento)
                
                # Flag para controlar se já foi adicionado
                evento_ja_adicionado = False
                
                # ==========================================
                # VERIFICAÇÃO 1: PERÍODO DE INSCRIÇÕES
                # ==========================================
                if DEBUG_NOTIFICACOES:
                    print(f"\n   🔍 Verificação 1: PERÍODO DE INSCRIÇÕES")
                    print(f"      Data Início Inscrição: {data_inicio_insc.strftime('%d/%m/%Y') if data_inicio_insc else 'NÃO DEFINIDA'}")
                    print(f"      Data Fim Inscrição: {data_fim_insc.strftime('%d/%m/%Y') if data_fim_insc else 'NÃO DEFINIDA'}")
                
                if data_inicio_insc and data_fim_insc:
                    esta_no_periodo_inscricao = data_inicio_insc <= hoje <= data_fim_insc
                    
                    if DEBUG_NOTIFICACOES:
                        print(f"      ✅ Hoje está no período? {esta_no_periodo_inscricao}")
                    
                    if esta_no_periodo_inscricao:
                        status_correto = evento.status and evento.status.nome == 'Inscrições Abertas'
                        
                        if DEBUG_NOTIFICACOES:
                            print(f"      ✅ Status é 'Inscrições Abertas'? {status_correto}")
                        
                        if not status_correto:
                            if DEBUG_NOTIFICACOES:
                                print(f"      ⚠️  ALERTA! Status deveria ser 'Inscrições Abertas'")
                            evento.tipo_alerta = 'inscricao'
                            eventos_para_notificar.append(evento)
                            evento_ja_adicionado = True
                            if DEBUG_NOTIFICACOES:
                                print(f"      ✅ Evento adicionado à lista de notificações")
                        else:
                            if DEBUG_NOTIFICACOES:
                                print(f"      ✅ Status está correto")
                    else:
                        if DEBUG_NOTIFICACOES:
                            print(f"      ℹ️  Hoje NÃO está no período de inscrições")
                else:
                    if DEBUG_NOTIFICACOES:
                        print(f"      ⚠️  Datas de inscrição incompletas - ignorando verificação")
                
                # ==========================================
                # VERIFICAÇÃO 2: ENTRE FIM INSCRIÇÕES E INÍCIO EVENTO
                # ==========================================
                if DEBUG_NOTIFICACOES:
                    print(f"\n   🔍 Verificação 2: PERÍODO ENTRE FIM INSCRIÇÕES E INÍCIO EVENTO")
                    print(f"      Data Fim Inscrição: {data_fim_insc.strftime('%d/%m/%Y') if data_fim_insc else 'NÃO DEFINIDA'}")
                    print(f"      Data Início Evento: {data_inicio_ev.strftime('%d/%m/%Y') if data_inicio_ev else 'NÃO DEFINIDA'}")
                
                if data_fim_insc and data_inicio_ev and not evento_ja_adicionado:
                    esta_entre_inscricao_evento = data_fim_insc < hoje < data_inicio_ev
                    
                    if DEBUG_NOTIFICACOES:
                        print(f"      ✅ Hoje está entre fim inscrição e início evento? {esta_entre_inscricao_evento}")
                    
                    if esta_entre_inscricao_evento:
                        status_validos = ['Inscrições Encerradas', 'Em Classificação', 'Resultado Divulgado', 'Cancelado']
                        status_correto = evento.status and evento.status.nome in status_validos
                        
                        if DEBUG_NOTIFICACOES:
                            print(f"      ✅ Status é um dos válidos {status_validos}? {status_correto}")
                            if evento.status:
                                print(f"      📊 Status atual: {evento.status.nome}")
                        
                        if not status_correto:
                            if DEBUG_NOTIFICACOES:
                                print(f"      ⚠️  ALERTA! Status deveria ser um de: {', '.join(status_validos)}")
                            evento.tipo_alerta = 'pos_inscricao'
                            eventos_para_notificar.append(evento)
                            evento_ja_adicionado = True
                            if DEBUG_NOTIFICACOES:
                                print(f"      ✅ Evento adicionado à lista de notificações")
                        else:
                            if DEBUG_NOTIFICACOES:
                                print(f"      ✅ Status está correto")
                    else:
                        if DEBUG_NOTIFICACOES:
                            print(f"      ℹ️  Hoje NÃO está entre fim inscrição e início evento")
                else:
                    if DEBUG_NOTIFICACOES:
                        if evento_ja_adicionado:
                            print(f"      ℹ️  Evento já foi adicionado em verificação anterior")
                        else:
                            print(f"      ⚠️  Datas incompletas - ignorando verificação")
                
                # ==========================================
                # VERIFICAÇÃO 3: PERÍODO DO EVENTO
                # ==========================================
                if DEBUG_NOTIFICACOES:
                    print(f"\n   🔍 Verificação 3: PERÍODO DO EVENTO")
                    print(f"      Data Início Evento: {data_inicio_ev.strftime('%d/%m/%Y') if data_inicio_ev else 'NÃO DEFINIDA'}")
                    print(f"      Data Fim Evento: {data_fim_ev.strftime('%d/%m/%Y') if data_fim_ev else 'NÃO DEFINIDA'}")
                
                if data_inicio_ev and data_fim_ev and not evento_ja_adicionado:
                    esta_no_periodo_evento = data_inicio_ev <= hoje <= data_fim_ev
                    
                    if DEBUG_NOTIFICACOES:
                        print(f"      ✅ Hoje está no período? {esta_no_periodo_evento}")
                    
                    if esta_no_periodo_evento:
                        status_correto = evento.status and evento.status.nome == 'Em Andamento'
                        
                        if DEBUG_NOTIFICACOES:
                            print(f"      ✅ Status é 'Em Andamento'? {status_correto}")
                        
                        if not status_correto:
                            if DEBUG_NOTIFICACOES:
                                print(f"      ⚠️  ALERTA! Status deveria ser 'Em Andamento'")
                            evento.tipo_alerta = 'evento'
                            eventos_para_notificar.append(evento)
                            evento_ja_adicionado = True
                            if DEBUG_NOTIFICACOES:
                                print(f"      ✅ Evento adicionado à lista de notificações")
                        else:
                            if DEBUG_NOTIFICACOES:
                                print(f"      ✅ Status está correto")
                    else:
                        if DEBUG_NOTIFICACOES:
                            print(f"      ℹ️  Hoje NÃO está no período do evento")
                else:
                    if DEBUG_NOTIFICACOES:
                        if evento_ja_adicionado:
                            print(f"      ℹ️  Evento já foi adicionado em verificação anterior")
                        else:
                            print(f"      ⚠️  Datas do evento incompletas - ignorando verificação")
                
                # ==========================================
                # VERIFICAÇÃO 4: POSTERIOR AO FIM DO EVENTO
                # ==========================================
                if DEBUG_NOTIFICACOES:
                    print(f"\n   🔍 Verificação 4: POSTERIOR AO FIM DO EVENTO")
                    print(f"      Data Fim Evento: {data_fim_ev.strftime('%d/%m/%Y') if data_fim_ev else 'NÃO DEFINIDA'}")
                
                if data_fim_ev and not evento_ja_adicionado:
                    evento_ja_finalizado = hoje > data_fim_ev
                    
                    if DEBUG_NOTIFICACOES:
                        print(f"      ✅ Hoje é posterior ao fim do evento? {evento_ja_finalizado}")
                    
                    if evento_ja_finalizado:
                        status_validos = ['Finalizado', 'Cancelado']
                        status_correto = evento.status and evento.status.nome in status_validos
                        
                        if DEBUG_NOTIFICACOES:
                            print(f"      ✅ Status é um dos válidos {status_validos}? {status_correto}")
                            if evento.status:
                                print(f"      📊 Status atual: {evento.status.nome}")
                        
                        if not status_correto:
                            if DEBUG_NOTIFICACOES:
                                print(f"      ⚠️  ALERTA! Status deveria ser 'Finalizado' ou 'Cancelado'")
                            evento.tipo_alerta = 'pos_evento'
                            eventos_para_notificar.append(evento)
                            evento_ja_adicionado = True
                            if DEBUG_NOTIFICACOES:
                                print(f"      ✅ Evento adicionado à lista de notificações")
                        else:
                            if DEBUG_NOTIFICACOES:
                                print(f"      ✅ Status está correto")
                    else:
                        if DEBUG_NOTIFICACOES:
                            print(f"      ℹ️  Hoje NÃO é posterior ao fim do evento")
                else:
                    if DEBUG_NOTIFICACOES:
                        if evento_ja_adicionado:
                            print(f"      ℹ️  Evento já foi adicionado em verificação anterior")
                        else:
                            print(f"      ⚠️  Data de fim do evento não definida - ignorando verificação")
                
                if DEBUG_NOTIFICACOES:
                    print(f"\n   {'─'*76}")
            
            # Resumo final
            if DEBUG_NOTIFICACOES:
                print("\n" + "="*80)
                print("📊 RESUMO FINAL")
                print("="*80)
                print(f"✅ Total de eventos verificados: {eventos.count()}")
                print(f"⚠️  Total de eventos com alertas: {len(eventos_para_notificar)}")
                
                if eventos_para_notificar:
                    print("\n🔔 EVENTOS QUE GERARÃO BANNER:")
                    for ev in eventos_para_notificar:
                        print(f"   • {ev.nome} (tipo: {ev.tipo_alerta})")
                else:
                    print("\n✅ Nenhum evento precisa de notificação")
                
                print("="*80 + "\n")
        
        except Exception as e:
            # Em caso de erro, não quebra a aplicação
            if DEBUG_NOTIFICACOES:
                print("\n" + "="*80)
                print("❌ ERRO NO CONTEXT PROCESSOR")
                print("="*80)
                print(f"Tipo de erro: {type(e).__name__}")
                print(f"Mensagem: {e}")
                print("="*80 + "\n")
                
                import traceback
                traceback.print_exc()
            
            eventos_para_notificar = []
    
    return {
        'eventos_notificacao': eventos_para_notificar
    }

