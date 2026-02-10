"""
URL Configuration for Eventos MetaReciclagem
Arquivo: eventosmeta/config/urls.py
Alteração: Admin customizado com dashboard + estrutura completa
Data: 20/01/2026

Alteração: Admin customizado + rotas de dashboard integradas
Data: 03/02/2026

Alteração: Utilidades para geração de PDF dos dashboards
Data: 06/02/2026
"""

from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib.units import cm
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer, Image
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.pdfgen import canvas
from io import BytesIO
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from datetime import datetime
import os


def criar_grafico_pizza(labels, values, title):
    """Cria gráfico de pizza e retorna BytesIO"""
    fig, ax = plt.subplots(figsize=(5, 4))
    
    colors_pizza = ['#4CAF50', '#2196F3', '#FF9800', '#E91E63', '#9C27B0',
                    '#00BCD4', '#FFEB3B', '#FF5722', '#795548', '#607D8B']
    
    filtered_data = [(label, value) for label, value in zip(labels, values) if value > 0]
    if not filtered_data:
        plt.close()
        return None
    
    labels_filtered, values_filtered = zip(*filtered_data)
    
    wedges, texts, autotexts = ax.pie(
        values_filtered, labels=labels_filtered, autopct='%1.1f%%',
        startangle=90, colors=colors_pizza[:len(labels_filtered)]
    )
    
    for text in texts:
        text.set_fontsize(8)
    for autotext in autotexts:
        autotext.set_color('white')
        autotext.set_fontweight('bold')
        autotext.set_fontsize(7)
    
    ax.set_title(title, fontsize=10, fontweight='bold', pad=10)
    plt.tight_layout()
    
    img_buffer = BytesIO()
    plt.savefig(img_buffer, format='png', dpi=100, bbox_inches='tight')
    img_buffer.seek(0)
    plt.close()
    return img_buffer


def criar_grafico_barras(labels, values, title):
    """Cria gráfico de barras e retorna BytesIO"""
    fig, ax = plt.subplots(figsize=(10, 4))
    
    bars = ax.bar(labels, values, color='#4CAF50', edgecolor='#388E3C', linewidth=1.5)
    
    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height,
                f'{int(height)}', ha='center', va='bottom', fontsize=8, fontweight='bold')
    
    ax.set_title(title, fontsize=10, fontweight='bold', pad=15)
    ax.set_ylabel('Quantidade', fontsize=9)
    ax.grid(axis='y', alpha=0.3, linestyle='--')
    plt.xticks(rotation=45, ha='right', fontsize=8)
    plt.tight_layout()
    
    img_buffer = BytesIO()
    plt.savefig(img_buffer, format='png', dpi=100, bbox_inches='tight')
    img_buffer.seek(0)
    plt.close()
    return img_buffer


