"""
Arquivo: visualizar_htmls.py
Caminho: scripts/visualizar_htmls.py
Alteração: Script para criar visualizador de templates renderizados (CORRIGIDO)
Data: 19/01/2026
"""

import os
import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

def criar_visualizador_htmls():
    """Cria um visualizador HTML que mostra cada template renderizado"""
    
    print('🎨 Criando visualizador de templates...\n')
    
    # Encontrar todos os arquivos HTML
    arquivos_html = []
    
    for root, dirs, files in os.walk(BASE_DIR):
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
    
    arquivos_html.sort(key=lambda x: x['caminho_relativo'])
    
    print(f'📊 Total de arquivos HTML encontrados: {len(arquivos_html)}\n')
    
    # Ler conteúdo de todos os arquivos
    templates_data = []
    for arquivo in arquivos_html:
        try:
            with open(arquivo['caminho_completo'], 'r', encoding='utf-8') as f:
                conteudo = f.read()
        except Exception as e:
            print(f'⚠️ Erro ao ler {arquivo["nome"]}: {e}')
            conteudo = f'Erro ao carregar arquivo: {str(e)}'
        
        templates_data.append({
            'nome': arquivo['nome'],
            'caminho': arquivo['caminho_relativo'],
            'diretorio': arquivo['diretorio'],
            'conteudo': conteudo
        })
    
    # Criar HTML do visualizador
    html_visualizador = '''<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Visualizador de Templates - MetaReciclagem</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: #1a1a2e;
            color: #eee;
        }
        
        .header {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            padding: 30px;
            text-align: center;
            box-shadow: 0 2px 10px rgba(0,0,0,0.3);
        }
        
        .header h1 {
            font-size: 2.5em;
            margin-bottom: 10px;
        }
        
        .header p {
            font-size: 1.2em;
            opacity: 0.9;
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
        }
        
        .container {
            display: flex;
            height: calc(100vh - 200px);
        }
        
        .sidebar {
            width: 350px;
            background: #16213e;
            border-right: 2px solid #0f3460;
            overflow-y: auto;
        }
        
        .filter-box {
            padding: 20px;
            background: #0f3460;
            border-bottom: 2px solid #667eea;
            position: sticky;
            top: 0;
            z-index: 10;
        }
        
        .filter-box input {
            width: 100%;
            padding: 12px;
            border: 2px solid #667eea;
            border-radius: 8px;
            font-size: 14px;
            background: #1a1a2e;
            color: #eee;
            transition: all 0.3s;
        }
        
        .filter-box input:focus {
            outline: none;
            border-color: #764ba2;
            box-shadow: 0 0 10px rgba(118, 75, 162, 0.5);
        }
        
        .file-list {
            list-style: none;
        }
        
        .file-item {
            padding: 20px;
            border-bottom: 1px solid #0f3460;
            cursor: pointer;
            transition: all 0.3s;
            position: relative;
        }
        
        .file-item:hover {
            background: #0f3460;
            transform: translateX(5px);
        }
        
        .file-item.active {
            background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
            border-left: 4px solid #ffd700;
        }
        
        .file-item.active::before {
            content: '▶';
            position: absolute;
            left: 5px;
            font-size: 12px;
        }
        
        .file-name {
            font-weight: bold;
            font-size: 1.1em;
            margin-bottom: 8px;
            color: #fff;
        }
        
        .file-path {
            font-size: 0.85em;
            color: #aaa;
            word-break: break-all;
        }
        
        .badge {
            display: inline-block;
            padding: 3px 10px;
            border-radius: 12px;
            font-size: 0.7em;
            font-weight: bold;
            margin-left: 8px;
            text-transform: uppercase;
        }
        
        .badge-base { background: #e74c3c; }
        .badge-index { background: #27ae60; }
        .badge-form { background: #3498db; }
        .badge-list { background: #9b59b6; }
        .badge-dashboard { background: #f39c12; }
        .badge-login { background: #e67e22; }
        
        .preview-area {
            flex: 1;
            background: #fff;
            position: relative;
            overflow: hidden;
        }
        
        .preview-header {
            background: #0f3460;
            padding: 15px 30px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            border-bottom: 2px solid #667eea;
        }
        
        .preview-title {
            font-size: 1.2em;
            font-weight: bold;
        }
        
        .preview-info {
            display: flex;
            gap: 20px;
            font-size: 0.9em;
            color: #aaa;
        }
        
        .empty-state {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            height: 100%;
            color: #666;
        }
        
        .empty-state-icon {
            font-size: 5em;
            margin-bottom: 20px;
            opacity: 0.3;
        }
        
        .empty-state-text {
            font-size: 1.5em;
            color: #999;
        }
        
        .device-selector {
            display: flex;
            gap: 10px;
            background: #0f3460;
            padding: 10px;
            border-bottom: 2px solid #667eea;
            justify-content: center;
        }
        
        .device-btn {
            background: #1a1a2e;
            border: 2px solid #667eea;
            color: #eee;
            padding: 8px 20px;
            border-radius: 5px;
            cursor: pointer;
            transition: all 0.3s;
            font-size: 14px;
        }
        
        .device-btn:hover {
            background: #667eea;
            transform: scale(1.05);
        }
        
        .device-btn.active {
            background: #764ba2;
            border-color: #764ba2;
        }
        
        .preview-container {
            height: calc(100% - 110px);
            display: flex;
            justify-content: center;
            align-items: flex-start;
            padding: 20px;
            overflow: auto;
            background: #f0f0f0;
        }
        
        .preview-wrapper {
            background: white;
            box-shadow: 0 5px 30px rgba(0,0,0,0.3);
            transition: all 0.3s;
            width: 100%;
            height: 100%;
        }
        
        .preview-wrapper.mobile {
            max-width: 375px;
            height: 667px;
        }
        
        .preview-wrapper.tablet {
            max-width: 768px;
            height: 1024px;
        }
        
        .preview-wrapper.desktop {
            width: 100%;
            height: 100%;
        }
        
        ::-webkit-scrollbar {
            width: 10px;
            height: 10px;
        }
        
        ::-webkit-scrollbar-track {
            background: #1a1a2e;
        }
        
        ::-webkit-scrollbar-thumb {
            background: #667eea;
            border-radius: 5px;
        }
        
        ::-webkit-scrollbar-thumb:hover {
            background: #764ba2;
        }
    </style>
</head>
<body>
    <div class="header">
        <h1>🎨 Visualizador de Templates</h1>
        <p>Projeto MetaReciclagem</p>
        <div class="stats">
            <div class="stat">
                <div class="stat-number">''' + str(len(arquivos_html)) + '''</div>
                <div class="stat-label">Templates HTML</div>
            </div>
            <div class="stat">
                <div class="stat-number">''' + str(len(set(a['diretorio'] for a in arquivos_html))) + '''</div>
                <div class="stat-label">Diretórios</div>
            </div>
        </div>
    </div>
    
    <div class="container">
        <div class="sidebar">
            <div class="filter-box">
                <input type="text" id="filter" placeholder="🔍 Buscar template..." onkeyup="filtrarTemplates()">
            </div>
            <ul class="file-list" id="fileList">
'''
    
    # Adicionar cada arquivo à lista
    for idx, arquivo in enumerate(arquivos_html):
        nome_lower = arquivo['nome'].lower()
        badge = ''
        if 'base' in nome_lower:
            badge = '<span class="badge badge-base">Base</span>'
        elif 'index' in nome_lower:
            badge = '<span class="badge badge-index">Index</span>'
        elif 'form' in nome_lower or 'cadastro' in nome_lower:
            badge = '<span class="badge badge-form">Form</span>'
        elif 'lista' in nome_lower:
            badge = '<span class="badge badge-list">List</span>'
        elif 'dashboard' in nome_lower:
            badge = '<span class="badge badge-dashboard">Dashboard</span>'
        elif 'login' in nome_lower:
            badge = '<span class="badge badge-login">Login</span>'
        
        html_visualizador += f'''
                <li class="file-item" onclick="mostrarTemplate({idx})" 
                    data-nome="{arquivo['nome']}" 
                    data-caminho="{arquivo['caminho_relativo']}">
                    <div class="file-name">📄 {arquivo['nome']}{badge}</div>
                    <div class="file-path">{arquivo['diretorio']}</div>
                </li>
'''
    
    html_visualizador += '''
            </ul>
        </div>
        
        <div class="preview-area">
            <div class="preview-header">
                <div class="preview-title" id="previewTitle">Selecione um template</div>
                <div class="preview-info">
                    <span id="previewPath"></span>
                </div>
            </div>
            
            <div class="device-selector">
                <button class="device-btn active" onclick="mudarDispositivo('desktop')">🖥️ Desktop</button>
                <button class="device-btn" onclick="mudarDispositivo('tablet')">📱 Tablet</button>
                <button class="device-btn" onclick="mudarDispositivo('mobile')">📱 Mobile</button>
            </div>
            
            <div class="preview-container" id="previewContainer">
                <div class="empty-state">
                    <div class="empty-state-icon">👈</div>
                    <div class="empty-state-text">Selecione um template na lista ao lado</div>
                </div>
            </div>
        </div>
    </div>
    
    <script>
        let templateAtual = null;
        let dispositivoAtual = 'desktop';
        
        const templates = ''' + json.dumps(templates_data, ensure_ascii=False) + ''';
        
        function mostrarTemplate(index) {
            templateAtual = index;
            
            document.querySelectorAll('.file-item').forEach(item => item.classList.remove('active'));
            document.querySelectorAll('.file-item')[index].classList.add('active');
            
            const template = templates[index];
            document.getElementById('previewTitle').textContent = template.nome;
            document.getElementById('previewPath').textContent = template.caminho;
            
            renderizarTemplate(template.conteudo);
        }
        
        function renderizarTemplate(conteudo) {
            const container = document.getElementById('previewContainer');
            
            let html = conteudo;
            
            html = html.replace(/{%\s*load\s+static\s*%}/g, '');
            html = html.replace(/{%\s*static\s+'([^']+)'\s*%}/g, '/static/$1');
            html = html.replace(/{%\s*url\s+'[^']+'\s*%}/g, '#');
            html = html.replace(/{{([^}]+)}}/g, '<span style="color: #e74c3c; font-weight: bold;">[Var]</span>');
            html = html.replace(/{%\s*if\s+[^%]+%}/g, '');
            html = html.replace(/{%\s*endif\s*%}/g, '');
            html = html.replace(/{%\s*for\s+[^%]+%}/g, '');
            html = html.replace(/{%\s*endfor\s*%}/g, '');
            html = html.replace(/{%\s*block\s+(\w+)\s*%}/g, '');
            html = html.replace(/{%\s*endblock\s*%}/g, '');
            html = html.replace(/{%\s*extends\s+'[^']+'\s*%}/g, '');
            html = html.replace(/{%\s*include\s+'[^']+'\s*%}/g, '<div style="background: #f0f0f0; padding: 10px; margin: 10px 0;">📄 Include</div>');
            
            const escapedHtml = html.replace(/"/g, '&quot;');
            container.innerHTML = `
                <div class="preview-wrapper ${dispositivoAtual}">
                    <iframe class="preview-frame" srcdoc="${escapedHtml}"></iframe>
                </div>
            `;
        }
        
        function mudarDispositivo(dispositivo) {
            dispositivoAtual = dispositivo;
            
            document.querySelectorAll('.device-btn').forEach(btn => btn.classList.remove('active'));
            event.target.classList.add('active');
            
            if (templateAtual !== null) {
                mostrarTemplate(templateAtual);
            }
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
    </script>
</body>
</html>
'''
    
    # Salvar visualizador
    caminho_visualizador = BASE_DIR / 'visualizador_templates.html'
    with open(caminho_visualizador, 'w', encoding='utf-8') as f:
        f.write(html_visualizador)
    
    print(f'✅ Visualizador criado: {caminho_visualizador}')
    print(f'\n🌐 ABRA NO NAVEGADOR: visualizador_templates.html')


if __name__ == '__main__':
    print('=' * 80)
    print('GERADOR DE VISUALIZADOR DE TEMPLATES')
    print('=' * 80)
    print()
    
    criar_visualizador_htmls()
    
    print('\n' + '=' * 80)
    print('✅ PRONTO!')
    print('=' * 80)
    print('\n📌 Abra visualizador_templates.html no navegador')
    print('=' * 80 + '\n')


    