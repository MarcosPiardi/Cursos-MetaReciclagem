

"""
Models do app ACADÊMICO
Responsável por: Matrículas, avaliações, execução do curso
"""
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from decimal import Decimal

from apps.eventos.models import Turma
from apps.interessados.models import Interessado
from apps.selecao.models import Inscricao


class StatusMatricula(models.Model):
    """Status de Matrículas (Ativa, Trancada, Concluída, etc.)"""
    
    nome = models.CharField(max_length=50, unique=True)
    cor = models.CharField(
        max_length=7,
        default='#6c757d',
        help_text="Código hexadecimal da cor (ex: #007bff)"
    )
    ordem = models.PositiveIntegerField(default=0)
    
    class Meta:
        verbose_name = "Status de Matrícula"
        verbose_name_plural = "Status de Matrículas"
        ordering = ['ordem', 'nome']
    
    def __str__(self):
        return self.nome


class Matricula(models.Model):
    """Matrículas de alunos em turmas (criada manualmente pelo staff)"""
    
    turma = models.ForeignKey(
        Turma,
        on_delete=models.PROTECT,
        related_name='matriculas'
    )
    interessado = models.ForeignKey(
        Interessado,
        on_delete=models.PROTECT,
        related_name='matriculas'
    )
    inscricao = models.ForeignKey(
        Inscricao,
        on_delete=models.PROTECT,
        related_name='matriculas',
        help_text="Inscrição que originou esta matrícula"
    )
    status = models.ForeignKey(
        StatusMatricula,
        on_delete=models.PROTECT,
        related_name='matriculas'
    )
    
    # Datas
    data_matricula = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)
    
    # Observações
    observacoes = models.TextField(blank=True)
    
    class Meta:
        verbose_name = "Matrícula"
        verbose_name_plural = "Matrículas"
        unique_together = ['turma', 'interessado']
        ordering = ['-data_matricula']
    
    def __str__(self):
        return f"{self.interessado.nome} → {self.turma.nome}"


class Avaliacao(models.Model):
    """Avaliações finais dos alunos matriculados"""
    
    matricula = models.OneToOneField(
        Matricula,
        on_delete=models.CASCADE,
        related_name='avaliacao'
    )
    
    # Desempenho
    nota_final = models.DecimalField(
        max_digits=4,
        decimal_places=2,
        validators=[MinValueValidator(Decimal('0.00')), MaxValueValidator(Decimal('10.00'))],
        blank=True,
        null=True,
        help_text="Nota de 0 a 10"
    )
    frequencia = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        validators=[MinValueValidator(Decimal('0.00')), MaxValueValidator(Decimal('100.00'))],
        help_text="Percentual de presença (%)"
    )
    
    # Resultado
    aprovado = models.BooleanField(default=False)
    observacoes = models.TextField(blank=True)
    
    # Certificado
    certificado_emitido = models.BooleanField(default=False)
    data_emissao_certificado = models.DateField(blank=True, null=True)
    
    # Auditoria
    avaliado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Avaliação"
        verbose_name_plural = "Avaliações"
        ordering = ['-avaliado_em']
    
    def __str__(self):
        status = "Aprovado" if self.aprovado else "Reprovado"
        return f"{self.matricula.interessado.nome} - {status}"
    
    