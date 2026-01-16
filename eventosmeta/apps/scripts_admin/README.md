# 🛠️ Scripts Administrativos Centralizados

Este app concentra todos os scripts auxiliares do sistema EventosMeta.

## 📂 Estrutura

- `management/commands/` - Comandos Django (Python)
- `powershell/` - Scripts PowerShell para administração

---

## 🐍 Comandos Django

### Como executar:
```bash
python manage.py nome_do_comando

# Exemplos:
# python manage.py gerar_dados_teste
# python manage.py popular_dados_iniciais
# python manage.py classificar_evento --evento=1

# Como executar Scripts PowerShell

# .\apps\scripts_admin\powershell\nome_script.ps1

# Exemplo:
# .\apps\scripts_admin\powershell\limpar_migrations_postgres.ps1

# Observações
# Todos os scripts foram centralizados para facilitar localização e manutenção
# Scripts Python devem ser executados via manage.py
# Scripts PowerShell são independentes do Django

# ---

# ## 🎯 RESUMO DO QUE FIZEMOS:

# ✅ Criamos o app `scripts_admin`  
# ✅ Registramos no `INSTALLED_APPS`  
# ✅ Movemos 6 comandos Django  
# ✅ Movemos 3 scripts PowerShell  
# ✅ Tudo centralizado e organizado!

# ---
