"""
Arquivo: limpar_sessoes.py
Caminho: scripts/limpar_sessoes.py
Alteração: Limpa todas as sessões ativas - CAMINHO SETTINGS CORRIGIDO
Data: 19/01/2026
"""

import os
import sys
import django

# Adicionar o diretório do projeto ao path
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE_DIR)

# Configurar Django com o caminho CORRETO (config.settings)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from django.contrib.sessions.models import Session

print('='*80)
print('LIMPANDO SESSÕES')
print('='*80)

# Contar sessões antes
total_antes = Session.objects.count()
print(f'\nSessões ativas antes: {total_antes}')

# Deletar todas as sessões
Session.objects.all().delete()

print(f'\n✅ Todas as {total_antes} sessões foram limpas!')
print('\nVocê pode acessar o sistema normalmente agora.')
print('Acesse: http://localhost:8000/')
print('='*80)

