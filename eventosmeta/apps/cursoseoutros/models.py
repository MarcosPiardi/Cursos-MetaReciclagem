"""
ARQUIVO: apps/cursoseoutros/models.py
AÇÃO: CRIAR/SUBSTITUIR arquivo completo
MUDANÇA: Models completos para sistema de eventos, cursos, inscrições, classificação e turmas
DATA/HORA: 2025-10-29 14:30:00
"""

from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator, RegexValidator
from django.utils import timezone
from decimal import Decimal


class Status(models.Model):
    """
    Status do Evento/Curso.
    Define o estado atual do evento e se permite inscrições.
    """
    status = models.CharField(
        'Status',
        max_length=30,
        unique=True,
        help_text='Nome do status (ex: Inscrições Abertas, Em Andamento, Encerrado)'
    )
    
    permite_inscricao = models.BooleanField(
        'Permite Inscrição',
        default=False,
        help_text='Se TRUE, interessados podem se inscrever neste status'
    )
    
    ordem = models.IntegerField(
        'Ordem',
        default=0,
        help_text='Ordem de exibição (menor número aparece primeiro)'
    )
    
    def __str__(self):
        return self.status
    
    class Meta:
        verbose_name = 'Status'
        verbose_name_plural = 'Status'
        ordering = ['ordem', 'status']


class TipoCriterio(models.TextChoices):
    """Tipos de critérios disponíveis para classificação"""
    NIS = 'NIS', 'Programa Social (NIS)'
    PCD = 'PCD', 'Necessidades Especiais (PCD)'
    FOTOTIPO = 'FOTOTIPO', 'Fototipo/Cor (Cotas Raciais)'
    IDADE_CRESCENTE = 'IDADE_CRESC', 'Idade Crescente (Mais Jovem Primeiro)'
    IDADE_DECRESCENTE = 'IDADE_DECRESC', 'Idade Decrescente (Mais Velho Primeiro)'
    FAIXA_ETARIA = 'FAIXA_ETARIA', 'Faixa Etária Específica'
    ORDEM = 'ORDEM', 'Ordem de Inscrição'
    CUSTOMIZADO = 'CUSTOMIZADO', 'Critério Customizado'


class Criterio(models.Model):
    """
    Catálogo de critérios de classificação.
    Critérios são reutilizáveis em múltiplos eventos.
    """
    descricao_criterio = models.CharField(
        'Descrição do Critério',
        max_length=100,
        help_text='Ex: Prioridade para beneficiários do Bolsa Família'
    )
    
    tipo_criterio = models.CharField(
        'Tipo de Critério',
        max_length=20,
        choices=TipoCriterio.choices,
        help_text='Tipo determina como o critério será avaliado'
    )
    
    ativo = models.BooleanField(
        'Ativo',
        default=True,
        help_text='Critérios inativos não aparecem para seleção'
    )
    
    criado_em = models.DateTimeField('Criado em', auto_now_add=True)
    
    def __str__(self):
        return f"{self.descricao_criterio} ({self.get_tipo_criterio_display()})"
    
    class Meta:
        verbose_name = 'Critério de Classificação'
        verbose_name_plural = 'Critérios de Classificação'
        ordering = ['tipo_criterio', 'descricao_criterio']


class Modalidade(models.TextChoices):
    """Modalidades de realização do evento"""
    PRESENCIAL = 'PRESENCIAL', 'Presencial'
    ONLINE = 'ONLINE', 'Online'
    HIBRIDO = 'HIBRIDO', 'Híbrido'


