# QUICKSTART - Containerizacao Django

## 5 Passos (5-10 minutos)

1. Configure .env
   cp .env.example .env

2. Build
   docker-compose build

3. Inicie
   docker-compose up -d

4. Verifique
   docker-compose ps

5. Acesse
   http://localhost
   http://localhost/admin

## Problemas

PostgreSQL nao conecta:
  docker-compose logs db
  docker-compose restart db

Statics nao encontrados:
  docker-compose exec web python manage.py collectstatic --noinput
  docker-compose restart web

Porta 80 em uso:
  Mude "80:80" para "8080:80" em docker-compose.yml
