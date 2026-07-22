"""
detect_orphans.py
Identifica arquivos orfaos e referencias orfas em um projeto Django.
Respeita padroes do .gitignore.

Etapa 1: Arquivos que existem mas nao sao referenciados (arquivos orfaos)
Etapa 2: Codigo que referencia arquivos que nao existem (referencias orfas)

Uso: python detect_orphans.py [caminho_do_projeto]
"""

import os
import re
import sys
import fnmatch
from pathlib import Path

# ============================================================
# 1. PARSER DO .GITIGNORE
# ============================================================

def carregar_gitignore(raiz):
    """Le o .gitignore e retorna listas de padroes e negacoes."""
    gitignore_path = raiz / '.gitignore'
    padroes = []
    negacoes = []

    if not gitignore_path.exists():
        return padroes, negacoes

    with open(gitignore_path, 'r', encoding='utf-8', errors='ignore') as f:
        for linha in f:
            linha = linha.strip()
            if not linha or linha.startswith('#'):
                continue
            if linha.startswith('!'):
                negacoes.append(linha[1:])
            else:
                padroes.append(linha)

    return padroes, negacoes

def corresponde_gitignore(caminho_relativo, padroes, negacoes):
    """Verifica se um caminho corresponde a algum padrao do gitignore."""
    partes = Path(caminho_relativo).parts
    caminho_posix = Path(caminho_relativo).as_posix()

    for padrao in padroes:
        padrao = padrao.rstrip('/')

        if '*' in padrao or '?' in padrao:
            for parte in partes:
                if fnmatch.fnmatch(parte, padrao):
                    return True
            if fnmatch.fnmatch(caminho_posix, padrao):
                return True
            continue

        if padrao in partes:
            return True

        if caminho_posix.startswith(padrao):
            return True
        if padrao in caminho_posix:
            if '/' + padrao in '/' + caminho_posix or padrao + '/' in caminho_posix:
                return True

    for neg in negacoes:
        if neg in caminho_posix:
            return False

    return False

# ============================================================
# 2. CONFIGURACAO
# ============================================================

EXTENSOES_ANALISADAS = {
    '.py', '.html', '.js', '.css', '.txt', '.json',
    '.cfg', '.ini', '.yaml', '.yml', '.md', '.rst',
}

ARQUIVOS_RAIZ = {
    'manage.py', 'settings.py', 'wsgi.py', 'asgi.py',
    'conftest.py', 'setup.py', 'setup.cfg', 'pyproject.toml',
    'requirements.txt', 'tox.ini', 'Makefile', 'Dockerfile',
    'docker-compose.yml', 'docker-compose.yaml', '.env',
    'urls.py', 'celery.py', '__init__.py',
}

DIRETORIOS_IGNORADOS = {
    '.git', '__pycache__', '.venv', 'venv', 'env',
    'node_modules', '.idea', '.vscode', 'media',
    '.pytest_cache', '.mypy_cache', 'htmlcov',
}

ARQUIVOS_UTILITARIOS = {
    'detect_orphans.py', 'listar_todos_htmls.py',
    'corrige_templates_extends.py',
}

ARQUIVOS_NAO_CODIGO = {
    'desktop.ini', '.gitkeep', '.gitattributes',
    'LICENSE', 'COPYING', 'QUICKSTART.md',
    'requirements-dev.txt', 'docker-compose-prod.yml',
}

# Extensoes de arquivo para verificar na etapa 2
EXTS_REFERENCIAS = {
    '.html', '.css', '.js', '.json', '.yaml', '.yml',
    '.txt', '.md', '.png', '.jpg', '.jpeg', '.gif',
    '.svg', '.ico', '.pdf', '.csv', '.woff', '.woff2',
}

# ============================================================
# 3. COLETA DE ARQUIVOS
# ============================================================

def coletar_arquivos(raiz, padroes_gitignore, negacoes_gitignore):
    """Percorre a arvore de diretorios e coleta todos os arquivos relevantes."""
    arquivos = []

    for dirpath, dirnames, filenames in os.walk(raiz):
        dirnames[:] = [
            d for d in dirnames
            if d not in DIRETORIOS_IGNORADOS
            and not d.startswith('.')
        ]

        for filename in filenames:
            caminho_completo = Path(dirpath) / filename
            caminho_relativo = caminho_completo.relative_to(raiz)

            if filename == '.gitignore':
                continue

            if corresponde_gitignore(
                str(caminho_relativo), padroes_gitignore, negacoes_gitignore
            ):
                continue

            ext = Path(filename).suffix.lower()
            if ext not in EXTENSOES_ANALISADAS and filename not in ARQUIVOS_RAIZ:
                if ext == '':
                    arquivos.append(caminho_completo)
                continue

            arquivos.append(caminho_completo)

    return arquivos

