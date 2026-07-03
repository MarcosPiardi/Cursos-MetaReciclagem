#!/bin/sh
set -e

echo "Aguardando PostgreSQL ficar pronto..."
sleep 15

echo "Executando migrations..."
python manage.py migrate --noinput

echo "Coletando arquivos estáticos..."
python manage.py collectstatic --noinput --clear

echo "Iniciando Gunicorn..."
exec "$@"

