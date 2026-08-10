# ============================================================
# Arquivo: Dockerfile
# Caminho: eventosmeta/Dockerfile
# Finalidade: Imagem Docker para Django MetaReciclagem (Desenvolvimento)
# Atualizacoes:
#  - 29/06/2026 - Versao inicial
#  - 08/03/2026 - Adicionado cabecalho padronizado
#               - Corrigido CMD: runserver para dev (gunicorn fica no Dockerfile.prod)
# ============================================================

FROM python:3.13-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    DJANGO_SETTINGS_MODULE=config.settings

# Criar usuario nao-root
RUN useradd -m -u 1000 django

WORKDIR /app

# Instalar dependencias primeiro (aproveita cache de layers)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar codigo do projeto
COPY . .

# Permissoes: chmod no entrypoint, criar diretorios, ownership
RUN chmod +x /app/entrypoint.sh && \
    mkdir -p /app/staticfiles_collected /app/media && \
    chown -R django:django /app

# Trocar para usuario nao-root
USER django

EXPOSE 8000

# Entrypoint: roda migrations + collectstatic antes de iniciar
ENTRYPOINT ["/app/entrypoint.sh"]

# CMD dev: runserver com auto-reload (compose sobrescreve se necessario)
RUN chmod +x /app/entrypoint.sh
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