class Evento(models.Model):
    """
    Eventos/Cursos oferecidos pela MetaReciclagem.
    Representa cursos, palestras, workshops, treinamentos, etc.
    """
    descricao = models.CharField(
        'Descrição/Nome do Evento',
        max_length=200,
        help_text='Nome do curso/evento'
    )
    
    status = models.ForeignKey(
        Status,
        on_delete=models.PROTECT,
        verbose_name='Status',
        related_name='eventos',
        help_text='Status atual do evento'
    )
    
    programa = models.TextField(
        'Programa/Conteúdo',
        blank=True,
        default='',
        help_text='Descrição detalhada do conteúdo programático'
    )
    
    objetivo = models.TextField(
        'Objetivo',
        blank=True,
        default='',
        help_text='Objetivos e competências a serem desenvolvidas'
    )
    
    pre_requisito = models.TextField(
        'Pré-requisitos',
        blank=True,
        default='',
        help_text='Requisitos necessários para participação'
    )
    
    carga_horaria = models.CharField(
        'Carga Horária',
        max_length=50,
        blank=True,
        default='',
        help_text='Ex: 40 horas, 20h teóricas + 20h práticas'
    )
    
    docente = models.CharField(
        'Docente/Instrutor',
        max_length=100,
        blank=True,
        default='',
        help_text='Nome do professor/instrutor'
    )
    
    # VAGAS
    vagas = models.IntegerField(
        'Número de Vagas',
        validators=[MinValueValidator(1)],
        help_text='Total de vagas disponíveis'
    )
    
    vagas_minimas = models.IntegerField(
        'Vagas Mínimas',
        validators=[MinValueValidator(1)],
        default=1,
        help_text='Mínimo de alunos para viabilizar o curso'
    )
    
    modalidade = models.CharField(
        'Modalidade',
        max_length=15,
        choices=Modalidade.choices,
        default=Modalidade.PRESENCIAL
    )
    
    # DATAS - INSCRIÇÕES
    inicio_inscricoes = models.DateField(
        'Início das Inscrições',
        null=True,
        blank=True
    )
    
    fim_inscricoes = models.DateField(
        'Fim das Inscrições',
        null=True,
        blank=True
    )
    
    # DATAS - MATRÍCULAS
    inicio_matricula = models.DateField(
        'Início das Matrículas',
        null=True,
        blank=True,
        help_text='Data para iniciar matrículas dos classificados'
    )
    
    fim_matricula = models.DateField(
        'Fim das Matrículas',
        null=True,
        blank=True
    )
    
    # DATAS - AULAS
    inicio_aulas = models.DateField(
        'Início das Aulas',
        null=True,
        blank=True
    )
    
    fim_aulas = models.DateField(
        'Fim das Aulas',
        null=True,
        blank=True
    )
    
    horario_aulas = models.CharField(
        'Horário das Aulas',
        max_length=100,
        blank=True,
        default='',
        help_text='Ex: Segunda a Sexta, 14h às 18h'
    )
    
    # LOCAL
    local = models.CharField(
        'Local',
        max_length=100,
        blank=True,
        default='',
        help_text='Nome do local (ex: Sala 3, Laboratório de Informática)'
    )
    
    endereco_local = models.CharField(
        'Endereço do Local',
        max_length=200,
        blank=True,
        default='',
        help_text='Endereço completo onde será realizado'
    )
    
    observacao = models.TextField(
        'Observações',
        blank=True,
        default='',
        help_text='Informações adicionais'
    )
    
    # AUDITORIA
    criado_em = models.DateTimeField('Criado em', auto_now_add=True)
    atualizado_em = models.DateTimeField('Atualizado em', auto_now=True)
    
    # Relacionamento Many-to-Many com Criterio via EventoCriterio
    criterios = models.ManyToManyField(
        Criterio,
        through='EventoCriterio',
        related_name='eventos',
        verbose_name='Critérios de Classificação'
    )
    
    def __str__(self):
        return f"{self.descricao} ({self.status})"
    
    def total_inscricoes(self):
        """Retorna o total de inscrições neste evento"""
        return self.inscricoes.count()
    
    def vagas_disponiveis(self):
        """Calcula vagas disponíveis"""
        matriculas_confirmadas = self.turmas.aggregate(
            total=models.Count('matriculas', filter=models.Q(matriculas__status='CONFIRMADA'))
        )['total'] or 0
        return self.vagas - matriculas_confirmadas
    
    class Meta:
        verbose_name = 'Evento/Curso'
        verbose_name_plural = 'Eventos/Cursos'
        ordering = ['-criado_em']


