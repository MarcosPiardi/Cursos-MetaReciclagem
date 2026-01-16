# Arquivo: limpar_migrations_postgres.ps1
# Caminho: scripts/limpar_migrations_postgres.ps1
# Alteração: Script corrigido para resetar BD com permissões corretas
# Data: 13/01/2026

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

# ✅ CORREÇÃO: Usar POSTGRES (superusuário) para criar/dropar
$DB_SUPERUSER = "postgres"              # ← Superusuário
$DB_USER = "metareciclagem_user"        # ← Usuário normal do app
$DB_NAME = "bdmetareciclagem"           # ← Nome do banco
$DB_HOST = "localhost"

# Solicitar senha do superusuário
Write-Host ""
Write-Host "⚠️  Digite a senha do superusuário 'postgres':" -ForegroundColor Yellow
$SecurePassword = Read-Host -AsSecureString
$BSTR = [System.Runtime.InteropServices.Marshal]::SecureStringToBSTR($SecurePassword)
$DB_PASSWORD = [System.Runtime.InteropServices.Marshal]::PtrToStringAuto($BSTR)

# Definir senha como variável de ambiente
$env:PGPASSWORD = $DB_PASSWORD

try {
    # Desconectar usuários ativos
    Write-Host "   - Desconectando usuários ativos..." -ForegroundColor Gray
    $disconnectQuery = @"
SELECT pg_terminate_backend(pg_stat_activity.pid)
FROM pg_stat_activity
WHERE pg_stat_activity.datname = '$DB_NAME'
  AND pid <> pg_backend_pid();
"@
    psql -U $DB_SUPERUSER -h $DB_HOST -d postgres -c $disconnectQuery 2>&1 | Out-Null
    
    # Dropar banco
    Write-Host "   - Dropando banco '$DB_NAME'..." -ForegroundColor Gray
    psql -U $DB_SUPERUSER -h $DB_HOST -d postgres -c "DROP DATABASE IF EXISTS $DB_NAME;" 2>&1
    
    if ($LASTEXITCODE -eq 0) {
        Write-Host "   ✅ Banco dropado com sucesso!" -ForegroundColor Green
    } else {
        throw "Erro ao dropar banco"
    }
    
    # Criar banco
    Write-Host "   - Criando banco '$DB_NAME'..." -ForegroundColor Gray
    psql -U $DB_SUPERUSER -h $DB_HOST -d postgres -c "CREATE DATABASE $DB_NAME OWNER $DB_USER ENCODING 'UTF8';" 2>&1
    
    if ($LASTEXITCODE -eq 0) {
        Write-Host "   ✅ Banco criado com sucesso!" -ForegroundColor Green
    } else {
        throw "Erro ao criar banco"
    }
}
catch {
    Write-Host "   ❌ Erro ao resetar banco: $_" -ForegroundColor Red
    Write-Host "   Tente manualmente com:" -ForegroundColor Yellow
    Write-Host "   psql -U postgres -h localhost -d postgres" -ForegroundColor White
    Write-Host "   DROP DATABASE IF EXISTS $DB_NAME;" -ForegroundColor White
    Write-Host "   CREATE DATABASE $DB_NAME OWNER $DB_USER;" -ForegroundColor White
    
    # Limpar senha e sair
    Remove-Item Env:\PGPASSWORD -ErrorAction SilentlyContinue
    exit 1
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

# 6. Aplicar migrations
Write-Host ""
Write-Host "6. Aplicando migrations..." -ForegroundColor Yellow
python manage.py migrate

Write-Host ""
Write-Host "========================================" -ForegroundColor Green
Write-Host "✅ LIMPEZA CONCLUÍDA!" -ForegroundColor Green
Write-Host "========================================" -ForegroundColor Green
Write-Host ""
Write-Host "Próximos passos:" -ForegroundColor Cyan
Write-Host "  1. python manage.py createsuperuser" -ForegroundColor White
Write-Host "  2. python manage.py runserver" -ForegroundColor White
Write-Host ""

