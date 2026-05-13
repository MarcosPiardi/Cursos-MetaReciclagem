import re
import os
import argparse
import logging
import datetime
from pathlib import Path
from typing import List, Dict, Any, Optional

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class DjangoCodeParser:
    """Parser para extrair informações do código Django concatenado."""
    
    def __init__(self, content: str):
        self.content = content

    def extract_installed_apps(self) -> List[str]:
        """Extrai lista de apps instalados de INSTALLED_APPS."""
        pattern = r'INSTALLED_APPS\s*=\s*\[\s*(.*?)\s*\]'
        match = re.search(pattern, self.content, re.DOTALL | re.IGNORECASE)
        if not match:
            return []
        apps_str = match.group(1)
        apps = re.findall(r"'([^']*)'|\"([^\"]*)\"", apps_str)
        return [app[0] if app[0] else app[1] for app in apps if app[0] or app[1]]

    def extract_models(self) -> List[Dict[str, Any]]:
        """Extrai models, campos, relacionamentos e índices."""
        models: List[Dict[str, Any]] = []
        pattern = r'class\s+(\w+)\s*\([^)]*?models\.Model[^)]*\)'
        matches = re.finditer(pattern, self.content, re.MULTILINE | re.IGNORECASE | re.DOTALL)
        for match in matches:
            model_name = match.group(1)
            start, end = match.span()
            snippet = self.content[start:end]
            
            # Campos
            fields = re.findall(r'(\w+)\s*=\s*models\.(\w+)\s*\(', snippet, re.MULTILINE)
            fields_list = [{'name': name, 'type': dtype} for name, dtype in fields]
            
            # Relacionamentos (ForeignKey)
            rels = re.findall(r'(\w+)\s*=\s*models\.ForeignKey\s*\([^)]*["\'](\w+)["\'][^)]*\)', snippet, re.MULTILINE | re.DOTALL)
            rels_list = [{'field': name, 'to': to_model} for name, to_model in rels]
            
            # Índices (simplificado)
            indexes = re.findall(r'indexes\s*=\s*\[([^\]]+)\]', snippet, re.MULTILINE | re.DOTALL)
            indexes_list = indexes if indexes else []
            
            models.append({
                'name': model_name,
                'fields': fields_list,
                'relationships': rels_list,
                'indexes': indexes_list
            })
        return models

    def extract_services(self) -> List[str]:
        """Extrai classes de serviços (*Service)."""
        pattern = r'class\s+(\w+Service)\s*\('
        matches = re.findall(pattern, self.content, re.MULTILINE | re.IGNORECASE)
        return list(set(matches))  # únicos

    def extract_urls(self) -> List[str]:
        """Extrai URLs principais."""
        pattern = r"path\s*\(\s*['\"]([^'\"]*)['\"]"
        matches = re.findall(pattern, self.content, re.MULTILINE)
        return matches[:20]  # top 20

    def extract_management_commands(self) -> List[str]:
        """Extrai management commands (simplificado)."""
        pattern = r'class\s+Command\s*\(BaseCommand\)'
        matches = re.finditer(pattern, self.content, re.MULTILINE | re.IGNORECASE)
        commands = []
        for match in matches:
            start = max(0, match.start() - 100)
            snippet = self.content[start:match.end() + 200]
            app_match = re.search(r'apps\.(\w+)/management', snippet)
            cmd_name = app_match.group(1) if app_match else 'unknown'
            commands.append(cmd_name)
        return list(set(commands))

    def extract_admin_actions(self) -> List[str]:
        """Extrai ações admin (simplificado)."""
        pattern = r'class\s+\w+Admin.*def\s+(\w+)\s*\(self,\s*request,\s*queryset'
        matches = re.findall(pattern, self.content, re.MULTILINE | re.DOTALL | re.IGNORECASE)
        return list(set(matches))

