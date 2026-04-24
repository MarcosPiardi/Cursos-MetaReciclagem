
# Esse script é para concatenar todos os arquivos importantes para o Claude verificar todo o projeto
# Em 13/03/2026 
# # Para eu fazer uma documentação completa + diagnóstico de arquitetura, preciso de:



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
                if any(parte in arquivo.parts for parte in ['venv', 'env', '__pycache__', 'migrations', 'htmlcov', 'staticfiles_collected', 'docs', 'fixtures', 'logs', 'scripts']) or 'htmlcov' in str(arquivo):
                    continue
                
                caminho_relativo = arquivo.relative_to(pasta)
                
                saida.write(f"\n{'=' * 80}\n")
                saida.write(f"# ARQUIVO: {caminho_relativo}\n")
                saida.write(f"{'=' * 80}\n\n")
                
                try:
                    conteudo = arquivo.read_text(encoding='utf-8')
                except UnicodeDecodeError:
                    conteudo = arquivo.read_text(encoding='latin-1')
                except Exception as e:
                    saida.write(f"# ERRO ao ler arquivo: {e}\n\n")
                    continue
                saida.write(conteudo)
                saida.write("\n\n")
    
    print(f"✓ Arquivo criado: {arquivo_saida}")

if __name__ == "__main__":
    PASTA_PROJETO1 = r"C:\PMS\PMS2025\Inscr-Meta\prg-Meta\Eventos-MetaReciclagem\eventosmeta"
    PASTA_PROJETO2 = r"C:\PMS\PMS2025\Inscr-Meta\prg-Meta\Eventos-MetaReciclagem\eventosmeta\apps\interessados\management\commands"
    PASTA_PROJETO3 = r"C:\PMS\PMS2025\Inscr-Meta\prg-Meta\Eventos-MetaReciclagem\eventosmeta\apps\scripts_admin\management\commands"

    
    data_atual = datetime.now().strftime('%Y-%m-%d')
    concatenar_arquivos(pasta_projeto=PASTA_PROJETO1, tipos_arquivo=['urls.py'], arquivo_saida=f'{data_atual}_Pasta01_URLs.txt')
    concatenar_arquivos(pasta_projeto=PASTA_PROJETO1, tipos_arquivo=['views.py', 'views_exclusao.py'], arquivo_saida=f'{data_atual}_Pasta02_views.txt')
    concatenar_arquivos(pasta_projeto=PASTA_PROJETO1, tipos_arquivo=['models.py'], arquivo_saida=f'{data_atual}_Pasta03_models.txt')
    concatenar_arquivos(pasta_projeto=PASTA_PROJETO1, tipos_arquivo=['authentication.py', 'middleware.py'], arquivo_saida=f'{data_atual}_Pasta04_Autenticacao.txt')
    concatenar_arquivos(pasta_projeto=PASTA_PROJETO1, tipos_arquivo=['*.html', '*.css', '*.js'], arquivo_saida=f'{data_atual}_Pasta05_Templates.txt')
    concatenar_arquivos(pasta_projeto=PASTA_PROJETO1, tipos_arquivo=['requirements.txt', 'asgi.py', 'settings.py', 'documentacao_sistema.json', 'documentacao_sistema.yaml', '2026-04-15_resumo_tecnico_classificacao.md', 'estrutura.txt'], arquivo_saida=f'{data_atual}_Pasta06_Doc_Existente.txt')
    concatenar_arquivos(pasta_projeto=PASTA_PROJETO1, tipos_arquivo=['services.py', 'context_processors.py'], arquivo_saida=f'{data_atual}_Pasta07_Services.txt')
    concatenar_arquivos(pasta_projeto=PASTA_PROJETO1, tipos_arquivo=['admin.py'], arquivo_saida=f'{data_atual}_Pasta08_Admin.txt')
    concatenar_arquivos(pasta_projeto=PASTA_PROJETO1, tipos_arquivo=['apps.py'], arquivo_saida=f'{data_atual}_Pasta09_Apps-in-Apps.txt')
    concatenar_arquivos(pasta_projeto=PASTA_PROJETO1, tipos_arquivo=['tests.py'], arquivo_saida=f'{data_atual}_Pasta10_Tests.txt')
    concatenar_arquivos(pasta_projeto=PASTA_PROJETO1, tipos_arquivo=['forms.py'], arquivo_saida=f'{data_atual}_Pasta11_Forms.txt')
    concatenar_arquivos(pasta_projeto=PASTA_PROJETO2, tipos_arquivo=['*.py'], arquivo_saida=f'{data_atual}_Pasta12_Management_interessados.txt')
    concatenar_arquivos(pasta_projeto=PASTA_PROJETO3, tipos_arquivo=['*.py'], arquivo_saida=f'{data_atual}_Pasta13_Management_scripts.txt')
    concatenar_arquivos(pasta_projeto=PASTA_PROJETO1, tipos_arquivo=['utils.py', 'utils_pdf.py'], arquivo_saida=f'{data_atual}_Pasta14_Utils.txt')
    concatenar_arquivos(pasta_projeto=PASTA_PROJETO1, tipos_arquivo=['reports.py'], arquivo_saida=f'{data_atual}_Pasta15_Reports.txt')
    concatenar_arquivos(pasta_projeto=PASTA_PROJETO1, tipos_arquivo=['validators.py'], arquivo_saida=f'{data_atual}_Pasta16_Validators.txt')

    concatenar_arquivos(
        pasta_projeto=PASTA_PROJETO1,
        tipos_arquivo=['*pasta*.txt'],     # <----  aqui estão todos arquivos da primeira geração, mudar aqui e o nome do arquivo a ser gerado abaixo para selecionar outros ou alguns desses
        arquivo_saida=f'{data_atual}_TodasPastasConcatenadas.txt')   #  <----  nome do arquivo que será gerado
            
       


