"""
Arquivo: verificar_templates.py
Caminho: scripts/verificar_templates.py
Alteração: Diagnóstico completo de templates
Data: 20/01/2026
"""

import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

print('='*80)
print('VERIFICAÇÃO DE TEMPLATES')
print('='*80)

# Verificar apps/portal/templates
portal_templates = BASE_DIR / 'apps' / 'portal' / 'templates'
print(f'\n📁 Diretório: {portal_templates}')
print(f'Existe? {portal_templates.exists()}')

if portal_templates.exists():
    print('\nArquivos encontrados:')
    for root, dirs, files in os.walk(portal_templates):
        level = root.replace(str(portal_templates), '').count(os.sep)
        indent = ' ' * 2 * level
        print(f'{indent}{os.path.basename(root)}/')
        subindent = ' ' * 2 * (level + 1)
        for file in files:
            print(f'{subindent}{file}')

# Verificar se portal está em INSTALLED_APPS
settings_file = BASE_DIR / 'config' / 'settings.py'
if settings_file.exists():
    with open(settings_file, 'r', encoding='utf-8') as f:
        content = f.read()
        if "'apps.portal'" in content or '"apps.portal"' in content:
            print('\n✅ apps.portal está em INSTALLED_APPS')
        else:
            print('\n❌ apps.portal NÃO está em INSTALLED_APPS')

print('='*80)

