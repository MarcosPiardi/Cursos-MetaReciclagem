"""
gerar_documentacao.py
Gera automaticamente três arquivos de documentação do projeto Django:

  1. stack_e_configuracoes.txt
  2. requisitos_e_funcionalidades.txt
  3. diretrizes_e_padroes.txt

Salvar em:
  C:\\PMS\\PMS2025\\Inscr-Meta\\prg-Meta\\Eventos-MetaReciclagem\\eventosmeta\\Scripts\\

Saída em:
  C:\\PMS\\PMS2025\\Inscr-Meta\\Meta-Memória\\docs_gerados\\

Uso:
  python Scripts\\gerar_documentacao.py           (gera os 3)
  python Scripts\\gerar_documentacao.py stack      (só stack)
  python Scripts\\gerar_documentacao.py requisitos (só requisitos)
  python Scripts\\gerar_documentacao.py diretrizes (só diretrizes)
"""

import ast
import re
import subprocess
import sys
from pathlib import Path
from datetime import datetime

# ══════════════════════════════════════════════
# CONFIGURAÇÃO DE CAMINHOS
# ══════════════════════════════════════════════

SCRIPT_DIR   = Path(__file__).resolve().parent
PROJECT_ROOT = SCRIPT_DIR.parent       # .../eventosmeta/
REPO_ROOT    = PROJECT_ROOT.parent     # .../Eventos-MetaReciclagem/

OUTPUT_DIR = Path(
    r"C:\PMS\PMS2025\Inscr-Meta\Meta-Memória\docs_gerados"
)

DATE_PREFIX = datetime.now().strftime("%Y-%m-%d")


# ══════════════════════════════════════════════
# HELPERS COMPARTILHADOS
# ══════════════════════════════════════════════

def ler_arquivo(path: Path, encoding="utf-8") -> str:
    """Lê arquivo com fallback de encoding."""
    for enc in (encoding, "utf-8-sig", "latin-1"):
        try:
            return path.read_text(encoding=enc)
        except (UnicodeDecodeError, FileNotFoundError):
            continue
    return ""


def encontrar_arquivo(nome: str, base: Path) -> Path | None:
    """Busca recursiva por nome de arquivo."""
    for p in base.rglob(nome):
        if ".git" not in p.parts and "venv" not in p.parts:
            return p
    return None


def ignorar_path(path: Path) -> bool:
    """Retorna True para paths que devem ser ignorados."""
    return any(
        p in path.parts
        for p in ("venv", ".git", "__pycache__", "migrations", "node_modules")
    )


def arquivos_python(base: Path) -> list[Path]:
    """Lista todos os .py do projeto ignorando venv/git/cache."""
    return [p for p in base.rglob("*.py") if not ignorar_path(p)]


def _tem_pacote(nome: str) -> bool:
    req = encontrar_arquivo("requirements.txt", REPO_ROOT)
    if not req:
        return False
    return nome.lower() in ler_arquivo(req).lower()


def listar_diretorios(base: Path) -> str:
    """Gera árvore de diretórios simplificada."""
    ignorar = ("venv", ".git", "__pycache__", "node_modules",
                ".vscode", "staticfiles", "migrations")
    linhas = []

    def _walk(path: Path, prefix: str = "", nivel: int = 0):
        if nivel > 4:
            return
        try:
            itens = sorted(path.iterdir(), key=lambda x: (x.is_file(), x.name))
        except PermissionError:
            return
        itens = [i for i in itens if i.name not in ignorar and not i.name.startswith(".")]
        for i, item in enumerate(itens):
            conector = "└── " if i == len(itens) - 1 else "├── "
            linhas.append(f"{prefix}{conector}{item.name}")
            if item.is_dir():
                extensao = "    " if i == len(itens) - 1 else "│   "
                _walk(item, prefix + extensao, nivel + 1)

    linhas.append(f"{base.name}/")
    _walk(base)
    return "\n".join(linhas)


# ══════════════════════════════════════════════
# MÓDULO 1 — STACK E CONFIGURAÇÕES
# ══════════════════════════════════════════════

def sc_versao_python() -> str:
    return f"{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}"


def sc_versao_django() -> str:
    req = encontrar_arquivo("requirements.txt", REPO_ROOT)
    if req:
        for linha in ler_arquivo(req).splitlines():
            if linha.lower().startswith("django=="):
                return linha.split("==")[1].strip()
    try:
        import django
        return django.__version__
    except ImportError:
        return "Não identificado"


def sc_dependencias() -> dict:
    req_path = encontrar_arquivo("requirements.txt", REPO_ROOT)
    if not req_path:
        return {}
    deps = {}
    secao = "Geral"
    for linha in ler_arquivo(req_path).splitlines():
        linha = linha.strip()
        if not linha:
            continue
        if linha.startswith("#"):
            secao = linha.lstrip("# ").strip()
            deps.setdefault(secao, [])
        elif "==" in linha or ">=" in linha or linha[0].isalpha():
            deps.setdefault(secao, []).append(linha)
    return deps


def sc_config_banco() -> dict:
    resultado = {}
    for base in (PROJECT_ROOT, REPO_ROOT):
        env_path = encontrar_arquivo(".env", base)
        if env_path:
            for linha in ler_arquivo(env_path).splitlines():
                if linha.startswith("DATABASE") or linha.startswith("DB_"):
                    chave, _, valor = linha.partition("=")
                    if "PASSWORD" in chave.upper() or "SECRET" in chave.upper():
                        valor = "********"
                    resultado[chave.strip()] = valor.strip()
            break
    if not resultado:
        settings_path = encontrar_arquivo("settings.py", PROJECT_ROOT)
        if settings_path:
            conteudo = ler_arquivo(settings_path)
            match = re.search(r"DATABASES\s*=\s*\{(.+?)\n\}", conteudo, re.DOTALL)
            if match:
                resultado["DATABASES_RAW"] = match.group(0)[:400]
    return resultado


def sc_variaveis_env() -> dict:
    sensiveis = ("PASSWORD", "SECRET", "KEY", "TOKEN", "PASS")
    for base in (PROJECT_ROOT, REPO_ROOT):
        env_path = encontrar_arquivo(".env", base)
        if env_path:
            variaveis = {}
            for linha in ler_arquivo(env_path).splitlines():
                linha = linha.strip()
                if not linha or linha.startswith("#"):
                    continue
                chave, _, valor = linha.partition("=")
                chave = chave.strip()
                if any(s in chave.upper() for s in sensiveis):
                    valor = "********"
                variaveis[chave] = valor.strip()
            return variaveis
    return {}


def sc_apps_instalados() -> list[str]:
    settings_path = encontrar_arquivo("settings.py", PROJECT_ROOT)
    if not settings_path:
        return []
    conteudo = ler_arquivo(settings_path)
    match = re.search(r"INSTALLED_APPS\s*=\s*\[(.+?)\]", conteudo, re.DOTALL)
    if not match:
        return []
    return re.findall(r"['\"]([^'\"]+)['\"]", match.group(1))