class TipoReserva(models.TextChoices):
    """Tipos de reserva de vagas por critério"""
    PERCENTUAL = 'PERCENTUAL', 'Percentual (%)'
    NUMERO_FIXO = 'NUMERO_FIXO', 'Número Fixo de Vagas'
    SEM_RESERVA = 'SEM_RESERVA', 'Sem Reserva (Apenas Pontuação)'


class OrdemIdade(models.TextChoices):
    """Ordem de priorização por idade"""
    CRESCENTE = 'CRESCENTE', 'Crescente (Mais Jovem Primeiro)'
    DECRESCENTE = 'DECRESCENTE', 'Decrescente (Mais Velho Primeiro)'
    FAIXA = 'FAIXA', 'Faixa Etária (Entre Idades)'


class EventoCriterio(models.Model):
    """
    Tabela intermediária entre Evento e Criterio.
    Configura como cada critério será aplicado em cada evento específico.
    """
    evento = models.ForeignKey(
        Evento,
        on_delete=models.CASCADE,
        related_name='evento_criterios',
        verbose_name='Evento'
    )
    
    criterio = models.ForeignKey(
        Criterio,
        on_delete=models.CASCADE,
        related_name='evento_criterios',
        verbose_name='Critério'
    )
    
    peso = models.IntegerField(
        'Peso (0-10)',
        validators=[MinValueValidator(0), MaxValueValidator(10)],
        default=5,
        help_text='Importância deste critério (0=irrelevante, 10=máximo)'
    )
    
    tipo_reserva = models.CharField(
        'Tipo de Reserva de Vagas',
        max_length=15,
        choices=TipoReserva.choices,
        default=TipoReserva.SEM_RESERVA,
        help_text='Como as vagas serão reservadas'
    )
    
    vagas_reservadas = models.IntegerField(
        'Vagas Reservadas',
        default=0,
        validators=[MinValueValidator(0)],
        help_text='Se PERCENTUAL: valor de 0-100. Se NUMERO_FIXO: quantidade de vagas'
    )
    
    ordem = models.IntegerField(
        'Ordem de Aplicação',
        default=1,
        validators=[MinValueValidator(1)],
        help_text='Ordem em que o critério será processado (1=primeiro)'
    )
    
    # CONFIGURAÇÕES ESPECÍFICAS PARA IDADE
    ordem_idade = models.CharField(
        'Ordem de Idade',
        max_length=15,
        choices=OrdemIdade.choices,
        null=True,
        blank=True,
        help_text='Usado apenas para critérios de tipo IDADE'
    )
    
    idade_minima = models.IntegerField(
        'Idade Mínima',
        null=True,
        blank=True,
        validators=[MinValueValidator(0), MaxValueValidator(120)],
        help_text='Para FAIXA_ETARIA: idade mínima prioritária'
    )
    
    idade_maxima = models.IntegerField(
        'Idade Máxima',
        null=True,
        blank=True,
        validators=[MinValueValidator(0), MaxValueValidator(120)],
        help_text='Para FAIXA_ETARIA: idade máxima prioritária'
    )
    
    observacao = models.TextField(
        'Observações',
        blank=True,
        default='',
        help_text='Informações adicionais sobre este critério no evento'
    )
    
    def __str__(self):
        return f"{self.evento.descricao} - {self.criterio.descricao_criterio} (Peso: {self.peso})"
    
    class Meta:
        verbose_name = 'Critério do Evento'
        verbose_name_plural = 'Critérios dos Eventos'
        ordering = ['evento', 'ordem', '-peso']
        unique_together = ['evento', 'criterio']


class StatusInscricao(models.TextChoices):
    """Status possíveis de uma inscrição"""
    INSCRITO = 'INSCRITO', 'Inscrito'
    AGUARDANDO_CLASSIFICACAO = 'AGUARD_CLASS', 'Aguardando Classificação'
    CLASSIFICADO = 'CLASSIFICADO', 'Classificado'
    APROVADO = 'APROVADO', 'Aprovado (Dentro das Vagas)'
    FILA_ESPERA = 'FILA_ESPERA', 'Fila de Espera'
    MATRICULADO = 'MATRICULADO', 'Matriculado'
    DESISTENTE = 'DESISTENTE', 'Desistente'
    NAO_COMPARECEU = 'NAO_COMPARECEU', 'Não Compareceu'


