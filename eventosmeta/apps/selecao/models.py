"""
Arquivo: models.py
Caminho: apps/selecao/models.py
Finalidade: Definir os modelos do app seleção.

Histórico de Alterações:
- 15/05/2026 - Inclusão de cabeçalho  
- 18/05/2026 - Adição de validadores (MaxValueValidator) e 
               método clean() para validar pontuação e exclusividade mútua de flags
"""

from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone
from django.core.exceptions import ValidationError

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
    # data_inscricao = models.DateTimeField(auto_now_add=True)   mudança por recomendação do Claude para evitar problemas de timezone em 23/06/2026
    data_inscricao = models.DateTimeField(default=timezone.now, editable=False)
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
        default=1,
        null=True,
        blank=True
    )
    
    pontuacao_total = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0), MaxValueValidator(100)]  # ← ALTERAÇÃO 18/05/2026
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
    
    def clean(self):
        """
        Valida regras de negócio da classificação.
        
        Alteração: 18/05/2026 - Implementação de validações
        - Pontuação total deve estar entre 0 e 100
        - Classificado e lista_espera são mutuamente exclusivos
        """
        errors = {}
        
        # Validação 1: Pontuação entre 0 e 100
        if self.pontuacao_total is not None:
            if self.pontuacao_total < 0 or self.pontuacao_total > 100:
                errors['pontuacao_total'] = 'Pontuação deve estar entre 0 e 100.'
        
        # Validação 2: Classificado e lista_espera são mutuamente exclusivos
        if self.classificado and self.lista_espera:
            errors['classificado'] = 'Não é possível estar classificado E na lista de espera simultaneamente.'
            errors['lista_espera'] = 'Não é possível estar classificado E na lista de espera simultaneamente.'
        
        if errors:
            raise ValidationError(errors)
    
    def save(self, *args, **kwargs):
        """
        Sobrescreve save() para chamar validação clean() antes de salvar.
        
        Alteração: 18/05/2026 - Adição de chamada a clean()
        """
        self.clean()
        super().save(*args, **kwargs)
    
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
    
    