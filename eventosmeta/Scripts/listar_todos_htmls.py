"""
Arquivo: listar_todos_htmls.py
Caminho: scripts/listar_todos_htmls.py
Alteração: Script para listar e visualizar todos os arquivos HTML do projeto
Data: 19/01/2026
"""

import os
from pathlib import Path

# Diretório base do projeto
BASE_DIR = Path(__file__).resolve().parent.parent

def extrair_preview_html(caminho_arquivo, linhas=15):
    """
    Extrai as primeiras linhas do arquivo HTML para preview
    
    Args:
        caminho_arquivo: Caminho do arquivo HTML
        linhas: Número de linhas para mostrar
    
    Returns:
        String com o preview
    """
    try:
        with open(caminho_arquivo, 'r', encoding='utf-8') as f:
            conteudo = f.readlines()
            preview = ''.join(conteudo[:linhas])
            
            if len(conteudo) > linhas:
                preview += f'\n... (mais {len(conteudo) - linhas} linhas)'
            
            return preview
    except Exception as e:
        return f'[Erro ao ler arquivo: {e}]'


def listar_todos_htmls():
    """Lista todos os arquivos HTML do projeto com preview"""
    
    print('=' * 100)
    print('LISTA COMPLETA DE ARQUIVOS HTML - PROJETO METARECICLAGEM')
    print('=' * 100)
    print()
    
    # Encontrar todos os arquivos HTML
    arquivos_html = []
    
    for root, dirs, files in os.walk(BASE_DIR):
        # Ignorar diretórios específicos
        dirs[:] = [d for d in dirs if d not in ['.venv', 'venv', '__pycache__', '.git', 'node_modules']]
        
        for file in files:
            if file.endswith('.html'):
                caminho_completo = Path(root) / file
                caminho_relativo = caminho_completo.relative_to(BASE_DIR)
                
                arquivos_html.append({
                    'nome': file,
                    'caminho_completo': str(caminho_completo),
                    'caminho_relativo': str(caminho_relativo),
                    'diretorio': str(Path(root).relative_to(BASE_DIR)),
                })
    
    # Ordenar por caminho
    arquivos_html.sort(key=lambda x: x['caminho_relativo'])
    
    print(f'📊 TOTAL DE ARQUIVOS HTML ENCONTRADOS: {len(arquivos_html)}\n')
    print('=' * 100)
    
    # Listar cada arquivo
    for idx, arquivo in enumerate(arquivos_html, 1):
        print(f'\n{"=" * 100}')
        print(f'🔹 ARQUIVO {idx}/{len(arquivos_html)}')
        print(f'{"=" * 100}')
        print(f'📁 Diretório:     {arquivo["diretorio"]}')
        print(f'📄 Nome:          {arquivo["nome"]}')
        print(f'🗂️  Caminho:       {arquivo["caminho_relativo"]}')
        print(f'💾 Caminho Full:  {arquivo["caminho_completo"]}')
        print(f'\n📝 PREVIEW DO CONTEÚDO:')
        print('-' * 100)
        print(extrair_preview_html(arquivo['caminho_completo']))
        print('-' * 100)
    
    # Resumo final
    print(f'\n\n{"=" * 100}')
    print('📋 RESUMO POR DIRETÓRIO')
    print(f'{"=" * 100}\n')
    
    # Agrupar por diretório
    por_diretorio = {}
    for arquivo in arquivos_html:
        diretorio = arquivo['diretorio']
        if diretorio not in por_diretorio:
            por_diretorio[diretorio] = []
        por_diretorio[diretorio].append(arquivo['nome'])
    
    for diretorio in sorted(por_diretorio.keys()):
        print(f'📁 {diretorio}/')
        for nome in sorted(por_diretorio[diretorio]):
            print(f'   └── {nome}')
        print()
    
    # Salvar relatório em arquivo
    salvar_relatorio(arquivos_html, por_diretorio)
    
    print(f'{"=" * 100}')
    print('✅ Análise concluída!')
    print(f'📄 Relatório salvo em: relatorio_htmls.txt')
    print(f'{"=" * 100}\n')


def salvar_relatorio(arquivos_html, por_diretorio):
    """Salva relatório completo em arquivo texto"""
    
    caminho_relatorio = BASE_DIR / 'relatorio_htmls.txt'
    
    with open(caminho_relatorio, 'w', encoding='utf-8') as f:
        f.write('=' * 100 + '\n')
        f.write('RELATÓRIO COMPLETO DE ARQUIVOS HTML - METARECICLAGEM\n')
        f.write('=' * 100 + '\n\n')
        
        f.write(f'Total de arquivos HTML: {len(arquivos_html)}\n\n')
        
        # Lista detalhada
        f.write('=' * 100 + '\n')
        f.write('LISTA DETALHADA\n')
        f.write('=' * 100 + '\n\n')
        
        for idx, arquivo in enumerate(arquivos_html, 1):
            f.write(f'\n{"=" * 100}\n')
            f.write(f'ARQUIVO {idx}/{len(arquivos_html)}\n')
            f.write(f'{"=" * 100}\n')
            f.write(f'Diretório:    {arquivo["diretorio"]}\n')
            f.write(f'Nome:         {arquivo["nome"]}\n')
            f.write(f'Caminho:      {arquivo["caminho_relativo"]}\n')
            f.write(f'Caminho Full: {arquivo["caminho_completo"]}\n')
            f.write(f'\nPREVIEW:\n')
            f.write('-' * 100 + '\n')
            f.write(extrair_preview_html(arquivo['caminho_completo'], linhas=20))
            f.write('\n' + '-' * 100 + '\n')
        
        # Resumo por diretório
        f.write(f'\n\n{"=" * 100}\n')
        f.write('RESUMO POR DIRETÓRIO\n')
        f.write(f'{"=" * 100}\n\n')
        
        for diretorio in sorted(por_diretorio.keys()):
            f.write(f'{diretorio}/\n')
            for nome in sorted(por_diretorio[diretorio]):
                f.write(f'   └── {nome}\n')
            f.write('\n')
    
    print(f'✅ Relatório salvo em: {caminho_relatorio}')


