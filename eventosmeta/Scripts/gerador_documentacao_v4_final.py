# -*- coding: utf-8 -*-
import os
import shutil
from datetime import datetime
from docx import Document

# Caminhos fixos no topo (ajuste conforme necessário)
DOCX_PATH = r'C:\PMS\PMS2025\Inscr-Meta\Contexto para alimentar Scripts\ESTATICO_Arquitetura-ADRs-Regras-Glossario-MER_2026-04-24.docx'
BANCO_PATH = r'C:\PMS\PMS2025\Inscr-Meta\Contexto para alimentar Scripts\documentacao_banco.md'
CODIGO_PATH = r'C:\PMS\PMS2025\Inscr-Meta\Contexto para alimentar Scripts\2026-04-23_TodasPastasConcatenadas.txt'
DIAGRAMA_PATH = r'C:\PMS\PMS2025\Inscr-Meta\Contexto para alimentar Scripts\Diagrama ER - bdmetareciclagem - public.png'
OUTPUT_DIR = r'C:\PMS\PMS2025\Inscr-Meta\Contexto para alimentar Scripts\Resultados_Scripts'

def extrair_secao(doc, titulo):
    """Extrai o conteúdo da seção especificada do documento DOCX."""
    content = []
    in_section = False
    titulos_proximos = ['adrs', 'regras', 'glossário']
    for para in doc.paragraphs:
        text = para.text.strip()
        if not text:
            continue
        text_lower = text.lower()
        if titulo.lower() in text_lower:
            in_section = True
            continue
        if in_section:
            if any(t in text_lower for t in titulos_proximos):
                break
            content.append(para.text)
    return '\n\n'.join(content)

# Carregar documento DOCX
try:
    doc = Document(DOCX_PATH)
except FileNotFoundError:
    print(f"Erro: Arquivo {DOCX_PATH} não encontrado.")
    exit(1)

# Extrair seções do DOCX
adrs_content = extrair_secao(doc, "ADRs")
regras_content = extrair_secao(doc, "Regras")
glossario_content = extrair_secao(doc, "Glossário")

# Ler banco de dados (máx 50 linhas)
try:
    with open(BANCO_PATH, 'r', encoding='utf-8') as f:
        banco_lines = f.readlines()[:50]
    banco_text = ''.join(banco_lines)
except FileNotFoundError:
    banco_text = "Arquivo de banco não encontrado."

# Ler código fonte (máx 100 linhas)
try:
    with open(CODIGO_PATH, 'r', encoding='utf-8') as f:
        codigo_lines = f.readlines()[:100]
    codigo_text = ''.join(codigo_lines)
except FileNotFoundError:
    codigo_text = "Arquivo de código não encontrado."

# Criar diretório de saída e copiar diagrama PNG
os.makedirs(OUTPUT_DIR, exist_ok=True)
png_dest = os.path.join(OUTPUT_DIR, "diagrama.png")
try:
    shutil.copy2(DIAGRAMA_PATH, png_dest)
except FileNotFoundError:
    print(f"Aviso: Arquivo {DIAGRAMA_PATH} não encontrado.")

# Gerar nome do arquivo com data
data_hoje = datetime.now().strftime("%Y-%m-%d")
md_filename = f"ESTÁTICO_Documentacao-Consolidada_{data_hoje}.md"
md_path = os.path.join(OUTPUT_DIR, md_filename)

# Gerar conteúdo Markdown corrigindo f-string triple-quoted com quebras de linha apropriadas
md_content = f"""# Documentação Consolidada ESTÁTICA\n\n## 1. ADRs\n\n{adrs_content}\n\n## 2. Regras de Negócio\n\n{regras_content}\n\n## 3. Glossário\n\n{glossario_content}\n\n## 4. Banco de Dados (primeiras 50 linhas)\n\n```sql\n{banco_text}```\n\n## 5. Código Fonte (primeiras 100 linhas)\n\n```python\n{codigo_text}```\n\n![Diagrama do Sistema](diagrama.png)"""

# Salvar arquivo Markdown em UTF-8
with open(md_path, 'w', encoding='utf-8') as f:
    f.write(md_content)

print(f"Documentação consolidada gerada com sucesso em: {md_path}")


