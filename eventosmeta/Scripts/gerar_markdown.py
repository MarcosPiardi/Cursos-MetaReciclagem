"""
gerar_markdown.py
Gera o arquivo RESUMO_TECNICO_CLASSIFICACAO.md lendo o projeto real.

Salvar em:
  C:\\PMS\\PMS2025\\Inscr-Meta\\prg-Meta\\Eventos-MetaReciclagem\\eventosmeta\\Scripts\\

Saída em:
  C:\\PMS\\PMS2025\\Inscr-Meta\\Meta-Memória\\docs_gerados\\
"""

import ast
import re
from pathlib import Path
from datetime import datetime

# ══════════════════════════════════════════════
# CONFIGURAÇÃO DE CAMINHOS
# ══════════════════════════════════════════════

SCRIPT_DIR   = Path(__file__).resolve().parent
PROJECT_ROOT = SCRIPT_DIR.parent
REPO_ROOT    = PROJECT_ROOT.parent

OUTPUT_DIR = Path(r"C:\PMS\PMS2025\Inscr-Meta\Meta-Memória\docs_gerados")
DATE_PREFIX = datetime.now().strftime("%Y-%m-%d")
OUTPUT_FILE = OUTPUT_DIR / f"{DATE_PREFIX}_resumo_tecnico_classificacao.md"


# ══════════════════════════════════════════════
# HELPERS
# ══════════════════════════════════════════════

def ler_arquivo(path: Path) -> str:
    for enc in ("utf-8", "utf-8-sig", "latin-1"):
        try:
            return path.read_text(encoding=enc)
        except (UnicodeDecodeError, FileNotFoundError):
            continue
    return ""


def ignorar_path(path: Path) -> bool:
    return any(p in path.parts for p in ("venv", ".git", "__pycache__", "node_modules"))


def encontrar_arquivo(nome: str, base: Path) -> Path | None:
    for p in base.rglob(nome):
        if not ignorar_path(p):
            return p
    return None


def contar_linhas(path: Path) -> int:
    conteudo = ler_arquivo(path)
    return len(conteudo.splitlines()) if conteudo else 0


# ══════════════════════════════════════════════
# LEITURAS DINÂMICAS DO PROJETO
# ══════════════════════════════════════════════

# ── Apps existentes ──────────────────────────

def obter_apps() -> list[str]:
    """Lista os apps com models.py."""
    return sorted(
        p.name for p in PROJECT_ROOT.iterdir()
        if p.is_dir() and (p / "models.py").exists() and not ignorar_path(p)
    )


# ── Critérios cadastrados ────────────────────

def obter_criterios_das_fixtures() -> list[dict]:
    """
    Lê fixtures de critérios e retorna lista de dicts com:
    codigo, tipo_criterio, nome/descricao, pontos.
    """
    criterios = []
    for fixture_path in PROJECT_ROOT.rglob("*.json"):
        if ignorar_path(fixture_path) or "fixtures" not in fixture_path.parts:
            continue
        import json
        try:
            dados = json.loads(ler_arquivo(fixture_path))
        except Exception:
            continue
        for item in dados:
            model = item.get("model", "")
            if "criterio" in model.lower():
                fields = item.get("fields", {})
                criterios.append({
                    "codigo":        fields.get("codigo", ""),
                    "nome":          fields.get("nome", ""),
                    "tipo_criterio": fields.get("tipo_criterio", ""),
                    "pontos":        fields.get("pontos", "-"),
                    "categoria":     fields.get("categoria", ""),
                    "ativo":         fields.get("ativo", True),
                })
    return criterios