# ============================================================
# 4. LEITURA DE CONTEUDO (com cache)
# ============================================================

_conteudo_cache = {}

def ler_conteudo(caminho):
    """Le o conteudo de um arquivo de texto com cache."""
    if caminho in _conteudo_cache:
        return _conteudo_cache[caminho]
    try:
        with open(caminho, 'r', encoding='utf-8', errors='ignore') as f:
            conteudo = f.read()
    except Exception:
        conteudo = ''
    _conteudo_cache[caminho] = conteudo
    return conteudo

# ============================================================
# 5. EXTRACAO DE REFERENCIAS (Etapa 1)
# ============================================================

def extrair_referencias_python(conteudo):
    """Extrai referencias de imports de um arquivo Python."""
    refs = set()

    for match in re.finditer(r'from\s+([\w.]+)\s+import', conteudo):
        modulo = match.group(1)
        refs.add(modulo)
        if '.' in modulo:
            refs.add(modulo.split('.')[-1])
        refs.add(modulo.replace('.', '/'))

    for match in re.finditer(r'^\s*import\s+([\w.]+)', conteudo, re.MULTILINE):
        modulo = match.group(1)
        refs.add(modulo)
        if '.' in modulo:
            refs.add(modulo.split('.')[-1])
        refs.add(modulo.replace('.', '/'))

    for match in re.finditer(r'["\']([\w/]+\.\w{2,5})["\']', conteudo):
        refs.add(match.group(1))
        refs.add(Path(match.group(1)).name)

    return refs

def extrair_referencias_html(conteudo):
    """Extrai referencias de templates HTML."""
    refs = set()

    for match in re.finditer(r'{%\s*(?:extends|include)\s+["\']([^"\']+)["\']', conteudo):
        refs.add(match.group(1))
        refs.add(Path(match.group(1)).name)

    for match in re.finditer(r'{%\s*load\s+([\w\s]+)%}', conteudo):
        for tag in match.group(1).split():
            refs.add(tag)

    for match in re.finditer(r"{%\s*static\s+['\"]([^'\"]+)['\"]", conteudo):
        refs.add(match.group(1))
        refs.add(Path(match.group(1)).name)

    for match in re.finditer(r'(?:static|src|href)\s*[=(]\s*["\']([^"\']+)["\']', conteudo):
        refs.add(match.group(1))
        refs.add(Path(match.group(1)).name)

    for match in re.finditer(r'(?:href|src)=["\']([^"\']+)["\']', conteudo):
        caminho = match.group(1)
        if not caminho.startswith(('http', '//', '#', 'mailto:')):
            refs.add(caminho)
            refs.add(Path(caminho).name)

    return refs

def extrair_referencias_generico(conteudo):
    """Busca referencias a nomes de arquivos em qualquer tipo de arquivo."""
    refs = set()

    for match in re.finditer(r'["\']([\w/\-]+\.\w{2,5})["\']', conteudo):
        caminho = match.group(1)
        if not caminho.startswith(('http', '//')):
            refs.add(caminho)
            refs.add(Path(caminho).name)

    for match in re.finditer(r'(?:import|require)\s*\(?\s*["\']([^"\']+)["\']', conteudo):
        refs.add(match.group(1))
        refs.add(Path(match.group(1)).name)

    return refs

def extrair_referencias(caminho):
    """Extrai todas as referencias de um arquivo baseado em sua extensao."""
    conteudo = ler_conteudo(caminho)
    if not conteudo:
        return set()

    ext = caminho.suffix.lower()
    refs = set()

    if ext == '.py':
        refs = extrair_referencias_python(conteudo)
    elif ext == '.html':
        refs = extrair_referencias_html(conteudo)
    else:
        refs = extrair_referencias_generico(conteudo)

    refs |= extrair_referencias_generico(conteudo)

    return refs

# ============================================================
# 6. EXTRACAO DE REFERENCIAS DE ARQUIVOS (Etapa 2)
# ============================================================