def sc_modelos_por_app() -> dict:
    resultado = {}
    for models_path in PROJECT_ROOT.rglob("models.py"):
        if ignorar_path(models_path):
            continue
        app = models_path.parent.name
        conteudo = ler_arquivo(models_path)
        try:
            tree = ast.parse(conteudo)
        except SyntaxError:
            resultado[app] = [{"nome": "(erro ao analisar)", "campos": []}]
            continue
        modelos = []
        for node in ast.walk(tree):
            if not isinstance(node, ast.ClassDef):
                continue
            bases = [
                (ast.unparse(b) if hasattr(ast, "unparse") else getattr(b, "id", ""))
                for b in node.bases
            ]
            if not any("Model" in str(b) for b in bases):
                continue
            campos = []
            for item in node.body:
                if isinstance(item, ast.Assign):
                    for target in item.targets:
                        if isinstance(target, ast.Name):
                            tipo = ""
                            if isinstance(item.value, ast.Call):
                                func = item.value.func
                                tipo = getattr(func, "attr", "") or getattr(func, "id", "")
                            campos.append(f"{target.id} ({tipo})" if tipo else target.id)
            modelos.append({"nome": node.name, "campos": campos[:10]})
        if modelos:
            resultado[app] = modelos
    return resultado


def sc_urls() -> list[str]:
    urls_path = encontrar_arquivo("urls.py", PROJECT_ROOT)
    if not urls_path:
        return []
    conteudo = ler_arquivo(urls_path)
    padroes = re.findall(r"path\(['\"]([^'\"]*)['\"]", conteudo)
    includes = re.findall(r"include\(['\"]([^'\"]*)['\"]", conteudo)
    return padroes + [f"include: {i}" for i in includes]


def sc_autenticacao() -> str:
    settings_path = encontrar_arquivo("settings.py", PROJECT_ROOT)
    if not settings_path:
        return "  - django.contrib.auth.backends.ModelBackend (padrão)"
    conteudo = ler_arquivo(settings_path)
    match = re.search(r"AUTHENTICATION_BACKENDS\s*=\s*\[(.+?)\]", conteudo, re.DOTALL)
    if match:
        backends = re.findall(r"['\"]([^'\"]+)['\"]", match.group(1))
        return "\n".join(f"  - {b}" for b in backends)
    return "  - django.contrib.auth.backends.ModelBackend (padrão)"


def sc_middlewares() -> list[str]:
    settings_path = encontrar_arquivo("settings.py", PROJECT_ROOT)
    if not settings_path:
        return []
    conteudo = ler_arquivo(settings_path)
    match = re.search(r"MIDDLEWARE\s*=\s*\[(.+?)\]", conteudo, re.DOTALL)
    if not match:
        return []
    return re.findall(r"['\"]([^'\"]+)['\"]", match.group(1))


def sc_email() -> dict:
    settings_path = encontrar_arquivo("settings.py", PROJECT_ROOT)
    if not settings_path:
        return {}
    conteudo = ler_arquivo(settings_path)
    config = {}
    for chave in ("EMAIL_HOST", "EMAIL_PORT", "EMAIL_USE_TLS",
                  "EMAIL_USE_SSL", "DEFAULT_FROM_EMAIL", "EMAIL_BACKEND"):
        match = re.search(rf"^{chave}\s*=\s*(.+)$", conteudo, re.MULTILINE)
        if match:
            config[chave] = match.group(1).strip().strip("'\"")
    return config


def sc_static_media() -> dict:
    settings_path = encontrar_arquivo("settings.py", PROJECT_ROOT)
    if not settings_path:
        return {}
    conteudo = ler_arquivo(settings_path)
    config = {}
    for chave in ("STATIC_URL", "STATIC_ROOT", "MEDIA_URL", "MEDIA_ROOT", "STATICFILES_DIRS"):
        match = re.search(rf"^{chave}\s*=\s*(.+)$", conteudo, re.MULTILINE)
        if match:
            config[chave] = match.group(1).strip()
    return config


def sc_fixtures() -> dict:
    fixtures = {}
    for f in PROJECT_ROOT.rglob("*.json"):
        if "fixtures" in f.parts and "venv" not in f.parts:
            app = f.parent.parent.name
            fixtures.setdefault(app, []).append(f.name)
    return fixtures


def sc_management_commands() -> list[str]:
    comandos = []
    for cmd_path in PROJECT_ROOT.rglob("management/commands/*.py"):
        if cmd_path.name != "__init__.py" and "venv" not in cmd_path.parts:
            partes = cmd_path.parts
            app = cmd_path.parts[partes.index("commands") - 2]
            comandos.append(f"{app}: {cmd_path.stem}")
    return comandos


def sc_arquivos_raiz() -> list[str]:
    arquivos = []
    for ext in ("*.txt", "*.md", "*.cfg", "*.ini", "*.toml"):
        for f in REPO_ROOT.glob(ext):
            arquivos.append(f.name)
    return arquivos


def sc_gitignore() -> str:
    gi_path = encontrar_arquivo(".gitignore", REPO_ROOT)
    if not gi_path:
        return "(não encontrado)"
    return ler_arquivo(gi_path)[:1500]


def gerar_stack(agora: str) -> str:
    linhas = []

    def h1(t): linhas.append(f"\n{'=' * 60}\n# {t}\n{'=' * 60}")
    def h2(t): linhas.append(f"\n## {t}\n{'-' * 40}")
    def h3(t): linhas.append(f"\n### {t}")
    def L(t=""): linhas.append(t)

    h1("Tecnologia - Stack e Configurações")
    L("Projeto: Sistema MetaReciclagem")
    L(f"Gerado automaticamente em: {agora}")

    h1("Stack Tecnológica")
    h2("Backend")
    L(f"- Framework:       Django {sc_versao_django()}")
    L(f"- Linguagem:       Python {sc_versao_python()}")
    L(f"- ORM:             Django ORM")
    config_banco = sc_config_banco()
    L(f"- Banco de Dados:  {config_banco.get('DATABASE_ENGINE', 'Verificar .env / settings.py')}")
    h2("Frontend")
    L("- Templates: Django Templates")
    L("- CSS Framework: Bootstrap")
    L("- JavaScript: Vanilla JS")
    h2("Ambiente de Desenvolvimento")
    L("- SO:              Windows")
    L("- Editor:          VS Code")
    L("- Ambiente Virtual: venv")
    L(f"- Python:          {sc_versao_python()}")

    h1("Configuração de Banco de Dados")
    h2("Variáveis identificadas (.env / settings)")
    for k, v in config_banco.items():
        L(f"  {k}={v}")
    h2("Variáveis de Ambiente (.env)")
    env_vars = sc_variaveis_env()
    if env_vars:
        for k, v in env_vars.items():
            L(f"  {k}={v}")
    else:
        L("  (arquivo .env não encontrado ou vazio)")

    h1("Dependências (requirements.txt)")
    deps = sc_dependencias()
    if deps:
        for secao, pkgs in deps.items():
            if pkgs:
                h3(secao)
                for p in pkgs:
                    L(f"  - {p}")
    else:
        L("(requirements.txt não encontrado)")

    h1("Arquitetura - Estrutura de Diretórios")
    L("```")
    try:
        L(listar_diretorios(REPO_ROOT))
    except Exception as e:
        L(f"(erro ao gerar árvore: {e})")
    L("```")

    h1("Apps Django (INSTALLED_APPS)")
    apps = sc_apps_instalados()
    for app in apps:
        L(f"  - {app}")
    if not apps:
        L("(não identificado)")

    h1("Modelos de Dados por App")
    modelos = sc_modelos_por_app()
    for app, lista in modelos.items():
        h2(f"App: {app}")
        for m in lista:
            if isinstance(m, dict):
                L(f"  - {m['nome']}")
                if m["campos"]:
                    L(f"    Campos: {', '.join(m['campos'])}")
            else:
                L(f"  {m}")

    h1("URLs Principais")
    for u in sc_urls() or ["(não identificado)"]:
        L(f"  - {u}")

    h1("Autenticação")
    L(sc_autenticacao())

    h1("Middlewares")
    for m in sc_middlewares():
        L(f"  - {m}")

    h1("Configurações de E-mail")
    email_cfg = sc_email()
    if email_cfg:
        for k, v in email_cfg.items():
            L(f"  {k} = {v}")
    else:
        L("(não identificado)")

    h1("Arquivos Estáticos e Media")
    static = sc_static_media()
    if static:
        for k, v in static.items():
            L(f"  {k} = {v}")
    else:
        L("(não identificado)")

    h1("Fixtures Disponíveis")
    fixtures = sc_fixtures()
    if fixtures:
        for app, lista in fixtures.items():
            h3(f"App: {app}")
            for f in lista:
                L(f"  - {f}")
    else:
        L("(nenhuma fixture encontrada)")

    h1("Management Commands Customizados")
    cmds = sc_management_commands()
    for c in cmds:
        L(f"  - {c}")
    if not cmds:
        L("(nenhum encontrado)")

    h1("Arquivos de Configuração na Raiz")
    for f in sc_arquivos_raiz():
        L(f"  - {f}")

    h1(".gitignore")
    L("```")
    L(sc_gitignore())
    L("```")

    h1("Comandos Úteis")
    h2("Setup Inicial")
    L("  python -m venv venv\n  venv\\Scripts\\activate\n  pip install -r requirements.txt"
      "\n  python manage.py migrate\n  python manage.py createsuperuser"
      "\n  python manage.py loaddata accounts/fixtures/*.json"
      "\n  python manage.py loaddata eventos/fixtures/*.json"
      "\n  python manage.py loaddata interessados/fixtures/*.json")
    h2("Desenvolvimento")
    L("  python manage.py runserver\n  python manage.py makemigrations"
      "\n  python manage.py migrate\n  python manage.py shell"
      "\n  python manage.py collectstatic")
    h2("Testes")
    L("  pytest\n  pytest --cov\n  pytest apps/selecao/tests/test_classificacao.py")

    L(f"\n\n{'=' * 60}\nFim do documento - Gerado em {agora}\n{'=' * 60}")
    return "\n".join(linhas)


