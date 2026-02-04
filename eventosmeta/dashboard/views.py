"""
Views do app DASHBOARD
Arquivo: dashboard/views.py
Alteração: Views customizadas para dashboards
Data: 03/02/2026
"""

from django.shortcuts import render
from django.contrib.admin.views.decorators import staff_member_required
from django.db.models import Count, Avg, F
from django.utils import timezone
from datetime import date, timedelta


@staff_member_required
def dashboard_academico(request):
    """Dashboard de Informações Acadêmicas"""
    from apps.academico.models import Avaliacao, Matricula
    from apps.accounts.admin import admin_site
    
    # Métricas gerais
    total_avaliacoes = Avaliacao.objects.count()
    total_aprovados = Avaliacao.objects.filter(aprovado=True).count()
    total_reprovados = total_avaliacoes - total_aprovados
    media_notas = Avaliacao.objects.aggregate(Avg('nota_final'))['nota_final__avg'] or 0
    media_frequencia = Avaliacao.objects.aggregate(Avg('frequencia'))['frequencia__avg'] or 0
    certificados_emitidos = Avaliacao.objects.filter(certificado_emitido=True).count()
    
    # Taxa de aprovação
    taxa_aprovacao = (total_aprovados / total_avaliacoes * 100) if total_avaliacoes > 0 else 0
    
    # Avaliações por status de matrícula
    avaliacoes_por_status = Matricula.objects.values('status__nome').annotate(
        total=Count('avaliacao')
    ).order_by('-total')
    
    # Top 5 cursos com mais aprovados
    top_cursos_aprovados = Avaliacao.objects.filter(aprovado=True).values(
        'matricula__turma__evento__nome'
    ).annotate(
        total=Count('id')
    ).order_by('-total')[:5]
    
    context = {
        'title': 'Dashboard - Informações Acadêmicas',
        'site_title': admin_site.site_title,
        'site_header': admin_site.site_header,
        
        'total_avaliacoes': total_avaliacoes,
        'total_aprovados': total_aprovados,
        'total_reprovados': total_reprovados,
        'taxa_aprovacao': round(taxa_aprovacao, 1),
        'media_notas': round(media_notas, 2),
        'media_frequencia': round(media_frequencia, 1),
        'certificados_emitidos': certificados_emitidos,
        
        'avaliacoes_por_status': avaliacoes_por_status,
        'top_cursos_aprovados': top_cursos_aprovados,
    }
    
    return render(request, 'admin/dashboard/academico.html', context)


@staff_member_required
def dashboard_eventos(request):
    """Dashboard de Eventos e Cursos"""
    from apps.eventos.models import Evento, Turma
    from apps.accounts.admin import admin_site
    
    # Métricas gerais
    total_eventos = Evento.objects.count()
    
    # Eventos ativos (ajuste conforme seu modelo - não há campo 'ativo')
    # Usando eventos com inscrições abertas como proxy de "ativo"
    hoje = timezone.now()
    eventos_ativos = Evento.objects.filter(
        data_inicio_inscricao__lte=hoje,
        data_fim_inscricao__gte=hoje
    ).count()
    
    total_turmas = Turma.objects.count()
    
    # Turmas ativas baseado em datas
    hoje_data = date.today()
    turmas_ativas = Turma.objects.filter(
        data_inicio__lte=hoje_data,
        data_fim__gte=hoje_data
    ).count()
    
    # Eventos por status
    eventos_por_status = Evento.objects.values('status__nome').annotate(
        total=Count('id')
    ).order_by('-total')
    
    # Turmas por período
    turmas_futuras = Turma.objects.filter(data_inicio__gt=hoje_data).count()
    turmas_em_andamento = Turma.objects.filter(
        data_inicio__lte=hoje_data,
        data_fim__gte=hoje_data
    ).count()
    turmas_encerradas = Turma.objects.filter(data_fim__lt=hoje_data).count()
    
    # Top 5 eventos com mais turmas
    top_eventos_turmas = Evento.objects.annotate(
        num_turmas=Count('turmas')
    ).order_by('-num_turmas')[:5]
    
    # Eventos recentes
    eventos_recentes = Evento.objects.order_by('-criado_em')[:5]
    
    context = {
        'title': 'Dashboard - Eventos e Cursos',
        'site_title': admin_site.site_title,
        'site_header': admin_site.site_header,
        
        'total_eventos': total_eventos,
        'eventos_ativos': eventos_ativos,
        'total_turmas': total_turmas,
        'turmas_ativas': turmas_ativas,
        
        'eventos_por_status': eventos_por_status,
        'turmas_futuras': turmas_futuras,
        'turmas_em_andamento': turmas_em_andamento,
        'turmas_encerradas': turmas_encerradas,
        
        'top_eventos_turmas': top_eventos_turmas,
        'eventos_recentes': eventos_recentes,
    }
    
    return render(request, 'admin/dashboard/eventos.html', context)


