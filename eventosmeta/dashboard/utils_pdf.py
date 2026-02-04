"""
Utilidades para geração de PDF dos dashboards
Arquivo: dashboard/utils_pdf.py
Data: 04/02/2026
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


class NumberedCanvas(canvas.Canvas):
    """Canvas com numeração de páginas"""
    def __init__(self, *args, **kwargs):
        canvas.Canvas.__init__(self, *args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_page_number(num_pages)
            canvas.Canvas.showPage(self)
        canvas.Canvas.save(self)

    def draw_page_number(self, page_count):
        self.setFont("Helvetica", 8)
        self.drawRightString(
            landscape(A4)[0] - 1*cm, 0.8*cm,
            f"Página {self._pageNumber} de {page_count}"
        )
        self.drawString(1*cm, 0.8*cm, f"Gerado em: {datetime.now().strftime('%d/%m/%Y %H:%M')}")


def gerar_pdf_interessados(context):
    """Gera PDF do dashboard de interessados"""
    buffer = BytesIO()
    
    doc = SimpleDocTemplate(
        buffer, pagesize=landscape(A4),
        rightMargin=1.5*cm, leftMargin=1.5*cm,
        topMargin=1.5*cm, bottomMargin=2*cm
    )
    
    styles = getSampleStyleSheet()
    
    style_title = ParagraphStyle(
        'CustomTitle', parent=styles['Heading1'],
        fontSize=16, textColor=colors.HexColor('#2196F3'),
        spaceAfter=8, alignment=TA_CENTER, fontName='Helvetica-Bold'
    )
    
    style_subtitle = ParagraphStyle(
        'CustomSubtitle', parent=styles['Heading2'],
        fontSize=12, textColor=colors.HexColor('#333333'),
        spaceAfter=8, spaceBefore=12, fontName='Helvetica-Bold'
    )
    
    story = []
    
    # Cabeçalho
    story.append(Paragraph("📊 Dashboard - Interessados", style_title))
    story.append(Spacer(1, 0.5*cm))
    
    # Métricas
    metricas_data = [
        ['Métrica', 'Valor'],
        ['Total de Interessados', str(context['total_interessados'])],
        ['Com Matrícula', str(context['interessados_matriculados'])],
        ['Sem Matrícula', str(context['interessados_sem_matricula'])],
        ['Cadastros (30 dias)', str(context['cadastros_recentes'])]
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
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#F5F5F5')])
    ]))
    
    story.append(metricas_table)
    story.append(Spacer(1, 0.6*cm))
    
    # Gráficos - Linha 1
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
    
    # Gráficos - Linha 2
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
    
    # Faixas Etárias (Barras)
    if context['faixas_etarias']:
        story.append(Paragraph("Distribuição por Faixa Etária", style_subtitle))
        labels = [item['faixa'] for item in context['faixas_etarias']]
        values = [item['total'] for item in context['faixas_etarias']]
        img = criar_grafico_barras(labels, values, 'Faixas Etárias')
        if img:
            story.append(Image(img, width=24*cm, height=8*cm))
    
    # Gerar PDF
    doc.build(story, canvasmaker=NumberedCanvas)
    buffer.seek(0)
    return buffer

