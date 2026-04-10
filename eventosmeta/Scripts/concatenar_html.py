import pathlib
import os

# Diretório base fixo
PASTA_PROJETO = pathlib.Path(r"C:\PMS\PMS2025\Inscr-Meta\prg-Meta\Eventos-MetaReciclagem\eventosmeta")

# Diretórios a excluir
EXCLUDED_DIRS = {'staticfiles_collected', 'htmlcov', 'node_modules', '.venv', 'venv', '__pycache__', '.git', '.env'}

# Extensões de arquivo a procurar
EXTENSIONS = ['.html', '.css', '.js']

# Função para obter o "app" de um arquivo (diretório pai imediato relativo ao projeto)
def get_app(file_path):
    try:
        relative_path = file_path.relative_to(PASTA_PROJETO)
        parts = relative_path.parts
        if len(parts) > 1:
            return parts[0]
        else:
            return "raiz"
    except ValueError:
        return "desconhecido"

# Função para coletar arquivos
def collect_files():
    files = {ext: [] for ext in EXTENSIONS}
    for root, dirs, filenames in os.walk(PASTA_PROJETO):
        # Filtrar diretórios excluídos
        dirs[:] = [d for d in dirs if d not in EXCLUDED_DIRS]
        
        root_path = pathlib.Path(root)
        for filename in filenames:
            file_path = root_path / filename
            if file_path.suffix in EXTENSIONS and not filename.startswith('z_'):
                files[file_path.suffix].append(file_path)
    return files

# Função para escrever o arquivo de saída
def write_output(files):
    output_file = PASTA_PROJETO / 'concatenado_html.txt'
    stats = {ext: {'count': 0, 'size': 0} for ext in EXTENSIONS}
    
    with open(output_file, 'w', encoding='utf-8') as f:
        for ext in EXTENSIONS:
            section_name = ext.upper().replace('.', '')
            f.write(f"{section_name}\n")
            f.write('=' * 50 + '\n')
            
            for file_path in files[ext]:
                try:
                    app = get_app(file_path)
                    f.write(f"Caminho: {file_path}\n")
                    f.write(f"App: {app}\n")
                    f.write('-' * 30 + '\n')
                    
                    with open(file_path, 'r', encoding='utf-8') as file:
                        content = file.read()
                        f.write(content)
                        f.write('\n\n')
                        
                    stats[ext]['count'] += 1
                    stats[ext]['size'] += file_path.stat().st_size
                except Exception as e:
                    print(f"Erro ao processar {file_path}: {e}")
                    continue
            
            f.write('\n')
        
        # Estatísticas
        f.write("ESTATÍSTICAS\n")
        f.write('=' * 50 + '\n')
        for ext in EXTENSIONS:
            f.write(f"{ext.upper().replace('.', '')}: {stats[ext]['count']} arquivos, {stats[ext]['size']} bytes\n")

# Execução principal
if __name__ == "__main__":
    try:
        files = collect_files()
        write_output(files)
        print("Arquivo 'concatenado_html.txt' gerado com sucesso.")
    except Exception as e:
        print(f"Erro geral: {e}")

        