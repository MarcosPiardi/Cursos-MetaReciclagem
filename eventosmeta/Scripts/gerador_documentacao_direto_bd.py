from sqlalchemy import create_engine, inspect, text
from urllib.parse import quote_plus
from datetime import datetime
import sys

# ==============================
# CONFIG (SEU BANCO)
# ==============================
DATABASE_ENGINE = "postgresql+psycopg2"
DATABASE_NAME = "bdmetareciclagem"
DATABASE_USER = "metareciclagem_user"
DATABASE_PASSWORD = "meta2025@forte"
DATABASE_HOST = "localhost"
DATABASE_PORT = "5432"

OUTPUT_FILE = "documentacao_banco.md"

# ==============================
# URL SEGURA
# ==============================
encoded_password = quote_plus(DATABASE_PASSWORD)

DB_URL = (
    f"{DATABASE_ENGINE}://{DATABASE_USER}:{encoded_password}"
    f"@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_NAME}"
)

print("🔎 DB_URL (debug):", DB_URL.replace(encoded_password, "******"))

# ==============================
# CONEXÃO
# ==============================
engine = create_engine(DB_URL, echo=False)

def test_connection():
    try:
        with engine.connect() as conn:
            conn.execute(text("SELECT 1"))
        print("✅ Conexão OK")
    except Exception as e:
        print("❌ ERRO DE CONEXÃO:")
        print(e)
        sys.exit(1)

# ==============================
# EXTRAÇÃO
# ==============================
def load_metadata():
    with engine.connect() as conn:
        inspector = inspect(conn)

        tables = inspector.get_table_names(schema="public")

        data = {}

        for table in tables:
            columns = inspector.get_columns(table, schema="public")
            pk = inspector.get_pk_constraint(table, schema="public").get("constrained_columns", [])
            fks = inspector.get_foreign_keys(table, schema="public")

            data[table] = {
                "columns": columns,
                "pk": pk,
                "fks": fks
            }

        return data

# ==============================
# MARKDOWN
# ==============================
def generate_markdown(data):
    md = []

    md.append("# 🗄️ Documentação do Banco\n")
    md.append(f"**Banco:** {DATABASE_NAME}\n")
    md.append(f"**Gerado em:** {datetime.now()}\n\n")

    for table, info in data.items():
        md.append("---\n")
        md.append(f"## 📦 Tabela: `{table}`\n")

        md.append("\n### Campos\n")
        md.append("| Campo | Tipo | PK | Nullable | Default |\n")
        md.append("|------|------|----|----------|---------|\n")

        for col in info["columns"]:
            name = col["name"]
            col_type = str(col["type"])
            nullable = col["nullable"]
            default = col.get("default")

            md.append(
                f"| {name} | {col_type} | "
                f"{'✔' if name in info['pk'] else ''} | "
                f"{'✔' if nullable else '✘'} | "
                f"{default if default else ''} |"
            )

        if info["fks"]:
            md.append("\n### 🔗 Relacionamentos\n")
            for fk in info["fks"]:
                md.append(
                    f"- `{table}.{','.join(fk['constrained_columns'])}` → "
                    f"`{fk['referred_table']}.{','.join(fk['referred_columns'])}`"
                )

        md.append("\n")

    return "\n".join(md)

# ==============================
# MERMAID ER DIAGRAM
# ==============================
def generate_mermaid(data):
    lines = []
    lines.append("## 🧩 Diagrama ER\n")
    lines.append("```mermaid")
    lines.append("erDiagram")

    # entidades
    for table, info in data.items():
        lines.append(f"    {table} {{")
        for col in info["columns"]:
            lines.append(f"        {str(col['type'])} {col['name']}")
        lines.append("    }")

    # relacionamentos
    for table, info in data.items():
        for fk in info["fks"]:
            ref_table = fk["referred_table"]
            lines.append(f"    {table} }}o--|| {ref_table} : FK")

    lines.append("```\n")

    return "\n".join(lines)

# ==============================
# EXECUÇÃO
# ==============================
if __name__ == "__main__":
    test_connection()

    data = load_metadata()

    markdown = generate_markdown(data)
    mermaid = generate_mermaid(data)

    final_doc = markdown + "\n" + mermaid

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(final_doc)

    print(f"✅ Documentação gerada: {OUTPUT_FILE}")


