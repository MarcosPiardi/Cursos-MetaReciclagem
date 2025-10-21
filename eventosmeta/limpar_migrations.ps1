
# Para limpar as migrations de Banco de dados
# Rodar no powershell do VSCode: 

# .\limpar_migrations.ps1

# Remover migrações
Get-ChildItem -Recurse -Include *.py,*.pyc |
Where-Object { $_.DirectoryName -like '*migrations*' -and $_.Name -ne '__init__.py' } |
Remove-Item -Force -Verbose

# Get-ChildItem -Recurse -Directory -Filter __pycache__ | 
# Remove-Item -Recurse -Force -Verbose


# Remover o banco de dados SQLite
if (Test-Path "db.sqlite3") {
    Remove-Item "db.sqlite3" -Force -Verbose
} else {
    Write-Host "Arquivo db.sqlite3 não encontrado."
}