# ══════════════════════════════════════════════
# MÓDULO 2 — REQUISITOS E FUNCIONALIDADES
# ══════════════════════════════════════════════

def rf_apps() -> list[str]:
    apps = []
    for p in PROJECT_ROOT.iterdir():
        if p.is_dir() and (p / "models.py").exists() and not ignorar_path(p):
            apps.append(p.name)
    return sorted(apps)


def rf_modelos_detalhados() -> dict:
    resultado = {}
    for models_path in PROJECT_ROOT.rglob("models.py"):
        if ignorar_path(models_path):
            continue
        app = models_path.parent.name
        conteudo = ler_arquivo(models_path)
        try:
            tree = ast.parse(conteudo)
        except SyntaxError:
            resultado[app] = [{"nome": "(erro)", "campos": [], "metodos": [], "meta": {}, "choices": []}]
            continue
        modelos = []
        for node in ast.walk(tree):
            if not isinstance(node, ast.ClassDef):
                continue
            bases = [
                (ast.unparse(b) if hasattr(ast, "unparse") else getattr(b, "id", ""))
                for b in node.bases
            ]
            if not any("Model" in str(b) for b in bases):
                continue
            campos, metodos, meta_info, choices = [], [], {}, []
            for item in node.body:
                if isinstance(item, ast.Assign):
                    for target in item.targets:
                        if isinstance(target, ast.Name):
                            nome_campo = target.id
                            tipo = ""
                            if isinstance(item.value, ast.Call):
                                func = item.value.func
                                tipo = getattr(func, "attr", "") or getattr(func, "id", "")
                            if nome_campo.isupper():
                                choices.append(nome_campo)
                            elif not nome_campo.startswith("_"):
                                campos.append({"nome": nome_campo, "tipo": tipo})
                elif isinstance(item, ast.FunctionDef):
                    if not item.name.startswith("__"):
                        metodos.append(item.name)
                elif isinstance(item, ast.ClassDef) and item.name == "Meta":
                    for mi in item.body:
                        if isinstance(mi, ast.Assign):
                            for t in mi.targets:
                                if isinstance(t, ast.Name):
                                    try:
                                        val = ast.unparse(mi.value) if hasattr(ast, "unparse") else "..."
                                    except Exception:
                                        val = "..."
                                    meta_info[t.id] = val
            modelos.append({"nome": node.name, "campos": campos, "metodos": metodos,
                             "meta": meta_info, "choices": choices})
        if modelos:
            resultado[app] = modelos
    return resultado


def rf_views_por_app() -> dict:
    resultado = {}
    for views_path in PROJECT_ROOT.rglob("views.py"):
        if ignorar_path(views_path):
            continue
        app = views_path.parent.name
        conteudo = ler_arquivo(views_path)
        try:
            tree = ast.parse(conteudo)
        except SyntaxError:
            continue
        views = []
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                args = [a.arg for a in node.args.args]
                if args and args[0] == "request":
                    decs = [(ast.unparse(d) if hasattr(ast, "unparse") else "") for d in node.decorator_list]
                    views.append({"nome": node.name, "tipo": "function", "decorators": decs})
            elif isinstance(node, ast.ClassDef):
                bases = [(ast.unparse(b) if hasattr(ast, "unparse") else getattr(b, "id", "")) for b in node.bases]
                if any("View" in str(b) or "Mixin" in str(b) for b in bases):
                    views.append({"nome": node.name, "tipo": "class", "bases": bases})
        if views:
            resultado[app] = views
    return resultado


def rf_urls_por_app() -> dict:
    resultado = {}
    for urls_path in PROJECT_ROOT.rglob("urls.py"):
        if ignorar_path(urls_path):
            continue
        app = urls_path.parent.name
        conteudo = ler_arquivo(urls_path)
        padroes = re.findall(r"path\(['\"]([^'\"]*)['\"].*?name=['\"]([^'\"]*)['\"]", conteudo)
        includes = re.findall(r"include\(['\"]([^'\"]*)['\"]", conteudo)
        entradas = [f"{p[0]}  →  name='{p[1]}'" for p in padroes]
        entradas += [f"include: {i}" for i in includes]
        if entradas:
            resultado[app] = entradas
    return resultado


def rf_forms_por_app() -> dict:
    resultado = {}
    for forms_path in PROJECT_ROOT.rglob("forms.py"):
        if ignorar_path(forms_path):
            continue
        app = forms_path.parent.name
        conteudo = ler_arquivo(forms_path)
        try:
            tree = ast.parse(conteudo)
        except SyntaxError:
            continue
        forms = []
        for node in ast.walk(tree):
            if isinstance(node, ast.ClassDef):
                bases = [(ast.unparse(b) if hasattr(ast, "unparse") else getattr(b, "id", "")) for b in node.bases]
                if any("Form" in str(b) for b in bases):
                    campos = []
                    for item in node.body:
                        if isinstance(item, ast.Assign):
                            for t in item.targets:
                                if isinstance(t, ast.Name) and not t.id.startswith("_"):
                                    tipo = ""
                                    if isinstance(item.value, ast.Call):
                                        func = item.value.func
                                        tipo = getattr(func, "attr", "") or getattr(func, "id", "")
                                    campos.append({"nome": t.id, "tipo": tipo})
                    forms.append({"nome": node.name, "campos": campos})
        if forms:
            resultado[app] = forms
    return resultado


