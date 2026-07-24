# investigar_template.ps1
# Uso: .\investigar_template.ps1
# Digite o nome do arquivo HTML quando solicitado (ex: gestao_matricula.html)

param(
    [Parameter(Mandatory=$false)]
    [string]$NomeArquivo
)

if (-not $NomeArquivo) {
    $NomeArquivo = Read-Host "Digite o nome (ou parte do nome) do arquivo HTML (ex: gestao_matricula.html)"
}

if (-not $NomeArquivo) {
    Write-Host "Nome invalido. Saindo." -ForegroundColor Red
    exit
}

# Remove a extensao .html se o usuario digitou, para buscar tambem sem extensao
$nomeBase = $NomeArquivo -replace '\.html$', ''

Write-Host ""
Write-Host "============================================" -ForegroundColor Cyan
Write-Host " Investigando: $NomeArquivo" -ForegroundColor Cyan
Write-Host " Buscando por: $NomeArquivo e $nomeBase" -ForegroundColor Cyan
Write-Host "============================================" -ForegroundColor Cyan
Write-Host ""

# Extensoes de arquivo onde procurar referencias
$extensoes = @("*.py", "*.html", "*.js", "*.css", "*.txt", "*.yaml", "*.yml")

# Diretorio base do projeto (sobe a partir de onde o script esta)
$dirBase = Get-Location

$totalRefs = 0
$arquivosComRef = @{}

foreach ($ext in $extensoes) {
    $arquivos = Get-ChildItem -Path $dirBase -Recurse -Include $ext -ErrorAction SilentlyContinue |
        Where-Object { $_.FullName -notlike "*\node_modules\*" -and $_.FullName -notlike "*\.git\*" -and $_.FullName -notlike "*\__pycache__\*" -and $_.FullName -notlike "*\temp\*" -and $_.FullName -notlike "*\htmlcov\*" }

    foreach ($arq in $arquivos) {
        $linhas = Select-String -Path $arq.FullName -Pattern $nomeBase -ErrorAction SilentlyContinue
        if ($linhas) {
            foreach ($linha in $linhas) {
                # Ignora o proprio arquivo se ele for o template sendo procurado
                if ($arq.Name -eq $NomeArquivo) {
                    continue
                }
                $totalRefs++
                if (-not $arquivosComRef.ContainsKey($arq.FullName)) {
                    $arquivosComRef[$arq.FullName] = @()
                }
                $arquivosComRef[$arq.FullName] += $linha
            }
        }
    }
}

# Resultado
if ($totalRefs -eq 0) {
    Write-Host "RESULTADO: Nenhuma referencia encontrada em todo o projeto." -ForegroundColor Yellow
    Write-Host " O template provavelmente NAO esta em uso." -ForegroundColor Yellow
} else {
    Write-Host "REFERENCIAS ENCONTRADAS ($totalRefs total):" -ForegroundColor Green
    Write-Host ""
    foreach ($arqPath in $arquivosComRef.Keys) {
        $nomeRelativo = Resolve-Path -Path $arqPath -Relative
        Write-Host "  Arquivo: $nomeRelativo" -ForegroundColor White
        foreach ($linha in $arquivosComRef[$arqPath]) {
            Write-Host "    Linha $($linha.LineNumber): $($linha.Line.Trim())" -ForegroundColor Gray
        }
        Write-Host ""
    }
}

Write-Host ""
Write-Host "============================================" -ForegroundColor Cyan
Write-Host " Fim da investigacao" -ForegroundColor Cyan
Write-Host "============================================" -ForegroundColor Cyan