@staff_member_required
def dashboard_interessados(request):
    """Dashboard de Interessados com dados demográficos detalhados"""
    from apps.interessados.models import Interessado, Sexo, Fototipo
    from apps.academico.models import Matricula
    from apps.accounts.admin import admin_site
    from django.db.models import Q, Count, Case, When, IntegerField, Value, F
    from datetime import date
    
    # ==========================================
    # MÉTRICAS GERAIS
    # ==========================================
    total_interessados = Interessado.objects.count()
    
    interessados_matriculados = Interessado.objects.filter(
        matriculas__isnull=False
    ).distinct().count()
    
    interessados_sem_matricula = total_interessados - interessados_matriculados
    
    trinta_dias_atras = date.today() - timedelta(days=30)
    cadastros_recentes = Interessado.objects.filter(
        criado_em__gte=trinta_dias_atras
    ).count()
    
    # ==========================================
    # DISTRIBUIÇÃO POR SEXO
    # ==========================================
    distribuicao_sexo = Interessado.objects.values('sexo__nome').annotate(
        total=Count('id')
    ).order_by('-total')
    
    # Calcular percentuais
    for item in distribuicao_sexo:
        item['percentual'] = round((item['total'] / total_interessados * 100), 1) if total_interessados > 0 else 0
    
    # ==========================================
    # DISTRIBUIÇÃO POR FOTOTIPO
    # ==========================================
    distribuicao_fototipo = Interessado.objects.values('fototipo__nome').annotate(
        total=Count('id')
    ).order_by('-total')
    
    for item in distribuicao_fototipo:
        item['percentual'] = round((item['total'] / total_interessados * 100), 1) if total_interessados > 0 else 0
    
    # ==========================================
    # DISTRIBUIÇÃO POR ESCOLARIDADE
    # ==========================================
    distribuicao_escolaridade = Interessado.objects.exclude(
        escolaridade=''
    ).values('escolaridade').annotate(
        total=Count('id')
    ).order_by('-total')
    
    # Traduzir códigos de escolaridade
    escolaridade_labels = {
        'FUNDAMENTAL_INCOMPLETO': 'Fundamental Incompleto',
        'FUNDAMENTAL_COMPLETO': 'Fundamental Completo',
        'MEDIO_INCOMPLETO': 'Médio Incompleto',
        'MEDIO_COMPLETO': 'Médio Completo',
        'SUPERIOR_INCOMPLETO': 'Superior Incompleto',
        'SUPERIOR_COMPLETO': 'Superior Completo',
        'POS_GRADUACAO': 'Pós-Graduação',
    }
    
    for item in distribuicao_escolaridade:
        item['escolaridade_label'] = escolaridade_labels.get(item['escolaridade'], item['escolaridade'])
    
    # ==========================================
    # PARTICIPAÇÃO EM PROGRAMAS SOCIAIS
    # ==========================================
    participa_programas = Interessado.objects.filter(programa_social=True).count()
    nao_participa_programas = total_interessados - participa_programas
    
    distribuicao_programas = [
        {
            'participa': 'Sim',
            'total': participa_programas,
            'percentual': round((participa_programas / total_interessados * 100), 1) if total_interessados > 0 else 0
        },
        {
            'participa': 'Não',
            'total': nao_participa_programas,
            'percentual': round((nao_participa_programas / total_interessados * 100), 1) if total_interessados > 0 else 0
        }
    ]
    
    # ==========================================
    # DEFICIÊNCIAS
    # ==========================================
    com_deficiencia = Interessado.objects.filter(necessidades_especiais=True).count()
    sem_deficiencia = total_interessados - com_deficiencia
    
    distribuicao_deficiencia = [
        {
            'tipo': 'Possui Deficiência',
            'total': com_deficiencia,
            'percentual': round((com_deficiencia / total_interessados * 100), 1) if total_interessados > 0 else 0
        },
        {
            'tipo': 'Não Possui',
            'total': sem_deficiencia,
            'percentual': round((sem_deficiencia / total_interessados * 100), 1) if total_interessados > 0 else 0
        }
    ]
    
    # Tipos específicos de deficiência
    tipos_deficiencia = []
    
    deficiencias_map = [
        ('pcd_fisica', 'Física'),
        ('pcd_visual', 'Visual'),
        ('pcd_auditiva', 'Auditiva'),
        ('pcd_intelectual', 'Intelectual'),
        ('pcd_psicossocial', 'Psicossocial'),
        ('pcd_multiplas', 'Múltiplas'),
    ]
    
    for campo, nome in deficiencias_map:
        count = Interessado.objects.filter(**{campo: True}).count()
        if count > 0:
            tipos_deficiencia.append({
                'tipo_deficiencia': nome,
                'total': count
            })
    
    # Ordenar por total decrescente
    tipos_deficiencia.sort(key=lambda x: x['total'], reverse=True)
    
    # ==========================================
    # DISTRIBUIÇÃO POR FAIXA ETÁRIA (5 em 5 anos)
    # ==========================================
    hoje = date.today()
    
    # Criar faixas etárias
    faixas_etarias = []
    faixas = [
        (0, 14, '0-14 anos'),
        (15, 19, '15-19 anos'),
        (20, 24, '20-24 anos'),
        (25, 29, '25-29 anos'),
        (30, 34, '30-34 anos'),
        (35, 39, '35-39 anos'),
        (40, 44, '40-44 anos'),
        (45, 49, '45-49 anos'),
        (50, 54, '50-54 anos'),
        (55, 59, '55-59 anos'),
        (60, 999, '60+ anos'),
    ]
    
    for inicio, fim, label in faixas:
        # Calcular data limite para cada faixa
        if fim == 999:  # 60+
            count = Interessado.objects.filter(
                data_nascimento__lte=hoje.replace(year=hoje.year - inicio)
            ).exclude(data_nascimento__isnull=True).count()
        else:
            data_inicio = hoje.replace(year=hoje.year - fim - 1)
            data_fim = hoje.replace(year=hoje.year - inicio)
            count = Interessado.objects.filter(
                data_nascimento__gt=data_inicio,
                data_nascimento__lte=data_fim
            ).count()
        
        if count > 0:
            faixas_etarias.append({
                'faixa': label,
                'total': count,
                'percentual': round((count / total_interessados * 100), 1) if total_interessados > 0 else 0
            })
    
    # ==========================================
    # TOP 5 COM MAIS MATRÍCULAS
    # ==========================================
    top_interessados_matriculas = Interessado.objects.annotate(
        num_matriculas=Count('matriculas')
    ).filter(num_matriculas__gt=0).order_by('-num_matriculas')[:5]
    
    # ==========================================
    # ÚLTIMOS CADASTROS
    # ==========================================
    ultimos_cadastros = Interessado.objects.order_by('-criado_em')[:10]
    
    context = {
        'title': 'Dashboard - Interessados',
        'site_title': admin_site.site_title,
        'site_header': admin_site.site_header,
        
        # Métricas gerais
        'total_interessados': total_interessados,
        'interessados_matriculados': interessados_matriculados,
        'interessados_sem_matricula': interessados_sem_matricula,
        'cadastros_recentes': cadastros_recentes,
        
        # Distribuições demográficas
        'distribuicao_sexo': distribuicao_sexo,
        'distribuicao_fototipo': distribuicao_fototipo,
        'distribuicao_escolaridade': distribuicao_escolaridade,
        'distribuicao_programas': distribuicao_programas,
        'distribuicao_deficiencia': distribuicao_deficiencia,
        'tipos_deficiencia': tipos_deficiencia,
        'faixas_etarias': faixas_etarias,
        
        # Listas
        'top_interessados_matriculas': top_interessados_matriculas,
        'ultimos_cadastros': ultimos_cadastros,
    }
    
    return render(request, 'admin/dashboard/interessados.html', context)



