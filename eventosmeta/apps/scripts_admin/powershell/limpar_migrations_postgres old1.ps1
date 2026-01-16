# Script para limpar migrations e resetar banco PostgreSQL
# Uso: .\limpar_migrations_postgres.ps1

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "LIMPEZA DE MIGRATIONS E RESET DE BANCO" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# 1. Remover arquivos de migração (mantém __init__.py)
Write-Host "1. Removendo arquivos de migração..." -ForegroundColor Yellow
Get-ChildItem -Recurse -Include *.py,*.pyc |
Where-Object { $_.DirectoryName -like '*migrations*' -and $_.Name -ne '__init__.py' } |
Remove-Item -Force -Verbose

# 2. Remover __pycache__
Write-Host ""
Write-Host "2. Removendo cache Python..." -ForegroundColor Yellow
Get-ChildItem -Recurse -Directory -Filter __pycache__ | 
Remove-Item -Recurse -Force -Verbose

# 3. Dropar e recriar banco PostgreSQL
Write-Host ""
Write-Host "3. Resetando banco PostgreSQL..." -ForegroundColor Yellow

# Configurações do banco (ajuste se necessário)
$DB_USER = "metareciclagem_user"
$DB_PASSWORD = "meta2025@forte"
$DB_NAME = "metareciclagem"
$DB_HOST = "localhost"

# Definir senha como variável de ambiente
$env:PGPASSWORD = $DB_PASSWORD

try {
    # Dropar banco
    Write-Host "   - Dropando banco '$DB_NAME'..." -ForegroundColor Gray
    psql -U $DB_USER -h $DB_HOST -d postgres -c "DROP DATABASE IF EXISTS $DB_NAME;" 2>&1 | Out-Null
    
    # Criar banco
    Write-Host "   - Criando banco '$DB_NAME'..." -ForegroundColor Gray
    psql -U $DB_USER -h $DB_HOST -d postgres -c "CREATE DATABASE $DB_NAME;" 2>&1 | Out-Null
    
    Write-Host "   ✅ Banco resetado com sucesso!" -ForegroundColor Green
}
catch {
    Write-Host "   ❌ Erro ao resetar banco: $_" -ForegroundColor Red
    Write-Host "   Tente manualmente com: psql -U $DB_USER -h $DB_HOST -d postgres" -ForegroundColor Yellow
}

# Limpar variável de senha
Remove-Item Env:\PGPASSWORD -ErrorAction SilentlyContinue

# 4. Criar novas migrations
Write-Host ""
Write-Host "4. Criando novas migrations..." -ForegroundColor Yellow

$apps = @("accounts", "interessados", "eventos", "selecao", "academico")

foreach ($app in $apps) {
    Write-Host "   - Criando migration para '$app'..." -ForegroundColor Gray
    python manage.py makemigrations $app
}

# 5. Mostrar status
Write-Host ""
Write-Host "5. Status das migrations:" -ForegroundColor Yellow
python manage.py showmigrations

Write-Host ""
Write-Host "========================================" -ForegroundColor Green
Write-Host "✅ LIMPEZA CONCLUÍDA!" -ForegroundColor Green
Write-Host "========================================" -ForegroundColor Green
Write-Host ""
Write-Host "Próximos passos:" -ForegroundColor Cyan
Write-Host "  1. python manage.py migrate" -ForegroundColor White
Write-Host "  2. python manage.py createsuperuser" -ForegroundColor White
Write-Host ""