def extrair_referencias_arquivos_especificas(conteudo, ext_arquivo):
    """
    Extrai referencias a arquivos reais (templates, static, etc).
    Usado na etapa 2 para detectar referencias a arquivos inexistentes.
    Retorna conjunto de strings representando caminhos/nomes de arquivos.
    """
    refs = set()

    if ext_arquivo == '.py':
        # render(request, 'template.html', ...)
        for match in re.finditer(r'render\s*\([^,]+,\s*["\']([^"\']+\.html)["\']', conteudo):
            refs.add(match.group(1))

        # template_name = 'template.html'
        for match in re.finditer(r'template_name\s*=\s*["\']([^"\']+\.html)["\']', conteudo):
            refs.add(match.group(1))

        # get_template('template.html')
        for match in re.finditer(r'get_template\s*\(\s*["\']([^"\']+\.html)["\']', conteudo):
            refs.add(match.group(1))

        # TemplateResponse(request, 'template.html')
        for match in re.finditer(r'TemplateResponse\s*\([^,]+,\s*["\']([^"\']+\.html)["\']', conteudo):
            refs.add(match.group(1))

        # select_template(['t1.html', 't2.html'])
        for match in re.finditer(r'select_template\s*\(\s*\[([^\]]+)\]', conteudo):
            for sub in re.finditer(r'["\']([^"\']+\.html)["\']', match.group(1)):
                refs.add(sub.group(1))

        # open('arquivo.ext')
        for match in re.finditer(r'open\s*\(\s*["\']([^"\']+\.\w{2,5})["\']', conteudo):
            refs.add(match.group(1))

    if ext_arquivo == '.html':
        # {% extends 'base.html' %}
        for match in re.finditer(r'{%\s*extends\s+["\']([^"\']+)["\']', conteudo):
            refs.add(match.group(1))

        # {% include 'partial.html' %}
        for match in re.finditer(r'{%\s*include\s+["\']([^"\']+)["\']', conteudo):
            refs.add(match.group(1))

        # {% static 'path/file.ext' %}
        for match in re.finditer(r"{%\s*static\s+['\"]([^'\"]+)['\"]", conteudo):
            refs.add(match.group(1))

        # href="..." src="..."
        for match in re.finditer(r'(?:href|src)=["\']([^"\']+)["\']', conteudo):
            caminho = match.group(1)
            if not caminho.startswith(('http', '//', '#', 'mailto:', 'data:')):
                refs.add(caminho)

    # Para todos os tipos: imports JS
    if ext_arquivo in ('.js', '.html'):
        for match in re.finditer(r'(?:import|require)\s*\(?\s*["\']([^"\']+)["\']', conteudo):
            caminho = match.group(1)
            if not caminho.startswith(('http', '//')):
                refs.add(caminho)

    return refs

# ============================================================
# 7. EXCLUSOES ESPECIFICAS DO DJANGO
# ============================================================