@staff_member_required
def dashboard_processo_seletivo(request):
    """Dashboard de Processo Seletivo (Inscrições e Classificações)"""
    from apps.selecao.models import Inscricao, Classificacao, StatusInscricao
    from apps.accounts.admin import admin_site
    
    # Métricas de Inscrições
    total_inscricoes = Inscricao.objects.count()
    
    # Inscrições por status
    inscricoes_por_status = Inscricao.objects.values('status__nome').annotate(
        total=Count('id')
    ).order_by('-total')
    
    # Inscrições recentes (últimos 30 dias)
    trinta_dias_atras = date.today() - timedelta(days=30)
    inscricoes_recentes = Inscricao.objects.filter(
        data_inscricao__gte=trinta_dias_atras
    ).count()
    
    # Métricas de Classificação
    total_classificacoes = Classificacao.objects.count()
    classificados = Classificacao.objects.filter(classificado=True).count()
    lista_espera = Classificacao.objects.filter(lista_espera=True).count()
    
    # Top 5 eventos com mais inscrições
    top_eventos_inscricoes = Inscricao.objects.values(
        'evento__nome'
    ).annotate(
        total=Count('id')
    ).order_by('-total')[:5]
    
    # Últimas classificações processadas
    ultimas_classificacoes = Classificacao.objects.select_related(
        'inscricao__interessado',
        'inscricao__evento'
    ).order_by('-processado_em')[:10]
    
    # Taxa de classificação
    taxa_classificacao = (classificados / total_classificacoes * 100) if total_classificacoes > 0 else 0
    
    context = {
        'title': 'Dashboard - Processo Seletivo',
        'site_title': admin_site.site_title,
        'site_header': admin_site.site_header,
        
        'total_inscricoes': total_inscricoes,
        'inscricoes_recentes': inscricoes_recentes,
        'inscricoes_por_status': inscricoes_por_status,
        
        'total_classificacoes': total_classificacoes,
        'classificados': classificados,
        'lista_espera': lista_espera,
        'taxa_classificacao': round(taxa_classificacao, 1),
        
        'top_eventos_inscricoes': top_eventos_inscricoes,
        'ultimas_classificacoes': ultimas_classificacoes,
    }
    
    return render(request, 'admin/dashboard/processo_seletivo.html', context)

