
"""
Arquivo: admin.py
Caminho: apps/eventos/admin.py
Alteração: Adicionado exportador de classificação detalhada para Excel/CSV
Data: 10/12/2025
"""

"""
Arquivo: admin.py
Caminho: apps/eventos/admin.py
Alteração: Simplificado para usar ClassificadorService (sem métodos _classificar_inscricao)
Data: 10/12/2025
"""

"""
Arquivo: admin.py
Caminho: apps/eventos/admin.py
Alteração: Campo codigo agora é editável (removido de readonly_fields)
Data: 10/12/2025
"""

"""
Arquivo: admin.py
Caminho: apps/eventos/admin.py
Alteração: EventoCriterio com campo prioridade e CriterioAdmin com tipo_criterio
Data: 09/12/2025
"""

from django.contrib import admin
from django.contrib import messages
from django.http import HttpResponse
from datetime import date
from decimal import Decimal
import csv

from .models import Status, Criterio, Evento, EventoCriterio, Turma, Horario


@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = ['nome', 'cor', 'ordem']
    list_editable = ['ordem']
    ordering = ['ordem']


@admin.register(Criterio)
class CriterioAdmin(admin.ModelAdmin):
    list_display = ['nome', 'tipo_criterio', 'categoria', 'pontos', 'ativo']
    list_filter = ['tipo_criterio', 'categoria', 'ativo']
    list_editable = ['ativo']
    search_fields = ['nome', 'codigo', 'descricao']
    readonly_fields = []
    
    fieldsets = (
        ('IDENTIFICAÇÃO', {
            'fields': ('tipo_criterio', 'codigo', 'nome', 'descricao')
        }),
        ('CLASSIFICAÇÃO', {
            'fields': ('categoria', 'pontos'),
            'description': 'Pontos: obrigatório para tipo PONTUACAO, deixe vazio para ORDENACAO'
        }),
        ('STATUS', {
            'fields': ('ativo',)
        }),
    )
    
    def has_delete_permission(self, request, obj=None):
        """Critérios fixos não podem ser deletados pelo admin"""
        return False


class EventoCriterioInline(admin.TabularInline):
    """
    Inline para vincular critérios ao evento
    """
    model = EventoCriterio
    extra = 1
    fields = ['criterio', 'prioridade', 'pontos_display', 'ativo']
    readonly_fields = ['pontos_display']
    ordering = ['prioridade', '-criterio__pontos']
    
    def pontos_display(self, obj):
        """Mostra os pontos do critério (não editável)"""
        if obj.criterio:
            if obj.criterio.pontos is not None:
                return f'{obj.criterio.pontos} pontos'
            return 'Ordenação'
        return '-'
    pontos_display.short_description = 'Pontuação'
    
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.select_related('criterio')
    
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "criterio":
            kwargs["queryset"] = Criterio.objects.filter(ativo=True)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


class TurmaInline(admin.TabularInline):
    """
    Inline para criar turmas do evento
    """
    model = Turma
    extra = 0
    fields = ['nome', 'turno', 'capacidade', 'local', 'data_inicio', 'data_fim']