def verificar_exclusao_django(arq, caminho_str, nome_arquivo):
    """
    Verifica se o arquivo deve ser excluido da analise de orfaos
    por ser auto-descoberto pelo Django.
    Retorna (excluir, motivo) ou (False, '').
    """
    # 0. Arquivos nao-codigo e utilitarios
    if nome_arquivo in ARQUIVOS_NAO_CODIGO:
        return (True, 'Arquivo de configuracao/documentacao')
    if nome_arquivo in ARQUIVOS_UTILITARIOS:
        return (True, 'Script utilitario standalone')
    if nome_arquivo == 'desktop.ini':
        return (True, 'Arquivo de sistema Windows')
    if 'documentacao/' in caminho_str or caminho_str.startswith('documentacao'):
        return (True, 'Arquivo de documentacao')
    if 'scripts_admin/' in caminho_str and nome_arquivo.endswith('.py'):
        return (True, 'Script administrativo standalone')

    # 1. Arquivos de teste
    if 'tests/' in caminho_str or caminho_str.endswith('/tests'):
        if nome_arquivo.startswith('test_') or nome_arquivo == 'tests.py' or nome_arquivo == 'test.py':
            return (True, 'Arquivo de teste (Django test runner)')

    # 2. Management commands
    if 'management/commands' in caminho_str:
        if nome_arquivo != '__init__.py':
            return (True, 'Management command (Django auto-descoberta)')

    # 3. views.py
    if nome_arquivo == 'views.py':
        return (True, 'Views (referenciado por urls.py)')

    # 4. Migrations
    if 'migrations' in caminho_str:
        if nome_arquivo != '__init__.py':
            return (True, 'Migration do Django (auto-descoberta)')

    # 5. admin.py
    if nome_arquivo == 'admin.py':
        return (True, 'Admin do Django (auto-descoberta via autodiscover)')

    # 6. apps.py
    if nome_arquivo == 'apps.py':
        return (True, 'AppConfig do Django (auto-descoberta)')

    # 7. models.py
    if nome_arquivo == 'models.py':
        return (True, 'Models do Django (auto-descoberta via app registry)')

    # 8. forms.py
    if nome_arquivo == 'forms.py':
        return (True, 'Forms (geralmente importado por views.py)')

    # 9. signals.py
    if nome_arquivo == 'signals.py':
        return (True, 'Signals (conectado via apps.py ready())')

    # 10. context_processors.py
    if nome_arquivo == 'context_processors.py':
        return (True, 'Context processor (referenciado em settings TEMPLATES)')

    # 11. middleware.py
    if nome_arquivo == 'middleware.py':
        return (True, 'Middleware (referenciado em settings MIDDLEWARE)')

    # 12. feeds.py
    if nome_arquivo == 'feeds.py':
        return (True, 'Feeds (referenciado em urls.py)')

    # 13. serializers.py
    if nome_arquivo == 'serializers.py':
        return (True, 'Serializers (importado por views/api)')

    # 14. __init__.py
    if nome_arquivo == '__init__.py':
        return (True, 'Marcador de pacote Python')

    # 15. conftest.py
    if nome_arquivo == 'conftest.py':
        return (True, 'Configuracao do pytest (auto-descoberta)')

    # 16. factories.py
    if nome_arquivo == 'factories.py':
        return (True, 'Factories (usado por testes)')

    # 17. Arquivos em static/
    if 'static/' in caminho_str:
        return (True, 'Arquivo static (referenciado via {% static %} nos templates)')

    return (False, '')

# ============================================================
# 8. ETAPA 1 - DETECCAO DE ARQUIVOS ORFAOS
# ============================================================

def detectar_orfaos(raiz):
    """Etapa 1: coleta arquivos, extrai referencias e identifica orfaos."""
    print("[1/5] Carregando .gitignore...")
    padroes, negacoes = carregar_gitignore(raiz)
    print("      {} padroes de ignorar, {} negacoes".format(len(padroes), len(negacoes)))

    print("[2/5] Coletando arquivos do projeto...")
    arquivos = coletar_arquivos(raiz, padroes, negacoes)
    print("      {} arquivos encontrados".format(len(arquivos)))

    print("[3/5] Extraindo referencias...")
    referencias_por_arquivo = {}
    todas_referencias = set()

    for arq in arquivos:
        refs = extrair_referencias(arq)
        referencias_por_arquivo[arq] = refs
        todas_referencias |= refs

    print("      {} referencias unicas coletadas".format(len(todas_referencias)))

    print("[4/5] Analisando arquivos orfaos...")
    orfaos = []
    nao_orfaos = []
    excluidos_django = 0

    for arq in arquivos:
        caminho_relativo = arq.relative_to(raiz)
        nome_arquivo = arq.name
        caminho_str = caminho_relativo.as_posix()

        if nome_arquivo in ARQUIVOS_RAIZ:
            nao_orfaos.append((arq, 'Arquivo de configuracao/entry point'))
            continue

        excluir, motivo_exclusao = verificar_exclusao_django(arq, caminho_str, nome_arquivo)
        if excluir:
            nao_orfaos.append((arq, motivo_exclusao))
            excluidos_django += 1
            continue

        referenciado = False
        motivo = ''

        if nome_arquivo in todas_referencias:
            referenciado = True
            motivo = 'Referenciado por nome: ' + nome_arquivo

        if not referenciado and caminho_str in todas_referencias:
            referenciado = True
            motivo = 'Referenciado por caminho: ' + caminho_str

        if not referenciado:
            caminho_sem_ext = caminho_str.rsplit('.', 1)[0]
            caminho_modulo = caminho_sem_ext.replace('/', '.')
            if caminho_modulo in todas_referencias:
                referenciado = True
                motivo = 'Referenciado como modulo: ' + caminho_modulo

        if not referenciado:
            nome_sem_ext = arq.stem
            if nome_sem_ext in todas_referencias:
                referenciado = True
                motivo = 'Referenciado por nome do modulo: ' + nome_sem_ext

        if not referenciado:
            caminho_sem_ext = caminho_str.rsplit('.', 1)[0]
            modulo_possivel = caminho_sem_ext.replace('/', '.')
            modulo_possivel_sem_init = modulo_possivel.replace('.__init__', '')
            for outro_arq, refs_outro in referencias_por_arquivo.items():
                if outro_arq == arq:
                    continue
                if modulo_possivel in refs_outro or modulo_possivel_sem_init in refs_outro:
                    referenciado = True
                    outro_nome = outro_arq.relative_to(raiz).as_posix()
                    motivo = 'Importado por: ' + outro_nome
                    break

        if referenciado:
            nao_orfaos.append((arq, motivo))
        else:
            orfaos.append((arq, 'Nenhuma referencia encontrada'))

    return orfaos, nao_orfaos, excluidos_django, arquivos, referencias_por_arquivo