class DashboardCanvas(canvas.Canvas):
    """Canvas personalizado com cabeçalho e rodapé limpos"""
    
    def __init__(self, *args, **kwargs):
        self.titulo_dashboard = kwargs.pop('titulo_dashboard', 'DASHBOARD')
        self.data_emissao = kwargs.pop('data_emissao', datetime.now().strftime('%d/%m/%Y %H:%M'))
        canvas.Canvas.__init__(self, *args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_page(num_pages)
            canvas.Canvas.showPage(self)
        canvas.Canvas.save(self)

    def draw_page(self, page_count):
        """Desenha cabeçalho e rodapé em cada página"""
        from django.conf import settings
        
        page_width, page_height = landscape(A4)
        
        # ==========================================
        # CABEÇALHO
        # ==========================================
        
        # Brasão (esquerda)
        try:
            brasao_path = os.path.join(settings.BASE_DIR, 'static', 'images', 'brasão-2.png')
            if os.path.exists(brasao_path):
                self.drawImage(
                    brasao_path, 
                    1.5*cm, 
                    page_height - 2*cm, 
                    width=1.8*cm, 
                    height=1.8*cm, 
                    preserveAspectRatio=True, 
                    mask='auto'
                )
        except Exception as e:
            # Fallback: círculo com texto
            self.setFillColor(colors.HexColor('#2196F3'))
            self.circle(2.4*cm, page_height - 1.3*cm, 0.5*cm, stroke=1, fill=1)
            self.setFillColor(colors.white)
            self.setFont("Helvetica-Bold", 7)
            self.drawCentredString(2.4*cm, page_height - 1.35*cm, "PMS")
        
        # Logo MetaReciclagem (direita)
        try:
            logo_path = os.path.join(settings.BASE_DIR, 'static', 'images', 'metareciclagem.png')
            if os.path.exists(logo_path):
                self.drawImage(
                    logo_path, 
                    page_width - 4.5*cm, 
                    page_height - 2*cm, 
                    width=3*cm, 
                    height=1.8*cm, 
                    preserveAspectRatio=True, 
                    mask='auto'
                )
        except Exception as e:
            # Fallback: retângulo com texto
            self.setFillColor(colors.HexColor('#4CAF50'))
            self.rect(page_width - 4*cm, page_height - 1.6*cm, 2.5*cm, 0.7*cm, fill=1, stroke=0)
            self.setFillColor(colors.white)
            self.setFont("Helvetica-Bold", 9)
            self.drawCentredString(page_width - 2.75*cm, page_height - 1.35*cm, "MetaReciclagem")
        
        # Título centralizado
        self.setFillColor(colors.HexColor('#1976D2'))
        self.setFont("Helvetica-Bold", 14)
        self.drawCentredString(page_width / 2, page_height - 1.3*cm, self.titulo_dashboard)
        
        # ==========================================
        # LINHA SIMPLES (única linha - abaixo do título)
        # ==========================================
        self.setStrokeColor(colors.HexColor('#2196F3'))
        self.setLineWidth(1)
        self.line(1.5*cm, page_height - 2.3*cm, page_width - 1.5*cm, page_height - 2.3*cm)
        
        # ==========================================
        # RODAPÉ (sem linhas)
        # ==========================================
        
        # Data de emissão (esquerda)
        self.setFillColor(colors.HexColor('#666666'))
        self.setFont("Helvetica", 8)
        self.drawString(1.5*cm, 0.8*cm, f"Emitido em: {self.data_emissao}")
        
        # Paginação (direita)
        self.drawRightString(page_width - 1.5*cm, 0.8*cm, f"Página {self._pageNumber} / {page_count}")


def gerar_pdf_interessados(context):
    """Gera PDF do dashboard de interessados com layout limpo"""
    buffer = BytesIO()
    
    # Data de emissão
    data_emissao = datetime.now().strftime('%d/%m/%Y às %H:%M')
    
    doc = SimpleDocTemplate(
        buffer,
        pagesize=landscape(A4),
        rightMargin=1.5*cm,
        leftMargin=1.5*cm,
        topMargin=3*cm,
        bottomMargin=1.5*cm
    )
    
    styles = getSampleStyleSheet()
    
    # Estilos personalizados
    style_subtitle = ParagraphStyle(
        'CustomSubtitle',
        parent=styles['Heading2'],
        fontSize=11,
        textColor=colors.HexColor('#2196F3'),
        spaceAfter=8,
        spaceBefore=12,
        fontName='Helvetica-Bold'
    )
    
    story = []
    
    # ==========================================
    # CARDS DE MÉTRICAS
    # ==========================================
    metricas_data = [
        ['Métrica', 'Valor'],
        ['Total de Interessados', str(context['total_interessados'])],
        ['Com Matrícula', str(context['interessados_matriculados'])],
        ['Sem Matrícula', str(context['interessados_sem_matricula'])]
    ]
    
    metricas_table = Table(metricas_data, colWidths=[15*cm, 5*cm])
    metricas_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#2196F3')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('ALIGN', (1, 0), (1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 10),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 10),
        ('GRID', (0, 0), (-1, -1), 1, colors.grey),
        ('FONTSIZE', (0, 1), (-1, -1), 9),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#F5F5F5')])
    ]))
    
    story.append(metricas_table)
    story.append(Spacer(1, 0.6*cm))
    
    # ==========================================
    # GRÁFICOS - LINHA 1
    # ==========================================
    story.append(Paragraph("Perfil Demográfico", style_subtitle))
    
    graficos_linha1 = []
    
    # Sexo
    if context['distribuicao_sexo']:
        labels = [item.get('sexo__nome') or 'Não informado' for item in context['distribuicao_sexo']]
        values = [item['total'] for item in context['distribuicao_sexo']]
        img = criar_grafico_pizza(labels, values, 'Distribuição por Sexo')
        if img:
            graficos_linha1.append(Image(img, width=7*cm, height=5*cm))
    
    # Fototipo
    if context['distribuicao_fototipo']:
        labels = [item.get('fototipo__nome') or 'Não informado' for item in context['distribuicao_fototipo']]
        values = [item['total'] for item in context['distribuicao_fototipo']]
        img = criar_grafico_pizza(labels, values, 'Distribuição por Fototipo')
        if img:
            graficos_linha1.append(Image(img, width=7*cm, height=5*cm))
    
    # Escolaridade
    if context['distribuicao_escolaridade']:
        labels = [item.get('escolaridade_label', 'Não informado') for item in context['distribuicao_escolaridade']]
        values = [item['total'] for item in context['distribuicao_escolaridade']]
        img = criar_grafico_pizza(labels, values, 'Distribuição por Escolaridade')
        if img:
            graficos_linha1.append(Image(img, width=7*cm, height=5*cm))
    
    if graficos_linha1:
        table_graficos = Table([graficos_linha1], colWidths=[7*cm] * len(graficos_linha1))
        story.append(table_graficos)
        story.append(Spacer(1, 0.6*cm))
    
    # ==========================================
    # GRÁFICOS - LINHA 2
    # ==========================================
    graficos_linha2 = []
    
    # Programas Sociais
    if context['distribuicao_programas']:
        labels = [item['participa'] for item in context['distribuicao_programas']]
        values = [item['total'] for item in context['distribuicao_programas']]
        img = criar_grafico_pizza(labels, values, 'Programas Sociais')
        if img:
            graficos_linha2.append(Image(img, width=7*cm, height=5*cm))
    
    # Deficiências
    if context['distribuicao_deficiencia']:
        labels = [item['tipo'] for item in context['distribuicao_deficiencia']]
        values = [item['total'] for item in context['distribuicao_deficiencia']]
        img = criar_grafico_pizza(labels, values, 'Pessoas com Deficiência')
        if img:
            graficos_linha2.append(Image(img, width=7*cm, height=5*cm))
    
    # Tipos de Deficiência
    if context['tipos_deficiencia']:
        labels = [item['tipo_deficiencia'] for item in context['tipos_deficiencia']]
        values = [item['total'] for item in context['tipos_deficiencia']]
        img = criar_grafico_pizza(labels, values, 'Tipos de Deficiência')
        if img:
            graficos_linha2.append(Image(img, width=7*cm, height=5*cm))
    
    if graficos_linha2:
        table_graficos2 = Table([graficos_linha2], colWidths=[7*cm] * len(graficos_linha2))
        story.append(table_graficos2)
        story.append(Spacer(1, 0.6*cm))
    
    # ==========================================
    # GRÁFICO DE BARRAS - FAIXAS ETÁRIAS
    # ==========================================
    if context['faixas_etarias']:
        story.append(Paragraph("Distribuição por Faixa Etária", style_subtitle))
        labels = [item['faixa'] for item in context['faixas_etarias']]
        values = [item['total'] for item in context['faixas_etarias']]
        img = criar_grafico_barras(labels, values, 'Faixas Etárias')
        if img:
            story.append(Image(img, width=24*cm, height=8*cm))
    
    # Gerar PDF com canvas personalizado
    doc.build(
        story,
        canvasmaker=lambda *args, **kwargs: DashboardCanvas(
            *args,
            titulo_dashboard='DASHBOARD - INTERESSADOS',
            data_emissao=data_emissao,
            **kwargs
        )
    )
    
    buffer.seek(0)
    return buffer


