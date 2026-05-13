import tkinter as tk
from tkinter import filedialog, messagebox
from docx import Document
from docx.text.paragraph import Paragraph
from docx.table import Table as TableBase, _Cell
from docx.oxml.ns import qn
import os
from datetime import datetime
import re


def iter_block_items(parent):
    """
    Gera parágrafos e tabelas em ordem do documento ou célula.
    """
    if isinstance(parent, Document):
        parent_elm = parent.element.body
    elif isinstance(parent, _Cell):
        parent_elm = parent._tc
    else:
        raise ValueError("parent deve ser Document ou _Cell")

    for child in parent_elm.iterchildren():
        if child.tag.endswith('p'):
            yield Paragraph(child, parent)
        elif child.tag.endswith('tbl'):
            yield TableBase(child, parent)


def get_formatted_text(para):
    """
    Extrai o texto do parágrafo com formatação Markdown para negrito e itálico.
    """
    parts = []
    for run in para.runs:
        text = run.text.replace('\r', '').replace('\n', ' ').replace('\t', ' ')
        if run.bold is True and run.italic is True:
            parts.append(f"***{text}***")
        elif run.bold is True:
            parts.append(f"**{text}**")
        elif run.italic is True:
            parts.append(f"*{text}*")
        else:
            parts.append(text)
    return ''.join(parts)


def is_list_item(para):
    """
    Verifica se o parágrafo é um item de lista (bullets ou numerada).
    """
    p_elm = para._element
    p_pr = p_elm.get_or_add_pPr()
    num_pr = p_pr.find(qn('w:numPr'))
    return num_pr is not None


def get_list_level(para):
    """
    Retorna o nível da lista (1 para primeiro nível).
    """
    p_elm = para._element
    p_pr = p_elm.get_or_add_pPr()
    num_pr = p_pr.find(qn('w:numPr'))
    if num_pr is None:
        return 0
    ilvl = num_pr.find(qn('w:ilvl'))
    if ilvl is not None:
        level_str = ilvl.get(qn('w:val'))
        if level_str is not None:
            try:
                return int(level_str) + 1
            except ValueError:
                pass
    return 1


def process_paragraph(para):
    """
    Converte parágrafo para linha de Markdown estruturado.
    """
    text_md = get_formatted_text(para).strip()
    if not text_md:
        return ''

    style_name = para.style.name.lower() if para.style and para.style.name else ''
    if 'heading' in style_name:
        match = re.search(r'heading\s*(\d+)', style_name)
        level = int(match.group(1)) if match else 1
        return f"{'#' * level} {text_md}"
    elif is_list_item(para):
        level = get_list_level(para)
        indent = '  ' * (level - 1)
        return f"{indent}- {text_md}"
    else:
        return text_md


def table_to_md(table):
    """
    Converte tabela DOCX para tabela Markdown.
    """
    if not table.rows:
        return ''

    md_lines = []
    # Linha de cabeçalho
    header_cells = [cell.text.strip() for cell in table.rows[0].cells]
    md_lines.append('| ' + ' | '.join(header_cells) + ' |')
    # Separador
    md_lines.append('| ' + ' | '.join(['---'] * len(header_cells)) + ' |')
    # Demais linhas
    for row in table.rows[1:]:
        cells = [cell.text.strip() for cell in row.cells]
        md_lines.append('| ' + ' | '.join(cells) + ' |')
    return '\n'.join(md_lines)


# Interface gráfica
root = tk.Tk()
root.title("Conversor DOCX para Markdown")
root.geometry("450x250")

label = tk.Label(root, text="Selecione um arquivo DOCX para converter em Markdown estruturado.\n\nDiretório inicial: C:\\PMS\\PMS2025\\Inscr-Meta", justify=tk.CENTER, font=('Arial', 10))
label.pack(pady=20)

btn = tk.Button(root, text="Selecionar Arquivo DOCX", command=lambda: None, font=('Arial', 12), bg='#4CAF50', fg='white', height=2, width=25)
btn.pack(pady=10)


def select_and_convert():
    """
    Função principal: seleciona arquivo, processa e salva.
    """
    try:
        start_dir = r"C:\PMS\PMS2025\Inscr-Meta"
        file_path = filedialog.askopenfilename(
            initialdir=start_dir,
            title="Selecione o arquivo DOCX",
            filetypes=[("Arquivos DOCX", "*.docx")]
        )
        if not file_path:
            return

        # Lê o documento
        doc = Document(file_path)

        # Processa blocos
        md_lines = []
        for block in iter_block_items(doc):
            if isinstance(block, Paragraph):
                para_md = process_paragraph(block)
                if para_md.strip():
                    md_lines.append(para_md)
                    md_lines.append('')
            elif isinstance(block, TableBase):
                table_md = table_to_md(block)
                if table_md.strip():
                    md_lines.append('')
                    md_lines.extend(table_md.splitlines())
                    md_lines.append('')

        content = '\n'.join(md_lines).rstrip() + '\n'

        # Salva arquivo
        data_str = datetime.now().strftime('%Y-%m-%d')
        out_dir = 'docs/estática'
        os.makedirs(out_dir, exist_ok=True)
        out_file = os.path.join(out_dir, f'DOCX_para_MARKDOWN_{data_str}.md')

        with open(out_file, 'w', encoding='utf-8-sig') as f:
            f.write(content)

        messagebox.showinfo("Sucesso", f"Conversão concluída!\n\nSalvo em:\n{out_file}")

    except Exception as e:
        messagebox.showerror("Erro", f"Falha no processamento:\n{str(e)}\n\nVerifique se o arquivo é válido e python-docx está instalado.")


btn.config(command=select_and_convert)

root.mainloop()