# ============================================================
# 9. ETAPA 2 - DETECCAO DE REFERENCIAS ORFAS
# ============================================================

def detectar_referencias_orfas(arquivos, raiz):
    """
    Etapa 2: Detecta codigo que referencia arquivos que nao existem no disco.
    Verifica templates, arquivos static, e outros arquivos referenciados.
    """
    # Construir indice de arquivos no disco
    nomes_no_disco = set()
    caminhos_no_disco = set()

    for arq in arquivos:
        nomes_no_disco.add(arq.name)
        caminhos_no_disco.add(arq.relative_to(raiz).as_posix())

    referencias_orfas = []

    for arq in arquivos:
        conteudo = ler_conteudo(arq)
        if not conteudo:
            continue

        ext = arq.suffix.lower()
        refs = extrair_referencias_arquivos_especificas(conteudo, ext)

        if not refs:
            continue

        caminho_arq = arq.relative_to(raiz).as_posix()

        for ref in refs:
            # Pular URLs externas e ancoras
            if ref.startswith(('http', '//', '#', 'mailto:', 'data:', '{{')):
                continue

            # Limpar prefixos comuns de static
            ref_limpa = ref
            if ref_limpa.startswith('/static/'):
                ref_limpa = ref_limpa[8:]
            elif ref_limpa.startswith('static/'):
                ref_limpa = ref_limpa[7:]

            ref_path = Path(ref_limpa)
            ext_ref = ref_path.suffix.lower()

            # So verificar referencias com extensao de arquivo valida
            if ext_ref not in EXTS_REFERENCIAS:
                continue

            ref_name = ref_path.name
            ref_posix = ref_path.as_posix()

            # Check 1: nome do arquivo existe em algum lugar do disco
            if ref_name in nomes_no_disco:
                continue

            # Check 2: caminho exato existe
            if ref_posix in caminhos_no_disco:
                continue

            # Check 3: referencia e sufixo de algum caminho no disco
            # (para templates Django: 'accounts/list.html' bate com
            #  'apps/accounts/templates/accounts/list.html')
            found = False
            for caminho in caminhos_no_disco:
                if caminho.endswith('/' + ref_posix):
                    found = True
                    break
            if found:
                continue

            # Check 4: para templates (.html), verificar por nome
            # em diretorios templates/
            if ext_ref == '.html':
                for caminho in caminhos_no_disco:
                    if caminho.endswith('/' + ref_name) and 'templates' in caminho:
                        found = True
                        break
                if found:
                    continue

            # Check 5: para arquivos static, verificar por nome
            # em diretorios static/
            if ext_ref in ('.css', '.js', '.png', '.jpg', '.jpeg', '.gif', '.svg', '.ico'):
                for caminho in caminhos_no_disco:
                    if caminho.endswith('/' + ref_name) and 'static' in caminho:
                        found = True
                        break
                if found:
                    continue

            # Nao encontrado em lugar nenhum: referencia orfa
            referencias_orfas.append((caminho_arq, ref, ext_ref))

    return referencias_orfas

# ============================================================
# 10. RELATORIO
# ============================================================

