
# Esse script é para concatenar todos os arquivos importantes para o Claude verificar todo o projeto


import os
from pathlib import Path
from datetime import datetime

def concatenar_arquivos(pasta_projeto, tipos_arquivo=['models.py', 'views.py'], arquivo_saida='projeto_concatenado.txt'):
    """
    Concatena arquivos específicos do projeto Django em um único arquivo.
    
    Args:
        pasta_projeto: Caminho da pasta raiz do projeto Django
        tipos_arquivo: Lista com nomes dos arquivos a buscar (ex: ['models.py', 'views.py'])
        arquivo_saida: Nome do arquivo de saída
    """
    
    pasta = Path(pasta_projeto)
    
    with open(arquivo_saida, 'w', encoding='utf-8') as saida:
        saida.write(f"# PROJETO DJANGO - ARQUIVOS CONCATENADOS\n")
        saida.write(f"# Pasta: {pasta_projeto}\n")
        # saida.write(f"# Data: {Path(arquivo_saida).stat().st_mtime}\n\n")
        saida.write(f"# Data: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\n\n")
        saida.write("=" * 80 + "\n\n")
        
        for tipo in tipos_arquivo:
            saida.write(f"\n{'#' * 80}\n")
            saida.write(f"# ARQUIVOS: {tipo}\n")
            saida.write(f"{'#' * 80}\n\n")
            
            # Busca recursivamente todos os arquivos do tipo especificado
            arquivos_encontrados = list(pasta.rglob(tipo))
            
            if not arquivos_encontrados:
                saida.write(f"# Nenhum arquivo {tipo} encontrado\n\n")
                continue
            
            for arquivo in sorted(arquivos_encontrados):
                # Pula arquivos em pastas de ambiente virtual ou cache
                if any(parte in arquivo.parts for parte in ['venv', 'env', '__pycache__', 'migrations']):
                    continue
                
                caminho_relativo = arquivo.relative_to(pasta)
                
                saida.write(f"\n{'=' * 80}\n")
                saida.write(f"# ARQUIVO: {caminho_relativo}\n")
                saida.write(f"{'=' * 80}\n\n")
                
                try:
                    conteudo = arquivo.read_text(encoding='utf-8')
                    saida.write(conteudo)
                    saida.write("\n\n")
                except Exception as e:
                    saida.write(f"# ERRO ao ler arquivo: {e}\n\n")
    
    print(f"✓ Arquivo criado: {arquivo_saida}")
    print(f"✓ Total de arquivos processados: {len(arquivos_encontrados)}")

# USO:
if __name__ == "__main__":
    # Substitua pelo caminho do seu projeto Django
    PASTA_PROJETO = r"C:\PMS\PMS2025\Inscr-Meta\prg-Meta\Eventos-MetaReciclagem\eventosmeta"
    
    # Escolha quais arquivos quer concatenar
    concatenar_arquivos(
        pasta_projeto=PASTA_PROJETO,
        # tipos_arquivo=['admin.py', 'apps.py', 'authentication.py', 
        #                'forms.py', 'models.py', 'services.py', 
        #                'urls.py', 'views.py', 'settings.py', 
        #                '*.html', '*.css', '*.js'],

        tipos_arquivo=['models.py', 'views.py', 'settings.py'],

        # tipos_arquivo=['admin.py', 'apps.py', 'authentication.py', 
                    #    'forms.py', 'services.py', 'urls.py', '*.html', '*.css', '*.js'],            
                          
        arquivo_saida='Artefatos-Primarios-MetaReciclagem-06-03-2026.txt'
    )

    concatenar_arquivos(
        pasta_projeto=PASTA_PROJETO,
        # tipos_arquivo=['admin.py', 'apps.py', 'authentication.py', 
        #                'forms.py', 'models.py', 'services.py', 
        #                'urls.py', 'views.py', 'settings.py', 
        #                '*.html', '*.css', '*.js'],

        # tipos_arquivo=['models.py', 'views.py', 'settings.py'],

        tipos_arquivo=['admin.py', 'apps.py', 'authentication.py', 
                       'forms.py', 'services.py', 'urls.py', '*.html', '*.css', '*.js'],            
                          
        arquivo_saida='Artefatos-Secundarios-MetaReciclagem-06-03-2026.txt'
        )       

# comando para rodar: python scripts\concatenar.py    

    """
    Arquivos gerados:
    
        Arquivo Artefatos-Primarios-projeto-data.txt tem 'models.py', 'views.py', 'settings.py'

        Arquivo Artefatos-Secundarios-projeto-data.txt tem 'admin.py', 'apps.py', 'authentication.py',
                                                           'forms.py', 'services.py', 'urls.py', '*.html', '*.css', '*.js'
        
    """


