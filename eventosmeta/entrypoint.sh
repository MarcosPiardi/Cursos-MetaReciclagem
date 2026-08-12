#!/bin/sh
# ============================================================
# Arquivo: entrypoint.sh
# Caminho: eventosmeta/entrypoint.sh
# Finalidade: Script de inicializacao do container Django
#             Executa migracoes, coleta estaticos e inicia Gunicorn
# Atualizacoes:
#  - 07/07/2026 - Versao inicial com healthcheck do PostgreSQL
#  - 01/08/2026 - Adicao de verificacao da variavel DEBUG para
#                 coletar arquivos estaticos apenas em producao
#  - 06/08/2026 - Removido --clear do collectstatic (era lento e
#                 desnecessario em todo restart).
#               - Removido bloco comentado antigo (confundia leitura).
#               - Adicionada espera pelo PostgreSQL antes de migrar.
#               - Adicionado echo de feedback para logs do container.
# 
#   host = os.environ.get('DATABASE_HOST', 'db_eventosmeta_prod')
# ============================================================

set -e

# Aguardar PostgreSQL estar pronto antes de continuar
echo "Aguardando PostgreSQL..."
while ! python -c "
import socket, os
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = os.environ.get('DATABASE_HOST', 'db_eventosmeta')
port = int(os.environ.get('DATABASE_PORT', 5432))
try:
    s.connect((host, port))
    s.close()
    exit(0)
except Exception:
    exit(1)
"; do
    echo "PostgreSQL nao esta pronto, tentando novamente em 2s..."
    sleep 2
done
echo "PostgreSQL esta pronto."

# Executar migracoes do banco de dados
echo "Executando migrations..."
python manage.py migrate --noinput

# Coletar arquivos estaticos apenas em producao
                    # if [ "$DEBUG" = "True" ] || [ "$DEBUG" = "1" ]; then
                    #     echo "Ambiente de desenvolvimento -- pulando collectstatic."
                    # else
                    #     echo "Coletando arquivos estaticos..."
                    #     python manage.py collectstatic --noinput
                    # fi
echo "Coletando arquivos estaticos..."
python manage.py collectstatic --noinput


# Passar o controle para o command definido no docker-compose
echo "Iniciando aplicacao..."
exec "$@"




