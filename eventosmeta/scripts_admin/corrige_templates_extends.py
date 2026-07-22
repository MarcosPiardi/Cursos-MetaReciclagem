"""
Arquivo: corrige_templates_extends.py
Caminho: scripts_admin/corrige_templates_extends.py
Finalidade: Corrigir {% extends %} sem namespace de app em templates HTML
Atualizacoes:
 - 21/07/2026 - Criacao do script
"""

import re
import sys
from pathlib import Path

# Raiz do projeto (sobe um nivel a partir de scripts_admin/)
PROJECT_ROOT = Path(__file__).resolve().parent.parent
APPS_DIR = PROJECT_ROOT / "apps"

def mapear_templates():
    """
    Escaneia apps/<app>/templates/<app>/ e mapeia:
      nome.html -> app/nome.html

    So mapeia arquivos que estao dentro de templates/<app_name>/
    (estrutura correta do Django com DIRS=[]).
    """
    mapeamento = {}
    conflitos = {}

    for app_dir in sorted(APPS_DIR.iterdir()):
        templates_dir = app_dir / "templates"
        if not templates_dir.is_dir():
            continue

        for html_file in templates_dir.rglob("*.html"):
            rel_path = html_file.relative_to(templates_dir)
            parts = rel_path.parts

            # So interessa templates/<app_name>/arquivo.html
            if len(parts) < 2:
                continue

            app_name = parts[0]
            nome_arquivo = parts[-1]

            if nome_arquivo in mapeamento:
                # Conflito: mesmo nome em apps diferentes
                if nome_arquivo not in conflitos:
                    conflitos[nome_arquivo] = [mapeamento[nome_arquivo]]
                conflitos[nome_arquivo].append(f"{app_name}/{nome_arquivo}")
            else:
                mapeamento[nome_arquivo] = f"{app_name}/{nome_arquivo}"

    return mapeamento, conflitos

def corrigir_extends(dry_run=True):
    """
    Encontra {% extends 'xxx' %} sem namespace (sem /)
    e corrige para {% extends 'app/xxx' %} com base no mapeamento.
    """
    mapeamento, conflitos = mapear_templates()

    print("=" * 60)
    print("MAPEAMENTO DE TEMPLATES ENCONTRADOS")
    print("=" * 60)
    for nome, namespaced in sorted(mapeamento.items()):
        print(f"  {nome:40s} -> {namespaced}")

    if conflitos:
        print("\n" + "!" * 60)
        print("CONFLITOS (mesmo nome em apps diferentes) - REVISAR MANUALMENTE:")
        print("!" * 60)
        for nome, apps in sorted(conflitos.items()):
            print(f"  {nome}: {', '.join(apps)}")
    print()

    # Padrao: {% extends 'xxx' %} ou {% extends "xxx" %}
    padrao = re.compile(r"""\{%\s*extends\s*['"]([^'"]+)['"]\s*%\}""")

    alteracoes = []
    ambiguidades = []

    for html_file in sorted(APPS_DIR.rglob("*.html")):
        try:
            conteudo = html_file.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            # Tenta latin-1 como fallback
            conteudo = html_file.read_text(encoding="latin-1")

        mudou = False
        matches = list(padrao.finditer(conteudo))

        for match in matches:
            template_ref = match.group(1)

            # Ja tem namespace (contem /) - pula
            if "/" in template_ref:
                continue

            # Esta no mapeamento?
            if template_ref in mapeamento:
                # Conflito? Nao altera, sinaliza
                if template_ref in conflitos:
                    ambiguidades.append({
                        "arquivo": str(html_file.relative_to(PROJECT_ROOT)),
                        "extends": match.group(0),
                        "conflito": template_ref,
                        "opcoes": conflitos[template_ref],
                    })
                    continue

                novo_ref = mapeamento[template_ref]
                velho = match.group(0)
                # Substitui o nome do template dentro da tag
                novo = velho.replace(
                    f"'{template_ref}'",
                    f"'{novo_ref}'",
                ).replace(
                    f'"{template_ref}"',
                    f'"{novo_ref}"',
                )

                alteracoes.append({
                    "arquivo": str(html_file.relative_to(PROJECT_ROOT)),
                    "velho": velho,
                    "novo": novo,
                })

                if not dry_run:
                    conteudo = conteudo.replace(velho, novo)
                    mudou = True

        if mudou and not dry_run:
            html_file.write_text(conteudo, encoding="utf-8")

    return alteracoes, ambiguidades

def main():
    dry_run = "--aplicar" not in sys.argv

    if dry_run:
        print("=" * 60)
        print("MODO DRY-RUN - apenas simulacao")
        print("Para aplicar: python corrige_templates_extends.py --aplicar")
        print("=" * 60)
        print()
    else:
        print("=" * 60)
        print("APLICANDO ALTERACOES")
        print("=" * 60)
        print()

    alteracoes, ambiguidades = corrigir_extends(dry_run)

    # Relatorio de alteracoes
    print("=" * 60)
    print(f"ALTERACOES: {len(alteracoes)}")
    print("=" * 60)
    for alt in alteracoes:
        print(f"\nArquivo: {alt['arquivo']}")
        print(f"  De:   {alt['velho']}")
        print(f"  Para: {alt['novo']}")

    # Relatorio de ambiguidades
    if ambiguidades:
        print("\n" + "=" * 60)
        print(f"AMBIGUIDADES (revisar manualmente): {len(ambiguidades)}")
        print("=" * 60)
        for amb in ambiguidades:
            print(f"\nArquivo: {amb['arquivo']}")
            print(f"  Tag:       {amb['extends']}")
            print(f"  Template:  {amb['conflito']}")
            print(f"  Opcoes:    {', '.join(amb['opcoes'])}")

    # Resumo final
    print("\n" + "=" * 60)
    print("RESUMO")
    print("=" * 60)
    print(f"  Alteracoes aplicaveis: {len(alteracoes)}")
    print(f"  Ambiguidades:          {len(ambiguidades)}")

    if dry_run and alteracoes:
        print(f"\nPara aplicar as {len(alteracoes)} alteracao(oes):")
        print(f"  python corrige_templates_extends.py --aplicar")

    if not dry_run and alteracoes:
        print(f"\n{len(alteracoes)} arquivo(s) alterado(s) com sucesso.")

    if not alteracoes and not ambiguidades:
        print("\nNenhum {% extends %} sem namespace encontrado. Tudo OK.")

if __name__ == "__main__":
    main()


    