def gerar_pdf_eventos(context):
    """Gera PDF do dashboard de eventos com layout limpo"""
    buffer = BytesIO()
    
    # Data de emissão
    data_emissao = datetime.now().strftime('%d/%m/%Y às %H:%M')
    
    doc = SimpleDocTemplate(
        buffer,
        pagesize=landscape(A4),
        rightMargin=1.5*cm,
        leftMargin=1.5*cm,
        topMargin=3*cm,
        bottomMargin=1.5*cm
    )
    
    styles = getSampleStyleSheet()
    
    # Estilos personalizados
    style_subtitle = ParagraphStyle(
        'CustomSubtitle',
        parent=styles['Heading2'],
        fontSize=11,
        textColor=colors.HexColor('#2196F3'),
        spaceAfter=8,
        spaceBefore=12,
        fontName='Helvetica-Bold'
    )
    
    story = []
    
    # ==========================================
    # CARDS DE MÉTRICAS
    # ==========================================
    metricas_data = [
        ['Métrica', 'Valor'],
        ['Total de Eventos', str(context['total_eventos'])],
        ['Inscrições Abertas', str(context['eventos_inscricoes_abertas'])],
        ['Total de Turmas', str(context['total_turmas'])],
        ['Turmas em Andamento', str(context['turmas_em_andamento'])]
    ]
    
    metricas_table = Table(metricas_data, colWidths=[15*cm, 5*cm])
    metricas_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#2196F3')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('ALIGN', (1, 0), (1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 10),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 10),
        ('GRID', (0, 0), (-1, -1), 1, colors.grey),
        ('FONTSIZE', (0, 1), (-1, -1), 9),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#F5F5F5')])
    ]))
    
    story.append(metricas_table)
    story.append(Spacer(1, 0.6*cm))
    
    # ==========================================
    # EVENTOS POR STATUS
    # ==========================================
    story.append(Paragraph("Eventos por Status", style_subtitle))
    
    eventos_status_data = [['Status', 'Total', '%']]
    for item in context['eventos_por_status']:
        percentual = round((item['total'] / context['total_eventos'] * 100), 1) if context['total_eventos'] > 0 else 0
        eventos_status_data.append([
            item['status__nome'],
            str(item['total']),
            f"{percentual}%"
        ])
    
    eventos_status_table = Table(eventos_status_data, colWidths=[12*cm, 4*cm, 4*cm])
    eventos_status_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#2196F3')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('ALIGN', (1, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 10),
        ('GRID', (0, 0), (-1, -1), 1, colors.grey),
        ('FONTSIZE', (0, 1), (-1, -1), 9),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#F5F5F5')])
    ]))
    
    story.append(eventos_status_table)
    story.append(Spacer(1, 0.6*cm))
    
    # ==========================================
    # STATUS TEMPORAL DAS TURMAS
    # ==========================================
    story.append(Paragraph("Status Temporal das Turmas", style_subtitle))
    
    turmas_status_data = [
        ['Status', 'Total'],
        ['Futuras (Não iniciadas)', str(context['turmas_futuras'])],
        ['Em Andamento', str(context['turmas_em_andamento'])],
        ['Encerradas', str(context['turmas_encerradas'])]
    ]
    
    turmas_status_table = Table(turmas_status_data, colWidths=[15*cm, 5*cm])
    turmas_status_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#2196F3')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('ALIGN', (1, 0), (1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 10),
        ('GRID', (0, 0), (-1, -1), 1, colors.grey),
        ('FONTSIZE', (0, 1), (-1, -1), 9),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#F5F5F5')])
    ]))
    
    story.append(turmas_status_table)
    story.append(Spacer(1, 0.6*cm))
    
    # ==========================================
    # TOP 5 CURSOS COM MAIS INSCRIÇÕES
    # ==========================================
    story.append(Paragraph("Top 5 Cursos com Mais Inscrições", style_subtitle))
    
    top_inscricoes_data = [['Curso/Evento', 'Inscrições']]
    for item in context['top_eventos_inscricoes']:
        top_inscricoes_data.append([
            item['evento__nome'],
            str(item['total_inscricoes'])
        ])
    
    if len(top_inscricoes_data) == 1:
        top_inscricoes_data.append(['Nenhuma inscrição registrada', '-'])
    
    top_inscricoes_table = Table(top_inscricoes_data, colWidths=[15*cm, 5*cm])
    top_inscricoes_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#2196F3')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('ALIGN', (1, 0), (1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 10),
        ('GRID', (0, 0), (-1, -1), 1, colors.grey),
        ('FONTSIZE', (0, 1), (-1, -1), 9),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#F5F5F5')])
    ]))
    
    story.append(top_inscricoes_table)
    
    # Gerar PDF
    doc.build(
        story,
        canvasmaker=lambda *args, **kwargs: DashboardCanvas(
            *args,
            titulo_dashboard='DASHBOARD - EVENTOS E CURSOS',
            data_emissao=data_emissao,
            **kwargs
        )
    )
    
    buffer.seek(0)
    return buffer


