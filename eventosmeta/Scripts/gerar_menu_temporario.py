"""
Arquivo: gerar_menu_temporario.py
Caminho: scripts/gerar_menu_temporario.py
Alteração: Menu temporário com URLs válidas - TODAS BARRAS CORRIGIDAS
Data: 19/01/2026
"""

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# Mapeamento APENAS com URLs que realmente existem
MAPEAMENTO_URLS = {
    # Portal
    'apps/portal/templates/portal/index.html': 'portal:index',
    'apps/portal/templates/portal/consulta_publica.html': 'portal:consulta_publica',
    
    # Interessados
    'apps/interessados/templates/interessados/cadastro.html': 'interessados:cadastro',
    'apps/interessados/templates/interessados/login_interessado.html': 'interessados:login',
    'apps/interessados/templates/interessados/dashboard.html': 'interessados:dashboard',
    
    # Accounts (Staff)
    'apps/accounts/templates/accounts/login_staff.html': 'accounts:login_staff',
    'apps/accounts/templates/accounts/dashboard_staff.html': 'accounts:dashboard_staff',
}

# Encontrar todos os HTMLs (exceto base.html)
arquivos_html = []

for caminho in Path(BASE_DIR).rglob('*.html'):
    caminho_str = str(caminho)
    if any(x in caminho_str for x in ['.venv', 'venv', '__pycache__', '.git', 'node_modules', 'menu_temporario']):
        continue
    
    if 'base' in caminho.name.lower():
        continue
    
    relativo = caminho.relative_to(BASE_DIR)
    # CORRIGIDO: usar método do pathlib para evitar problema de barras
    caminho_normalizado = str(relativo).replace(chr(92), '/')  # chr(92) = backslash
    
    url_name = MAPEAMENTO_URLS.get(caminho_normalizado, None)
    
    arquivos_html.append({
        'nome': caminho.name,
        'caminho': caminho_normalizado,
        'tipo': caminho.parent.name,
        'url': url_name
    })

arquivos_html.sort(key=lambda x: x['caminho'])

# Gerar HTML do menu
menu_html = '''
<!-- MENU TEMPORÁRIO DE DESENVOLVIMENTO -->
<div id="menu-dev" style="position: fixed; top: 0; right: 0; width: 320px; height: 100vh; background: #2c3e50; color: white; overflow-y: auto; z-index: 9999; padding: 20px; box-shadow: -5px 0 15px rgba(0,0,0,0.3); font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;">
    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 20px; padding-bottom: 15px; border-bottom: 2px solid #3498db;">
        <h3 style="margin: 0; font-size: 1.2em;">🔧 Menu Dev</h3>
        <button onclick="document.getElementById('menu-dev').style.display='none'" style="background: #e74c3c; border: none; color: white; padding: 5px 10px; border-radius: 4px; cursor: pointer; font-weight: bold;">✖</button>
    </div>
    <p style="font-size: 0.85em; opacity: 0.8; margin-bottom: 20px;">Navegação entre Templates</p>
    
    <div style="margin-bottom: 20px;">
'''

# Agrupar por app
por_app = {}
for arquivo in arquivos_html:
    partes = arquivo['caminho'].split('/')
    if 'apps' in partes:
        idx = partes.index('apps')
        app = partes[idx + 1] if idx + 1 < len(partes) else 'outros'
    elif 'template' in partes:
        app = 'global'
    else:
        app = 'outros'
    
    if app not in por_app:
        por_app[app] = []
    por_app[app].append(arquivo)

# Gerar menu por app
for app in sorted(por_app.keys()):
    menu_html += f'''
        <div style="margin-bottom: 25px;">
            <h4 style="margin: 0 0 12px 0; color: #3498db; font-size: 0.9em; text-transform: uppercase; letter-spacing: 1px; font-weight: bold;">📁 {app}</h4>
'''
    for arquivo in por_app[app]:
        if arquivo['url']:
            menu_html += f'''
            <a href="{{% url '{arquivo['url']}' %}}" style="display: block; padding: 10px; margin-bottom: 8px; background: #34495e; color: white; text-decoration: none; border-radius: 5px; font-size: 0.85em; transition: all 0.3s; border-left: 3px solid #27ae60;" onmouseover="this.style.background='#3498db'; this.style.borderLeftColor='#2ecc71'" onmouseout="this.style.background='#34495e'; this.style.borderLeftColor='#27ae60'">
                <div style="display: flex; align-items: center; justify-content: space-between;">
                    <div>
                        <div style="font-weight: bold; margin-bottom: 3px;">✅ {arquivo['nome'].replace('.html', '')}</div>
                        <div style="color: #95a5a6; font-size: 0.75em;">{arquivo['url']}</div>
                    </div>
                    <div style="color: #2ecc71;">▶</div>
                </div>
            </a>
'''
        else:
            menu_html += f'''
            <div style="padding: 10px; margin-bottom: 8px; background: #2c3e50; border-radius: 5px; font-size: 0.85em; border-left: 3px solid #95a5a6; opacity: 0.6;">
                <div style="font-weight: bold; margin-bottom: 3px; color: #95a5a6;">⚠️ {arquivo['nome'].replace('.html', '')}</div>
                <div style="color: #7f8c8d; font-size: 0.75em;">Sem URL mapeada</div>
            </div>
'''
    
    menu_html += '''
        </div>
'''

menu_html += '''
    </div>
    
    <div style="padding-top: 15px; border-top: 2px solid #34495e; margin-top: 20px;">
        <div style="font-size: 0.8em; color: #95a5a6; text-align: center;">
            <p style="margin: 5px 0;">✅ Clicável | ⚠️ Sem URL</p>
        </div>
    </div>
</div>

<button onclick="document.getElementById('menu-dev').style.display='block'" style="position: fixed; bottom: 20px; right: 20px; background: #3498db; color: white; border: none; padding: 15px 20px; border-radius: 50px; cursor: pointer; box-shadow: 0 4px 12px rgba(52, 152, 219, 0.4); font-weight: bold; z-index: 9998; transition: all 0.3s;" onmouseover="this.style.background='#2980b9'; this.style.transform='scale(1.1)'" onmouseout="this.style.background='#3498db'; this.style.transform='scale(1)'">
    🔧 Menu Dev
</button>
'''

# Salvar menu
caminho_menu = BASE_DIR / 'menu_temporario.html'
with open(caminho_menu, 'w', encoding='utf-8') as f:
    f.write(menu_html)

print('='*80)
print('MENU TEMPORARIO GERADO COM SUCESSO!')
print('='*80)
print(f'\nArquivo criado: menu_temporario.html')
print(f'\nTemplates encontrados: {len(arquivos_html)}')
print(f'  - Com URL: {sum(1 for a in arquivos_html if a["url"])}')
print(f'  - Sem URL: {sum(1 for a in arquivos_html if not a["url"])}')
print('\n' + '='*80)
print('PROXIMOS PASSOS:')
print('='*80)
print('\n1. Copiar menu:')
print('   Copy-Item menu_temporario.html templates')
print('\n2. Rodar servidor:')
print('   python manage.py runserver')
print('\n' + '='*80)