@admin.register(Evento)
class EventoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'status', 'total_vagas', 'data_inicio_evento', 'data_fim_evento']
    list_filter = ['status', 'data_inicio_evento']
    search_fields = ['nome', 'descricao']
    actions = ['classificar_inscricoes', 'exportar_classificacao_excel']
    
    fieldsets = (
        ('INFORMAÇÕES BÁSICAS', {
            'fields': ('nome', 'descricao', 'status')
        }),
        ('VAGAS E INSCRIÇÕES', {
            'fields': ('total_vagas', 'data_inicio_inscricao', 'data_fim_inscricao')
        }),
        ('PERÍODO DO EVENTO', {
            'fields': ('data_inicio_evento', 'data_fim_evento')
        }),
    )
    
    inlines = [EventoCriterioInline, TurmaInline]
    
    def classificar_inscricoes(self, request, queryset):
        """
        Action para classificar inscrições dos eventos selecionados
        Delega toda a lógica para o ClassificadorService
        """
        from apps.selecao.services import ClassificadorService
        from apps.selecao.models import Inscricao
        
        total_eventos = 0
        total_inscricoes = 0
        
        for evento in queryset:
            from apps.eventos.models import EventoCriterio
            
            # Verificar se tem critérios ativos
            criterios_ativos = EventoCriterio.objects.filter(
                evento=evento,
                ativo=True
            )
            
            if not criterios_ativos.exists():
                messages.warning(
                    request,
                    f'⚠️ Evento "{evento.nome}" não possui critérios ativos!'
                )
                continue
            
            # Contar inscrições para feedback
            inscricoes_count = Inscricao.objects.filter(evento=evento).count()
            
            if inscricoes_count == 0:
                messages.warning(
                    request,
                    f'⚠️ Evento "{evento.nome}" não possui inscrições!'
                )
                continue
            
            # Classificar usando o service
            try:
                ClassificadorService.classificar_evento(evento)
                total_eventos += 1
                total_inscricoes += inscricoes_count
                
                messages.success(
                    request,
                    f'✅ Evento "{evento.nome}": {inscricoes_count} inscrição(ões) classificada(s)!'
                )
            except Exception as e:
                messages.error(
                    request,
                    f'❌ Erro ao classificar "{evento.nome}": {str(e)}'
                )
        
        if total_eventos > 0:
            messages.success(
                request,
                f'🎯 TOTAL: {total_eventos} evento(s) processado(s), {total_inscricoes} inscrição(ões) classificada(s)!'
            )
    
    classificar_inscricoes.short_description = '🎯 Classificar inscrições dos eventos selecionados'
    
    def exportar_classificacao_excel(self, request, queryset):
        """
        Exporta classificação detalhada para CSV/Excel
        Inclui: pontuação calculada vs salva, critérios atendidos, dados pessoais
        """
        from apps.selecao.models import Classificacao, InscricaoCriterioAtendido
        
        # Criar resposta HTTP com CSV
        response = HttpResponse(content_type='text/csv; charset=utf-8-sig')
        response['Content-Disposition'] = 'attachment; filename="classificacao_detalhada.csv"'
        
        # Adicionar BOM para Excel reconhecer UTF-8
        response.write('\ufeff')
        
        writer = csv.writer(response, delimiter=';')
        
        # Cabeçalho
        writer.writerow([
            'Evento',
            'Posição',
            'Nome',
            'CPF',
            'Data Nascimento',
            'Idade',
            'Status Inscrição',
            'Critérios Atendidos',
            'Pontuação Calculada',
            'Pontuação Salva',
            'Diferença',
            'Classificado',
            'Detalhes Critérios'
        ])
        
        for evento in queryset:
            classificacoes = Classificacao.objects.filter(
                inscricao__evento=evento
            ).select_related(
                'inscricao__interessado',
                'inscricao__status'
            ).order_by('posicao')
            
            hoje = date.today()
            
            for c in classificacoes:
                interessado = c.inscricao.interessado
                
                # Calcular idade
                dn = interessado.data_nascimento
                idade = hoje.year - dn.year - ((hoje.month, hoje.day) < (dn.month, dn.day))
                
                # Buscar critérios atendidos
                criterios_atendidos = InscricaoCriterioAtendido.objects.filter(
                    inscricao=c.inscricao
                ).select_related('criterio')
                
                # Calcular pontuação manualmente
                pontuacao_calculada = sum(
                    ca.pontos_atribuidos for ca in criterios_atendidos
                )
                
                # Pontuação salva
                pontuacao_salva = c.pontuacao_total
                
                # Diferença
                diferenca = Decimal(str(pontuacao_calculada)) - pontuacao_salva
                
                # Detalhes dos critérios
                detalhes_criterios = ' | '.join([
                    f"{ca.criterio.nome}: {ca.pontos_atribuidos} pts"
                    for ca in criterios_atendidos
                ]) if criterios_atendidos.exists() else 'Nenhum'
                
                # Nome dos critérios
                nomes_criterios = ', '.join([
                    ca.criterio.nome for ca in criterios_atendidos
                ]) if criterios_atendidos.exists() else 'Nenhum'
                
                writer.writerow([
                    evento.nome,
                    c.posicao or 'N/A',
                    interessado.nome,
                    interessado.cpf,
                    dn.strftime('%d/%m/%Y'),
                    idade,
                    c.inscricao.status.nome,
                    nomes_criterios,
                    f'{pontuacao_calculada:.2f}',
                    f'{pontuacao_salva:.2f}',
                    f'{diferenca:.2f}',
                    'Sim' if c.classificado else 'Não',
                    detalhes_criterios
                ])
        
        messages.success(request, '✅ Classificação exportada com sucesso!')
        return response
    
    exportar_classificacao_excel.short_description = '📊 Exportar classificação detalhada (Excel)'


@admin.register(Turma)
class TurmaAdmin(admin.ModelAdmin):
    list_display = ['nome', 'evento', 'turno', 'capacidade', 'data_inicio', 'data_fim']
    list_filter = ['evento', 'turno']
    search_fields = ['nome', 'evento__nome']


@admin.register(Horario)
class HorarioAdmin(admin.ModelAdmin):
    list_display = ['turma', 'dia_semana_display', 'hora_inicio', 'hora_fim']
    list_filter = ['turma', 'dia_semana']
    
    def dia_semana_display(self, obj):
        return obj.get_dia_semana_display()
    dia_semana_display.short_description = 'Dia da Semana'


