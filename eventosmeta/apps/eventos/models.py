"""
Models do app EVENTOS
Responsável por: Configuração de eventos, critérios, turmas
"""
from django.db import models
from django.core.validators import MinValueValidator
from django.utils import timezone


class Status(models.Model):
    """Status de Eventos (Aberto, Em andamento, Encerrado)"""
    nome = models.CharField(max_length=100, unique=True)
    descricao = models.TextField(blank=True)
    ordem = models.PositiveIntegerField(default=0)
    ativo = models.BooleanField(default=True)
    
    class Meta:
        verbose_name = "Status de Evento"
        verbose_name_plural = "Status de Eventos"
        ordering = ['ordem', 'nome']
    
    def __str__(self):
        return self.nome


class Criterio(models.Model):
    """Critérios de classificação (NIS, PCD, Idade, etc.)"""
    
    TIPO_CHOICES = [
        ('NIS', 'Número de Identificação Social (NIS)'),
        ('PCD', 'Pessoa com Deficiência'),
        ('FOTOTIPO', 'Fototipo/Raça'),
        ('IDADE', 'Idade'),
        ('ORDEM', 'Ordem de Inscrição'),
        ('CUSTOM', 'Customizado'),
    ]
    
    ORDEM_IDADE_CHOICES = [
        ('CRESCENTE', 'Crescente (mais novos primeiro)'),
        ('DECRESCENTE', 'Decrescente (mais velhos primeiro)'),
    ]
    
    nome = models.CharField(max_length=100, unique=True)
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES)
    descricao = models.TextField(blank=True)
    pontos = models.PositiveIntegerField(
        default=0,
        validators=[MinValueValidator(0)],
        help_text="Pontos atribuídos ao atender este critério"
    )
    ordem_idade = models.CharField(
        max_length=20,
        choices=ORDEM_IDADE_CHOICES,
        blank=True,
        null=True,
        help_text="Apenas para critério tipo IDADE"
    )
    requer_validacao_manual = models.BooleanField(
        default=False,
        help_text="Se marcado, critério precisa ser validado manualmente pela equipe"
    )
    ativo = models.BooleanField(default=True)
    
    class Meta:
        verbose_name = "Critério de Classificação"
        verbose_name_plural = "Critérios de Classificação"
        ordering = ['nome']
    
    def __str__(self):
        return f"{self.nome} ({self.pontos} pontos)"


class Evento(models.Model):
    """Eventos/Cursos oferecidos"""
    
    nome = models.CharField(max_length=200)
    descricao = models.TextField()
    
    # Datas
    data_inicio_inscricao = models.DateTimeField()
    data_fim_inscricao = models.DateTimeField()
    data_inicio_evento = models.DateField()
    data_fim_evento = models.DateField()
    
    # Vagas
    total_vagas = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    vagas_disponiveis = models.PositiveIntegerField(editable=False)
    
    # Relacionamentos
    status = models.ForeignKey(
        Status,
        on_delete=models.PROTECT,
        related_name='eventos'
    )
    criterios = models.ManyToManyField(
        Criterio,
        through='EventoCriterio',
        related_name='eventos'
    )
    
    # Auditoria
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Evento"
        verbose_name_plural = "Eventos"
        ordering = ['-data_inicio_inscricao']
    
    def __str__(self):
        return f"{self.nome} ({self.data_inicio_evento.year})"
    
    def save(self, *args, **kwargs):
        if not self.pk:
            self.vagas_disponiveis = self.total_vagas
        super().save(*args, **kwargs)
    
    @property
    def inscricoes_abertas(self):
        agora = timezone.now()
        return self.data_inicio_inscricao <= agora <= self.data_fim_inscricao
    
    @property
    def em_andamento(self):
        hoje = timezone.now().date()
        return self.data_inicio_evento <= hoje <= self.data_fim_evento


class EventoCriterio(models.Model):
    """Critérios vinculados a um evento específico"""
    
    evento = models.ForeignKey(
        Evento,
        on_delete=models.CASCADE,
        related_name='evento_criterios'
    )
    criterio = models.ForeignKey(
        Criterio,
        on_delete=models.PROTECT,
        related_name='evento_criterios'
    )
    pontos_customizados = models.PositiveIntegerField(
        blank=True,
        null=True,
        help_text="Sobrescreve pontos padrão do critério (opcional)"
    )
    reserva_vagas = models.PositiveIntegerField(
        default=0,
        validators=[MinValueValidator(0)],
        help_text="Número de vagas reservadas para este critério"
    )
    ordem = models.PositiveIntegerField(default=0)
    
    class Meta:
        verbose_name = "Critério do Evento"
        verbose_name_plural = "Critérios do Evento"
        unique_together = ['evento', 'criterio']
        ordering = ['evento', 'ordem', 'criterio__nome']
    
    def __str__(self):
        return f"{self.evento.nome} - {self.criterio.nome}"
    
    @property
    def pontos_efetivos(self):
        """Retorna pontos customizados ou padrão do critério"""
        return self.pontos_customizados if self.pontos_customizados is not None else self.criterio.pontos


class Turma(models.Model):
    """Turmas de um evento (criadas junto com o evento)"""
    
    TURNO_CHOICES = [
        ('MATUTINO', 'Matutino'),
        ('VESPERTINO', 'Vespertino'),
        ('NOTURNO', 'Noturno'),
        ('INTEGRAL', 'Integral'),
    ]
    
    evento = models.ForeignKey(
        Evento,
        on_delete=models.PROTECT,
        related_name='turmas'
    )
    nome = models.CharField(max_length=100)
    turno = models.CharField(max_length=20, choices=TURNO_CHOICES)
    capacidade = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    local = models.CharField(max_length=200)
    
    # Datas
    data_inicio = models.DateField()
    data_fim = models.DateField()
    
    # Auditoria
    criada_em = models.DateTimeField(auto_now_add=True)
    atualizada_em = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Turma"
        verbose_name_plural = "Turmas"
        ordering = ['evento', 'nome']
    
    def __str__(self):
        return f"{self.nome} - {self.evento.nome} ({self.turno})"
    
    @property
    def vagas_disponiveis(self):
        """Calcula vagas disponíveis baseado em matrículas ativas"""
        from apps.academico.models import Matricula
        matriculas_ativas = Matricula.objects.filter(
            turma=self,
            status__nome='Ativa'
        ).count()
        return self.capacidade - matriculas_ativas
    
    