# debug-admin-csv.ps1
# Propósito: Capturar erro 500 do admin e salvar em CSV

Write-Host "=== DEBUG ADMIN 500 - FORMATO CSV ===" -ForegroundColor Cyan

# 1. Configurar logging
Write-Host "`n[1/4] Configurando logging..." -ForegroundColor Yellow
docker compose exec web_eventosmeta sh -c 'cat >> /app/config/settings.py << "EOF"

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "level": "DEBUG",
        },
    },
    "loggers": {
        "django": {
            "handlers": ["console"],
            "level": "DEBUG",
            "propagate": True,
        },
    },
}
EOF'

# 2. Reiniciar Django
Write-Host "`n[2/4] Reiniciando Django..." -ForegroundColor Yellow
docker compose restart web_eventosmeta
Start-Sleep -Seconds 10

# 3. Capturar logs
Write-Host "`n[3/4] Capturando logs..." -ForegroundColor Yellow
Start-Process "http://localhost/eventosmeta/admin/" -WindowStyle Hidden
Start-Sleep -Seconds 3

$logs = docker compose logs web_eventosmeta 2>&1

# 4. Salvar em CSV
Write-Host "`n[4/4] Salvando em CSV..." -ForegroundColor Yellow
$csvFile = "debug-admin-logs.csv"

$logs | ForEach-Object {
    [PSCustomObject]@{
        Timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
        Message = $_
    }
} | Export-Csv -Path $csvFile -NoTypeInformation -Encoding UTF8 -Force

Write-Host "`n✓ Arquivo criado: $csvFile" -ForegroundColor Green
Write-Host "`nAbra o arquivo com Excel ou Notepad e procure por:" -ForegroundColor Cyan
Write-Host "  - Traceback" -ForegroundColor Yellow
Write-Host "  - Exception" -ForegroundColor Yellow
Write-Host "  - Error" -ForegroundColor Yellow
Write-Host "  - 500" -ForegroundColor Yellow
Write-Host "`nCompartilhe o conteúdo do arquivo $csvFile" -ForegroundColor Green
