"""
Arquivo: services.py
Caminho: apps/dashboard/services.py
Finalidade: Serviços de classificação para o app dashboard.

Atualizações:
 - 10/06/2026 - Criação do arquivo - Implementação inicial dos serviços de dashboard
 - 11/06/2026 - Correção de lógica de faixas etárias com relativedelta, proteção contra divisão por zero, docstrings
 """


from datetime import date
from dateutil.relativedelta import relativedelta
from django.db.models import Count, Avg
from django.utils import timezone


class DashboardInteressadosService:
    """Serviço de cálculos demográficos de interessados."""
    
    @staticmethod
    def calcular_metricas_gerais():
        from apps.interessados.models import Interessado
        total = Interessado.objects.count()
        matriculados = Interessado.objects.filter(matriculas__isnull=False).distinct().count()
        return {
            'total_interessados': total,
            'interessados_matriculados': matriculados,
            'interessados_sem_matricula': total - matriculados,
        }
    
    @staticmethod
    def calcular_distribuicao_sexo():
        from apps.interessados.models import Interessado
        total = Interessado.objects.count()
        distribuicao = Interessado.objects.values('sexo__nome').annotate(
            total=Count('id')
        ).order_by('-total')
        
        for item in distribuicao:
            item['percentual'] = round((item['total'] / total * 100), 1) if total > 0 else 0
        
        return list(distribuicao)
    
    @staticmethod
    def calcular_distribuicao_fototipo():
        from apps.interessados.models import Interessado
        total = Interessado.objects.count()
        distribuicao = Interessado.objects.values('fototipo__nome').annotate(
            total=Count('id')
        ).order_by('-total')
        
        for item in distribuicao:
            item['percentual'] = round((item['total'] / total * 100), 1) if total > 0 else 0
        
        return list(distribuicao)
    
    @staticmethod
    def calcular_distribuicao_escolaridade():
        from apps.interessados.models import Interessado
        
        escolaridade_labels = {
            'FUNDAMENTAL_INCOMPLETO': 'Fundamental Incompleto',
            'FUNDAMENTAL_COMPLETO': 'Fundamental Completo',
            'MEDIO_INCOMPLETO': 'Médio Incompleto',
            'MEDIO_COMPLETO': 'Médio Completo',
            'SUPERIOR_INCOMPLETO': 'Superior Incompleto',
            'SUPERIOR_COMPLETO': 'Superior Completo',
            'POS_GRADUACAO': 'Pós-Graduação',
        }
        
        distribuicao = Interessado.objects.exclude(
            escolaridade=''
        ).values('escolaridade').annotate(
            total=Count('id')
        ).order_by('-total')
        
        for item in distribuicao:
            item['escolaridade_label'] = escolaridade_labels.get(item['escolaridade'], item['escolaridade'])
        
        return list(distribuicao)
    
    @staticmethod
    def calcular_distribuicao_programas_sociais():
        from apps.interessados.models import Interessado
        total = Interessado.objects.count()
        if total == 0:
            return []
        
        participa = Interessado.objects.filter(programa_social=True).count()
        nao_participa = total - participa
        
        return [
            {
                'participa': 'Sim',
                'total': participa,
                'percentual': round((participa / total * 100), 1)
            },
            {
                'participa': 'Não',
                'total': nao_participa,
                'percentual': round((nao_participa / total * 100), 1)
            }
        ]
    
    @staticmethod
    def calcular_distribuicao_deficiencias():
        from apps.interessados.models import Interessado
        total = Interessado.objects.count()
        if total == 0:
            return []
        
        com_deficiencia = Interessado.objects.filter(necessidades_especiais=True).count()
        sem_deficiencia = total - com_deficiencia
        
        return [
            {
                'tipo': 'Possui Deficiência',
                'total': com_deficiencia,
                'percentual': round((com_deficiencia / total * 100), 1)
            },
            {
                'tipo': 'Não Possui',
                'total': sem_deficiencia,
                'percentual': round((sem_deficiencia / total * 100), 1)
            }
        ]
    
    @staticmethod
    def calcular_tipos_deficiencia():
        from apps.interessados.models import Interessado
        
        deficiencias_map = [
            ('pcd_fisica', 'Física'),
            ('pcd_visual', 'Visual'),
            ('pcd_auditiva', 'Auditiva'),
            ('pcd_intelectual', 'Intelectual'),
            ('pcd_psicossocial', 'Psicossocial'),
            ('pcd_multiplas', 'Múltiplas'),
        ]
        
        tipos = []
        for campo, nome in deficiencias_map:
            count = Interessado.objects.filter(**{campo: True}).count()
            if count > 0:
                tipos.append({
                    'tipo_deficiencia': nome,
                    'total': count
                })
        
        tipos.sort(key=lambda x: x['total'], reverse=True)
        return tipos
    
    @staticmethod
    def calcular_faixas_etarias():
        from apps.interessados.models import Interessado
        
        hoje = date.today()
        total = Interessado.objects.count()
        if total == 0:
            return []
        
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
        
        faixas_etarias = []
        for inicio, fim, label in faixas:
            if fim == 999:
                data_limite = hoje - relativedelta(years=inicio)
                count = Interessado.objects.filter(
                    data_nascimento__lte=data_limite
                ).exclude(data_nascimento__isnull=True).count()
            else:
                data_inicio = hoje - relativedelta(years=fim + 1)
                data_fim = hoje - relativedelta(years=inicio)
                count = Interessado.objects.filter(
                    data_nascimento__gt=data_inicio,
                    data_nascimento__lte=data_fim
                ).count()
            
            if count > 0:
                faixas_etarias.append({
                    'faixa': label,
                    'total': count,
                    'percentual': round((count / total * 100), 1)
                })
        
        return faixas_etarias
    
    @staticmethod
    def obter_contexto_completo():
        return {
            **DashboardInteressadosService.calcular_metricas_gerais(),
            'distribuicao_sexo': DashboardInteressadosService.calcular_distribuicao_sexo(),
            'distribuicao_fototipo': DashboardInteressadosService.calcular_distribuicao_fototipo(),
            'distribuicao_escolaridade': DashboardInteressadosService.calcular_distribuicao_escolaridade(),
            'distribuicao_programas': DashboardInteressadosService.calcular_distribuicao_programas_sociais(),
            'distribuicao_deficiencia': DashboardInteressadosService.calcular_distribuicao_deficiencias(),
            'tipos_deficiencia': DashboardInteressadosService.calcular_tipos_deficiencia(),
            'faixas_etarias': DashboardInteressadosService.calcular_faixas_etarias(),
        }


