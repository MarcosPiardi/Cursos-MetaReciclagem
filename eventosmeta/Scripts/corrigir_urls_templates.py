"""
Arquivo: corrigir_urls_templates.py
Caminho: scripts/corrigir_urls_templates.py
Alteração: Corrige URLs antigas/quebradas nos templates HTML
Data: 19/01/2026
"""

from pathlib import Path
import re
from datetime import datetime

BASE_DIR = Path(__file__).resolve().parent.parent

# Mapeamento de URLs antigas para novas
CORRECOES_URLS = {
    "{% url 'home' %}": "{% url 'portal:index' %}",
    '{% url "home" %}': '{% url "portal:index" %}',
    "{% url 'login' %}": "{% url 'interessados:login' %}",
    '{% url "login" %}': '{% url "interessados:login" %}',
    "{% url 'cadastro' %}": "{% url 'interessados:cadastro' %}",
    '{% url "cadastro" %}': '{% url "interessados:cadastro" %}',
    "{% url 'dashboard' %}": "{% url 'interessados:dashboard' %}",
    '{% url "dashboard" %}': '{% url "interessados:dashboard" %}',
}

def criar_backup():
    """Cria backup de todos os templates antes de modificar"""
    backup_dir = BASE_DIR / 'backup_templates' / datetime.now().strftime('%Y%m%d_%H%M%S')
    backup_dir.mkdir(parents=True, exist_ok=True)
    
    print(f'\n📦 Criando backup em: {backup_dir}')
    
    count = 0
    for caminho in Path(BASE_DIR).rglob('*.html'):
        if any(x in str(caminho) for x in ['.venv', 'venv', '__pycache__', '.git', 'backup_templates']):
            continue
        
        # Criar estrutura de diretórios no backup
        relativo = caminho.relative_to(BASE_DIR)
        destino = backup_dir / relativo
        destino.parent.mkdir(parents=True, exist_ok=True)
        
        # Copiar arquivo
        destino.write_text(caminho.read_text(encoding='utf-8'), encoding='utf-8')
        count += 1
    
    print(f'✅ Backup de {count} arquivos concluído!\n')
    return backup_dir

def corrigir_templates():
    """Corrige URLs em todos os templates"""
    
    print('='*80)
    print('CORREÇÃO DE URLs EM TEMPLATES')
    print('='*80)
    
    # Criar backup primeiro
    backup_dir = criar_backup()
    
    print('🔧 Iniciando correções...\n')
    
    arquivos_modificados = []
    total_correcoes = 0
    
    for caminho in Path(BASE_DIR).rglob('*.html'):
        if any(x in str(caminho) for x in ['.venv', 'venv', '__pycache__', '.git', 'backup_templates', 'menu_temporario']):
            continue
        
        try:
            conteudo_original = caminho.read_text(encoding='utf-8')
            conteudo_novo = conteudo_original
            correcoes_neste_arquivo = []
            
            # Aplicar todas as correções
            for url_antiga, url_nova in CORRECOES_URLS.items():
                if url_antiga in conteudo_novo:
                    # Contar ocorrências
                    ocorrencias = conteudo_novo.count(url_antiga)
                    conteudo_novo = conteudo_novo.replace(url_antiga, url_nova)
                    correcoes_neste_arquivo.append(f'{url_antiga} → {url_nova} ({ocorrencias}x)')
                    total_correcoes += ocorrencias
            
            # Se houve modificações, salvar
            if conteudo_novo != conteudo_original:
                caminho.write_text(conteudo_novo, encoding='utf-8')
                arquivos_modificados.append({
                    'caminho': str(caminho.relative_to(BASE_DIR)),
                    'correcoes': correcoes_neste_arquivo
                })
                
                print(f'✅ {caminho.name}')
                for correcao in correcoes_neste_arquivo:
                    print(f'   - {correcao}')
                print()
        
        except Exception as e:
            print(f'❌ Erro em {caminho.name}: {e}')
    
    # Relatório final
    print('='*80)
    print('RESUMO')
    print('='*80)
    print(f'\n📄 Arquivos modificados: {len(arquivos_modificados)}')
    print(f'🔧 Total de correções: {total_correcoes}')
    print(f'📦 Backup em: {backup_dir}')
    
    if arquivos_modificados:
        print('\n' + '='*80)
        print('ARQUIVOS MODIFICADOS:')
        print('='*80)
        for item in arquivos_modificados:
            print(f'\n📄 {item["caminho"]}')
            for correcao in item['correcoes']:
                print(f'   {correcao}')
    
    print('\n' + '='*80)
    print('✅ CORREÇÃO CONCLUÍDA!')
    print('='*80)
    print('\nPRÓXIMOS PASSOS:')
    print('1. Teste o sistema: python manage.py runserver')
    print('2. Se houver problemas, restaure do backup')
    print(f'3. Backup localizado em: {backup_dir}')
    print('='*80)

if __name__ == '__main__':
    corrigir_templates()

    