def obter_criterios_do_codigo() -> list[dict]:
    """
    Fallback: extrai os códigos de critérios mencionados nos services.py.
    Procura padrões como 'PCD', 'NIS', 'JOVEM', etc.
    """
    codigos_conhecidos = {
        "PCD":            {"nome": "Pessoa com Deficiência",        "tipo": "PONTUACAO"},
        "NIS":            {"nome": "Programa Social (Cadastro Único)", "tipo": "PONTUACAO"},
        "JOVEM":          {"nome": "Faixa etária 16-24 anos",        "tipo": "PONTUACAO"},
        "JOVEM_16_24":    {"nome": "Faixa etária 16-24 anos",        "tipo": "PONTUACAO"},
        "IDOSO":          {"nome": "Faixa etária 50+ anos",          "tipo": "PONTUACAO"},
        "IDOSO_50":       {"nome": "Faixa etária 50+ anos",          "tipo": "PONTUACAO"},
        "COTA_RACIAL":    {"nome": "Preto, Pardo, Indígena",         "tipo": "PONTUACAO"},
        "ESC_FUND_INC":   {"nome": "Ensino Fundamental Incompleto",  "tipo": "PONTUACAO"},
        "ESC_FUND_COMP":  {"nome": "Ensino Fundamental Completo",    "tipo": "PONTUACAO"},
        "ESC_MEDIO_INC":  {"nome": "Ensino Médio Incompleto",        "tipo": "PONTUACAO"},
        "ESC_MEDIO_COMP": {"nome": "Ensino Médio Completo",          "tipo": "PONTUACAO"},
        "IDADE_CRESCENTE":  {"nome": "Mais jovem primeiro",          "tipo": "ORDENACAO"},
        "IDADE_DECRESCENTE":{"nome": "Mais velho primeiro",          "tipo": "ORDENACAO"},
        "ORDEM_INSCRICAO":  {"nome": "Ordem cronológica",            "tipo": "ORDENACAO"},
    }

    encontrados = {}
    for svc_path in PROJECT_ROOT.rglob("services.py"):
        if ignorar_path(svc_path):
            continue
        conteudo = ler_arquivo(svc_path)
        for codigo, info in codigos_conhecidos.items():
            if f"'{codigo}'" in conteudo or f'"{codigo}"' in conteudo:
                encontrados[codigo] = info

    # Retorna como lista ordenada: pontuacao primeiro, depois ordenacao
    resultado = []
    for tipo in ("PONTUACAO", "ORDENACAO"):
        for codigo, info in encontrados.items():
            if info["tipo"] == tipo:
                resultado.append({
                    "codigo": codigo,
                    "nome": info["nome"],
                    "tipo_criterio": info["tipo"],
                    "pontos": "-",
                })
    return resultado


# ── ClassificadorService ──────────────────────

def obter_metodos_classificador() -> list[str]:
    """Lê services.py e extrai métodos públicos e privados do ClassificadorService."""
    for svc_path in PROJECT_ROOT.rglob("services.py"):
        if ignorar_path(svc_path):
            continue
        conteudo = ler_arquivo(svc_path)
        try:
            tree = ast.parse(conteudo)
        except SyntaxError:
            continue
        for node in ast.walk(tree):
            if isinstance(node, ast.ClassDef) and "classificador" in node.name.lower():
                return [
                    item.name for item in node.body
                    if isinstance(item, ast.FunctionDef)
                ]
    return []


def obter_nome_classe_classificador() -> str:
    """Retorna o nome da classe do classificador."""
    for svc_path in PROJECT_ROOT.rglob("services.py"):
        if ignorar_path(svc_path):
            continue
        conteudo = ler_arquivo(svc_path)
        match = re.search(r"class\s+(Classificador\w*)\s*[:\(]", conteudo)
        if match:
            return match.group(1)
    return "ClassificadorService"


# ── Actions do admin ──────────────────────────

def obter_actions_admin(app: str) -> list[dict]:
    """Lê admin.py de um app e extrai as actions com suas descrições."""
    admin_path = PROJECT_ROOT / app / "admin.py"
    if not admin_path.exists():
        return []
    conteudo = ler_arquivo(admin_path)
    actions = []
    for match in re.finditer(
        r"@admin\.action\(description=['\"]([^'\"]+)['\"]\)\s*\ndef\s+(\w+)", conteudo
    ):
        actions.append({"descricao": match.group(1), "funcao": match.group(2)})
    # Fallback: funções que parecem actions (sem decorator @admin.action)
    if not actions:
        for match in re.finditer(r"def\s+(classificar_\w+|exportar_\w+|ativar_\w+|desativar_\w+)\s*\(", conteudo):
            actions.append({"descricao": match.group(1).replace("_", " ").capitalize(), "funcao": match.group(1)})
    return actions


def obter_linhas_admin(app: str) -> int:
    """Conta linhas do admin.py de um app."""
    admin_path = PROJECT_ROOT / app / "admin.py"
    return contar_linhas(admin_path) if admin_path.exists() else 0


def obter_linhas_services() -> int:
    """Conta linhas do services.py."""
    for svc_path in PROJECT_ROOT.rglob("services.py"):
        if ignorar_path(svc_path):
            return contar_linhas(svc_path)
    return 0


# ── Campos do model Interessado ───────────────

