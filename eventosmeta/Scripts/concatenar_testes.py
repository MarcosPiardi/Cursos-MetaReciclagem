import pathlib
import os

# Diretório base fixo
diretorio_base = pathlib.Path(r"C:\PMS\PMS2025\Inscr-Meta\prg-Meta\Eventos-MetaReciclagem\eventosmeta")

# Diretórios a excluir
excluidos = {'staticfiles_collected', 'htmlcov', 'node_modules', '.venv', 'venv', '__pycache__', '.git', '.env'}

# Padrões de arquivos de teste
padroes = ['test_*.py', 'tests.py', '*_tests.py']

# Função para encontrar apps (subdiretórios não excluídos)
def encontrar_apps():
    apps = []
    for item in diretorio_base.iterdir():
        if item.is_dir() and item.name not in excluidos:
            apps.append(item)
    return apps

# Função para encontrar arquivos de teste em um app
def encontrar_testes(app_path):
    testes = []
    for padrao in padroes:
        for arquivo in app_path.rglob(padrao):
            if not any(parte in excluidos for parte in arquivo.parts) and not arquivo.name.startswith('z_'):
                testes.append(arquivo)
    return testes

# Função para concatenar arquivos
def concatenar_testes():
    apps = encontrar_apps()
    arquivo_saida = diretorio_base / 'concatenado_testes.txt'
    total_arquivos = 0
    total_bytes = 0
    estatisticas_apps = {}
    
    try:
        with open(arquivo_saida, 'w', encoding='utf-8') as f:
            for app in apps:
                app_nome = app.name
                testes = encontrar_testes(app)
                if testes:
                    f.write(f"{'='*50}\nAPP: {app_nome}\n{'='*50}\n\n")
                    estatisticas_apps[app_nome] = len(testes)
                    for teste in testes:
                        try:
                            with open(teste, 'r', encoding='utf-8') as tf:
                                conteudo = tf.read()
                            tamanho = teste.stat().st_size
                            total_arquivos += 1
                            total_bytes += tamanho
                            f.write(f"{'='*30}\nArquivo: {teste}\nApp: {app_nome}\n{'='*30}\n")
                            f.write(conteudo)
                            f.write('\n\n')
                        except Exception as e:
                            print(f"Erro ao processar {teste}: {e}")
            
            # Estatísticas
            f.write(f"{'='*50}\nESTATÍSTICAS\n{'='*50}\n")
            f.write(f"Total de arquivos de teste: {total_arquivos}\n")
            f.write(f"Total de bytes: {total_bytes}\n")
            f.write("Quantidade por app:\n")
            for app, qtd in estatisticas_apps.items():
                f.write(f"  {app}: {qtd}\n")
        
        print(f"Arquivo concatenado salvo em: {arquivo_saida}")
    
    except Exception as e:
        print(f"Erro geral: {e}")

# Executar a função
if __name__ == "__main__":
    concatenar_testes()

    