class Inscricao(models.Model):
    """
    Inscrição de interessado em evento/curso.
    Representa o ato de se inscrever em um evento.
    """
    evento = models.ForeignKey(
        Evento,
        on_delete=models.CASCADE,
        related_name='inscricoes',
        verbose_name='Evento'
    )
    
    interessado = models.ForeignKey(
        'interessados.Interessado',
        on_delete=models.CASCADE,
        related_name='inscricoes',
        verbose_name='Interessado'
    )
    
    data_inscricao = models.DateTimeField(
        'Data da Inscrição',
        default=timezone.now,
        help_text='Data e hora em que a inscrição foi realizada'
    )
    
    status = models.CharField(
        'Status da Inscrição',
        max_length=20,
        choices=StatusInscricao.choices,
        default=StatusInscricao.INSCRITO
    )
    
    def __str__(self):
        return f"{self.interessado.nome} → {self.evento.descricao}"
    
    class Meta:
        verbose_name = 'Inscrição'
        verbose_name_plural = 'Inscrições'
        ordering = ['data_inscricao']
        unique_together = ['evento', 'interessado']


class Classificacao(models.Model):
    """
    Resultado da classificação de uma inscrição.
    Gerado após o processamento dos critérios de classificação.
    """
    inscricao = models.OneToOneField(
        Inscricao,
        on_delete=models.CASCADE,
        related_name='classificacao',
        verbose_name='Inscrição'
    )
    
    score_total = models.DecimalField(
        'Score Total',
        max_digits=10,
        decimal_places=2,
        default=Decimal('0.00'),
        help_text='Pontuação total calculada pelos critérios'
    )
    
    posicao = models.IntegerField(
        'Posição/Classificação',
        null=True,
        blank=True,
        help_text='Posição final na classificação (1=primeiro lugar)'
    )
    
    data_classificacao = models.DateTimeField(
        'Data da Classificação',
        default=timezone.now,
        help_text='Quando a classificação foi processada'
    )
    
    def __str__(self):
        return f"{self.inscricao.interessado.nome} - Posição: {self.posicao} (Score: {self.score_total})"
    
    class Meta:
        verbose_name = 'Classificação'
        verbose_name_plural = 'Classificações'
        ordering = ['inscricao__evento', 'posicao']


class InscricaoCriterioAtendido(models.Model):
    """
    Registra quais critérios cada inscrição atende.
    Para critérios CUSTOMIZADOS, permite validação manual pelo operador.
    """
    inscricao = models.ForeignKey(
        Inscricao,
        on_delete=models.CASCADE,
        related_name='criterios_atendidos',
        verbose_name='Inscrição'
    )
    
    criterio = models.ForeignKey(
        Criterio,
        on_delete=models.CASCADE,
        related_name='inscricoes_atendidas',
        verbose_name='Critério'
    )
    
    pontos_obtidos = models.DecimalField(
        'Pontos Obtidos',
        max_digits=10,
        decimal_places=2,
        default=Decimal('0.00'),
        help_text='Pontos atribuídos por este critério'
    )
    
    validado = models.BooleanField(
        'Validado',
        default=False,
        help_text='Para critérios customizados: se foi validado manualmente'
    )
    
    validado_por = models.ForeignKey(
        'accounts.Usuario',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='criterios_validados',
        verbose_name='Validado Por'
    )
    
    data_validacao = models.DateTimeField(
        'Data da Validação',
        null=True,
        blank=True
    )
    
    def __str__(self):
        return f"{self.inscricao.interessado.nome} - {self.criterio.descricao_criterio} ({self.pontos_obtidos} pts)"
    
    class Meta:
        verbose_name = 'Critério Atendido'
        verbose_name_plural = 'Critérios Atendidos'
        ordering = ['inscricao', '-pontos_obtidos']
        unique_together = ['inscricao', 'criterio']