@staff_member_required
def dashboard_interessados_pdf(request):
    """Gera PDF do dashboard de interessados"""
    from apps.interessados.models import Interessado
    from django.http import HttpResponse
    from django.db.models import Count
    from .utils_pdf import gerar_pdf_interessados
    from datetime import datetime
    
    # Reutilizar a mesma lógica da view normal
    total_interessados = Interessado.objects.count()
    
    interessados_matriculados = Interessado.objects.filter(
        matriculas__isnull=False
    ).distinct().count()
    
    interessados_sem_matricula = total_interessados - interessados_matriculados
    
    trinta_dias_atras = date.today() - timedelta(days=30)
    cadastros_recentes = Interessado.objects.filter(
        criado_em__gte=trinta_dias_atras
    ).count()
    
    # Distribuição por sexo
    distribuicao_sexo = Interessado.objects.values('sexo__nome').annotate(
        total=Count('id')
    ).order_by('-total')
    
    # Distribuição por fototipo
    distribuicao_fototipo = Interessado.objects.values('fototipo__nome').annotate(
        total=Count('id')
    ).order_by('-total')
    
    # Distribuição por escolaridade
    distribuicao_escolaridade = Interessado.objects.exclude(
        escolaridade=''
    ).values('escolaridade').annotate(
        total=Count('id')
    ).order_by('-total')
    
    escolaridade_labels = {
        'FUNDAMENTAL_INCOMPLETO': 'Fundamental Incompleto',
        'FUNDAMENTAL_COMPLETO': 'Fundamental Completo',
        'MEDIO_INCOMPLETO': 'Médio Incompleto',
        'MEDIO_COMPLETO': 'Médio Completo',
        'SUPERIOR_INCOMPLETO': 'Superior Incompleto',
        'SUPERIOR_COMPLETO': 'Superior Completo',
        'POS_GRADUACAO': 'Pós-Graduação',
    }
    
    for item in distribuicao_escolaridade:
        item['escolaridade_label'] = escolaridade_labels.get(item['escolaridade'], item['escolaridade'])
    
    # Programas sociais
    participa_programas = Interessado.objects.filter(programa_social=True).count()
    nao_participa_programas = total_interessados - participa_programas
    
    distribuicao_programas = [
        {'participa': 'Sim', 'total': participa_programas},
        {'participa': 'Não', 'total': nao_participa_programas}
    ]
    
    # Deficiências
    com_deficiencia = Interessado.objects.filter(necessidades_especiais=True).count()
    sem_deficiencia = total_interessados - com_deficiencia
    
    distribuicao_deficiencia = [
        {'tipo': 'Possui Deficiência', 'total': com_deficiencia},
        {'tipo': 'Não Possui', 'total': sem_deficiencia}
    ]
    
    # Tipos de deficiência
    tipos_deficiencia = []
    deficiencias_map = [
        ('pcd_fisica', 'Física'),
        ('pcd_visual', 'Visual'),
        ('pcd_auditiva', 'Auditiva'),
        ('pcd_intelectual', 'Intelectual'),
        ('pcd_psicossocial', 'Psicossocial'),
        ('pcd_multiplas', 'Múltiplas'),
    ]
    
    for campo, nome in deficiencias_map:
        count = Interessado.objects.filter(**{campo: True}).count()
        if count > 0:
            tipos_deficiencia.append({'tipo_deficiencia': nome, 'total': count})
    
    tipos_deficiencia.sort(key=lambda x: x['total'], reverse=True)
    
    # Faixas etárias
    hoje = date.today()
    faixas_etarias = []
    faixas = [
        (0, 14, '0-14 anos'),
        (15, 19, '15-19 anos'),
        (20, 24, '20-24 anos'),
        (25, 29, '25-29 anos'),
        (30, 34, '30-34 anos'),
        (35, 39, '35-39 anos'),
        (40, 44, '40-44 anos'),
        (45, 49, '45-49 anos'),
        (50, 54, '50-54 anos'),
        (55, 59, '55-59 anos'),
        (60, 999, '60+ anos'),
    ]
    
    for inicio, fim, label in faixas:
        if fim == 999:
            count = Interessado.objects.filter(
                data_nascimento__lte=hoje.replace(year=hoje.year - inicio)
            ).exclude(data_nascimento__isnull=True).count()
        else:
            data_inicio = hoje.replace(year=hoje.year - fim - 1)
            data_fim = hoje.replace(year=hoje.year - inicio)
            count = Interessado.objects.filter(
                data_nascimento__gt=data_inicio,
                data_nascimento__lte=data_fim
            ).count()
        
        if count > 0:
            faixas_etarias.append({'faixa': label, 'total': count})
    
    # Preparar context
    context = {
        'total_interessados': total_interessados,
        'interessados_matriculados': interessados_matriculados,
        'interessados_sem_matricula': interessados_sem_matricula,
        'cadastros_recentes': cadastros_recentes,
        'distribuicao_sexo': list(distribuicao_sexo),
        'distribuicao_fototipo': list(distribuicao_fototipo),
        'distribuicao_escolaridade': list(distribuicao_escolaridade),
        'distribuicao_programas': distribuicao_programas,
        'distribuicao_deficiencia': distribuicao_deficiencia,
        'tipos_deficiencia': tipos_deficiencia,
        'faixas_etarias': faixas_etarias,
    }
    
    # Gerar PDF
    pdf_buffer = gerar_pdf_interessados(context)
    
    # Retornar response
    response = HttpResponse(pdf_buffer, content_type='application/pdf')
    filename = f'dashboard_interessados_{datetime.now().strftime("%Y%m%d_%H%M%S")}.pdf'
    response['Content-Disposition'] = f'attachment; filename="{filename}"'
    
    return response

