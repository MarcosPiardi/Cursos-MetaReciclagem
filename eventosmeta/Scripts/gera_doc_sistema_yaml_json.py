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
import ast
import json
import yaml
from datetime import date
from pathlib import Path

# ============================================================
# CONFIGURAÇÃO — edite conforme necessário
# ============================================================

BASE_DIR = Path(__file__).resolve().parent.parent

# Apps do projeto (exclui apps de terceiros)
APPS_PROJETO = [
    "apps/accounts",
    "apps/interessados",
    "apps/eventos",
    "apps/selecao",
    "apps/academico",
    "apps/portal",
    "apps/scripts_admin",
    "dashboard",
]

# ============================================================
# SEÇÕES NARRATIVAS — edite manualmente quando necessário
# ============================================================

DESCRICAO_SISTEMA = (
    "Sistema desenvolvido em Django para gestão de eventos, inscrições, "
    "classificação de candidatos e processos acadêmicos posteriores "
    "(matrícula, avaliações, certificados, relatórios)."
)

PRIMARY_FLOW = "Inscrição -> Classificação -> Resultado -> Matrícula -> Avaliação -> Certificado"

FLUXOS_NEGOCIO = {
    "classificacao": {
        "description": "Processo de avaliação e ordenação de inscrições com base em critérios configuráveis por evento.",
        "detailed_documentation": {
            "file": "2026-04-15_resumo_tecnico_classificacao.md",
            "role": "Fonte técnica oficial do subsistema de Classificação"
        },
        "summary_steps": [
            "Leitura dos critérios ativos do evento (EventoCriterio)",
            "Cálculo de pontuação por critério PONTUACAO",
            "Aplicação de ordenação por critério ORDENACAO",
            "Desempate final por data_inscricao (ordem de chegada)",
            "Definição de posição final e flags (classificado/lista_espera)",
            "Persistência em Classificacao e InscricaoCriterioAtendido",
        ],
    },
    "matricula": {
        "description": "Matrícula de classificados em turmas, com validação de capacidade, proteção contra duplicidade e atomicidade.",
        "summary_steps": [
            "Seleção de classificações no admin (mesmo evento)",
            "Escolha da turma de destino",
            "Validação de vagas disponíveis",
            "Criação de Matricula (número auto-gerado)",
            "Atualização do status da inscrição para CONFIRMADA",
            "Criação automática de Avaliacao (signal post_save)",
        ],
    },
    "avaliacao_e_certificado": {
        "description": "Registro de desempenho do aluno e emissão de certificado.",
        "summary_steps": [
            "Lançamento de nota e frequência no admin",
            "Aprovação: nota >= 7.0 E frequência >= 75%",
            "Geração e download de certificado (individual ou lote ZIP)",
        ],
    },
}

WARNINGS_ONBOARDING = [
    "Não alterar ClassificadorService sem entender critérios e desempate",
    "Classificação é área sensível — alterações impactam resultados diretos",
    "CPF e NIS são criptografados; usar cpf_hash para buscas",
    "Matrícula em lote exige status ATIVA e CONFIRMADA cadastrados no banco",
    "admin_site customizado (CustomAdminSite) — não usar o admin padrão do Django",
]

RISKS_AND_NOTES = [
    "Subsistema de Classificação é crítico e complexo",
    "Documentação especializada deve ser mantida alinhada ao código",
    "Alterações em critérios impactam resultados de eventos já processados",
    "CPF criptografado exige FERNET_KEY no .env — sem ela o sistema não inicia",
    "Status de matrícula e inscrição precisam existir no banco com nomes exatos (ex: ATIVA, CONFIRMADA, Pendente)",
]

# ============================================================
# FUNÇÕES DE EXTRAÇÃO
# ============================================================

def arquivo_existe(app_path, nome):
    """Verifica se um arquivo existe dentro do app."""
    return (BASE_DIR / app_path / nome).exists()


def extrair_classes_python(app_path, nome_arquivo):
    """Retorna lista de nomes de classes definidas no arquivo."""
    caminho = BASE_DIR / app_path / nome_arquivo
    if not caminho.exists():
        return []
    try:
        tree = ast.parse(caminho.read_text(encoding="utf-8"))
        return [node.name for node in ast.walk(tree) if isinstance(node, ast.ClassDef)]
    except Exception:
        return []


def extrair_actions_admin(app_path):
    """
    Extrai as descriptions das actions do admin.py.
    Busca por short_description e @admin.action(description=...)
    """
    caminho = BASE_DIR / app_path / "admin.py"
    if not caminho.exists():
        return []

    actions = []
    try:
        conteudo = caminho.read_text(encoding="utf-8")
        tree = ast.parse(conteudo)

        for node in ast.walk(tree):
            # Padrão: func.short_description = '...'
            if isinstance(node, ast.Assign):
                for target in node.targets:
                    if isinstance(target, ast.Attribute) and target.attr == "short_description":
                        if isinstance(node.value, ast.Constant):
                            actions.append(node.value.value)

            # Padrão: @admin.action(description='...')
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                for decorator in node.decorator_list:
                    if isinstance(decorator, ast.Call):
                        for keyword in decorator.keywords:
                            if keyword.arg == "description" and isinstance(keyword.value, ast.Constant):
                                actions.append(keyword.value.value)
    except Exception:
        pass

    # Remove duplicatas preservando ordem
    vistos = set()
    resultado = []
    for a in actions:
        if a not in vistos:
            vistos.add(a)
            resultado.append(a)
    return resultado