def gerar_pdf_academico(context):
    """Gera PDF do dashboard acadêmico"""
    buffer = BytesIO()
    data_emissao = datetime.now().strftime('%d/%m/%Y às %H:%M')
    
    doc = SimpleDocTemplate(
        buffer, pagesize=landscape(A4),
        rightMargin=1.5*cm, leftMargin=1.5*cm,
        topMargin=3*cm, bottomMargin=1.5*cm
    )
    
    styles = getSampleStyleSheet()
    style_subtitle = ParagraphStyle(
        'CustomSubtitle', parent=styles['Heading2'],
        fontSize=11, textColor=colors.HexColor('#2196F3'),
        spaceAfter=8, spaceBefore=12, fontName='Helvetica-Bold'
    )
    
    story = []
    
    # Métricas
    metricas_data = [
        ['Métrica', 'Valor'],
        ['Total de Avaliações', str(context['total_avaliacoes'])],
        ['Aprovados', str(context['total_aprovados'])],
        ['Reprovados', str(context['total_reprovados'])],
        ['Taxa de Aprovação (%)', f"{context['taxa_aprovacao']}%"],
        ['Média de Notas', str(context['media_notas'])],
        ['Certificados Emitidos', str(context['certificados_emitidos'])]
    ]
    
    metricas_table = Table(metricas_data, colWidths=[15*cm, 5*cm])
    metricas_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#2196F3')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('ALIGN', (1, 0), (1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 10),
        ('GRID', (0, 0), (-1, -1), 1, colors.grey),
        ('FONTSIZE', (0, 1), (-1, -1), 9),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#F5F5F5')])
    ]))
    
    story.append(metricas_table)
    story.append(Spacer(1, 0.6*cm))
    
    # Top Cursos
    story.append(Paragraph("Top 5 Cursos com Mais Aprovados", style_subtitle))
    
    top_data = [['Curso', 'Aprovados']]
    for item in context['top_cursos_aprovados']:
        top_data.append([item['matricula__turma__evento__nome'], str(item['total'])])
    
    if len(top_data) == 1:
        top_data.append(['Nenhum dado disponível', '-'])
    
    top_table = Table(top_data, colWidths=[15*cm, 5*cm])
    top_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#2196F3')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('ALIGN', (1, 0), (1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 10),
        ('GRID', (0, 0), (-1, -1), 1, colors.grey),
        ('FONTSIZE', (0, 1), (-1, -1), 9),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#F5F5F5')])
    ]))
    
    story.append(top_table)
    
    doc.build(story, canvasmaker=lambda *args, **kwargs: DashboardCanvas(
        *args, titulo_dashboard='DASHBOARD - INFORMAÇÕES ACADÊMICAS',
        data_emissao=data_emissao, **kwargs
    ))
    
    buffer.seek(0)
    return buffer


