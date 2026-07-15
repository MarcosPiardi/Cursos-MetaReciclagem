"""
Gerador de Certificados em PDF
Arquivo: apps/academico/certificado.py

Alteração: Logos trocados, tamanhos ajustados, layout corrigido
Data: 02/02/2026
"""

from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib.units import cm
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from django.conf import settings
import os
from datetime import datetime


class GeradorCertificado:
    """Classe para gerar certificados em PDF"""
    
    def __init__(self, avaliacao):
        self.avaliacao = avaliacao
        self.matricula = avaliacao.matricula
        self.aluno = self.matricula.interessado
        self.turma = self.matricula.turma
        self.evento = self.turma.evento
        
        # Configurações da página (A4 paisagem)
        self.pagesize = landscape(A4)
        self.width, self.height = self.pagesize
        
        # Caminhos das imagens
        self.static_path = os.path.join(settings.BASE_DIR, 'static', 'images')
        self.logo_meta = os.path.join(self.static_path, 'favicon-metareciclagem.png')
        self.brasao = os.path.join(self.static_path, 'brasao-2.png')
    
    def gerar_pdf(self, buffer):
        """Gera o PDF do certificado"""
        
        # Criar canvas
        p = canvas.Canvas(buffer, pagesize=self.pagesize)
        
        # Desenhar borda decorativa
        self._desenhar_borda(p)
        
        # Adicionar logos (TROCADOS DE LADO)
        self._adicionar_logos(p)
        
        # Adicionar título
        self._adicionar_titulo(p)
        
        # Adicionar texto do certificado
        self._adicionar_texto_certificado(p)
        
        # Adicionar informações do curso
        self._adicionar_info_curso(p)
        
        # Adicionar data e assinaturas
        self._adicionar_rodape(p)
        
        # Finalizar
        p.showPage()
        p.save()
        
        return buffer
    
    def _desenhar_borda(self, p):
        """Desenha borda decorativa dourada"""
        # Borda externa (dourada)
        p.setStrokeColorRGB(0.8, 0.6, 0.0)  # Dourado
        p.setLineWidth(3)
        p.rect(1*cm, 1*cm, self.width - 2*cm, self.height - 2*cm)
        
        # Borda interna
        p.setStrokeColorRGB(0.6, 0.4, 0.0)  # Dourado escuro
        p.setLineWidth(1)
        p.rect(1.3*cm, 1.3*cm, self.width - 2.6*cm, self.height - 2.6*cm)
    
    def _adicionar_logos(self, p):
        """Adiciona logos (TROCADOS: Brasão esquerda, MetaReciclagem direita)"""
        try:
            # Brasão (ESQUERDA) - ajustado para não cortar a borda
            if os.path.exists(self.brasao):
                p.drawImage(
                    self.brasao,
                    2*cm, self.height - 4.5*cm,  # Ajustado para não cortar
                    width=3*cm, height=3*cm,
                    preserveAspectRatio=True,
                    mask='auto'
                )
            
            # Logo MetaReciclagem (DIREITA) - AUMENTADO
            if os.path.exists(self.logo_meta):
                p.drawImage(
                    self.logo_meta,
                    self.width - 6*cm, self.height - 4.8*cm,  # Ajustado
                    width=4*cm, height=4*cm,  # AUMENTADO de 3cm para 4cm
                    preserveAspectRatio=True,
                    mask='auto'
                )
        except Exception as e:
            print(f"Erro ao carregar imagens: {str(e)}")
    
    def _adicionar_titulo(self, p):
        """Adiciona título 'CERTIFICADO'"""
        p.setFont("Helvetica-Bold", 36)
        p.setFillColorRGB(0.1, 0.3, 0.6)  # Azul escuro
        
        titulo = "CERTIFICADO"
        titulo_width = p.stringWidth(titulo, "Helvetica-Bold", 36)
        x = (self.width - titulo_width) / 2
        y = self.height - 5.5*cm  # SUBIU de 6cm para 5.5cm
        
        p.drawString(x, y, titulo)
    
    def _adicionar_texto_certificado(self, p):
        """Adiciona texto principal do certificado"""
        y = self.height - 7.5*cm  # SUBIU de 8cm para 7.5cm
        
        # Texto de certificação
        p.setFont("Helvetica", 14)
        p.setFillColorRGB(0, 0, 0)
        
        texto1 = "Certificamos que"
        texto1_width = p.stringWidth(texto1, "Helvetica", 14)
        p.drawString((self.width - texto1_width) / 2, y, texto1)
        
        # Nome do aluno (destaque)
        y -= 1.5*cm
        p.setFont("Helvetica-Bold", 20)
        p.setFillColorRGB(0.1, 0.3, 0.6)
        
        nome_aluno = self.aluno.nome.upper()
        nome_width = p.stringWidth(nome_aluno, "Helvetica-Bold", 20)
        p.drawString((self.width - nome_width) / 2, y, nome_aluno)
        
        # Linha decorativa sob o nome
        p.setStrokeColorRGB(0.8, 0.6, 0.0)
        p.setLineWidth(1)
        p.line(
            (self.width - nome_width) / 2 - 0.5*cm, y - 0.2*cm,
            (self.width + nome_width) / 2 + 0.5*cm, y - 0.2*cm
        )
        
        # CPF
        y -= 1*cm
        p.setFont("Helvetica", 10)
        p.setFillColorRGB(0.3, 0.3, 0.3)
        cpf = self.aluno.cpf
        cpf_formatado = f"CPF: {cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"
        cpf_width = p.stringWidth(cpf_formatado, "Helvetica", 10)
        p.drawString((self.width - cpf_width) / 2, y, cpf_formatado)
        
        # Texto continuação
        y -= 1.5*cm
        p.setFont("Helvetica", 14)
        p.setFillColorRGB(0, 0, 0)
        
        texto2 = "participou e concluiu com aproveitamento o curso de"
        texto2_width = p.stringWidth(texto2, "Helvetica", 14)
        p.drawString((self.width - texto2_width) / 2, y, texto2)
    
    def _adicionar_info_curso(self, p):
        """Adiciona informações do curso"""
        y = self.height - 13*cm  # SUBIU de 13.5cm para 13cm
        
        # Nome do curso
        p.setFont("Helvetica-Bold", 18)
        p.setFillColorRGB(0.1, 0.3, 0.6)
        
        nome_curso = self.evento.nome.upper()
        curso_width = p.stringWidth(nome_curso, "Helvetica-Bold", 18)
        p.drawString((self.width - curso_width) / 2, y, nome_curso)
        
        # Carga horária e período
        y -= 1.2*cm
        p.setFont("Helvetica", 12)
        p.setFillColorRGB(0, 0, 0)
        
        # Calcular carga horária (se disponível)
        carga_horaria = f"{self.evento.carga_horaria}h" if hasattr(self.evento, 'carga_horaria') and self.evento.carga_horaria else "40h"
        
        periodo = f"com carga horária de {carga_horaria}"
        
        # Adicionar datas se disponível
        if self.turma.data_inicio and self.turma.data_fim:
            data_inicio = self.turma.data_inicio.strftime("%d/%m/%Y")
            data_fim = self.turma.data_fim.strftime("%d/%m/%Y")
            periodo += f", realizado no período de {data_inicio} a {data_fim}."
        else:
            periodo += "."
        
        periodo_width = p.stringWidth(periodo, "Helvetica", 12)
        p.drawString((self.width - periodo_width) / 2, y, periodo)
        
        # Nota e frequência - ESPAÇAMENTO AUMENTADO
        y -= 1.3*cm  # AUMENTADO de 1cm para 1.3cm
        p.setFont("Helvetica", 11)
        p.setFillColorRGB(0.3, 0.3, 0.3)
        
        nota = f"Nota: {self.avaliacao.nota_final}" if self.avaliacao.nota_final else "Nota: -"
        freq = f"Frequência: {self.avaliacao.frequencia}%"
        
        desempenho = f"{nota}  |  {freq}"
        desempenho_width = p.stringWidth(desempenho, "Helvetica", 11)
        p.drawString((self.width - desempenho_width) / 2, y, desempenho)
    
    def _adicionar_rodape(self, p):
        """Adiciona data de emissão e linha para assinatura - AJUSTADO"""
        y = 4.5*cm  # SUBIU de 3.5cm para 4.5cm (mais distante da borda)
        
        # Data de emissão
        p.setFont("Helvetica", 11)
        p.setFillColorRGB(0, 0, 0)
        
        if self.avaliacao.data_emissao_certificado:
            data_emissao = self.avaliacao.data_emissao_certificado.strftime("%d de %B de %Y")
        else:
            data_emissao = datetime.now().strftime("%d de %B de %Y")
        
        # Traduzir mês para português
        meses = {
            'January': 'janeiro', 'February': 'fevereiro', 'March': 'março',
            'April': 'abril', 'May': 'maio', 'June': 'junho',
            'July': 'julho', 'August': 'agosto', 'September': 'setembro',
            'October': 'outubro', 'November': 'novembro', 'December': 'dezembro'
        }
        for eng, pt in meses.items():
            data_emissao = data_emissao.replace(eng, pt)
        
        cidade = "Sorocaba, SP"  # Ajuste conforme sua cidade
        local_data = f"{cidade}, {data_emissao}."
        
        local_width = p.stringWidth(local_data, "Helvetica", 11)
        p.drawString((self.width - local_width) / 2, y, local_data)
        
        # Linha para assinatura - AJUSTADA
        y -= 1.5*cm  # REDUZIDO de 2cm para 1.5cm
        linha_x_inicio = self.width / 2 - 6*cm
        linha_x_fim = self.width / 2 + 6*cm
        
        p.setStrokeColorRGB(0, 0, 0)
        p.setLineWidth(1)
        p.line(linha_x_inicio, y, linha_x_fim, y)
        
        # Texto da assinatura - AJUSTADO
        y -= 0.4*cm  # REDUZIDO de 0.5cm para 0.4cm
        p.setFont("Helvetica", 10)
        
        assinatura_texto = "Coordenação do Projeto MetaReciclagem"
        assinatura_width = p.stringWidth(assinatura_texto, "Helvetica", 10)
        p.drawString((self.width - assinatura_width) / 2, y, assinatura_texto)

