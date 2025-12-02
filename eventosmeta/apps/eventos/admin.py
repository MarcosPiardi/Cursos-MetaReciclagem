"""
Admin do app EVENTOS - Modelo Simplificado
"""
from django.contrib import admin
from django.contrib import messages
from django.db import transaction
from datetime import date
from .models import Status, Criterio, Evento, EventoCriterio, Turma, Horario


@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = ['nome', 'cor', 'ordem']
    list_editable = ['ordem']
    ordering = ['ordem']


@admin.register(Criterio)
class CriterioAdmin(admin.ModelAdmin):
    list_display = ['nome', 'categoria', 'pontos', 'ativo']
    list_filter = ['categoria', 'ativo']
    list_editable = ['ativo']
    search_fields = ['nome', 'codigo', 'descricao']
    readonly_fields = ['codigo', 'pontos']
    
    fieldsets = (
        ('IDENTIFICAÇÃO', {
            'fields': ('codigo', 'nome', 'descricao')
        }),
        ('CLASSIFICAÇÃO', {
            'fields': ('categoria', 'pontos')
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
    fields = ['criterio', 'pontos_display', 'ativo']
    readonly_fields = ['pontos_display']
    
    def pontos_display(self, obj):
        """Mostra os pontos do critério (não editável)"""
        if obj.criterio:
            return f'{obj.criterio.pontos} pontos'
        return '-'
    pontos_display.short_description = 'Pontuação'
    
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.select_related('criterio')


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
    actions = ['classificar_inscricoes']
    
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
        """
        from apps.selecao.models import Inscricao, Classificacao, InscricaoCriterioAtendido, StatusInscricao
        
        total_eventos = 0
        total_classificados = 0
        
        for evento in queryset:
            # Buscar critérios ativos
            criterios_ativos = EventoCriterio.objects.filter(
                evento=evento,
                ativo=True
            ).select_related('criterio')
            
            if not criterios_ativos.exists():
                messages.warning(
                    request,
                    f'⚠️ Evento "{evento.nome}" não possui critérios ativos!'
                )
                continue
            
            # Buscar status "CONFIRMADA" (ou similar)
            try:
                status_confirmada = StatusInscricao.objects.get(nome__iexact='CONFIRMADA')
            except StatusInscricao.DoesNotExist:
                # Tentar variações
                try:
                    status_confirmada = StatusInscricao.objects.get(nome__icontains='CONFIRM')
                except StatusInscricao.DoesNotExist:
                    messages.error(
                        request,
                        f'❌ Status "CONFIRMADA" não encontrado! Crie um StatusInscricao com esse nome.'
                    )
                    continue
            
            # Buscar inscrições confirmadas
            inscricoes = Inscricao.objects.filter(
                evento=evento,
                status=status_confirmada
            ).select_related('interessado')
            
            if not inscricoes.exists():
                messages.warning(
                    request,
                    f'⚠️ Evento "{evento.nome}" não possui inscrições confirmadas!'
                )
                continue
            
            # Classificar cada inscrição
            for inscricao in inscricoes:
                try:
                    with transaction.atomic():
                        resultado = self._classificar_inscricao(inscricao, criterios_ativos)
                        self._salvar_classificacao(inscricao, resultado)
                        total_classificados += 1
                except Exception as e:
                    messages.error(
                        request,
                        f'❌ Erro ao classificar {inscricao.interessado.nome}: {str(e)}'
                    )
            
            # Atualizar posições
            self._atualizar_posicoes(evento, criterios_ativos, status_confirmada)
            total_eventos += 1
            
            messages.success(
                request,
                f'✅ Evento "{evento.nome}": {inscricoes.count()} inscrições classificadas!'
            )
        
        if total_eventos > 0:
            messages.success(
                request,
                f'🎯 TOTAL: {total_eventos} evento(s) processado(s), {total_classificados} inscrição(ões) classificada(s)!'
            )
    
    classificar_inscricoes.short_description = '🎯 Classificar inscrições dos eventos selecionados'
    
    def _classificar_inscricao(self, inscricao, criterios_ativos):
        """Calcula pontuação de uma inscrição"""
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
            atendido = False
            observacao = ''
            
            # PCD
            if criterio.codigo == 'PCD':
                if interessado.tem_deficiencia:
                    atendido = True
                    observacao = f'PCD: {interessado.tipo_deficiencia or "Sim"}'
            
            # NIS
            elif criterio.codigo == 'NIS':
                if interessado.num_nis:
                    atendido = True
                    observacao = f'NIS: {interessado.num_nis}'
            
            # JOVEM
            elif criterio.codigo == 'JOVEM':
                if 16 <= idade <= 24:
                    atendido = True
                    observacao = f'Idade: {idade} anos'
            
            # IDOSO
            elif criterio.codigo == 'IDOSO':
                if idade >= 50:
                    atendido = True
                    observacao = f'Idade: {idade} anos'
            
            # COTA RACIAL
            elif criterio.codigo == 'COTA_RACIAL':
                racas_cotistas = ['PRETO', 'PARDO', 'INDIGENA']
                if interessado.fototipo and interessado.fototipo.upper() in racas_cotistas:
                    atendido = True
                    observacao = f'Raça/Cor: {interessado.get_fototipo_display()}'
            
            # ESCOLARIDADE
            elif criterio.codigo == 'ESC_FUND_INC':
                if interessado.escolaridade == 'FUNDAMENTAL_INCOMPLETO':
                    atendido = True
                    observacao = 'Ens. Fundamental Incompleto'
            
            elif criterio.codigo == 'ESC_FUND_COMP':
                if interessado.escolaridade == 'FUNDAMENTAL_COMPLETO':
                    atendido = True
                    observacao = 'Ens. Fundamental Completo'
            
            elif criterio.codigo == 'ESC_MEDIO_INC':
                if interessado.escolaridade == 'MEDIO_INCOMPLETO':
                    atendido = True
                    observacao = 'Ens. Médio Incompleto'
            
            elif criterio.codigo == 'ESC_MEDIO_COMP':
                if interessado.escolaridade == 'MEDIO_COMPLETO':
                    atendido = True
                    observacao = 'Ens. Médio Completo'
            
            if atendido:
                pontuacao_total += criterio.pontos
                criterios_atendidos.append({
                    'criterio': criterio,
                    'pontos': criterio.pontos,
                    'observacao': observacao
                })
        
        return {
            'pontuacao': pontuacao_total,
            'criterios_atendidos': criterios_atendidos,
            'idade': idade
        }
    
    def _salvar_classificacao(self, inscricao, resultado):
        """Salva a classificação no banco"""
        from apps.selecao.models import Classificacao, InscricaoCriterioAtendido
        
        classificacao, _ = Classificacao.objects.update_or_create(
            inscricao=inscricao,
            defaults={
                'pontuacao_total': resultado['pontuacao'],
                'classificado': False,  # Será atualizado depois
                'lista_espera': False
            }
        )
        
        InscricaoCriterioAtendido.objects.filter(inscricao=inscricao).delete()
        
        for crit in resultado['criterios_atendidos']:
            InscricaoCriterioAtendido.objects.create(
                inscricao=inscricao,
                criterio=crit['criterio'],
                pontos_atribuidos=crit['pontos'],
                observacao_validacao=crit['observacao']
            )
        
        return classificacao
    
    def _atualizar_posicoes(self, evento, criterios_ativos, status_confirmada):
        """Atualiza posições de classificação"""
        from apps.selecao.models import Classificacao
        
        tem_jovem = criterios_ativos.filter(criterio__codigo='JOVEM').exists()
        tem_idoso = criterios_ativos.filter(criterio__codigo='IDOSO').exists()
        
        classificacoes = Classificacao.objects.filter(
            inscricao__evento=evento,
            inscricao__status=status_confirmada
        ).select_related('inscricao', 'inscricao__interessado')
        
        classificacoes_list = list(classificacoes)
        hoje = date.today()
        
        for c in classificacoes_list:
            dn = c.inscricao.interessado.data_nascimento
            c.idade_calc = (
                hoje.year - dn.year -
                ((hoje.month, hoje.day) < (dn.month, dn.day))
            )
        
        if tem_jovem:
            classificacoes_list.sort(
                key=lambda x: (-x.pontuacao_total, x.idade_calc, x.inscricao.data_inscricao)
            )
        elif tem_idoso:
            classificacoes_list.sort(
                key=lambda x: (-x.pontuacao_total, -x.idade_calc, x.inscricao.data_inscricao)
            )
        else:
            classificacoes_list.sort(
                key=lambda x: (-x.pontuacao_total, x.inscricao.data_inscricao)
            )
        
        # Atualizar posições e flags classificado/lista_espera
        total_vagas = evento.total_vagas
        
        for posicao, classificacao in enumerate(classificacoes_list, start=1):
            classificacao.posicao = posicao
            classificacao.classificado = (posicao <= total_vagas)
            classificacao.lista_espera = (posicao > total_vagas)
            classificacao.save(update_fields=['posicao', 'classificado', 'lista_espera'])


@admin.register(EventoCriterio)
class EventoCriterioAdmin(admin.ModelAdmin):
    """
    Admin separado para visualizar todos os vínculos evento-critério
    """
    list_display = ['evento', 'criterio', 'pontos', 'ativo']
    list_filter = ['evento', 'ativo', 'criterio__categoria']
    list_editable = ['ativo']
    ordering = ['evento', '-criterio__pontos']


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
    