class Turma(models.Model):
    """
    Turma/Classe formada após matrículas.
    Um evento pode ter múltiplas turmas (ex: Turma A, Turma B).
    """
    descricao_turma = models.CharField(
        'Descrição da Turma',
        max_length=100,
        help_text='Ex: Turma A - Manhã, Turma Avançada'
    )
    
    evento = models.ForeignKey(
        Evento,
        on_delete=models.CASCADE,
        related_name='turmas',
        verbose_name='Evento'
    )
    
    data_inicio = models.DateField(
        'Data de Início',
        null=True,
        blank=True
    )
    
    data_fim = models.DateField(
        'Data de Término',
        null=True,
        blank=True
    )
    
    horario_aulas = models.CharField(
        'Horário das Aulas',
        max_length=100,
        blank=True,
        default='',
        help_text='Ex: Segunda a Sexta, 8h às 12h'
    )
    
    local_aulas = models.CharField(
        'Local das Aulas',
        max_length=100,
        blank=True,
        default='',
        help_text='Sala/local específico desta turma'
    )
    
    def __str__(self):
        return f"{self.evento.descricao} - {self.descricao_turma}"
    
    def total_alunos(self):
        """Retorna total de alunos matriculados"""
        return self.matriculas.filter(status='CONFIRMADA').count()
    
    class Meta:
        verbose_name = 'Turma'
        verbose_name_plural = 'Turmas'
        ordering = ['evento', 'descricao_turma']


class StatusMatricula(models.TextChoices):
    """Status possíveis de uma matrícula"""
    PENDENTE = 'PENDENTE', 'Pendente'
    CONFIRMADA = 'CONFIRMADA', 'Confirmada'
    CANCELADA = 'CANCELADA', 'Cancelada'
    TRANCADA = 'TRANCADA', 'Trancada'


class Matricula(models.Model):
    """
    Matrícula de interessado em turma.
    Representa o vínculo efetivo aluno-turma.
    """
    turma = models.ForeignKey(
        Turma,
        on_delete=models.CASCADE,
        related_name='matriculas',
        verbose_name='Turma'
    )
    
    interessado = models.ForeignKey(
        'interessados.Interessado',
        on_delete=models.CASCADE,
        related_name='matriculas',
        verbose_name='Interessado'
    )
    
    data_matricula = models.DateTimeField(
        'Data da Matrícula',
        default=timezone.now
    )
    
    status = models.CharField(
        'Status da Matrícula',
        max_length=15,
        choices=StatusMatricula.choices,
        default=StatusMatricula.PENDENTE
    )
    
    def __str__(self):
        return f"{self.interessado.nome} - {self.turma.descricao_turma}"
    
    class Meta:
        verbose_name = 'Matrícula'
        verbose_name_plural = 'Matrículas'
        ordering = ['turma', 'data_matricula']
        unique_together = ['turma', 'interessado']


class Avaliacao(models.Model):
    """
    Avaliação final do aluno na turma.
    Controla frequência, nota e aprovação.
    """
    matricula = models.OneToOneField(
        Matricula,
        on_delete=models.CASCADE,
        related_name='avaliacao',
        verbose_name='Matrícula'
    )
    
    frequencia = models.DecimalField(
        'Frequência (%)',
        max_digits=5,
        decimal_places=2,
        default=Decimal('0.00'),
        validators=[MinValueValidator(0), MaxValueValidator(100)],
        help_text='Percentual de presença (0-100%)'
    )
    
    nota = models.DecimalField(
        'Nota',
        max_digits=5,
        decimal_places=2,
        null=True,
        blank=True,
        validators=[MinValueValidator(0), MaxValueValidator(10)],
        help_text='Nota final (0-10)'
    )
    
    aprovado = models.BooleanField(
        'Aprovado',
        default=False,
        help_text='Se o aluno foi aprovado no curso'
    )
    
    emite_certificado = models.BooleanField(
        'Emite Certificado',
        default=False,
        help_text='Se deve emitir certificado para este aluno'
    )
    
    def __str__(self):
        status = "APROVADO" if self.aprovado else "REPROVADO"
        return f"{self.matricula.interessado.nome} - {status}"
    
    class Meta:
        verbose_name = 'Avaliação'
        verbose_name_plural = 'Avaliações'
        ordering = ['matricula__turma']