def rf_admin_por_app() -> dict:
    resultado = {}
    for admin_path in PROJECT_ROOT.rglob("admin.py"):
        if ignorar_path(admin_path):
            continue
        app = admin_path.parent.name
        conteudo = ler_arquivo(admin_path)
        registros = list(set(
            re.findall(r"@admin\.register\((\w+)\)", conteudo) +
            re.findall(r"admin\.site\.register\((\w+)", conteudo)
        ))
        classes_admin = re.findall(r"class\s+(\w+Admin)\s*\(", conteudo)
        list_displays = {}
        for match in re.finditer(r"class\s+(\w+Admin).*?list_display\s*=\s*\[([^\]]+)\]", conteudo, re.DOTALL):
            list_displays[match.group(1)] = re.findall(r"['\"]([^'\"]+)['\"]", match.group(2))
        entradas = {"modelos_registrados": registros, "classes_admin": classes_admin, "list_displays": list_displays}
        if any(entradas.values()):
            resultado[app] = entradas
    return resultado


def rf_services() -> dict:
    resultado = {}
    for svc_path in PROJECT_ROOT.rglob("services.py"):
        if ignorar_path(svc_path):
            continue
        app = svc_path.parent.name
        conteudo = ler_arquivo(svc_path)
        try:
            tree = ast.parse(conteudo)
        except SyntaxError:
            continue
        itens = []
        for node in ast.walk(tree):
            if isinstance(node, ast.ClassDef):
                metodos = [i.name for i in node.body if isinstance(i, ast.FunctionDef) and not i.name.startswith("__")]
                itens.append({"tipo": "class", "nome": node.name, "metodos": metodos})
            elif isinstance(node, ast.FunctionDef) and not node.name.startswith("_"):
                itens.append({"tipo": "function", "nome": node.name})
        if itens:
            resultado[app] = itens
    return resultado


def rf_management_commands() -> dict:
    resultado = {}
    for cmd_path in PROJECT_ROOT.rglob("management/commands/*.py"):
        if ignorar_path(cmd_path) or cmd_path.name == "__init__.py":
            continue
        partes = cmd_path.parts
        try:
            app = partes[partes.index("commands") - 2]
        except (ValueError, IndexError):
            app = "desconhecido"
        conteudo = ler_arquivo(cmd_path)
        help_match = re.search(r"help\s*=\s*['\"]([^'\"]+)['\"]", conteudo)
        resultado.setdefault(app, []).append({
            "nome": cmd_path.stem,
            "descricao": help_match.group(1) if help_match else "(sem descrição)",
        })
    return resultado


def rf_fixtures_por_app() -> dict:
    resultado = {}
    for f in PROJECT_ROOT.rglob("fixtures/*.json"):
        if ignorar_path(f):
            continue
        app = f.parent.parent.name
        tam = f.stat().st_size
        resultado.setdefault(app, []).append(
            f"{f.name} ({tam // 1024} KB)" if tam >= 1024 else f"{f.name} ({tam} bytes)"
        )
    return resultado


def rf_templates() -> dict:
    resultado = {}
    templates_dir = PROJECT_ROOT / "templates"
    if not templates_dir.exists():
        for td in PROJECT_ROOT.rglob("templates"):
            if td.is_dir() and not ignorar_path(td):
                templates_dir = td
                break
    if templates_dir.exists():
        for html in templates_dir.rglob("*.html"):
            pasta = html.parent.name if html.parent != templates_dir else "(raiz)"
            resultado.setdefault(pasta, []).append(html.name)
    return resultado


def rf_signals() -> dict:
    resultado = {}
    for sig_path in PROJECT_ROOT.rglob("signals.py"):
        if ignorar_path(sig_path):
            continue
        app = sig_path.parent.name
        conteudo = ler_arquivo(sig_path)
        sinais = re.findall(r"@[\w.]*(?:post_save|pre_save|post_delete|pre_delete|[\w]+_signal)\b", conteudo)
        receivers = re.findall(r"def\s+(\w+)\s*\(sender", conteudo)
        if sinais or receivers:
            resultado[app] = {"decorators": list(set(sinais)), "receivers": receivers}
    return resultado


def rf_autenticacao() -> str:
    settings_path = encontrar_arquivo("settings.py", PROJECT_ROOT)
    if not settings_path:
        return "(não identificado)"
    conteudo = ler_arquivo(settings_path)
    backends = []
    match = re.search(r"AUTHENTICATION_BACKENDS\s*=\s*\[(.+?)\]", conteudo, re.DOTALL)
    if match:
        backends = re.findall(r"['\"]([^'\"]+)['\"]", match.group(1))
    login_url = re.search(r"LOGIN_URL\s*=\s*['\"]([^'\"]+)['\"]", conteudo)
    login_red = re.search(r"LOGIN_REDIRECT_URL\s*=\s*['\"]([^'\"]+)['\"]", conteudo)
    logout_red = re.search(r"LOGOUT_REDIRECT_URL\s*=\s*['\"]([^'\"]+)['\"]", conteudo)
    linhas = []
    if backends:
        linhas.append("Backends:")
        for b in backends:
            linhas.append(f"  - {b}")
    if login_url:
        linhas.append(f"LOGIN_URL = {login_url.group(1)}")
    if login_red:
        linhas.append(f"LOGIN_REDIRECT_URL = {login_red.group(1)}")
    if logout_red:
        linhas.append(f"LOGOUT_REDIRECT_URL = {logout_red.group(1)}")
    return "\n".join(linhas) if linhas else "(configurações padrão Django)"


def rf_testes() -> dict:
    resultado = {}
    for test_path in PROJECT_ROOT.rglob("test*.py"):
        if ignorar_path(test_path):
            continue
        app = test_path.parent.name if "tests" not in test_path.parent.name else test_path.parent.parent.name
        conteudo = ler_arquivo(test_path)
        try:
            tree = ast.parse(conteudo)
        except SyntaxError:
            continue
        for node in ast.walk(tree):
            if isinstance(node, ast.ClassDef):
                bases = [(ast.unparse(b) if hasattr(ast, "unparse") else getattr(b, "id", "")) for b in node.bases]
                if any("Test" in str(b) for b in bases):
                    metodos = [i.name for i in node.body if isinstance(i, ast.FunctionDef) and i.name.startswith("test_")]
                    resultado.setdefault(app, []).append({"classe": node.name, "testes": metodos})
    return resultado


