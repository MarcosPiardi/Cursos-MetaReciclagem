
# Esse script é para concatenar todos os arquivos importantes para o Claude verificar todo o projeto
# Em 13/03/2026 o Claude pediu o que está abaixo:
# Para eu fazer uma documentação completa + diagnóstico de arquitetura, preciso de:
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
        tipos_arquivo=['urls.py'],
        arquivo_saida='Pasta01_URLs_24-03-2026.txt'
    )

    concatenar_arquivos(
        pasta_projeto=PASTA_PROJETO,
        tipos_arquivo=['views.py'],
        arquivo_saida='Pasta02_views_24-03-2026.txt'
    )

    concatenar_arquivos(
        pasta_projeto=PASTA_PROJETO,
        tipos_arquivo=['models.py'],
        arquivo_saida='Pasta03_models_24-03-2026.txt'
    )

    concatenar_arquivos(
        pasta_projeto=PASTA_PROJETO,
        tipos_arquivo=['authentication.py', 'middleware.py'],
        arquivo_saida='Pasta04_Autenticacao_24-03-2026.txt'
    )

    concatenar_arquivos(
        pasta_projeto=PASTA_PROJETO,
        tipos_arquivo=['*.html', '*.css', '*.js'],
        arquivo_saida='Pasta05_Templates_24-03-2026.txt'
    )

    concatenar_arquivos(
        pasta_projeto=PASTA_PROJETO,
        tipos_arquivo=['requirements.txt', 'documentacao_sistema.json', 'documentacao_sistema.yaml', '2026-03-06_resumo_tecnico_classificacao.md', '2026-03-06_estrutura.txt'],
        arquivo_saida='Pasta06_Doc_Existente_24-03-2026.txt'
    )


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
   


