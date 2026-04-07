# scripts/concatenar_por_app.py

import os
from pathlib import Path
from datetime import datetime

def concatenar_por_app(pasta_projeto, pasta_apps='apps', tipos_arquivo=None, pasta_saida='artefatos'):
    """
    Concatena arquivos específicos por APP em arquivos separados.
    
    Args:
        pasta_projeto: Caminho da pasta raiz do projeto Django
        pasta_apps: Nome da pasta que contém os apps (padrão: 'apps')
        tipos_arquivo: Lista com nomes dos arquivos a buscar
        pasta_saida: Pasta onde salvar os arquivos gerados
    """
    
    if tipos_arquivo is None:
        tipos_arquivo = ['models.py', 'views.py', 'forms.py', 'admin.py', 'urls.py', 'services.py']
    
    pasta_projeto = Path(pasta_projeto)
    pasta_apps_path = pasta_projeto / pasta_apps
    pasta_saida_path = pasta_projeto / pasta_saida
    pasta_saida_path.mkdir(exist_ok=True)
    
    # Lista de apps a processar
    apps = ['academico', 'accounts', 'core', 'eventos', 'interessados', 'portal', 'scripts_admin', 'selecao']
    
    data_atual = datetime.now().strftime('%d-%m-%Y')
    hora_atual = datetime.now().strftime('%H:%M:%S')
    
    for app_nome in apps:
        caminho_app = pasta_apps_path / app_nome
        
        if not caminho_app.exists():
            print(f"⚠️  App '{app_nome}' não encontrado em {caminho_app}")
            continue
        
        arquivo_saida = pasta_saida_path / f"{app_nome}-{data_atual}.txt"
        
        with open(arquivo_saida, 'w', encoding='utf-8') as saida:
            # Cabeçalho
            saida.write(f"{'=' * 80}\n")
            saida.write(f"APP: {app_nome.upper()}\n")
            saida.write(f"Data: {data_atual}\n")
            saida.write(f"Hora: {hora_atual}\n")
            saida.write(f"{'=' * 80}\n\n")
            
            contador_arquivos = 0
            
            for tipo in tipos_arquivo:
                saida.write(f"\n{'#' * 80}\n")
                saida.write(f"# TIPO: {tipo}\n")
                saida.write(f"{'#' * 80}\n\n")
                
                # Busca arquivos do tipo especificado neste app
                if tipo.startswith('*'):
                    # Busca por extensão (ex: *.html)
                    arquivos_encontrados = list(caminho_app.rglob(tipo))
                else:
                    # Busca por nome de arquivo específico
                    arquivos_encontrados = list(caminho_app.rglob(tipo))
                
                if not arquivos_encontrados:
                    saida.write(f"# Nenhum arquivo {tipo} encontrado\n\n")
                    continue
                
                for arquivo in sorted(arquivos_encontrados):
                    # Pula pastas de environment, cache e migrations
                    if any(parte in arquivo.parts for parte in ['venv', 'env', '__pycache__', 'migrations', '.venv']):
                        continue
                    
                    caminho_relativo = arquivo.relative_to(caminho_app)
                    
                    saida.write(f"\n{'-' * 80}\n")
                    saida.write(f"ARQUIVO: {caminho_relativo}\n")
                    saida.write(f"{'-' * 80}\n\n")
                    
                    try:
                        conteudo = arquivo.read_text(encoding='utf-8')
                        saida.write(conteudo)
                        saida.write("\n\n")
                        contador_arquivos += 1
                    except Exception as e:
                        saida.write(f"# ERRO ao ler arquivo: {e}\n\n")
        
        print(f"✓ {app_nome:20} | {contador_arquivos:2} arquivos | {arquivo_saida.name}")
    
    print(f"\n✓ Arquivos gerados em: {pasta_saida_path}")

# USO
if __name__ == "__main__":
    PASTA_PROJETO = r"C:\PMS\PMS2025\Inscr-Meta\prg-Meta\Eventos-MetaReciclagem\eventosmeta"
    
    print("\n" + "=" * 80)
    print("GERANDO ARTEFATOS POR APP")
    print("=" * 80 + "\n")
    
    concatenar_por_app(
        pasta_projeto=PASTA_PROJETO,
        pasta_apps='apps',
        tipos_arquivo=['models.py', 'views.py', 'forms.py', 'admin.py', 'urls.py', 'services.py'],
        pasta_saida='artefatos'
    )
    
    print("\n" + "=" * 80)
    print("CONCLUÍDO!")
    print("=" * 80)

# Comando para rodar: python scripts/concatenar_por_app.py