class DashboardEventosService:
    """Serviço de cálculos de eventos e turmas."""
    
    @staticmethod
    def calcular_metricas_gerais():
        from apps.eventos.models import Evento, Turma
        
        return {
            'total_eventos': Evento.objects.count(),
            'total_turmas': Turma.objects.count(),
            'eventos_inscricoes_abertas': Evento.objects.filter(
                data_inicio_inscricao__lte=timezone.now(),
                data_fim_inscricao__gte=timezone.now()
            ).count(),
        }
    
    @staticmethod
    def calcular_turmas_por_status():
        from apps.eventos.models import Turma
        
        hoje = date.today()
        return {
            'turmas_futuras': Turma.objects.filter(data_inicio__gt=hoje).count(),
            'turmas_em_andamento': Turma.objects.filter(
                data_inicio__lte=hoje,
                data_fim__gte=hoje
            ).count(),
            'turmas_encerradas': Turma.objects.filter(data_fim__lt=hoje).count(),
        }
    
    @staticmethod
    def calcular_eventos_por_status():
        from apps.eventos.models import Evento
        
        return list(Evento.objects.values('status__nome').annotate(
            total=Count('id')
        ).order_by('-total'))
    
    @staticmethod
    def calcular_top_eventos_inscricoes(limit=5):
        from apps.selecao.models import Inscricao
        
        return list(Inscricao.objects.values(
            'evento__nome'
        ).annotate(
            total_inscricoes=Count('id')
        ).order_by('-total_inscricoes')[:limit])
    
    @staticmethod
    def obter_contexto_completo():
        return {
            **DashboardEventosService.calcular_metricas_gerais(),
            **DashboardEventosService.calcular_turmas_por_status(),
            'eventos_por_status': DashboardEventosService.calcular_eventos_por_status(),
            'top_eventos_inscricoes': DashboardEventosService.calcular_top_eventos_inscricoes(),
        }


