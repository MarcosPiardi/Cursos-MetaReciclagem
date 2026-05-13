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

from pathlib import Path
import sys
import ast
import json
import yaml

# Configurações hardcoded
DESCRICAO_SISTEMA = """O projeto MetaReciclagem é uma plataforma digital em Python/Django que automatiza e integra todo o ciclo de vida de eventos acadêmicos,
                    substituindo processos manuais por um sistema de missão crítica que garante eficiência, transparência e segurança na seleção.

FLUXOS_NEGOCIO = {
    "classificacao": "Fluxo principal para classificação de participantes em eventos.",
    "matricula": "Processo de matrícula e inscrição em cursos/eventos.",
    "avaliacao_e_certificado": "Sistema de avaliação e geração de certificados."
}

WARNINGS_ONBOARDING = [
    "Verificar dependências antes de deploy.",
    "Configurar banco de dados PostgreSQL.",
    "Executar migrations pendentes."
]

RISKS_AND_NOTES = [
    "Risco: Dependência de serviços externos para notificações.",
    "Nota: Implementar cache com Redis para performance.",
    "Risco: Validações de segurança em uploads de arquivos."
]

def get_str_value(node):
    """Extrai valor string compatível com ast.Constant ou ast.Str."""
    if hasattr(node, 'value'):
        return node.value
    elif hasattr(node, 's'):
        return node.s
    return None

def extract_classes(file_path):
    """Extrai lista de classes top-level de um arquivo Python via AST."""
    if not file_path.exists():
        return []
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            tree = ast.parse(f.read())
        return [node.name for node in tree.body if isinstance(node, ast.ClassDef)]
    except Exception:
        return []

def extract_admin_actions(app_path):
    """Extrai admin actions de admin.py (funções com @admin.action)."""
    admin_file = app_path / 'admin.py'
    if not admin_file.exists():
        return []
    try:
        with open(admin_file, 'r', encoding='utf-8') as f:
            tree = ast.parse(f.read())
        actions = []
        for node in tree.body:
            if isinstance(node, ast.FunctionDef) and node.decorator_list:
                for dec in node.decorator_list:
                    if (isinstance(dec, ast.Call) and
                        isinstance(dec.func, ast.Attribute) and
                        dec.func.attr == 'action' and
                        isinstance(dec.func.value, ast.Name) and
                        dec.func.value.id == 'admin'):
                        short_desc = None
                        for kw in dec.keywords:
                            if kw.arg == 'short_description':
                                short_desc = get_str_value(kw.value)
                                break
                        actions.append({
                            'name': node.name,
                            'short_description': short_desc or node.name
                        })
                        break  # Primeira action decorator
        return actions
    except Exception:
        return []

def extract_urls(app_path):
    """Extrai patterns de path() calls em urls.py."""
    urls_file = app_path / 'urls.py'
    if not urls_file.exists():
        return []
    try:
        with open(urls_file, 'r', encoding='utf-8') as f:
            tree = ast.parse(f.read())
        paths = []
        for node in ast.walk(tree):
            if (isinstance(node, ast.Call) and
                isinstance(node.func, ast.Name) and
                node.func.id == 'path' and
                node.args):
                arg0 = node.args[0]
                pattern = get_str_value(arg0)
                if pattern:
                    paths.append(pattern)
        return paths
    except Exception:
        return []

def extract_commands(app_path):
    """Extrai comandos Django de management/commands/*.py (classes que herdam de BaseCommand)."""
    cmds_dir = app_path / 'management' / 'commands'
    if not cmds_dir.exists():
        return []
    commands = []
    for cmd_file in cmds_dir.glob('*.py'):
        if cmd_file.name == '__init__.py':
            continue
        try:
            with open(cmd_file, 'r', encoding='utf-8') as f:
                tree = ast.parse(f.read())
            for node in tree.body:
                if isinstance(node, ast.ClassDef):
                    for base in node.bases:
                        if (isinstance(base, ast.Name) and base.id == 'BaseCommand') or \
                           (isinstance(base, ast.Attribute) and base.attr == 'BaseCommand'):
                            commands.append(node.name)
                            break
        except Exception:
            pass
    return list(set(commands))  # Remove duplicatas

if __name__ == '__main__':
    # Determina BASE_DIR: scripts/ -> parent.parent
    script_dir = Path(__file__).resolve().parent
    BASE_DIR = script_dir.parent
    print(f"BASE_DIR detectado: {BASE_DIR.resolve()}")

    # Validação manage.py
    manage_py = BASE_DIR / 'manage.py'
    if not manage_py.exists():
        print("ERRO: manage.py não encontrado em BASE_DIR!")
        sys.exit(1)

    # Detecta apps automaticamente
    apps_dir = BASE_DIR / 'apps'
    if not apps_dir.exists():
        print("ERRO: diretório apps/ não encontrado!")
        sys.exit(1)

    apps = []
    for d in apps_dir.iterdir():
        if d.is_dir() and (d / '__init__.py').exists():
            apps.append(d.name)

    # Inclui dashboard se existir
    dashboard_path = BASE_DIR / 'dashboard'
    if dashboard_path.exists() and (dashboard_path / '__init__.py').exists():
        apps.append('dashboard')

    apps.sort()  # Ordena alfabeticamente
    print(f"Apps detectados: {apps}")

    # Monta documento
    doc = {
        "system": {
            "descricao": DESCRICAO_SISTEMA
        },
        "documentation_strategy": {
            "metodo": "Extração automática via AST de arquivos Python + dados narrativos hardcoded.",
            "versao": "VERSÃO FINAL"
        },
        "overview": {
            "resumo": "Sistema Django modular para gestão de eventos com apps especializados.",
            "apps": apps
        },
        "architecture": {
            "framework": "Django",
            "estrutura": "Apps em apps/ + dashboard opcional",
            "extensoes": ["AST para extração dinâmica"]
        },
        "apps": {},
        "business_flows": FLUXOS_NEGOCIO,
        "onboarding": {
            "warnings": WARNINGS_ONBOARDING
        },
        "risks_and_notes": RISKS_AND_NOTES
    }

    # Extrai dados por app
    for app in apps:
        if app == 'dashboard':
            app_path = BASE_DIR / 'dashboard'
        else:
            app_path = apps_dir / app
        
        app_data = {
            "models": extract_classes(app_path / 'models.py'),
            "services": extract_classes(app_path / 'services.py'),
            "admin_actions": extract_admin_actions(app_path),
            "urls": extract_urls(app_path),
            "commands": extract_commands(app_path)
        }
        doc["apps"][app] = app_data

    # Salva YAML e JSON
    output_yaml = BASE_DIR / 'doc_sistema.yaml'
    output_json = BASE_DIR / 'doc_sistema.json'

    try:
        with open(output_yaml, 'w', encoding='utf-8') as f:
            yaml.dump(doc, f, default_flow_style=False, allow_unicode=True, sort_keys=False)
        print(f"✅ YAML salvo em: {output_yaml.resolve()}")
    except Exception as e:
        print(f"ERRO ao salvar YAML: {e}")

    try:
        with open(output_json, 'w', encoding='utf-8') as f:
            json.dump(doc, f, ensure_ascii=False, indent=2)
        print(f"✅ JSON salvo em: {output_json.resolve()}")
    except Exception as e:
        print(f"ERRO ao salvar JSON: {e}")

    print("\nDocumentação gerada com sucesso - VERSÃO FINAL!")

