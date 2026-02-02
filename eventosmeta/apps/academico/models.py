"""
Models do app ACADÊMICO
Arquivo: apps/academico/models.py
Responsável por: Matrículas, avaliações, execução do curso

Alteração: Adicionado numero_matricula auto-gerado (formato AAAANNN)
Data: 14/01/2026

Alteração: Mantidos interessado_id e inscricao_id com validação automática
Data: 30/01/2026

Alteração: Adicionado signal para reverter status ao excluir matrícula
Data: 02/02/2026

Responsável por: Matrículas, avaliações, execução do curso
"""
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError
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
    """
    Matrículas de alunos em turmas
    
    IMPORTANTE: interessado e inscricao devem ser da mesma pessoa
    A validação garante consistência entre os dois campos
    """
    
    # Número de matrícula único e auto-gerado
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
            models.Index(fields=['inscricao']),
        ]
    
    def __str__(self):
        return f"{self.numero_matricula} - {self.interessado.nome}"
    
    def clean(self):
        """
        Validações customizadas - CRÍTICO: interessado deve ser igual a inscricao.interessado
        """
        super().clean()
        
        # VALIDAÇÃO PRINCIPAL: Interessado deve corresponder à inscrição
        if self.inscricao and self.interessado:
            if self.inscricao.interessado != self.interessado:
                raise ValidationError({
                    'interessado': 'O interessado selecionado não corresponde ao interessado da inscrição.',
                    'inscricao': f'Esta inscrição pertence a {self.inscricao.interessado.nome}, '
                                f'não a {self.interessado.nome}.'
                })
        
        # Validar que a inscrição pertence ao evento da turma
        if self.inscricao and self.turma:
            if self.inscricao.evento != self.turma.evento:
                raise ValidationError({
                    'inscricao': f'Esta inscrição é do evento "{self.inscricao.evento.nome}", '
                                f'mas a turma é do evento "{self.turma.evento.nome}". '
                                f'Escolha uma turma do mesmo evento.'
                })
        
        # Validar que o interessado não está matriculado duas vezes na mesma turma
        if self.pk is None:  # Apenas na criação
            if Matricula.objects.filter(
                turma=self.turma,
                interessado=self.interessado
            ).exists():
                raise ValidationError({
                    'interessado': f'O interessado {self.interessado.nome} '
                                  f'já está matriculado nesta turma.'
                })
    
    def save(self, *args, **kwargs):
        """
        Sobrescrita do save para:
        1. Validar consistência
        2. Gerar numero_matricula automaticamente
        3. Auto-preencher interessado se não fornecido
        """
        # AUTO-PREENCHER: Se só inscricao foi fornecida, preenche interessado automaticamente
        if self.inscricao and not self.interessado:
            self.interessado = self.inscricao.interessado
        
        # Validações
        self.full_clean()
        
        if not self.numero_matricula:
            self.numero_matricula = self._gerar_numero_matricula()
        
        super().save(*args, **kwargs)
    
    def _gerar_numero_matricula(self):
        """
        Gera número de matrícula no formato AAAANNN
        
        Lógica:
        - AAAA = Ano atual (ex: 2026)
        - NNNN = Número sequencial de 4 dígitos (ex: 0001, 0002, ..., 9999)
        
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


# ==========================================
# SIGNALS PARA ATUALIZAR STATUS DA INSCRIÇÃO
# ==========================================

from django.db.models.signals import post_delete
from django.dispatch import receiver
from apps.selecao.models import StatusInscricao


@receiver(post_delete, sender=Matricula)
def reverter_status_inscricao(sender, instance, **kwargs):
    """
    Quando uma matrícula é excluída, reverte o status da inscrição para 'Pendente'
    """
    try:
        # Buscar status "Pendente" (case-insensitive)
        status_pendente = StatusInscricao.objects.get(nome__iexact='pendente')
        
        # Atualizar a inscrição relacionada
        inscricao = instance.inscricao
        inscricao.status = status_pendente
        inscricao.save()
        
    except StatusInscricao.DoesNotExist:
        # Se não encontrar o status Pendente, não faz nada
        pass
    except Exception as e:
        # Log do erro (opcional)
        import logging
        logger = logging.getLogger(__name__)
        logger.error(f"Erro ao reverter status da inscrição {instance.inscricao.id}: {str(e)}")

# ==========================================
# SIGNAL: CRIAR AVALIAÇÃO AUTOMATICAMENTE
# ==========================================

from django.db.models.signals import post_save


@receiver(post_save, sender=Matricula)
def criar_avaliacao_automatica(sender, instance, created, **kwargs):
    """
    Quando uma matrícula é criada, cria automaticamente uma avaliação vazia
    """
    if created:  # Apenas na criação da matrícula
        try:
            # Verifica se já existe avaliação (por segurança)
            if not hasattr(instance, 'avaliacao'):
                Avaliacao.objects.create(
                    matricula=instance,
                    frequencia=0.00,  # Frequência inicial zerada
                    aprovado=False     # Inicialmente não aprovado
                )
        except Exception as e:
            import logging
            logger = logging.getLogger(__name__)
            logger.error(f"Erro ao criar avaliação para matrícula {instance.numero_matricula}: {str(e)}")

            