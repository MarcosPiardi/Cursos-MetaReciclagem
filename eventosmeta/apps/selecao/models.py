

"""
Models do app SELEÇÃO
Responsável por: Processo seletivo, inscrições, classificação
"""
from django.db import models
from django.core.validators import MinValueValidator
from django.utils import timezone

from apps.eventos.models import Evento, Criterio
from apps.interessados.models import Interessado


class StatusInscricao(models.Model):
    """Status de Inscrições (Pendente, Confirmada, Cancelada, etc.)"""
    
    nome = models.CharField(max_length=50, unique=True)
    cor = models.CharField(
        max_length=7,
        default='#6c757d',
        help_text="Código hexadecimal da cor (ex: #28a745)"
    )
    ordem = models.PositiveIntegerField(default=0)
    
    class Meta:
        verbose_name = "Status de Inscrição"
        verbose_name_plural = "Status de Inscrições"
        ordering = ['ordem', 'nome']
    
    def __str__(self):
        return self.nome


class Inscricao(models.Model):
    """Inscrições de interessados em eventos"""
    
    interessado = models.ForeignKey(
        Interessado,
        on_delete=models.PROTECT,
        related_name='inscricoes'
    )
    evento = models.ForeignKey(
        Evento,
        on_delete=models.PROTECT,
        related_name='inscricoes'
    )
    status = models.ForeignKey(
        StatusInscricao,
        on_delete=models.PROTECT,
        related_name='inscricoes'
    )
    
    # Datas
    data_inscricao = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)
    
    # Observações
    observacoes = models.TextField(blank=True)
    
    class Meta:
        verbose_name = "Inscrição"
        verbose_name_plural = "Inscrições"
        unique_together = ['interessado', 'evento']
        ordering = ['-data_inscricao']
    
    def __str__(self):
        return f"{self.interessado.nome} → {self.evento.nome}"


class Classificacao(models.Model):
    """Classificação final dos inscritos (READ-ONLY para staff)"""
    
    inscricao = models.OneToOneField(
        Inscricao,
        on_delete=models.CASCADE,
        related_name='classificacao'
    )
    
    # ========================================================================
    # ALTERAÇÃO: Campo 'posicao' agora permite NULL
    # MOTIVO: A posição é atribuída apenas após o processamento completo
    #         da classificação. Durante o cálculo de pontos, o registro
    #         é criado sem posição definida.
    # ========================================================================
    posicao = models.PositiveIntegerField(
        null=True,      # ← ADICIONADO: Permite valores nulos
        blank=True      # ← ADICIONADO: Permite campo vazio no admin
    )
    
    pontuacao_total = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0)]
    )
    classificado = models.BooleanField(
        default=False,
        help_text="Se foi classificado dentro das vagas disponíveis"
    )
    lista_espera = models.BooleanField(
        default=False,
        help_text="Se está na lista de espera"
    )
    
    # Auditoria
    processado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Classificação"
        verbose_name_plural = "Classificações"
        unique_together = ['inscricao']
        ordering = ['inscricao__evento', 'posicao']
    
    def __str__(self):
        return f"{self.posicao}º - {self.inscricao.interessado.nome} ({self.pontuacao_total} pts)"


class InscricaoCriterioAtendido(models.Model):
    """
    Critérios atendidos por cada inscrição (READ-ONLY - apenas auditoria)
    Gerado automaticamente pelo ClassificadorService
    """
    
    inscricao = models.ForeignKey(
        Inscricao,
        on_delete=models.CASCADE,
        related_name='criterios_atendidos'
    )
    criterio = models.ForeignKey(
        Criterio,
        on_delete=models.PROTECT,
        related_name='inscricoes_atendidas'
    )
    pontos_atribuidos = models.PositiveIntegerField()
    validado = models.BooleanField(
        default=False,
        help_text="Indica se critério customizado foi validado manualmente"
    )
    observacao_validacao = models.TextField(blank=True)
    
    class Meta:
        verbose_name = "Critério Atendido"
        verbose_name_plural = "Critérios Atendidos"
        unique_together = ['inscricao', 'criterio']
        ordering = ['inscricao', '-pontos_atribuidos']
    
    def __str__(self):
        return f"{self.inscricao.interessado.nome} - {self.criterio.nome} ({self.pontos_atribuidos} pts)"
    
    