class MarkdownGenerator:
    """Gera Markdown estruturado com 5 seções estáticas."""
    
    def __init__(self, parser: DjangoCodeParser):
        self.parser = parser

    def generate(self) -> str:
        """Gera o conteúdo Markdown completo."""
        apps = self.parser.extract_installed_apps()
        models = self.parser.extract_models()
        services = self.parser.extract_services()
        urls = self.parser.extract_urls()
        mgmt_cmds = self.parser.extract_management_commands()
        admin_actions = self.parser.extract_admin_actions()

        md = []

        # Cabeçalho
        md.append("# Documentação Técnica Consolidada\n")
        md.append(f"Gerada em: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}\n\n")

        # Seção 1: Arquitetura Geral
        md.append("## Arquitetura Geral do Sistema\n")
        md.append("- **Framework**: Django 5.2.4 [VALIDAR]\n")
        md.append("- **Banco de dados**: SQLite (dev) / configurável [VALIDAR]\n")
        md.append("- **Apps instalados** [VALIDAR]:\n")
        for app in apps:
            md.append(f"  - {app}\n")
        md.append("- **Padrão**: MVT (Models, Views, Templates)\n")
        md.append("- **Serviços críticos** [VALIDAR]:\n")
        for svc in services:
            md.append(f"  - {svc}\n")
        md.append("  - ClassificadorService\n")
        md.append("  - CustomEmailBackend\n")
        md.append("- **Segurança**: django-axes, django-csp, autenticação customizada, criptografia CPF/NIS [VALIDAR]\n")
        md.append("- **URLs principais** [VALIDAR] (amostra):\n")
        for url in urls[:10]:
            md.append(f"  - {url}\n")
        if len(urls) > 10:
            md.append(f"  - ... e mais {len(urls)-10}\n")
        md.append("- **Management Commands** [VALIDAR]:\n")
        for cmd in mgmt_cmds:
            md.append(f"  - {cmd}\n")
        md.append("- **Admin Actions** [VALIDAR]:\n")
        for action in admin_actions:
            md.append(f"  - {action}\n")

        # Seção 2: ADRs
        md.append("\n## Decisões Arquiteturais (ADRs)\n")
        md.append("[REVISAR] Nenhuma ADR extraída automaticamente do código. Verificar arquivos ADRs se existirem.\n")

        # Seção 3: Regras de Negócio
        md.append("\n## Regras de Negócio Imutáveis\n")
        md.append("[VALIDAR] Regras inferidas de serviços e models:\n")
        md.append("- Criptografia de CPF/NIS\n")
        md.append("- Lógica em ClassificadorService\n")
        md.append("[REVISAR] Seção incompleta. Revisar manualmente.\n")

        # Seção 4: Glossário
        md.append("\n## Glossário Técnico e Funcional\n")
        md.append("[REVISAR] Glossário não extraído automaticamente.\n")
        md.append("- MVT: Model-View-Template\n")
        md.append("- MER: Modelo Entidade-Relacionamento\n")
        md.append("- ADR: Architecture Decision Record\n")

        # Seção 5: MER
        md.append("\n## Modelo Entidade-Relacionamento (MER)\n")
        md.append("[VALIDAR] Extraído automaticamente dos models.\n")
        if models:
            md.append("```mermaid\nerDiagram\n")
            for model in models:
                md.append(f"{model['name']} {{ \n")
                for field in model['fields']:
                    md.append(f"  {field['name']} : {field['type']}\n")
                md.append("}\n")
                for rel in model['relationships']:
                    md.append(f"{model['name'] } }}--|| {rel['to']} : \"{rel['field']}\"\n")
            md.append("```\n")
        else:
            md.append("[CONFLITO] Nenhum model encontrado. Verificar extração.\n")

        return ''.join(md)

def main() -> None:
    """Função principal do script."""
    arg_parser = argparse.ArgumentParser(description="Gera documentação Markdown de projeto Django.")
    arg_parser.add_argument('--code-file', required=True, help="Caminho para o arquivo concatenado do código.")
    args = arg_parser.parse_args()

    try:
        code_path: Path = Path(args.code_file)
        if not code_path.exists():
            raise FileNotFoundError(f"Arquivo não encontrado: {code_path}")
        
        with code_path.open('r', encoding='utf-8') as f:
            content = f.read()
        
        parser = DjangoCodeParser(content)
        generator = MarkdownGenerator(parser)
        md_content = generator.generate()
        
        output_dir = Path('docs/estática')
        output_dir.mkdir(parents=True, exist_ok=True)
        
        date_str = datetime.datetime.now().strftime('%Y%m%d')
        filename = output_dir / f"ESTÁTICO_Documentacao-Consolidada_{date_str}.md"
        
        with filename.open('w', encoding='utf-8') as f:
            f.write(md_content)
        
        logger.info(f"Documentação gerada com sucesso em: {filename}")
    
    except Exception as e:
        logger.error(f"Erro ao gerar documentação: {e}")
        raise

if __name__ == '__main__':
    main()


