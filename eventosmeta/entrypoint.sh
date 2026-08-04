#!/bin/sh
# ============================================================
# Arquivo: entrypoint.sh
# Caminho: eventosmeta/entrypoint.sh
# Finalidade: Script de inicialização do container Django
#             Executa migrações, coleta estáticos e inicia Gunicorn
# Atualizações:
#  - 07/07/2026 - Versão inicial com healthcheck do PostgreSQL
#  - 01/08/2026 - Adição de verificação da variável DEBUG para coletar arquivos estáticos apenas em produção
# ============================================================


# o que está comentado abaixo é para ser usado em produção, mas não é necessário para desenvolvimento local, pois o Django já serve arquivos estáticos no modo DEBUG=True.
# e foi uma sugestão do claude o que vem mais abaixo é o que está sendo usado atualmente foi uma sugestão do Claude/Adapta

# set -e

# echo "Executando migrations..."
# python manage.py migrate --noinput

# echo "Coletando arquivos estáticos..."
# python manage.py collectstatic --noinput --clear

# echo "Iniciando aplicação..."
# exec "$@"



set -e

echo "Executando migrations..."
python manage.py migrate --noinput

if [ "$DEBUG" = "True" ] || [ "$DEBUG" = "1" ]; then
    echo "Ambiente de desenvolvimento — pulando collectstatic."
else
    echo "Coletando arquivos estáticos..."
    python manage.py collectstatic --noinput --clear
fi

echo "Iniciando aplicação..."
exec "$@"