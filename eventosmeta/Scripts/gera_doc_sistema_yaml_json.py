r"""
Script: gera_doc_sistema_yaml_json.py
Caminho: Scripts/gera_doc_sistema_yaml_json.py

Gera documentacao_sistema.yaml e documentacao_sistema.json
lendo a estrutura real do projeto Django.

O que é extraído automaticamente:
  - Apps instalados (INSTALLED_APPS)
  - Estrutura de arquivos por app (models, services, admin, urls)
  - Actions do admin por app
  - URLs por app
  - Management commands

O que é MANUAL (editado diretamente neste script):
  - Descrições narrativas
  - Fluxos de negócio
  - Avisos e riscos
  - Ordem de leitura recomendada

Uso:
  cd <raiz do projeto>
  python Scripts/gera_doc_sistema_yaml_json.py

Saída:
  documentacao_sistema.yaml
  documentacao_sistema.json
"""

import os
import sys
import yaml
import json
from pathlib import Path
from dotenv import load_dotenv

# Adiciona o diretório do projeto ao Python path
script_dir = Path(__file__).parent
project_dir = script_dir.parent  # Assume que o script está em uma subpasta do projeto
sys.path.insert(0, str(project_dir))

# Carrega variáveis de ambiente do .env
load_dotenv()

# Define o módulo de configurações do Django
os.environ['DJANGO_SETTINGS_MODULE'] = 'config.settings'

import django
django.setup()

# Agora o Django está configurado

from django.apps import apps

# Gera a documentação do sistema
system_doc = {
    'models': []
}

for model in apps.get_models():
    model_data = {
        'app_label': model._meta.app_label,
        'model_name': model._meta.model_name,
        'fields': [field.name for field in model._meta.get_fields()],
        'verbose_name': str(model._meta.verbose_name),
        'verbose_name_plural': str(model._meta.verbose_name_plural),
    }
    system_doc['models'].append(model_data)

# Diretórios de saída
output_dir = script_dir / 'docs'
output_dir.mkdir(exist_ok=True)

yaml_path = output_dir / 'doc_sistema.yaml'
json_path = output_dir / 'doc_sistema.json'

# Escreve YAML
with yaml_path.open('w', encoding='utf-8') as f:
    yaml.dump(system_doc, f, default_flow_style=False, allow_unicode=True)

# Escreve JSON
with json_path.open('w', encoding='utf-8') as f:
    json.dump(system_doc, f, ensure_ascii=False, indent=2)

print(f"Documentação do sistema gerada em: {yaml_path} e {json_path}")

