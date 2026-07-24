import os
from pathlib import Path

# Pega o diretório raiz onde este script está rodando
BASE_DIR = Path(__file__).resolve().parent

def buscar_templates_orfaos():
    templates = []

    # 1. Encontra todos os arquivos .html dentro de pastas chamadas 'templates'
    for path in BASE_DIR.rglob('*.html'):
        parts = path.parts
        if 'templates' in parts:
            # Pega o caminho relativo do template a partir de 'templates/'
            # Exemplo: 'portal/index.html' ou 'academico/gestao_matricula.html'
            idx = len(parts) - 1 - parts[::-1].index('templates')
            rel_path = "/".join(parts[idx+1:])
            templates.append((rel_path, path))

    print(f"🔍 Encontrados {len(templates)} templates HTML no projeto. Analisando referências...\n")

    # 2. Carrega todo o texto dos arquivos .py e .html do projeto na memória
    conteudo_projeto = ""
    for ext in ['*.py', '*.html']:
        for path in BASE_DIR.rglob(ext):
            # Ignora o próprio script de busca
            if path.name == 'encontrar_templates_orfaos.py':
                continue
            try:
                conteudo_projeto += path.read_text(encoding='utf-8', errors='ignore') + "\n"
            except Exception:
                pass

    # 3. Verifica quais templates nunca aparecem no texto do projeto
    orfaos = []
    for rel_path, full_path in templates:
        nome_arquivo = Path(rel_path).name
        
        # Se nem o caminho relativo ('academico/gestao_matricula.html') 
        # nem o nome do arquivo ('gestao_matricula.html') aparecerem no código
        if rel_path not in conteudo_projeto and nome_arquivo not in conteudo_projeto:
            orfaos.append((rel_path, full_path))

    # 4. Imprime o resultado
    print("=" * 60)
    if orfaos:
        print(f"⚠️  Encontrados {len(orfaos)} template(s) aparentemente SEM USO:\n")
        for rel_path, full_path in orfaos:
            print(f" ❌ {rel_path}")
            print(f"    Caminho completo: {full_path}\n")
    else:
        print("✅ Todos os arquivos HTML parecem estar em uso no projeto!")
    print("=" * 60)

if __name__ == "__main__":
    buscar_templates_orfaos()

    