def criar_indice_interativo():
    """Cria um índice HTML interativo para visualizar todos os templates"""
    
    print('\n🌐 Criando índice HTML interativo...')
    
    # Encontrar todos os arquivos HTML
    arquivos_html = []
    
    for root, dirs, files in os.walk(BASE_DIR):
        dirs[:] = [d for d in dirs if d not in ['.venv', 'venv', '__pycache__', '.git', 'node_modules']]
        
        for file in files:
            if file.endswith('.html'):
                caminho_completo = Path(root) / file
                caminho_relativo = caminho_completo.relative_to(BASE_DIR)
                
                with open(caminho_completo, 'r', encoding='utf-8') as f:
                    conteudo = f.read()
                
                arquivos_html.append({
                    'nome': file,
                    'caminho_relativo': str(caminho_relativo),
                    'diretorio': str(Path(root).relative_to(BASE_DIR)),
                    'conteudo': conteudo,
                    'linhas': len(conteudo.split('\n'))
                })
    
    # Criar HTML do índice
    html_indice = '''<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Índice de Templates - MetaReciclagem</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: #f5f5f5;
            padding: 20px;
        }
        
        .container {
            max-width: 1400px;
            margin: 0 auto;
            background: white;
            border-radius: 10px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
            overflow: hidden;
        }
        
        header {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 30px;
            text-align: center;
        }
        
        header h1 {
            font-size: 2.5em;
            margin-bottom: 10px;
        }
        
        .stats {
            display: flex;
            justify-content: center;
            gap: 30px;
            margin-top: 20px;
        }
        
        .stat {
            background: rgba(255,255,255,0.2);
            padding: 15px 30px;
            border-radius: 10px;
        }
        
        .stat-number {
            font-size: 2em;
            font-weight: bold;
        }
        
        .stat-label {
            font-size: 0.9em;
            opacity: 0.9;
        }
        
        .sidebar {
            float: left;
            width: 300px;
            background: #f8f9fa;
            border-right: 1px solid #dee2e6;
            height: calc(100vh - 200px);
            overflow-y: auto;
        }
        
        .content {
            margin-left: 300px;
            padding: 30px;
            height: calc(100vh - 200px);
            overflow-y: auto;
        }
        
        .file-list {
            list-style: none;
        }
        
        .file-item {
            padding: 15px 20px;
            border-bottom: 1px solid #dee2e6;
            cursor: pointer;
            transition: all 0.3s;
        }
        
        .file-item:hover {
            background: #e9ecef;
        }
        
        .file-item.active {
            background: #667eea;
            color: white;
        }
        
        .file-name {
            font-weight: bold;
            margin-bottom: 5px;
        }
        
        .file-path {
            font-size: 0.85em;
            opacity: 0.7;
        }
        
        .file-detail {
            display: none;
        }
        
        .file-detail.active {
            display: block;
        }
        
        .file-header {
            background: #f8f9fa;
            padding: 20px;
            border-radius: 10px;
            margin-bottom: 20px;
        }
        
        .file-header h2 {
            color: #667eea;
            margin-bottom: 10px;
        }
        
        .file-info {
            display: flex;
            gap: 20px;
            font-size: 0.9em;
            color: #6c757d;
        }
        
        .code-preview {
            background: #282c34;
            color: #abb2bf;
            padding: 20px;
            border-radius: 10px;
            overflow-x: auto;
            font-family: 'Courier New', monospace;
            font-size: 14px;
            line-height: 1.5;
        }
        
        .line-numbers {
            color: #5c6370;
            user-select: none;
            margin-right: 20px;
            display: inline-block;
            text-align: right;
            min-width: 40px;
        }
        
        .filter-box {
            padding: 20px;
            border-bottom: 1px solid #dee2e6;
        }
        
        .filter-box input {
            width: 100%;
            padding: 10px;
            border: 1px solid #dee2e6;
            border-radius: 5px;
            font-size: 14px;
        }
        
        .badge {
            display: inline-block;
            padding: 3px 8px;
            border-radius: 3px;
            font-size: 0.75em;
            font-weight: bold;
            margin-left: 10px;
        }
        
        .badge-primary {
            background: #667eea;
            color: white;
        }
        
        .badge-success {
            background: #28a745;
            color: white;
        }
        
        .badge-warning {
            background: #ffc107;
            color: #212529;
        }
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1>📄 Índice de Templates HTML</h1>
            <p>Projeto MetaReciclagem</p>
            <div class="stats">
                <div class="stat">
                    <div class="stat-number">''' + str(len(arquivos_html)) + '''</div>
                    <div class="stat-label">Arquivos HTML</div>
                </div>
                <div class="stat">
                    <div class="stat-number">''' + str(len(set(a['diretorio'] for a in arquivos_html))) + '''</div>
                    <div class="stat-label">Diretórios</div>
                </div>
                <div class="stat">
                    <div class="stat-number">''' + str(sum(a['linhas'] for a in arquivos_html)) + '''</div>
                    <div class="stat-label">Linhas Totais</div>
                </div>
            </div>
        </header>
        
        <div class="sidebar">
            <div class="filter-box">
                <input type="text" id="filter" placeholder="🔍 Filtrar templates..." onkeyup="filtrarTemplates()">
            </div>
            <ul class="file-list" id="fileList">
'''
    
    # Adicionar cada arquivo
    for idx, arquivo in enumerate(arquivos_html):
        status_badge = ''
        if 'base' in arquivo['nome'].lower():
            status_badge = '<span class="badge badge-primary">BASE</span>'
        elif 'index' in arquivo['nome'].lower():
            status_badge = '<span class="badge badge-success">INDEX</span>'
        elif 'login' in arquivo['nome'].lower() or 'dashboard' in arquivo['nome'].lower():
            status_badge = '<span class="badge badge-warning">AUTH</span>'
        
        html_indice += f'''
                <li class="file-item" onclick="mostrarArquivo({idx})" data-nome="{arquivo['nome']}" data-caminho="{arquivo['caminho_relativo']}">
                    <div class="file-name">{arquivo['nome']}{status_badge}</div>
                    <div class="file-path">{arquivo['diretorio']}</div>
                </li>
'''
    
    html_indice += '''
            </ul>
        </div>
        
        <div class="content">
'''
    
    # Adicionar detalhes de cada arquivo
    for idx, arquivo in enumerate(arquivos_html):
        conteudo_escapado = arquivo['conteudo'].replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
        linhas = conteudo_escapado.split('\n')
        
        codigo_com_numeros = ''
        for num_linha, linha in enumerate(linhas, 1):
            codigo_com_numeros += f'<span class="line-numbers">{num_linha}</span>{linha}\n'
        
        html_indice += f'''
            <div class="file-detail" id="file-{idx}">
                <div class="file-header">
                    <h2>📄 {arquivo['nome']}</h2>
                    <div class="file-info">
                        <span>📁 {arquivo['diretorio']}</span>
                        <span>📊 {arquivo['linhas']} linhas</span>
                        <span>🗂️ {arquivo['caminho_relativo']}</span>
                    </div>
                </div>
                <div class="code-preview"><pre>{codigo_com_numeros}</pre></div>
            </div>
'''
    
    html_indice += '''
        </div>
    </div>
    
    <script>
        function mostrarArquivo(index) {
            // Remover active de todos
            document.querySelectorAll('.file-item').forEach(item => item.classList.remove('active'));
            document.querySelectorAll('.file-detail').forEach(detail => detail.classList.remove('active'));
            
            // Adicionar active no selecionado
            document.querySelectorAll('.file-item')[index].classList.add('active');
            document.getElementById('file-' + index).classList.add('active');
        }
        
        function filtrarTemplates() {
            const filtro = document.getElementById('filter').value.toLowerCase();
            const items = document.querySelectorAll('.file-item');
            
            items.forEach(item => {
                const nome = item.getAttribute('data-nome').toLowerCase();
                const caminho = item.getAttribute('data-caminho').toLowerCase();
                
                if (nome.includes(filtro) || caminho.includes(filtro)) {
                    item.style.display = 'block';
                } else {
                    item.style.display = 'none';
                }
            });
        }
        
        // Mostrar primeiro arquivo ao carregar
        window.onload = () => mostrarArquivo(0);
    </script>
</body>
</html>
'''
    
    # Salvar índice HTML
    caminho_indice = BASE_DIR / 'indice_htmls.html'
    with open(caminho_indice, 'w', encoding='utf-8') as f:
        f.write(html_indice)
    
    print(f'✅ Índice interativo criado: {caminho_indice}')
    print(f'🌐 Abra no navegador para visualizar todos os templates!')


if __name__ == '__main__':
    listar_todos_htmls()
    criar_indice_interativo()
    
    print('\n' + '=' * 100)
    print('✅ PROCESSO CONCLUÍDO!')
    print('=' * 100)
    print('\n📄 Arquivos gerados:')
    print('   1. relatorio_htmls.txt     → Relatório em texto')
    print('   2. indice_htmls.html       → Visualizador interativo (abra no navegador)')
    print('\n💡 Dica: Abra o indice_htmls.html no navegador para uma visualização mais fácil!')
    print('=' * 100 + '\n')

    