def gerar_requisitos(agora: str) -> str:
    linhas = []

    def h1(t): linhas.append(f"\n{'=' * 60}\n# {t}\n{'=' * 60}")
    def h2(t): linhas.append(f"\n## {t}\n{'-' * 40}")
    def h3(t): linhas.append(f"\n### {t}")
    def L(t=""): linhas.append(t)

    h1("Projeto - Requisitos e Funcionalidades")
    L("Sistema: MetaReciclagem - Gestão de Eventos e Cursos")
    L(f"Gerado automaticamente em: {agora}")

    h1("Apps Django do Projeto")
    for app in rf_apps():
        L(f"  - {app}")

    h1("Modelos de Dados (Models)")
    for app, lista in rf_modelos_detalhados().items():
        h2(f"App: {app}")
        for m in lista:
            h3(m["nome"])
            if m.get("campos"):
                L("  Campos:")
                for c in m["campos"]:
                    L(f"    - {c['nome']}" + (f" ({c['tipo']})" if c.get("tipo") else ""))
            if m.get("metodos"):
                L(f"  Métodos: {', '.join(m['metodos'])}")
            if m.get("meta"):
                for k, v in m["meta"].items():
                    L(f"  Meta.{k} = {v}")
            if m.get("choices"):
                L(f"  Choices: {', '.join(m['choices'])}")

    h1("Views por App")
    for app, lista in rf_views_por_app().items():
        h2(f"App: {app}")
        for v in lista:
            if v["tipo"] == "function":
                dec = f"  [{', '.join(v['decorators'])}]" if v.get("decorators") else ""
                L(f"  - {v['nome']} (function){dec}")
            else:
                L(f"  - {v['nome']} (class: {', '.join(v.get('bases', []))})")

    h1("URLs por App")
    for app, lista in rf_urls_por_app().items():
        h2(f"App: {app}")
        for u in lista:
            L(f"  - {u}")

    h1("Formulários por App")
    forms = rf_forms_por_app()
    if forms:
        for app, lista in forms.items():
            h2(f"App: {app}")
            for f in lista:
                campos_str = ", ".join(
                    f"{c['nome']}({c['tipo']})" if c.get("tipo") else c["nome"]
                    for c in f["campos"]
                ) if f["campos"] else "(sem campos definidos)"
                L(f"  - {f['nome']}: {campos_str}")
    else:
        L("(nenhum forms.py encontrado)")

    h1("Configuração do Admin por App")
    for app, info in rf_admin_por_app().items():
        h2(f"App: {app}")
        if info.get("modelos_registrados"):
            L(f"  Modelos: {', '.join(info['modelos_registrados'])}")
        if info.get("classes_admin"):
            L(f"  Classes Admin: {', '.join(info['classes_admin'])}")
        for classe, campos in info.get("list_displays", {}).items():
            L(f"  {classe}.list_display: {', '.join(campos)}")

    h1("Services (Regras de Negócio)")
    services = rf_services()
    if services:
        for app, itens in services.items():
            h2(f"App: {app}")
            for item in itens:
                if item["tipo"] == "class":
                    L(f"  Classe: {item['nome']}")
                    for m in item.get("metodos", []):
                        L(f"    - {m}()")
                else:
                    L(f"  Função: {item['nome']}()")
    else:
        L("(nenhum services.py encontrado)")

    h1("Management Commands Customizados")
    cmds = rf_management_commands()
    if cmds:
        for app, lista in cmds.items():
            h2(f"App: {app}")
            for c in lista:
                L(f"  - {c['nome']}: {c['descricao']}")
    else:
        L("(nenhum encontrado)")

    h1("Fixtures por App")
    fixtures = rf_fixtures_por_app()
    if fixtures:
        for app, lista in fixtures.items():
            h2(f"App: {app}")
            for f in lista:
                L(f"  - {f}")
    else:
        L("(nenhuma fixture encontrada)")

    h1("Templates HTML")
    templates = rf_templates()
    if templates:
        for pasta, lista in templates.items():
            h3(f"Pasta: {pasta}")
            for t in sorted(lista):
                L(f"  - {t}")
    else:
        L("(nenhum template encontrado)")

    h1("Signals")
    signals = rf_signals()
    if signals:
        for app, info in signals.items():
            h2(f"App: {app}")
            if info.get("decorators"):
                L(f"  Decorators: {', '.join(info['decorators'])}")
            if info.get("receivers"):
                L(f"  Receivers: {', '.join(info['receivers'])}")
    else:
        L("(nenhum signals.py encontrado)")

    h1("Autenticação e Permissões")
    L(rf_autenticacao())

    h1("Testes Automatizados")
    testes = rf_testes()
    if testes:
        for app, lista in testes.items():
            h2(f"App: {app}")
            for t in lista:
                L(f"  Classe: {t['classe']}")
                for metodo in t["testes"]:
                    L(f"    - {metodo}")
    else:
        L("(nenhum arquivo de teste encontrado)")

    L(f"\n\n{'=' * 60}\nFim do documento - Gerado em {agora}\n{'=' * 60}")
    return "\n".join(linhas)


# ══════════════════════════════════════════════
# MÓDULO 3 — DIRETRIZES E PADRÕES
# ══════════════════════════════════════════════

def dp_nomenclatura() -> dict:
    resultado = {
        "models_pascal": [], "models_nao_pascal": [],
        "funcoes_snake": 0, "funcoes_nao_snake": [],
        "constantes_upper": 0, "constantes_nao_upper": [],
    }
    for py_path in arquivos_python(PROJECT_ROOT):
        conteudo = ler_arquivo(py_path)
        try:
            tree = ast.parse(conteudo)
        except SyntaxError:
            continue
        for node in ast.walk(tree):
            if isinstance(node, ast.ClassDef):
                bases = [(ast.unparse(b) if hasattr(ast, "unparse") else getattr(b, "id", "")) for b in node.bases]
                if any("Model" in str(b) for b in bases):
                    if node.name[0].isupper() and "_" not in node.name:
                        resultado["models_pascal"].append(node.name)
                    else:
                        resultado["models_nao_pascal"].append(node.name)
            elif isinstance(node, ast.FunctionDef):
                if node.name.startswith("_"):
                    continue
                if node.name == node.name.lower():
                    resultado["funcoes_snake"] += 1
                else:
                    resultado["funcoes_nao_snake"].append(node.name)
            elif isinstance(node, ast.Assign):
                for target in node.targets:
                    if isinstance(target, ast.Name):
                        nome = target.id
                        if nome.isupper() and len(nome) > 2:
                            resultado["constantes_upper"] += 1
                        elif nome.upper() == nome and len(nome) > 2:
                            resultado["constantes_nao_upper"].append(nome)
    return resultado


def dp_docstrings() -> dict:
    resultado = {"com_docstring": [], "sem_docstring": []}
    for py_path in arquivos_python(PROJECT_ROOT):
        if py_path.name not in ("models.py", "views.py", "services.py"):
            continue
        conteudo = ler_arquivo(py_path)
        try:
            tree = ast.parse(conteudo)
        except SyntaxError:
            continue
        app = py_path.parent.name
        for node in ast.walk(tree):
            if isinstance(node, (ast.ClassDef, ast.FunctionDef)):
                if node.name.startswith("_"):
                    continue
                tem_doc = (
                    node.body and isinstance(node.body[0], ast.Expr)
                    and isinstance(node.body[0].value, ast.Constant)
                    and isinstance(node.body[0].value.value, str)
                )
                ref = f"{app}/{py_path.name}::{node.name}"
                (resultado["com_docstring"] if tem_doc else resultado["sem_docstring"]).append(ref)
    return resultado


