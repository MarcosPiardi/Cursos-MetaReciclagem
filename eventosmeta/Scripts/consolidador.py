import os
import glob
import re
from docx import Document
from sentence_transformers import SentenceTransformer, util
import torch

# Diretórios de input e output
input_dir = r"C:\PMS\PMS2025\Inscr-Meta\prg-Meta\Eventos-MetaReciclagem\eventosmeta\input"
output_path = r"C:\PMS\PMS2025\Inscr-Meta\prg-Meta\Eventos-MetaReciclagem\eventosmeta\input\relatorio_consolidado.md"

# Função para dividir texto em sentenças (multilíngue aproximado)
def split_sentences(text):
    sentences = re.split(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?|\!)\s', text)
    return [s.strip() for s in sentences if len(s.strip()) > 10]

# Função para detectar negação
neg_words = ['não', 'nao', 'nunca', 'jamais', 'nenhum', 'ninguém', 'negativo']
def has_negation(sentence):
    sentence_lower = sentence.lower()
    return any(word in sentence_lower for word in neg_words)

# Lista para armazenar todas as sentenças com origem
all_sentences = []
all_files = []

# Padrões de arquivos
patterns = ['*.docx', '*.txt', '*.md']

print("*** INICIANDO CONSOLIDAÇÃO DE ARQUIVOS ***")

for pattern in patterns:
    files = glob.glob(os.path.join(input_dir, pattern))
    for file_path in files:
        filename = os.path.basename(file_path)
        print(f"\033[94m=== LENDO ARQUIVO: {filename} ===\033[0m")
        try:
            if file_path.endswith('.txt') or file_path.endswith('.md'):
                with open(file_path, 'r', encoding='utf-8') as f:
                    text = f.read()
            elif file_path.endswith('.docx'):
                doc = Document(file_path)
                text = '\n'.join([para.text for para in doc.paragraphs])
            else:
                continue

            sentences = split_sentences(text)
            for sent in sentences:
                all_sentences.append(sent)
                all_files.append(filename)
            print(f"   -> {len(sentences)} sentenças extraídas.")
        except Exception as e:
            print(f"   ERRO ao processar {filename}: {str(e)}")

if not all_sentences:
    print("Nenhuma sentença encontrada!")
    exit(1)

print(f"*** PROCESSANDO {len(all_sentences)} SENTENÇAS TOTAIS ***")

# Carregar modelo de embeddings multilíngue
model = SentenceTransformer('paraphrase-multilingual-MiniLM-L12-v2')
embeddings = model.encode(all_sentences, convert_to_tensor=True)

# Thresholds
threshold_red = 0.75
threshold_conf = 0.80

# Detectar redundâncias e conflitos
redundancias_intra = []
redundancias_inter = []
conflitos = []

print("*** CALCULANDO SIMILARIDADES ***")
for i in range(len(all_sentences)):
    for j in range(i + 1, len(all_sentences)):
        sim = util.cos_sim(embeddings[i:i+1], embeddings[j:j+1]).item()
        file_i = all_files[i]
        file_j = all_files[j]
        if sim > threshold_red:
            pair = (all_sentences[i][:100] + '...', all_sentences[j][:100] + '...', round(sim, 3))
            if file_i == file_j:
                redundancias_intra.append((*pair, file_i))
            else:
                redundancias_inter.append((*pair, file_i, file_j))
        if sim > threshold_conf:
            neg1 = has_negation(all_sentences[i])
            neg2 = has_negation(all_sentences[j])
            if neg1 != neg2:
                conflitos.append((all_sentences[i][:100] + '...', all_sentences[j][:100] + '...', round(sim, 3), file_i, file_j))

# Conteúdo consolidado (seleção gulosa sem duplicatas)
print("*** GERANDO CONTEÚDO CONSOLIDADO ***")
used_indices = set()
consolidated_sentences = []
for i in range(len(all_sentences)):
    if i in used_indices:
        continue
    is_similar = any(util.cos_sim(embeddings[i:i+1], embeddings[uj:uj+1]).item() > threshold_red for uj in used_indices)
    if not is_similar:
        consolidated_sentences.append(all_sentences[i])
        used_indices.add(i)

# Resumo executivo (primeiras sentenças principais)
resumo = ' '.join(consolidated_sentences[:3])[:500] + '...'

# Dados obsoletos (datas antes de 2024)
print("*** DETECTANDO DADOS OBSOLETOS ***")
obsolete = []
date_pattern = r'\b(20[0-3]\d)\b'
for sent, filename in zip(all_sentences, all_files):
    dates = re.findall(date_pattern, sent)
    if dates and any(int(d) < 2024 for d in dates):
        obsolete.append((sent[:100] + '...', filename))

# Gerar relatório Markdown
print("*** GERANDO RELATÓRIO MARKDOWN ***")
md_content = "# Relatório Consolidado\n\n"

md_content += "## Resumo Executivo\n" + resumo + "\n\n"

md_content += "## Conteúdo Consolidado (sem duplicatas)\n"
for sent in consolidated_sentences:
    md_content += f"- {sent[:200]}...\n"
md_content += "\n"

md_content += "## Redundâncias Intra-Documento\n"
for r in redundancias_intra[:20]:
    md_content += f"- **{r[3]}**: '{r[0]}' ~ '{r[1]}' (sim={r[2]})\n"
md_content += "\n"

md_content += "## Redundâncias Inter-Documento\n"
for r in redundancias_inter[:20]:
    md_content += f"- **{r[3]} vs {r[4]}**: '{r[0]}' ~ '{r[1]}' (sim={r[2]})\n"
md_content += "\n"

md_content += "## Conflitos Potenciais\n"
for c in conflitos[:20]:
    md_content += f"- **{c[3]} vs {c[4]}**: '{c[0]}' vs '{c[1]}' (sim={c[2]}, neg1={c[5]}, neg2={c[6]})\n"
md_content += "\n"

md_content += "## Dados Obsoletos\n"
for o in obsolete[:20]:
    md_content += f"- **{o[1]}**: '{o[0]}'\n"

# Salvar relatório
try:
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(md_content)
    print(f"\033[92m*** RELATÓRIO GERADO COM SUCESSO: {output_path} ***\033[0m")
except Exception as e:
    print(f"ERRO ao salvar relatório: {e}")

print("*** PROCESSO CONCLUÍDO ***")

