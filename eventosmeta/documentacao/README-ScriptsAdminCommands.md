## 🎯 Comandos por Ambiente

### Produção (1x após deploy)
- `python manage.py popular_dados_iniciais`

### Operacional (admin/scheduler)
- `python manage.py classificar_evento --evento_id=1`
- `python manage.py configurar_criterios_evento --evento_id=1`

### Desenvolvimento (local/staging)
- `python manage.py gerar_dados_teste --eventos=5 --interessados=50`
- `.\limpar_migrations_postgres.ps1` (reset completo)