def dp_comentarios_pt() -> dict:
    palavras_pt = {
        "não", "sim", "para", "com", "sem", "por", "uma", "um", "são", "está",
        "retorna", "verifica", "calcula", "busca", "cria", "define",
        "lista", "obtém", "salva", "remove", "atualiza", "processa",
    }
    total = em_pt = 0
    exemplos_pt, exemplos_outros = [], []
    for py_path in arquivos_python(PROJECT_ROOT):
        for linha in ler_arquivo(py_path).splitlines():
            ls = linha.strip()
            if not ls.startswith("#"):
                continue
            comentario = ls.lstrip("# ").lower()
            if len(comentario) < 5:
                continue
            total += 1
            if set(comentario.split()) & palavras_pt:
                em_pt += 1
                if len(exemplos_pt) < 5:
                    exemplos_pt.append(ls[:80])
            else:
                if len(exemplos_outros) < 5:
                    exemplos_outros.append(ls[:80])
    return {
        "total": total,
        "em_portugues": em_pt,
        "percentual": round((em_pt / total * 100) if total else 0, 1),
        "exemplos_pt": exemplos_pt,
        "exemplos_outros": exemplos_outros,
    }


def dp_padroes_views() -> dict:
    resultado = {
        "login_required": 0, "get_object_or_404": 0,
        "messages_uso": 0, "select_related": 0,
        "prefetch_related": 0, "views_sem_login": [],
    }
    for views_path in PROJECT_ROOT.rglob("views.py"):
        if ignorar_path(views_path):
            continue
        conteudo = ler_arquivo(views_path)
        app = views_path.parent.name
        resultado["login_required"] += conteudo.count("@login_required")
        resultado["get_object_or_404"] += conteudo.count("get_object_or_404")
        resultado["messages_uso"] += conteudo.count("messages.")
        resultado["select_related"] += conteudo.count("select_related")
        resultado["prefetch_related"] += conteudo.count("prefetch_related")
        try:
            tree = ast.parse(conteudo)
            for node in ast.walk(tree):
                if isinstance(node, ast.FunctionDef):
                    args = [a.arg for a in node.args.args]
                    if not args or args[0] != "request":
                        continue
                    decs = [(ast.unparse(d) if hasattr(ast, "unparse") else "") for d in node.decorator_list]
                    if not any("login_required" in d for d in decs):
                        resultado["views_sem_login"].append(f"{app}::{node.name}")
        except SyntaxError:
            pass
    return resultado


def dp_service_layer() -> dict:
    resultado = {
        "services_encontrados": [], "uso_transaction_atomic": 0,
        "uso_logging": 0, "metodos_privados": 0,
        "metodos_publicos": 0, "uso_staticmethod": 0,
    }
    for svc_path in PROJECT_ROOT.rglob("services.py"):
        if ignorar_path(svc_path):
            continue
        app = svc_path.parent.name
        conteudo = ler_arquivo(svc_path)
        resultado["services_encontrados"].append(app)
        resultado["uso_transaction_atomic"] += conteudo.count("transaction.atomic")
        resultado["uso_logging"] += conteudo.count("logging.getLogger")
        resultado["uso_staticmethod"] += conteudo.count("@staticmethod")
        try:
            tree = ast.parse(conteudo)
            for node in ast.walk(tree):
                if isinstance(node, ast.FunctionDef):
                    if node.name.startswith("_"):
                        resultado["metodos_privados"] += 1
                    else:
                        resultado["metodos_publicos"] += 1
        except SyntaxError:
            pass
    return resultado


def dp_admin() -> dict:
    resultado = {
        "list_display": 0, "search_fields": 0, "list_filter": 0,
        "actions_customizadas": [], "inlines": [],
        "readonly_fields": 0, "fieldsets": 0, "exportacoes": [],
    }
    for admin_path in PROJECT_ROOT.rglob("admin.py"):
        if ignorar_path(admin_path):
            continue
        conteudo = ler_arquivo(admin_path)
        app = admin_path.parent.name
        resultado["list_display"] += conteudo.count("list_display")
        resultado["search_fields"] += conteudo.count("search_fields")
        resultado["list_filter"] += conteudo.count("list_filter")
        resultado["readonly_fields"] += conteudo.count("readonly_fields")
        resultado["fieldsets"] += conteudo.count("fieldsets")
        for match in re.finditer(r"@admin\.action\(description=['\"]([^'\"]+)['\"]", conteudo):
            resultado["actions_customizadas"].append(f"{app}: {match.group(1)}")
        for match in re.finditer(r"class\s+(\w+Inline)\s*\(", conteudo):
            resultado["inlines"].append(f"{app}: {match.group(1)}")
        if "HttpResponse" in conteudo and "csv" in conteudo.lower():
            resultado["exportacoes"].append(f"{app}: CSV/Excel")
        if "openpyxl" in conteudo or "xlwt" in conteudo:
            resultado["exportacoes"].append(f"{app}: Excel (openpyxl)")
        if "reportlab" in conteudo:
            resultado["exportacoes"].append(f"{app}: PDF")
    return resultado


def dp_testes() -> dict:
    resultado = {
        "arquivos_teste": [], "classes_teste": 0, "metodos_teste": 0,
        "uso_mock": 0, "apps_com_teste": [], "apps_sem_teste": [],
    }
    apps_com_teste = set()
    for test_path in PROJECT_ROOT.rglob("test*.py"):
        if ignorar_path(test_path):
            continue
        app = test_path.parent.name if "tests" not in test_path.parent.name else test_path.parent.parent.name
        conteudo = ler_arquivo(test_path)
        resultado["arquivos_teste"].append(str(test_path.relative_to(PROJECT_ROOT)))
        resultado["uso_mock"] += conteudo.count("mock") + conteudo.count("patch")
        try:
            tree = ast.parse(conteudo)
            for node in ast.walk(tree):
                if isinstance(node, ast.ClassDef):
                    bases = [(ast.unparse(b) if hasattr(ast, "unparse") else getattr(b, "id", "")) for b in node.bases]
                    if any("Test" in str(b) for b in bases):
                        resultado["classes_teste"] += 1
                        apps_com_teste.add(app)
                        for item in node.body:
                            if isinstance(item, ast.FunctionDef):
                                if item.name.startswith("test_"):
                                    resultado["metodos_teste"] += 1
        except SyntaxError:
            pass
    todos_apps = [p.name for p in PROJECT_ROOT.iterdir()
                  if p.is_dir() and (p / "models.py").exists() and not ignorar_path(p)]
    resultado["apps_com_teste"] = list(apps_com_teste)
    resultado["apps_sem_teste"] = [a for a in todos_apps if a not in apps_com_teste]
    return resultado


def dp_migrations() -> dict:
    resultado = {}
    for mig_dir in PROJECT_ROOT.rglob("migrations"):
        if ignorar_path(mig_dir) or not mig_dir.is_dir():
            continue
        app = mig_dir.parent.name
        arquivos = [f for f in mig_dir.glob("*.py") if f.name != "__init__.py"]
        squash = [f for f in arquivos if "squash" in f.name]
        resultado[app] = {
            "total": len(arquivos),
            "squash": len(squash),
            "ultima": sorted(f.name for f in arquivos)[-1] if arquivos else "(nenhuma)",
        }
    return resultado