def gerar_pdf_processo_seletivo(context):
    """Gera PDF do dashboard de processo seletivo"""
    buffer = BytesIO()
    data_emissao = datetime.now().strftime('%d/%m/%Y às %H:%M')
    
    doc = SimpleDocTemplate(
        buffer, pagesize=landscape(A4),
        rightMargin=1.5*cm, leftMargin=1.5*cm,
        topMargin=3*cm, bottomMargin=1.5*cm
    )
    
    styles = getSampleStyleSheet()
    style_subtitle = ParagraphStyle(
        'CustomSubtitle', parent=styles['Heading2'],
        fontSize=11, textColor=colors.HexColor('#2196F3'),
        spaceAfter=8, spaceBefore=12, fontName='Helvetica-Bold'
    )
    
    story = []
    
    # Métricas
    metricas_data = [
        ['Métrica', 'Valor'],
        ['Total de Inscrições', str(context['total_inscricoes'])],
        ['Inscrições Recentes (30 dias)', str(context['inscricoes_recentes'])],
        ['Total de Classificações', str(context['total_classificacoes'])],
        ['Classificados', str(context['classificados'])],
        ['Lista de Espera', str(context['lista_espera'])],
        ['Taxa de Classificação (%)', f"{context['taxa_classificacao']}%"]
    ]
    
    metricas_table = Table(metricas_data, colWidths=[15*cm, 5*cm])
    metricas_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#2196F3')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('ALIGN', (1, 0), (1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 10),
        ('GRID', (0, 0), (-1, -1), 1, colors.grey),
        ('FONTSIZE', (0, 1), (-1, -1), 9),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#F5F5F5')])
    ]))
    
    story.append(metricas_table)
    story.append(Spacer(1, 0.6*cm))
    
    # Top Eventos
    story.append(Paragraph("Top 5 Eventos com Mais Inscrições", style_subtitle))
    
    top_data = [['Evento', 'Inscrições']]
    for item in context['top_eventos_inscricoes']:
        top_data.append([item['evento__nome'], str(item['total'])])
    
    if len(top_data) == 1:
        top_data.append(['Nenhum dado disponível', '-'])
    
    top_table = Table(top_data, colWidths=[15*cm, 5*cm])
    top_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#2196F3')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('ALIGN', (1, 0), (1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 10),
        ('GRID', (0, 0), (-1, -1), 1, colors.grey),
        ('FONTSIZE', (0, 1), (-1, -1), 9),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#F5F5F5')])
    ]))
    
    story.append(top_table)
    
    doc.build(story, canvasmaker=lambda *args, **kwargs: DashboardCanvas(
        *args, titulo_dashboard='DASHBOARD - PROCESSO SELETIVO',
        data_emissao=data_emissao, **kwargs
    ))
    
    buffer.seek(0)
    return buffer