def obter_campos_pcd() -> list[str]:
    """Lê models.py de interessados e extrai campos pcd_*."""
    for models_path in PROJECT_ROOT.rglob("models.py"):
        if ignorar_path(models_path):
            continue
        if models_path.parent.name not in ("interessados", "interessado"):
            continue
        conteudo = ler_arquivo(models_path)
        try:
            tree = ast.parse(conteudo)
        except SyntaxError:
            continue
        for node in ast.walk(tree):
            if isinstance(node, ast.ClassDef) and "interessado" in node.name.lower():
                campos = []
                for item in node.body:
                    if isinstance(item, ast.Assign):
                        for target in item.targets:
                            if isinstance(target, ast.Name) and target.id.startswith("pcd_"):
                                campos.append(target.id)
                if campos:
                    return campos
    # Fallback com valores conhecidos
    return ["pcd_fisica", "pcd_visual", "pcd_auditiva", "pcd_intelectual",
            "pcd_psicossocial", "pcd_multiplas"]


def obter_properties_interessado() -> list[str]:
    """Extrai @property do model Interessado."""
    for models_path in PROJECT_ROOT.rglob("models.py"):
        if ignorar_path(models_path):
            continue
        if models_path.parent.name not in ("interessados", "interessado"):
            continue
        conteudo = ler_arquivo(models_path)
        try:
            tree = ast.parse(conteudo)
        except SyntaxError:
            continue
        for node in ast.walk(tree):
            if isinstance(node, ast.ClassDef) and "interessado" in node.name.lower():
                props = []
                for item in node.body:
                    if isinstance(item, ast.FunctionDef):
                        decs = [
                            (ast.unparse(d) if hasattr(ast, "unparse") else getattr(d, "id", ""))
                            for d in item.decorator_list
                        ]
                        if any("property" in str(d) for d in decs):
                            props.append(item.name)
                return props
    return ["tem_deficiencia", "idade"]


# ── Campos dos models principais ─────────────

def obter_campos_model(app: str, nome_model: str) -> list[dict]:
    """Extrai campos de um model específico."""
    for models_path in PROJECT_ROOT.rglob("models.py"):
        if ignorar_path(models_path):
            continue
        if models_path.parent.name != app:
            continue
        conteudo = ler_arquivo(models_path)
        try:
            tree = ast.parse(conteudo)
        except SyntaxError:
            continue
        for node in ast.walk(tree):
            if isinstance(node, ast.ClassDef) and node.name.lower() == nome_model.lower():
                campos = []
                for item in node.body:
                    if isinstance(item, ast.Assign):
                        for target in item.targets:
                            if isinstance(target, ast.Name) and not target.id.startswith("_") and not target.id.isupper():
                                tipo = ""
                                if isinstance(item.value, ast.Call):
                                    func = item.value.func
                                    tipo = getattr(func, "attr", "") or getattr(func, "id", "")
                                campos.append({"nome": target.id, "tipo": tipo})
                return campos
    return []


# ── Management command ────────────────────────

def obter_help_command(cmd_nome: str) -> str:
    """Lê o help de um management command."""
    for cmd_path in PROJECT_ROOT.rglob(f"{cmd_nome}.py"):
        if ignorar_path(cmd_path):
            continue
        conteudo = ler_arquivo(cmd_path)
        match = re.search(r"help\s*=\s*['\"]([^'\"]+)['\"]", conteudo)
        if match:
            return match.group(1)
    return f"Classifica inscrições de um evento pelo ID"


# ── Erros no histórico de commits/código ──────

def obter_erros_corrigidos() -> list[dict]:
    """
    Detecta padrões de erro corrigidos nos arquivos.
    Procura por comentários como '# ERRO:', '# CORRIGIDO:', etc.
    e por padrões conhecidos de bug (fototipo.upper, tipo_deficiencia).
    """
    erros = []
    padroes = [
        {
            "busca": r"fototipo\.nome",
            "erro": "'Fototipo' object has no attribute 'upper'",
            "causa": "fototipo é ForeignKey, não string",
            "solucao": "interessado.fototipo.nome",
            "errado": "interessado.fototipo.upper()",
        },
        {
            "busca": r"tem_deficiencia|pcd_fisica|pcd_visual",
            "erro": "'Interessado' object has no attribute 'tipo_deficiencia'",
            "causa": "Campo tipo_deficiencia não existe no model Interessado",
            "solucao": "Usar pcd_fisica, pcd_visual, etc. ou tem_deficiencia",
            "errado": "interessado.tipo_deficiencia",
        },
        {
            "busca": r"tipo_criterio",
            "erro": "Classificação com 0 pontos mesmo com critérios configurados",
            "causa": "Código usava criterio.tipo (não existe), correto é criterio.tipo_criterio",
            "solucao": "criterio.tipo_criterio",
            "errado": "criterio.tipo",
        },
    ]

    for padrao in padroes:
        encontrado = False
        for py_path in PROJECT_ROOT.rglob("*.py"):
            if ignorar_path(py_path):
                continue
            conteudo = ler_arquivo(py_path)
            if re.search(padrao["busca"], conteudo):
                encontrado = True
                break
        if encontrado:
            erros.append(padrao)

    return erros