def dp_seguranca() -> dict:
    resultado = {
        "csrf_middleware": False, "debug_false_configuravel": False,
        "secret_key_env": False, "allowed_hosts_configurado": False,
        "password_hashers": False, "https_settings": [], "senhas_hardcoded": [],
    }
    settings_path = encontrar_arquivo("settings.py", PROJECT_ROOT)
    if settings_path:
        conteudo = ler_arquivo(settings_path)
        resultado["csrf_middleware"] = "CsrfViewMiddleware" in conteudo
        resultado["debug_false_configuravel"] = ("os.environ" in conteudo and "DEBUG" in conteudo) or "env(" in conteudo
        resultado["secret_key_env"] = ("os.environ" in conteudo or "env(" in conteudo) and "SECRET_KEY" in conteudo
        resultado["allowed_hosts_configurado"] = bool(re.search(r"ALLOWED_HOSTS\s*=\s*\[.+\]", conteudo))
        resultado["password_hashers"] = "PASSWORD_HASHERS" in conteudo
        for s in ("SECURE_SSL_REDIRECT", "SECURE_HSTS_SECONDS", "SESSION_COOKIE_SECURE",
                  "CSRF_COOKIE_SECURE", "X_FRAME_OPTIONS"):
            if s in conteudo:
                resultado["https_settings"].append(s)
    for py_path in arquivos_python(PROJECT_ROOT):
        conteudo = ler_arquivo(py_path)
        for i, linha in enumerate(conteudo.splitlines(), 1):
            if re.search(r"(password|senha|secret)\s*=\s*['\"][^'\"]{4,}['\"]", linha, re.IGNORECASE):
                if not any(x in linha.lower() for x in ("env", "os.", "config", "get(", "placeholder", "exemplo")):
                    resultado["senhas_hardcoded"].append(f"{py_path.name}:{i} → {linha.strip()[:60]}")
    return resultado


def dp_ferramentas_qualidade() -> dict:
    resultado = {}
    for cfg_file in ("pyproject.toml", "setup.cfg", ".flake8", "tox.ini"):
        path = encontrar_arquivo(cfg_file, REPO_ROOT)
        if path:
            resultado[cfg_file] = ler_arquivo(path)[:500]
    req_path = encontrar_arquivo("requirements.txt", REPO_ROOT)
    if req_path:
        conteudo = ler_arquivo(req_path).lower()
        resultado["ferramentas_instaladas"] = [
            f for f in ("black", "flake8", "isort", "autopep8", "mypy", "pylint") if f in conteudo
        ]
    return resultado


def dp_git_info() -> dict:
    def git(cmd):
        try:
            r = subprocess.run(cmd, cwd=str(REPO_ROOT), capture_output=True, text=True, timeout=5)
            return r.stdout.strip() if r.returncode == 0 else ""
        except Exception:
            return ""
    return {
        "branch_atual": git(["git", "rev-parse", "--abbrev-ref", "HEAD"]),
        "ultimo_commit": git(["git", "log", "-1", "--format=%h %s (%ad)", "--date=short"]),
        "total_commits": git(["git", "rev-list", "--count", "HEAD"]),
        "branches": git(["git", "branch", "-a"]).splitlines(),
        "tags": git(["git", "tag"]).splitlines(),
    }


def dp_roadmap() -> dict:
    apps = [p.name for p in PROJECT_ROOT.iterdir()
            if p.is_dir() and (p / "models.py").exists() and not ignorar_path(p)]
    tem_services = bool(list(PROJECT_ROOT.rglob("services.py")))
    tem_testes = bool(list(PROJECT_ROOT.rglob("test*.py")))
    tem_migrations = any(
        list((PROJECT_ROOT / a / "migrations").glob("0*.py"))
        for a in apps if (PROJECT_ROOT / a / "migrations").exists()
    )
    return {
        "Fase 1 - Fundação": {
            "apps criados": ", ".join(apps) if apps else "(nenhum)",
            "autenticação": "accounts app presente" if "accounts" in apps else "não encontrado",
            "admin configurado": "sim" if any((PROJECT_ROOT / a / "admin.py").exists() for a in apps) else "não",
            "migrations": "sim" if tem_migrations else "não",
            "status": "Concluído" if apps and tem_migrations else "Em progresso",
        },
        "Fase 2 - Otimização": {
            "service layer": "implementado" if tem_services else "não encontrado",
            "testes": "presentes" if tem_testes else "não encontrados",
            "status": "Em progresso" if tem_services else "Não iniciado",
        },
        "Fase 3 - Produção": {
            "gunicorn": "no requirements" if _tem_pacote("gunicorn") else "não encontrado",
            "whitenoise": "no requirements" if _tem_pacote("whitenoise") else "não encontrado",
            "sentry": "no requirements" if _tem_pacote("sentry") else "não encontrado",
            "status": "Planejado",
        },
    }