r"""
Para gerar esse arquivos: 
requirements.txt            --->    pip freeze > requirements.txt 
documentacao_sistema.json   --->    python scripts\gera_doc_sistema_yaml_json.py
documentacao_sistema.yaml   --->    e os dois arquivos serão gravados no diretório \docs
2026-mm-dd_resumo_tecnico_classificacao.md  --->     python scripts\gerar_markdown.py
2026-mm-dd_estrutura.txt    --->    tree /f /a > yyyy-mm-dd_estrutura.txt
"""



# comando para rodar: python scripts\concatenar_doc_completo_diag_arquitetura.py    

    # modelo da função para gerar arquivo - escolher nos tipos_arquivo:
    
    # concatenar_arquivos(
    #     pasta_projeto=PASTA_PROJETO,
    #     tipos_arquivo=['admin.py', 'apps.py', 'authentication.py', 
    #                    'forms.py', 'models.py', 'services.py', 
    #                    'urls.py', 'views.py', 'settings.py', 
    #                    '*.html', '*.css', '*.js'],      <----  aqui estão todos arquivos da primeira geração, mudar aqui e o nome do arquivo a ser gerado abaixo para selecionar outros ou alguns desses
    #     arquivo_saida='Pasta01_URLs_13-03-2026.txt'     <----  nome do arquivo que será gerado
    # )        
   
# Pasta 1: URLs (Rotas)
# config/urls.py (raiz do projeto)
# apps/interessados/urls.py
# apps/accounts/urls.py (se existir)
# Qualquer outra urls.py de apps
# 
# Pasta 2: Views (Lógica)
# apps/accounts/views.py (login staff/admin)
# apps/interessados/views.py (login interessados)
# apps/portal/views.py (se existir)
# 
# Pasta 3: Models (Estrutura)
# apps/accounts/models.py (model Usuario/Staff)
# apps/interessados/models.py (model Interessado)
# 
# Pasta 4: Autenticação
# apps/interessados/authentication.py (backend customizado)
# apps/accounts/middleware.py (se existir)
# apps/interessados/middleware.py (se existir)
# 
# Pasta 5: Templates (Interface)
# template/staff/login.html ou similar (login admin)
# template/interessados/login.html (login CPF)
# template/base.html ou estrutura base
# 
# Pasta 6: Documentação Existente
# Qualquer .txt ou .md que descreva fluxos
# Requisitos do projeto
# Diagramas ou anotações de design
# 
# Pasta 7..................    completr depois