def extrair_urls(app_path):
    """Extrai os paths definidos no urls.py do app."""
    caminho = BASE_DIR / app_path / "urls.py"
    if not caminho.exists():
        return []

    urls = []
    try:
        conteudo = caminho.read_text(encoding="utf-8")
        tree = ast.parse(conteudo)

        for node in ast.walk(tree):
            if isinstance(node, ast.Call):
                func = node.func
                nome_func = ""
                if isinstance(func, ast.Name):
                    nome_func = func.id
                elif isinstance(func, ast.Attribute):
                    nome_func = func.attr

                if nome_func == "path" and node.args:
                    primeiro = node.args[0]
                    if isinstance(primeiro, ast.Constant):
                        urls.append("/" + primeiro.value)
    except Exception:
        pass

    return urls


def extrair_management_commands(app_path):
    """Lista management commands do app."""
    commands_dir = BASE_DIR / app_path / "management" / "commands"
    if not commands_dir.exists():
        return []
    return [
        f.stem
        for f in commands_dir.glob("*.py")
        if not f.name.startswith("_")
    ]


def extrair_models(app_path):
    """Retorna lista de classes de model definidas em models.py."""
    return extrair_classes_python(app_path, "models.py")


def extrair_services(app_path):
    """Retorna lista de classes de service definidas em services.py."""
    return extrair_classes_python(app_path, "services.py")


def nome_app(app_path):
    """Retorna o nome curto do app a partir do caminho."""
    return Path(app_path).name


# ============================================================
# MONTAGEM DO DOCUMENTO
# ============================================================

def montar_doc():
    doc = {
        "system": {
            "name": "Sistema Acadêmico / MetaReciclagem",
            "description": DESCRICAO_SISTEMA,
            "versao_documentacao": str(date.today()),
        },
        "documentation_strategy": {
            "approach": "referenciada",
            "rationale": (
                "A documentação principal mantém visão sistêmica e arquitetural. "
                "Subsistemas complexos possuem documentação técnica especializada "
                "em arquivos separados."
            ),
        },
        "overview": {
            "main_domains": ["Eventos", "Inscrições", "Classificação", "Matrícula", "Acadêmico (Avaliações e Certificados)"],
            "primary_flow": PRIMARY_FLOW,
        },
        "architecture": {
            "framework": "Django",
            "language": "Python",
            "database": "SQLite (dev) / configurável via .env",
            "patterns": [
                "Apps desacoplados",
                "Services para regras de negócio",
                "Admin Django customizado como interface operacional",
                "Templates para apresentação",
                "Signals para automação (pós-save/delete)",
            ],
            "separation_of_concerns": {
                "models": "Persistência de dados e validações",
                "services": "Regras de negócio e cálculos",
                "admin": "Operações em massa, exportações e controle",
                "templates": "Interface e UX",
                "signals": "Automações pós-operação",
            },
        },
        "apps": {},
        "business_flows": FLUXOS_NEGOCIO,
        "onboarding": {
            "recommended_reading_order": [
                "documentacao_sistema.yaml (este arquivo)",
                "2026-04-15_resumo_tecnico_classificacao.md",
                "apps/selecao/services.py (ClassificadorService)",
                "apps/academico/models.py (Matricula, signals)",
                "apps/eventos/models.py (Criterio, EventoCriterio)",
                "Código (services -> models -> admin)",
            ],
            "warnings": WARNINGS_ONBOARDING,
        },
        "risks_and_notes": RISKS_AND_NOTES,
    }

    for app_path in APPS_PROJETO:
        key = nome_app(app_path)

        models = extrair_models(app_path)
        services = extrair_services(app_path)
        actions = extrair_actions_admin(app_path)
        urls = extrair_urls(app_path)
        commands = extrair_management_commands(app_path)

        entrada = {
            "caminho": app_path,
            "arquivos_detectados": {
                "models": arquivo_existe(app_path, "models.py"),
                "services": arquivo_existe(app_path, "services.py"),
                "admin": arquivo_existe(app_path, "admin.py"),
                "urls": arquivo_existe(app_path, "urls.py"),
            },
        }

        if models:
            entrada["models"] = models
        if services:
            entrada["services"] = services
        if actions:
            entrada["admin_actions"] = actions
        if urls:
            entrada["urls"] = urls
        if commands:
            entrada["management_commands"] = commands

        doc["apps"][key] = entrada

    return doc


# ============================================================
# SAÍDA
# ============================================================

def salvar(doc):
    yaml_path = BASE_DIR / "documentacao_sistema.yaml"
    json_path = BASE_DIR / "documentacao_sistema.json"

    # YAML
    with open(yaml_path, "w", encoding="utf-8") as f:
        yaml.dump(doc, f, allow_unicode=True, default_flow_style=False, sort_keys=False)

    # JSON
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(doc, f, ensure_ascii=False, indent=2)

    print(f"Gerado: {yaml_path}")
    print(f"Gerado: {json_path}")


if __name__ == "__main__":
    doc = montar_doc()
    salvar(doc)
    print("Concluído.")