def gerar_relatorio(orfaos, nao_orfaos, excluidos_django, refs_orfas, raiz):
    """Gera o relatorio final no console com as duas etapas."""

    # ===== ETAPA 1 =====
    print("")
    print("=" * 70)
    print("ETAPA 1: ARQUIVOS ORFAOS")
    print("Arquivos que existem mas nao sao referenciados por nenhum outro")
    print("=" * 70)

    if not orfaos:
        print("")
        print("Nenhum arquivo orfao encontrado! Todos os arquivos sao referenciados.")
    else:
        print("")
        print("{} arquivo(s) orfao(s) encontrado(s):".format(len(orfaos)))
        print("")
        for i, (arq, motivo) in enumerate(sorted(orfaos), 1):
            rel = arq.relative_to(raiz).as_posix()
            print("  {:3d}. {}".format(i, rel))
            print("       Motivo: {}".format(motivo))

    total = len(orfaos) + len(nao_orfaos)
    print("")
    print("--- Resumo Etapa 1 ---")
    print("  Total de arquivos analisados:     {}".format(total))
    print("  Arquivos orfaos:                  {}".format(len(orfaos)))
    print("  Arquivos referenciados:           {}".format(len(nao_orfaos)))
    print("  Excluidos por regras do Django:   {}".format(excluidos_django))
    if total > 0:
        pct = len(orfaos) / total * 100
        print("  Percentual de orfaos:             {:.1f}%".format(pct))

    if orfaos:
        print("")
        print("--- Orfaos por extensao ---")
        por_ext = {}
        for arq, _ in orfaos:
            ext = arq.suffix or '(sem extensao)'
            por_ext[ext] = por_ext.get(ext, 0) + 1
        for ext, count in sorted(por_ext.items(), key=lambda x: -x[1]):
            print("  {:15s}: {}".format(ext, count))

        print("")
        print("--- Orfaos por diretorio ---")
        por_dir = {}
        for arq, _ in orfaos:
            diretorio = str(arq.parent.relative_to(raiz).as_posix())
            por_dir[diretorio] = por_dir.get(diretorio, 0) + 1
        for diretorio, count in sorted(por_dir.items(), key=lambda x: -x[1]):
            print("  {:40s}: {}".format(diretorio, count))

    # ===== ETAPA 2 =====
    print("")
    print("=" * 70)
    print("ETAPA 2: REFERENCIAS ORFAS")
    print("Codigo que referencia arquivos que nao existem no disco")
    print("=" * 70)

    if not refs_orfas:
        print("")
        print("Nenhuma referencia orfa encontrada! Todas as referencias apontam")
        print("para arquivos que existem no projeto.")
    else:
        print("")
        print("{} referencia(s) orfa(s) encontrada(s):".format(len(refs_orfas)))
        print("")
        for i, (origem, ref, ext_ref) in enumerate(sorted(refs_orfas), 1):
            print("  {:3d}. Arquivo: {}".format(i, origem))
            print("       Referencia: '{}'".format(ref))
            if ext_ref == '.html':
                print("       Tipo: Template")
            elif ext_ref in ('.css', '.js', '.png', '.jpg', '.jpeg', '.gif', '.svg', '.ico'):
                print("       Tipo: Static")
            else:
                print("       Tipo: Arquivo")

        print("")
        print("--- Resumo Etapa 2 ---")
        print("  Total de referencias orfas:       {}".format(len(refs_orfas)))
        por_tipo = {}
        for _, _, ext_ref in refs_orfas:
            if ext_ref == '.html':
                tipo = 'Templates'
            elif ext_ref in ('.css', '.js'):
                tipo = 'Static (CSS/JS)'
            elif ext_ref in ('.png', '.jpg', '.jpeg', '.gif', '.svg', '.ico'):
                tipo = 'Static (Imagens)'
            else:
                tipo = 'Outros'
            por_tipo[tipo] = por_tipo.get(tipo, 0) + 1
        for tipo, count in sorted(por_tipo.items(), key=lambda x: -x[1]):
            print("  {:35s}: {}".format(tipo, count))

    print("")
    print("=" * 70)

# ============================================================
# 11. EXECUCAO
# ============================================================

if __name__ == '__main__':
    if len(sys.argv) > 1:
        raiz_projeto = Path(sys.argv[1]).resolve()
    else:
        raiz_projeto = Path.cwd()

    if not raiz_projeto.exists():
        print("Erro: caminho nao existe: {}".format(raiz_projeto))
        sys.exit(1)

    print("Projeto: {}".format(raiz_projeto))
    print("")

    # Etapa 1: arquivos orfaos
    orfaos, nao_orfaos, excluidos_django, arquivos, _ = detectar_orfaos(raiz_projeto)

    # Etapa 2: referencias orfas
    print("[5/5] Analisando referencias orfas...")
    refs_orfas = detectar_referencias_orfas(arquivos, raiz_projeto)

    # Relatorio completo
    gerar_relatorio(orfaos, nao_orfaos, excluidos_django, refs_orfas, raiz_projeto)

    