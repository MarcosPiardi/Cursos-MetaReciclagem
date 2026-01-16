"""
Models do app ACADÊMICO
Arquivo: apps/academico/models.py
Alteração: Adicionado numero_matricula auto-gerado (formato AAAANNN)
Data: 14/01/2026

Responsável por: Matrículas, avaliações, execução do curso
"""
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone
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
    """Matrículas de alunos em turmas"""
    
    # 🆕 NOVO: Número de matrícula único e auto-gerado
    numero_matricula = models.CharField(
        max_length=10,
        unique=True,
        editable=False,
        verbose_name='Nº Matrícula',
        help_text='Gerado automaticamente no formato AAAANNN (ex: 2026001)'
    )
    
    turma = models.ForeignKey(
        Turma,
        on_delete=models.PROTECT,
        related_name='matriculas',
        verbose_name='Turma'
    )
    interessado = models.ForeignKey(
        Interessado,
        on_delete=models.PROTECT,
        related_name='matriculas',
        verbose_name='Interessado'
    )
    inscricao = models.ForeignKey(
        Inscricao,
        on_delete=models.PROTECT,
        related_name='matriculas',
        verbose_name='Inscrição',
        help_text="Inscrição que originou esta matrícula"
    )
    status = models.ForeignKey(
        StatusMatricula,
        on_delete=models.PROTECT,
        related_name='matriculas',
        verbose_name='Status'
    )
    
    # Datas
    data_matricula = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Data da Matrícula'
    )
    data_atualizacao = models.DateTimeField(
        auto_now=True,
        verbose_name='Última Atualização'
    )
    
    # Observações
    observacoes = models.TextField(
        blank=True,
        verbose_name='Observações/Anotações'
    )
    
    class Meta:
        verbose_name = "Matrícula"
        verbose_name_plural = "Matrículas"
        unique_together = ['turma', 'interessado']
        ordering = ['-data_matricula']
        indexes = [
            models.Index(fields=['numero_matricula']),
            models.Index(fields=['turma', 'interessado']),
        ]
    
    def __str__(self):
        return f"{self.numero_matricula} - {self.interessado.nome}"
    
    def save(self, *args, **kwargs):
        """
        Sobrescrita do save para gerar numero_matricula automaticamente
        """
        if not self.numero_matricula:
            self.numero_matricula = self._gerar_numero_matricula()
        super().save(*args, **kwargs)
    
    def _gerar_numero_matricula(self):
        """
        Gera número de matrícula no formato AAAANNN
        
        Lógica:
        - AAAA = Ano atual (ex: 2026)
        - NNN = Número sequencial de 4 dígitos (ex: 0001, 002, ..., 9999)
        
        Exemplos: 20260001, 20260002, 20269999, 20270001, ...
        
        Returns:
            str: Número de matrícula único
        """
        ano_atual = timezone.now().year
        prefixo = str(ano_atual)
        
        # Buscar última matrícula do ano
        ultima_matricula = Matricula.objects.filter(
            numero_matricula__startswith=prefixo
        ).order_by('-numero_matricula').first()
        
        if ultima_matricula:
            # Extrair o número sequencial (últimos 4 dígitos)
            try:
                ultimo_numero = int(ultima_matricula.numero_matricula[4:])
                proximo_numero = ultimo_numero + 1
            except (ValueError, IndexError):
                # Se houver erro na conversão, começar do 1
                proximo_numero = 1
        else:
            # Primeira matrícula do ano
            proximo_numero = 1
        
        # Formatar com 4 dígitos (0001, 0002, ..., 9999)
        numero_formatado = f"{prefixo}{proximo_numero:04d}"
        
        return numero_formatado


class Avaliacao(models.Model):
    """Avaliações finais dos alunos matriculados"""
    
    matricula = models.OneToOneField(
        Matricula,
        on_delete=models.CASCADE,
        related_name='avaliacao',
        verbose_name='Matrícula'
    )
    
    # Desempenho
    nota_final = models.DecimalField(
        max_digits=4,
        decimal_places=2,
        validators=[MinValueValidator(Decimal('0.00')), MaxValueValidator(Decimal('10.00'))],
        blank=True,
        null=True,
        verbose_name='Nota Final',
        help_text="Nota de 0 a 10"
    )
    frequencia = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        validators=[MinValueValidator(Decimal('0.00')), MaxValueValidator(Decimal('100.00'))],
        verbose_name='Frequência (%)',
        help_text="Percentual de presença (%)"
    )
    
    # Resultado
    aprovado = models.BooleanField(
        default=False,
        verbose_name='Aprovado'
    )
    observacoes = models.TextField(
        blank=True,
        verbose_name='Observações'
    )
    
    # Certificado
    certificado_emitido = models.BooleanField(
        default=False,
        verbose_name='Certificado Emitido'
    )
    data_emissao_certificado = models.DateField(
        blank=True,
        null=True,
        verbose_name='Data de Emissão do Certificado'
    )
    
    # Auditoria
    avaliado_em = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Avaliado em'
    )
    atualizado_em = models.DateTimeField(
        auto_now=True,
        verbose_name='Atualizado em'
    )
    
    class Meta:
        verbose_name = "Avaliação"
        verbose_name_plural = "Avaliações"
        ordering = ['-avaliado_em']
    
    def __str__(self):
        status = "Aprovado" if self.aprovado else "Reprovado"
        return f"{self.matricula.numero_matricula} - {self.matricula.interessado.nome} - {status}"
    