class DashboardAcademicoService:
    """Serviço de cálculos acadêmicos."""
    
    @staticmethod
    def calcular_metricas_avaliacoes():
        from apps.academico.models import Avaliacao
        
        total = Avaliacao.objects.count()
        if total == 0:
            return {
                'total_avaliacoes': 0,
                'total_aprovados': 0,
                'total_reprovados': 0,
                'media_notas': 0,
                'media_frequencia': 0,
                'certificados_emitidos': 0,
            }
        
        aprovados = Avaliacao.objects.filter(aprovado=True).count()
        
        return {
            'total_avaliacoes': total,
            'total_aprovados': aprovados,
            'total_reprovados': total - aprovados,
            'media_notas': round(Avaliacao.objects.aggregate(Avg('nota_final'))['nota_final__avg'] or 0, 2),
            'media_frequencia': round(Avaliacao.objects.aggregate(Avg('frequencia'))['frequencia__avg'] or 0, 1),
            'certificados_emitidos': Avaliacao.objects.filter(certificado_emitido=True).count(),
        }
    
    @staticmethod
    def calcular_taxa_aprovacao():
        from apps.academico.models import Avaliacao
        
        total = Avaliacao.objects.count()
        if total == 0:
            return 0
        
        aprovados = Avaliacao.objects.filter(aprovado=True).count()
        return round((aprovados / total * 100), 1)
    
    @staticmethod
    def calcular_top_cursos_aprovados(limit=5):
        from apps.academico.models import Avaliacao
        
        return list(Avaliacao.objects.filter(aprovado=True).values(
            'matricula__turma__evento__nome'
        ).annotate(
            total=Count('id')
        ).order_by('-total')[:limit])
    
    @staticmethod
    def obter_contexto_completo():
        metricas = DashboardAcademicoService.calcular_metricas_avaliacoes()
        return {
            **metricas,
            'taxa_aprovacao': DashboardAcademicoService.calcular_taxa_aprovacao(),
            'top_cursos_aprovados': DashboardAcademicoService.calcular_top_cursos_aprovados(),
        }


class DashboardProcessoSeletivoService:
    """Serviço de cálculos de processo seletivo."""
    
    @staticmethod
    def calcular_metricas_inscricoes():
        from django.utils import timezone
        from datetime import timedelta
        from apps.selecao.models import Inscricao    
        total = Inscricao.objects.count()
        trinta_dias_atras = timezone.now() - timedelta(days=30)
        return {
            'total_inscricoes': total,
            'inscricoes_recentes': Inscricao.objects.filter(
            data_inscricao__gte=trinta_dias_atras
            ).count(),
        }



        # from apps.selecao.models import Inscricao
        # from datetime import timedelta
        
        # total = Inscricao.objects.count()
        # trinta_dias_atras = date.today() - timedelta(days=30)
        
        # return {
        #     'total_inscricoes': total,
        #     'inscricoes_recentes': Inscricao.objects.filter(
        #         data_inscricao__gte=trinta_dias_atras
        #     ).count(),
        # }
    
    @staticmethod
    def calcular_metricas_classificacoes():
        from apps.selecao.models import Classificacao
        
        total = Classificacao.objects.count()
        if total == 0:
            return {
                'total_classificacoes': 0,
                'classificados': 0,
                'lista_espera': 0,
                'taxa_classificacao': 0,
            }
        
        classificados = Classificacao.objects.filter(classificado=True).count()
        lista_espera = Classificacao.objects.filter(lista_espera=True).count()
        
        return {
            'total_classificacoes': total,
            'classificados': classificados,
            'lista_espera': lista_espera,
            'taxa_classificacao': round((classificados / total * 100), 1),
        }
    
    @staticmethod
    def calcular_top_eventos_inscricoes(limit=5):
        from apps.selecao.models import Inscricao
        
        return list(Inscricao.objects.values(
            'evento__nome'
        ).annotate(
            total_inscricoes=Count('id')
        ).order_by('-total_inscricoes')[:limit])
    
    @staticmethod
    def obter_contexto_completo():
        return {
            **DashboardProcessoSeletivoService.calcular_metricas_inscricoes(),
            **DashboardProcessoSeletivoService.calcular_metricas_classificacoes(),
            'top_eventos_inscricoes': DashboardProcessoSeletivoService.calcular_top_eventos_inscricoes(),
        }
    

    

