"""
Arquivo: models.py
Caminho: apps/eventos/models.py
Alteração: Adicionado tipo_criterio em Criterio e prioridade em EventoCriterio
Data: 09/12/2025
"""
from django.db import models
from django.core.validators import MinValueValidator
from django.utils import timezone


class Status(models.Model):
    """
    Status dos eventos (Inscrições Abertas, Em Andamento, Concluído, etc.)
    """
    nome = models.CharField('Nome', max_length=50, unique=True)
    cor = models.CharField('Cor', max_length=7, default='#6c757d',
                          help_text='Cor em hexadecimal (ex: #007bff)')
    ordem = models.IntegerField('Ordem de Exibição', default=0)
    
    class Meta:
        verbose_name = 'Status'
        verbose_name_plural = 'Status'
        ordering = ['ordem', 'nome']
    
    def __str__(self):
        return self.nome


class Criterio(models.Model):
    """
    Critérios de classificação: pontuação OU ordenação
    """
    TIPO_CHOICES = [
        ('PONTUACAO', 'Pontuação'),
        ('ORDENACAO', 'Ordenação'),
    ]
    
    tipo_criterio = models.CharField(
        'Tipo de Critério',
        max_length=20,
        choices=TIPO_CHOICES,
        default='PONTUACAO',
        help_text='Pontuação = soma pontos | Ordenação = define ordem de classificação'
    )
    
    codigo = models.CharField(
        'Código',
        max_length=30,
        unique=True,
        help_text='Código único do critério (ex: PCD, ORDEM_INSCRICAO, IDADE_CRESCENTE)'
    )
    
    nome = models.CharField(
        'Nome',
        max_length=200,
        help_text='Nome descritivo do critério'
    )
    
    descricao = models.TextField(
        'Descrição',
        blank=True,
        help_text='Descrição detalhada do critério'
    )
    
    pontos = models.IntegerField(
        'Pontos',
        null=True,
        blank=True,
        help_text='Pontuação (apenas para tipo PONTUACAO)'
    )
    
    categoria = models.CharField(
        'Categoria',
        max_length=50,
        choices=[
            ('ORDENACAO', 'Ordenação'),
            ('CRONOLÓGICA', 'Ordem de Inscrição'),
            ('IDADE', 'Idade'),
            ('VULNERABILIDADE', 'Vulnerabilidade Social'),
            ('FAIXA_ETARIA', 'Faixa Etária'),
            ('ESCOLARIDADE', 'Escolaridade'),
            ('COTA_RACIAL', 'Cota Racial'),
        ],
        help_text='Categoria do critério'
    )
    
    ativo = models.BooleanField(
        'Ativo',
        default=True,
        help_text='Se False, não aparece para seleção'
    )
    
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'Critério de Classificação'
        verbose_name_plural = 'Critérios de Classificação'
        ordering = ['categoria', '-pontos', 'nome']
    
    def __str__(self):
        if self.pontos is not None:
            return f'{self.nome} ({self.pontos} pts)'
        return self.nome


class Evento(models.Model):
    """
    Eventos/Cursos oferecidos
    """
    nome = models.CharField('Nome do Evento', max_length=200)
    descricao = models.TextField('Descrição', blank=True)
    status = models.ForeignKey(
        Status,
        on_delete=models.PROTECT,
        related_name='eventos',
        verbose_name='Status'
    )
    
    # Vagas
    total_vagas = models.IntegerField(
        'Total de Vagas',
        validators=[MinValueValidator(1)]
    )
    
    # Datas de inscrição
    data_inicio_inscricao = models.DateTimeField('Início das Inscrições')
    data_fim_inscricao = models.DateTimeField('Fim das Inscrições')
    
    # Período do evento
    data_inicio_evento = models.DateField('Início do Evento')
    data_fim_evento = models.DateField('Fim do Evento')
    
    # Metadata
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'Evento'
        verbose_name_plural = 'Eventos'
        ordering = ['-data_inicio_evento']
    
    def __str__(self):
        return self.nome
    
    def inscricoes_abertas(self):
        """Verifica se as inscrições estão abertas"""
        agora = timezone.now()
        return self.data_inicio_inscricao <= agora <= self.data_fim_inscricao


class EventoCriterio(models.Model):
    """
    Relacionamento entre Evento e Critérios ativos
    """
    evento = models.ForeignKey(
        Evento,
        on_delete=models.CASCADE,
        related_name='evento_criterios',
        verbose_name='Evento'
    )
    
    criterio = models.ForeignKey(
        Criterio,
        on_delete=models.PROTECT,
        verbose_name='Critério'
    )
    
    prioridade = models.IntegerField(
        'Prioridade',
        default=999,
        help_text='Ordem de aplicação (1 = primeiro, 2 = segundo, etc.)'
    )
    
    ativo = models.BooleanField(
        'Ativo',
        default=True,
        help_text='Critério será usado na classificação?'
    )
    
    criado_em = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'Critério do Evento'
        verbose_name_plural = 'Critérios do Evento'
        unique_together = ['evento', 'criterio']
        ordering = ['prioridade', '-criterio__pontos', 'criterio__nome']
    
    def __str__(self):
        return f'{self.evento.nome} - {self.criterio.nome}'
    
    @property
    def pontos(self):
        """Retorna os pontos do critério (apenas leitura)"""
        return self.criterio.pontos


class Turma(models.Model):
    """
    Turmas de um evento
    """
    TURNO_CHOICES = [
        ('MATUTINO', 'Matutino'),
        ('VESPERTINO', 'Vespertino'),
        ('NOTURNO', 'Noturno'),
        ('INTEGRAL', 'Integral'),
    ]
    
    evento = models.ForeignKey(
        Evento,
        on_delete=models.CASCADE,
        related_name='turmas',
        verbose_name='Evento'
    )
    nome = models.CharField('Nome da Turma', max_length=100)
    turno = models.CharField('Turno', max_length=20, choices=TURNO_CHOICES)
    capacidade = models.IntegerField(
        'Capacidade',
        validators=[MinValueValidator(1)]
    )
    local = models.CharField('Local', max_length=200, blank=True)
    
    data_inicio = models.DateField('Data de Início')
    data_fim = models.DateField('Data de Término')
    
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'Turma'
        verbose_name_plural = 'Turmas'
        ordering = ['evento', 'nome']
        unique_together = ['evento', 'nome']
    
    def __str__(self):
        return f'{self.evento.nome} - {self.nome}'


class Horario(models.Model):
    """
    Horários das aulas de uma turma
    """
    DIA_SEMANA_CHOICES = [
        (0, 'Segunda-feira'),
        (1, 'Terça-feira'),
        (2, 'Quarta-feira'),
        (3, 'Quinta-feira'),
        (4, 'Sexta-feira'),
        (5, 'Sábado'),
        (6, 'Domingo'),
    ]
    
    turma = models.ForeignKey(
        Turma,
        on_delete=models.CASCADE,
        related_name='horarios',
        verbose_name='Turma'
    )
    dia_semana = models.IntegerField('Dia da Semana', choices=DIA_SEMANA_CHOICES)
    hora_inicio = models.TimeField('Horário de Início')
    hora_fim = models.TimeField('Horário de Término')
    
    class Meta:
        verbose_name = 'Horário'
        verbose_name_plural = 'Horários'
        ordering = ['turma', 'dia_semana', 'hora_inicio']
    
    def __str__(self):
        return f'{self.turma.nome} - {self.get_dia_semana_display()}'