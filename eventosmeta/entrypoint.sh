#!/bin/sh
# ============================================================
# Arquivo: entrypoint.sh
# Caminho: eventosmeta/entrypoint.sh
# Finalidade: Script de inicialização do container Django
#             Executa migrações, coleta estáticos e inicia Gunicorn
# Atualizações:
#  - 07/07/2026 - Versão inicial com healthcheck do PostgreSQL
# ============================================================
set -e

echo "Aguardando PostgreSQL ficar pronto..."
sleep 15

echo "Executando migrations..."
python manage.py migrate --noinput

echo "Coletando arquivos estáticos..."
python manage.py collectstatic --noinput --clear

echo "Iniciando Gunicorn..."
exec "$@"