def gerar_diretrizes(agora: str) -> str:
    linhas = []

    def h1(t): linhas.append(f"\n{'=' * 60}\n# {t}\n{'=' * 60}")
    def h2(t): linhas.append(f"\n## {t}\n{'-' * 40}")
    def h3(t): linhas.append(f"\n### {t}")
    def L(t=""): linhas.append(t)

    h1("Desenvolvimento - Diretrizes e Padrões")
    L("Projeto: Sistema MetaReciclagem")
    L(f"Gerado automaticamente em: {agora}")

    h1("Análise de Nomenclatura")
    nom = dp_nomenclatura()
    h2("Models (PascalCase)")
    if nom["models_pascal"]:
        L(f"  Conformes ({len(nom['models_pascal'])}): {', '.join(nom['models_pascal'])}")
    if nom["models_nao_pascal"]:
        L(f"  Fora do padrão: {', '.join(nom['models_nao_pascal'])}")
    h2("Funções/Variáveis (snake_case)")
    L(f"  Funções snake_case: {nom['funcoes_snake']}")
    if nom["funcoes_nao_snake"]:
        L(f"  Fora do padrão: {', '.join(nom['funcoes_nao_snake'][:10])}")
    h2("Constantes (UPPER_SNAKE_CASE)")
    L(f"  Constantes corretas: {nom['constantes_upper']}")
    if nom["constantes_nao_upper"]:
        L(f"  Fora do padrão: {', '.join(nom['constantes_nao_upper'][:10])}")

    h1("Cobertura de Docstrings")
    doc = dp_docstrings()
    total_doc = len(doc["com_docstring"]) + len(doc["sem_docstring"])
    pct = round(len(doc["com_docstring"]) / total_doc * 100, 1) if total_doc else 0
    L(f"  Com docstring: {len(doc['com_docstring'])} de {total_doc} ({pct}%)")
    if doc["sem_docstring"]:
        h3("Precisam de docstring:")
        for item in doc["sem_docstring"][:15]:
            L(f"  - {item}")

    h1("Comentários em Português")
    cmt = dp_comentarios_pt()
    L(f"  Total: {cmt['total']} | Em português: {cmt['em_portugues']} ({cmt['percentual']}%)")
    if cmt["exemplos_pt"]:
        h3("Exemplos PT:")
        for e in cmt["exemplos_pt"]:
            L(f"  {e}")
    if cmt["exemplos_outros"]:
        h3("Exemplos outros:")
        for e in cmt["exemplos_outros"]:
            L(f"  {e}")

    h1("Padrões de Views")
    views = dp_padroes_views()
    L(f"  @login_required:    {views['login_required']}")
    L(f"  get_object_or_404:  {views['get_object_or_404']}")
    L(f"  messages.*:         {views['messages_uso']}")
    L(f"  select_related:     {views['select_related']}")
    L(f"  prefetch_related:   {views['prefetch_related']}")
    if views["views_sem_login"]:
        h3(f"Views sem @login_required ({len(views['views_sem_login'])}):")
        for v in views["views_sem_login"][:15]:
            L(f"  - {v}")

    h1("Service Layer")
    svc = dp_service_layer()
    if svc["services_encontrados"]:
        L(f"  Services: {', '.join(svc['services_encontrados'])}")
        L(f"  @transaction.atomic: {svc['uso_transaction_atomic']}")
        L(f"  logging.getLogger:   {svc['uso_logging']}")
        L(f"  @staticmethod:       {svc['uso_staticmethod']}")
        L(f"  Métodos públicos:    {svc['metodos_publicos']}")
        L(f"  Métodos privados:    {svc['metodos_privados']}")
    else:
        L("  (nenhum services.py encontrado)")

    h1("Configuração do Admin")
    adm = dp_admin()
    L(f"  list_display: {adm['list_display']} | search_fields: {adm['search_fields']} | list_filter: {adm['list_filter']}")
    L(f"  readonly_fields: {adm['readonly_fields']} | fieldsets: {adm['fieldsets']}")
    if adm["actions_customizadas"]:
        h3("Actions:")
        for a in adm["actions_customizadas"]:
            L(f"  - {a}")
    if adm["inlines"]:
        h3("Inlines:")
        for i in adm["inlines"]:
            L(f"  - {i}")
    if adm["exportacoes"]:
        h3("Exportações:")
        for e in set(adm["exportacoes"]):
            L(f"  - {e}")

    h1("Testes Automatizados")
    tst = dp_testes()
    L(f"  Arquivos: {len(tst['arquivos_teste'])} | Classes: {tst['classes_teste']} | Métodos: {tst['metodos_teste']}")
    L(f"  Uso de mock/patch: {tst['uso_mock']}")
    if tst["arquivos_teste"]:
        h3("Arquivos:")
        for f in tst["arquivos_teste"]:
            L(f"  - {f}")
    if tst["apps_com_teste"]:
        L(f"  Apps com testes:  {', '.join(tst['apps_com_teste'])}")
    if tst["apps_sem_teste"]:
        L(f"  Apps sem testes:  {', '.join(tst['apps_sem_teste'])}")

    h1("Migrations por App")
    for app, info in dp_migrations().items():
        L(f"  {app}: {info['total']} migration(s)"
          + (f" | {info['squash']} squash" if info["squash"] else "")
          + f" | última: {info['ultima']}")

    h1("Análise de Segurança")
    seg = dp_seguranca()
    L(f"  CSRF Middleware:    {'sim' if seg['csrf_middleware'] else 'NÃO'}")
    L(f"  DEBUG via env:      {'sim' if seg['debug_false_configuravel'] else 'NÃO'}")
    L(f"  SECRET_KEY via env: {'sim' if seg['secret_key_env'] else 'NÃO'}")
    L(f"  ALLOWED_HOSTS:      {'configurado' if seg['allowed_hosts_configurado'] else 'NÃO configurado'}")
    L(f"  Settings HTTPS:     {', '.join(seg['https_settings']) if seg['https_settings'] else '(não configurados)'}")
    if seg["senhas_hardcoded"]:
        h3("ATENÇÃO - Possíveis senhas hardcoded:")
        for s in seg["senhas_hardcoded"]:
            L(f"  ! {s}")
    else:
        L("  Senhas hardcoded: nenhuma detectada")

    h1("Ferramentas de Qualidade")
    ferramentas = dp_ferramentas_qualidade()
    instaladas = ferramentas.get("ferramentas_instaladas", [])
    L(f"  Instaladas: {', '.join(instaladas) if instaladas else '(não identificadas)'}")
    for cfg in ("pyproject.toml", "setup.cfg", ".flake8", "tox.ini"):
        if cfg in ferramentas:
            h3(f"Configuração ({cfg}):")
            L(ferramentas[cfg])

    h1("Git")
    git = dp_git_info()
    if git.get("branch_atual"):
        L(f"  Branch:  {git['branch_atual']}")
        L(f"  Último:  {git['ultimo_commit']}")
        L(f"  Commits: {git['total_commits']}")
        if git.get("branches"):
            h3("Branches:")
            for b in git["branches"]:
                L(f"  {b.strip()}")
    else:
        L("  (Git não disponível)")

    h1("Roadmap - Status das Fases")
    for fase, info in dp_roadmap().items():
        h2(fase)
        for k, v in info.items():
            L(f"  {k}: {v}")

    h1("Checklist de Qualidade")
    instaladas = dp_ferramentas_qualidade().get("ferramentas_instaladas", [])
    h2("Antes de Commitar")
    for pkg, desc in [("black", "Formatado com black"), ("isort", "Imports com isort"), ("flake8", "Sem erros flake8")]:
        status = "[x]" if pkg in instaladas else "[ ]"
        L(f"  {status} {desc}")
    L("  [ ] Testes passando (pytest)")
    L("  [ ] Docstrings atualizadas")
    L("  [ ] Comentários em português")
    L("  [ ] Migrations criadas (se necessário)")
    h2("Antes de Deploy")
    for item in ("DEBUG=False", "Variáveis de ambiente", "Migrations aplicadas",
                 "collectstatic", "Backup do banco", "HTTPS", "Sentry configurado"):
        L(f"  [ ] {item}")

    L(f"\n\n{'=' * 60}\nFim do documento - Gerado em {agora}\n{'=' * 60}")
    return "\n".join(linhas)


# ══════════════════════════════════════════════
# MAIN
# ══════════════════════════════════════════════

DOCUMENTOS = {
    "stack":      ("stack_e_configuracoes",      gerar_stack),
    "requisitos": ("requisitos_e_funcionalidades", gerar_requisitos),
    "diretrizes": ("diretrizes_e_padroes",        gerar_diretrizes),
}

if __name__ == "__main__":
    # Determina quais docs gerar (argumento opcional)
    arg = sys.argv[1].lower() if len(sys.argv) > 1 else "todos"
    if arg != "todos" and arg not in DOCUMENTOS:
        print(f"Argumento inválido: '{arg}'")
        print(f"Opções: todos | {' | '.join(DOCUMENTOS.keys())}")
        sys.exit(1)

    selecionados = DOCUMENTOS if arg == "todos" else {arg: DOCUMENTOS[arg]}

    print(f"Projeto:    {PROJECT_ROOT}")
    print(f"Repositório:{REPO_ROOT}")
    print(f"Saída:      {OUTPUT_DIR}\n")

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    agora = datetime.now().strftime("%d/%m/%Y %H:%M")

    for chave, (nome_arquivo, funcao_geradora) in selecionados.items():
        arquivo = OUTPUT_DIR / f"{DATE_PREFIX}_{nome_arquivo}.txt"
        print(f"Gerando {chave}...", end=" ")
        conteudo = funcao_geradora(agora)
        arquivo.write_text(conteudo, encoding="utf-8")
        print(f"OK → {arquivo.name} ({len(conteudo.splitlines())} linhas)")

    print(f"\nConcluído. {len(selecionados)} arquivo(s) gerado(s) em:\n  {OUTPUT_DIR}")