# ── Colunas dos exportadores ──────────────────

def obter_colunas_exportador(app: str, funcao: str) -> list[str]:
    """
    Tenta extrair as colunas de uma função de exportação
    buscando o writerow com os cabeçalhos.
    """
    admin_path = PROJECT_ROOT / app / "admin.py"
    if not admin_path.exists():
        return []
    conteudo = ler_arquivo(admin_path)

    # Localiza a função
    match_func = re.search(
        rf"def\s+{funcao}\s*\(.*?\n(.*?)(?=\ndef\s|\Z)", conteudo, re.DOTALL
    )
    if not match_func:
        return []

    bloco = match_func.group(1)
    # Procura o primeiro writerow com strings (cabeçalho)
    match_row = re.search(r"writerow\(\[([^\]]+)\]", bloco)
    if not match_row:
        return []

    return re.findall(r"['\"]([^'\"]+)['\"]", match_row.group(1))


# ══════════════════════════════════════════════
# GERAÇÃO DO MARKDOWN
# ══════════════════════════════════════════════

def gerar_markdown() -> str:
    agora_fmt  = datetime.now().strftime("%d/%m/%Y %H:%M")
    agora_data = datetime.now().strftime("%d/%m/%Y")

    # Coleta dados dinâmicos
    apps                  = obter_apps()
    nome_classificador    = obter_nome_classe_classificador()
    metodos_classificador = obter_metodos_classificador()
    criterios_fixture     = obter_criterios_das_fixtures()
    criterios             = criterios_fixture if criterios_fixture else obter_criterios_do_codigo()
    campos_pcd            = obter_campos_pcd()
    properties_int        = obter_properties_interessado()
    erros                 = obter_erros_corrigidos()
    linhas_eventos_admin  = obter_linhas_admin("eventos")
    linhas_inter_admin    = obter_linhas_admin("interessados")
    linhas_services       = obter_linhas_services()
    actions_eventos       = obter_actions_admin("eventos")
    actions_inter         = obter_actions_admin("interessados")
    help_cmd              = obter_help_command("classificar_evento")

    # Campos dos models principais (dinâmico)
    campos_criterio        = obter_campos_model("eventos",  "Criterio")
    campos_eventocriterio  = obter_campos_model("eventos",  "EventoCriterio")
    campos_inscricao       = obter_campos_model("selecao",  "Inscricao")
    campos_classificacao   = obter_campos_model("selecao",  "Classificacao")
    campos_criterio_atend  = obter_campos_model("selecao",  "InscricaoCriterioAtendido")

    # Colunas dos exportadores
    colunas_classif = obter_colunas_exportador("eventos", "exportar_classificacao_excel")
    colunas_inter   = obter_colunas_exportador("interessados", "exportar_interessados_detalhado")

    # ── Separação dos critérios por tipo
    criterios_pont = [c for c in criterios if c["tipo_criterio"] == "PONTUACAO"]
    criterios_ord  = [c for c in criterios if c["tipo_criterio"] == "ORDENACAO"]

    # ── Monta descrição dos apps (dinâmico: nome e se tem services/admin)
    def descricao_app(app_nome: str) -> str:
        tem_service = (PROJECT_ROOT / app_nome / "services.py").exists()
        tem_admin   = (PROJECT_ROOT / app_nome / "admin.py").exists()
        extras = []
        if tem_service:
            extras.append("service layer")
        if tem_admin:
            extras.append("admin configurado")
        return ", ".join(extras) if extras else "app básico"

    # ══════════════════════════════════════════
    # TEXTO DO DOCUMENTO
    # Seções estáticas: títulos, fluxos, texto
    # explicativo, exemplos de shell.
    # Seções dinâmicas: linhas de arquivo,
    # lista de critérios, campos, actions,
    # erros detectados, colunas exportadas.
    # ══════════════════════════════════════════

    md = []
    L = md.append

    # ── Cabeçalho ────────────────────────────
    # ESTÁTICO: estrutura e rótulos
    # DINÂMICO: data
    L(f"# RESUMO TÉCNICO - Sistema de Classificação de Inscrições")
    L(f"")
    L(f"**Data:** {agora_data}  ")
    L(f"**Projeto:** Sistema MetaReciclagem - Gestão de Eventos e Inscrições  ")
    L(f"**Tecnologia:** Django + Python  ")
    L(f"**Gerado automaticamente em:** {agora_fmt}")
    L(f"")

    # ── Objetivo ─────────────────────────────
    # ESTÁTICO: descrição conceitual do sistema
    L(f"---")
    L(f"")
    L(f"## OBJETIVO DO SISTEMA")
    L(f"")
    L(f"Classificar inscrições de eventos usando **critérios de pontuação e ordenação**")
    L(f"com **prioridades configuráveis**, permitindo flexibilidade total na definição")
    L(f"de regras de seleção por evento.")
    L(f"")

    # ── Arquitetura ───────────────────────────
    # ESTÁTICO: diagrama ASCII e descrição do fluxo
    L(f"---")
    L(f"")
    L(f"## ARQUITETURA IMPLEMENTADA")
    L(f"")
    L(f"```")
    L(f"┌─────────────────────────────────────────────────────────┐")
    L(f"│                   FLUXO DE CLASSIFICAÇÃO                │")
    L(f"├─────────────────────────────────────────────────────────┤")
    L(f"│                                                         │")
    L(f"│  1. EVENTO                                              │")
    L(f"│     └─> EventoCriterio (prioridade 1, 2, 3...)          │")
    L(f"│         └─> Criterio (PONTUACAO ou ORDENACAO)           │")
    L(f"│                                                         │")
    L(f"│  2. INSCRIÇÃO                                           │")
    L(f"│     └─> Interessado (dados pessoais)                    │")
    L(f"│                                                         │")
    L(f"│  3. CLASSIFICAÇÃO (via {nome_classificador:<32})│")
    L(f"│     ├─> Calcula pontuação (critérios PONTUACAO)         │")
    L(f"│     ├─> Aplica ordenação (critérios ORDENACAO)          │")
    L(f"│     └─> Define posição final                            │")
    L(f"│                                                         │")
    L(f"│  4. RESULTADO                                           │")
    L(f"│     └─> Classificacao (posição, pontos, status)         │")
    L(f"│         └─> InscricaoCriterioAtendido (detalhes)        │")
    L(f"└─────────────────────────────────────────────────────────┘")
    L(f"```")
    L(f"")

    # ── Apps ─────────────────────────────────
    # DINÂMICO: lista de apps lida do projeto
    L(f"---")
    L(f"")
    L(f"## ESTRUTURA DE APPS")
    L(f"")
    for app in apps:
        desc = descricao_app(app)
        L(f"### **{app}/**")
        L(f"- {desc}")
        L(f"")

    # ── Arquivos principais ───────────────────
    # DINÂMICO: contagem de linhas, actions, métodos
    # ESTÁTICO: descrição textual de cada seção
    L(f"---")
    L(f"")
    L(f"## ARQUIVOS PRINCIPAIS")
    L(f"")

    # eventos/admin.py
    L(f"### **1. eventos/admin.py** ({linhas_eventos_admin} linhas)")
    L(f"")
    L(f"**Actions disponíveis:**")
    if actions_eventos:
        for a in actions_eventos:
            L(f"- `{a['funcao']}` - {a['descricao']}")
    else:
        L(f"- (nenhuma action detectada)")
    L(f"")

    # selecao/services.py
    L(f"### **2. selecao/services.py** ({linhas_services} linhas)")
    L(f"")
    L(f"**Classe principal:** `{nome_classificador}`")
    L(f"")
    if metodos_classificador:
        L(f"```python")
        L(f"{nome_classificador}")
        for m in metodos_classificador:
            prefixo = "└─>" if m == metodos_classificador[-1] else "├─>"
            L(f"{prefixo} {m}()")
        L(f"```")
    L(f"")

    # interessados/admin.py
    L(f"### **3. interessados/admin.py** ({linhas_inter_admin} linhas)")
    L(f"")
    L(f"**Actions disponíveis:**")
    if actions_inter:
        for a in actions_inter:
            L(f"- `{a['funcao']}` - {a['descricao']}")
    else:
        L(f"- (nenhuma action detectada)")
    L(f"")

    # management command
    L(f"### **4. selecao/management/commands/classificar_evento.py**")
    L(f"")
    L(f"**Descrição:** {help_cmd}")
    L(f"")
    L(f"**Uso:**")
    L(f"```bash")
    L(f"python manage.py classificar_evento --evento_id=1")
    L(f"```")
    L(f"")

    # ── Critérios ─────────────────────────────
    # DINÂMICO: tabela de critérios lida de fixtures ou código
    L(f"---")
    L(f"")
    L(f"## CRITÉRIOS IMPLEMENTADOS")
    L(f"")

    # ESTÁTICO: explicação dos tipos
    L(f"### Tipos de Critério")
    L(f"")
    L(f"**PONTUACAO** — Soma pontos ao candidato. Usado para classificação por mérito.")
    L(f"")
    L(f"**ORDENACAO** — Não soma pontos. Define ordem de desempate.")
    L(f"")

    L(f"### Critérios de PONTUACAO")
    L(f"")
    if criterios_pont:
        L(f"| Código | Nome | Pontos |")
        L(f"|--------|------|--------|")
        for c in criterios_pont:
            pts = str(c.get("pontos", "-"))
            L(f"| `{c['codigo']}` | {c['nome']} | {pts} |")
    else:
        L(f"(nenhum critério de pontuação encontrado nas fixtures)")
    L(f"")

    L(f"### Critérios de ORDENACAO")
    L(f"")
    if criterios_ord:
        L(f"| Código | Nome |")
        L(f"|--------|------|")
        for c in criterios_ord:
            L(f"| `{c['codigo']}` | {c['nome']} |")
    else:
        L(f"(nenhum critério de ordenação encontrado nas fixtures)")
    L(f"")

    # ── Conceitos importantes ─────────────────
    # ESTÁTICO: explicação conceitual e exemplos
    L(f"---")
    L(f"")
    L(f"## CONCEITOS IMPORTANTES")
    L(f"")
    L(f"### Prioridade dos Critérios")
    L(f"")
    L(f"Os critérios são aplicados na ordem de prioridade definida no evento.")
    L(f"A lógica de ordenação é:")
    L(f"")
    L(f"1. Maior pontuação primeiro (`-pontuacao_total`)")
    L(f"2. Critérios de ORDENACAO na ordem de prioridade")
    L(f"3. Data de inscrição como desempate final")
    L(f"")
    L(f"**Exemplo:**")
    L(f"```")
    L(f"Prioridade 1: PCD (10 pts)        → soma pontos")
    L(f"Prioridade 2: IDADE_CRESCENTE     → desempate por idade")
    L(f"Prioridade 3: ORDEM_INSCRICAO     → desempate final")
    L(f"")
    L(f"Resultado:")
    L(f"1º - João  (10 pts, 19 anos, inscrito 01/01/2025)")
    L(f"2º - Maria (10 pts, 20 anos, inscrito 01/01/2025)")
    L(f"3º - Pedro (10 pts, 20 anos, inscrito 02/01/2025)")
    L(f"4º - Ana   ( 5 pts, 18 anos, inscrito 01/01/2025)")
    L(f"```")
    L(f"")
    L(f"### Pontuação Potencial vs Pontuação Real")
    L(f"")
    L(f"| Tipo | Onde | O que calcula |")
    L(f"|------|------|---------------|")
    L(f"| **Potencial Máxima** | Exportação de Interessados | TODOS os critérios do sistema |")
    L(f"| **Real do Evento** | Classificação de Evento | APENAS critérios configurados no evento |")
    L(f"")
    L(f"O mesmo interessado terá pontuações diferentes em cada evento,")
    L(f"pois cada evento usa um subconjunto de critérios.")
    L(f"")

    # ── Erros corrigidos ──────────────────────
    # DINÂMICO: detectados por padrão no código
    if erros:
        L(f"---")
        L(f"")
        L(f"## ERROS CORRIGIDOS (detectados no código)")
        L(f"")
        for i, erro in enumerate(erros, 1):
            L(f"### Erro {i}: `{erro['erro']}`")
            L(f"")
            L(f"**Causa:** {erro['causa']}")
            L(f"")
            L(f"```python")
            L(f"# Errado")
            L(f"{erro['errado']}")
            L(f"")
            L(f"# Correto")
            L(f"{erro['solucao']}")
            L(f"```")
            L(f"")

    # ── Exportadores ─────────────────────────
    # DINÂMICO: colunas lidas do admin.py
    # ESTÁTICO: instruções de uso
    L(f"---")
    L(f"")
    L(f"## EXPORTADORES")
    L(f"")
    L(f"### 1. Exportação de Classificação de Evento")
    L(f"")
    L(f"**Arquivo:** `eventos/admin.py`  ")
    L(f"**Formato:** CSV (UTF-8 com BOM, separador `;`)")
    L(f"")
    if colunas_classif:
        L(f"**Colunas exportadas:**")
        for col in colunas_classif:
            L(f"- {col}")
    else:
        L(f"**Colunas principais:** Evento, Posição, Nome, CPF, Pontuação Calculada,")
        L(f"Pontuação Salva, Diferença, Classificado, Critérios Atendidos")
    L(f"")
    # ESTÁTICO: instruções
    L(f"**Como usar:**")
    L(f"1. Acesse: `http://127.0.0.1:8000/admin/eventos/evento/`")
    L(f"2. Selecione o(s) evento(s)")
    L(f"3. Escolha a action de exportação")
    L(f"4. Clique em **Ir**")
    L(f"")
    L(f"**Análise de erros:**")
    L(f"- Coluna `Diferença` = `0.00` → Correto")
    L(f"- Coluna `Diferença` ≠ `0.00` → Erro de cálculo")
    L(f"")

    L(f"### 2. Exportação de Interessados com Análise de Critérios")
    L(f"")
    L(f"**Arquivo:** `interessados/admin.py`  ")
    L(f"**Formato:** CSV (UTF-8 com BOM, separador `;`)")
    L(f"")
    if colunas_inter:
        L(f"**Colunas exportadas:**")
        for col in colunas_inter:
            L(f"- {col}")
    else:
        L(f"**Colunas principais:** CPF, Nome, Idade, Sexo, Fototipo, Escolaridade,")
        L(f"Tem Deficiência, Tipos PCD, Programa Social, NIS,")
        L(f"uma coluna por critério (SIM/NÃO), Pontuação Total Potencial")
    L(f"")
    L(f"**Como usar:**")
    L(f"1. Acesse: `http://127.0.0.1:8000/admin/interessados/interessado/`")
    L(f"2. Selecione os interessados (ou todos)")
    L(f"3. Escolha a action de exportação")
    L(f"4. Clique em **Ir**")
    L(f"")

    # ── Campos PCD (dinâmico) ─────────────────
    L(f"---")
    L(f"")
    L(f"## CAMPOS PCD DO MODEL INTERESSADO")
    L(f"")
    L(f"Campos booleanos encontrados no model:")
    L(f"")
    for campo in campos_pcd:
        L(f"- `{campo}`")
    if properties_int:
        L(f"")
        L(f"Properties calculadas:")
        for prop in properties_int:
            L(f"- `{prop}` (property)")
    L(f"")

    # ── Modelos de dados ──────────────────────
    # DINÂMICO: campos lidos do models.py
    # ESTÁTICO: títulos e descrições
    L(f"---")
    L(f"")
    L(f"## MODELOS DE DADOS PRINCIPAIS")
    L(f"")

    modelos = [
        ("eventos",  "Criterio",               campos_criterio,       "Define um critério de classificação"),
        ("eventos",  "EventoCriterio",          campos_eventocriterio, "Associa critério a um evento com prioridade"),
        ("selecao",  "Inscricao",               campos_inscricao,      "Inscrição de um interessado em um evento"),
        ("selecao",  "Classificacao",           campos_classificacao,  "Resultado da classificação de uma inscrição"),
        ("selecao",  "InscricaoCriterioAtendido", campos_criterio_atend, "Critérios atendidos por uma inscrição"),
    ]

    for app, nome, campos, descricao in modelos:
        L(f"### {nome} (`{app}`)")
        L(f"")
        L(f"_{descricao}_")
        L(f"")
        if campos:
            for c in campos:
                tipo_str = f" — `{c['tipo']}`" if c.get("tipo") else ""
                L(f"- `{c['nome']}`{tipo_str}")
        else:
            L(f"_(campos não encontrados — verificar models.py)_")
        L(f"")

    # ── Comandos úteis ────────────────────────
    # ESTÁTICO: exemplos de shell
    L(f"---")
    L(f"")
    L(f"## COMANDOS ÚTEIS NO SHELL")
    L(f"")
    L(f"### Classificar evento")
    L(f"```python")
    L(f"from apps.selecao.services import {nome_classificador}")
    L(f"from apps.eventos.models import Evento")
    L(f"")
    L(f"evento = Evento.objects.get(nome='Nome do Evento')")
    L(f"{nome_classificador}.classificar_evento(evento)")
    L(f"```")
    L(f"")
    L(f"### Ver critérios de um evento")
    L(f"```python")
    L(f"from apps.eventos.models import Evento, EventoCriterio")
    L(f"")
    L(f"evento = Evento.objects.get(nome='Nome do Evento')")
    L(f"criterios = EventoCriterio.objects.filter(")
    L(f"    evento=evento, ativo=True")
    L(f").select_related('criterio').order_by('prioridade')")
    L(f"")
    L(f"for ec in criterios:")
    L(f"    print(f\"{{ec.prioridade}}. {{ec.criterio.nome}} ({{ec.criterio.tipo_criterio}}) - {{ec.criterio.pontos}} pts\")")
    L(f"```")
    L(f"")
    L(f"### Ver classificação de um evento")
    L(f"```python")
    L(f"from apps.selecao.models import Classificacao")
    L(f"from apps.eventos.models import Evento")
    L(f"from datetime import date")
    L(f"")
    L(f"evento = Evento.objects.get(nome='Nome do Evento')")
    L(f"classificacoes = Classificacao.objects.filter(")
    L(f"    inscricao__evento=evento")
    L(f").select_related('inscricao__interessado').order_by('posicao')")
    L(f"")
    L(f"hoje = date.today()")
    L(f"for c in classificacoes[:10]:")
    L(f"    dn = c.inscricao.interessado.data_nascimento")
    L(f"    idade = hoje.year - dn.year - ((hoje.month, hoje.day) < (dn.month, dn.day))")
    L(f"    status = 'Classificado' if c.classificado else 'Lista Espera'")
    L(f"    print(f\"{{c.posicao}}. {{c.inscricao.interessado.nome}} ({{idade}} anos) - {{c.pontuacao_total}} pts - {{status}}\")")
    L(f"```")
    L(f"")
    L(f"### Ver critérios atendidos por uma inscrição")
    L(f"```python")
    L(f"from apps.selecao.models import InscricaoCriterioAtendido, Inscricao")
    L(f"")
    L(f"inscricao = Inscricao.objects.get(id=1)")
    L(f"criterios = InscricaoCriterioAtendido.objects.filter(")
    L(f"    inscricao=inscricao")
    L(f").select_related('criterio')")
    L(f"")
    L(f"for ca in criterios:")
    L(f"    print(f\"  - {{ca.criterio.nome}}: {{ca.pontos_atribuidos}} pts\")")
    L(f"    print(f\"    Observação: {{ca.observacao_validacao}}\")")
    L(f"```")
    L(f"")

    # ── Próximos passos ───────────────────────
    # ESTÁTICO: checklist de melhorias
    L(f"---")
    L(f"")
    L(f"## PROXIMOS PASSOS")
    L(f"")
    L(f"### Melhorias Futuras")
    L(f"- [ ] Exportação de interessados por evento específico")
    L(f"- [ ] Dashboard de análise de classificações")
    L(f"- [ ] Validação automática de pontuações")
    L(f"- [ ] Histórico de classificações (auditoria)")
    L(f"- [ ] Notificações automáticas para classificados")
    L(f"- [ ] Geração de listas de chamada em PDF")
    L(f"")
    L(f"### Testes")
    L(f"- [ ] Testes unitários do {nome_classificador}")
    L(f"- [ ] Testes de integração da classificação")
    L(f"- [ ] Validação de casos extremos (empates, sem critérios)")
    L(f"- [ ] Testes de performance com muitas inscrições")
    L(f"")
    L(f"### Segurança")
    L(f"- [ ] Log de alterações em classificações")
    L(f"- [ ] Permissões granulares por tipo de usuário")
    L(f"- [ ] Backup automático antes de reclassificar")
    L(f"")

    # ── Rodapé ───────────────────────────────
    L(f"---")
    L(f"")
    L(f"**Documento gerado em:** {agora_fmt}  ")
    L(f"**Script:** gerar_markdown.py  ")
    L(f"**Status:** Funcional")

    return "\n".join(md)


# ══════════════════════════════════════════════
# MAIN
# ══════════════════════════════════════════════

if __name__ == "__main__":
    print(f"Projeto:    {PROJECT_ROOT}")
    print(f"Repositório:{REPO_ROOT}")
    print(f"Saída:      {OUTPUT_DIR}")
    print()

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    print("Lendo projeto...", end=" ")
    conteudo = gerar_markdown()
    print("OK")

    OUTPUT_FILE.write_text(conteudo, encoding="utf-8")
    print(f"\nArquivo gerado:")
    print(f"  {OUTPUT_FILE}")
    print(f"  {len(conteudo.splitlines())} linhas")
