<#
.DESCRIPTION
    Script PowerShell para fazer backup de arquivo antes de modificacao.
    Cria uma pasta "backup" no mesmo diretorio do arquivo (se nao existir),
    copia o arquivo original adicionando timestamp no formato YYYYMMDD_HHMMSS
    e exibe o caminho do backup criado.

.PARAMETER FileName
    Caminho completo ou relativo do arquivo que sera copiado para o backup.

.EXAMPLE
    .\Backup-Arquivo.ps1 -FileName "C:\Projetos\app\config.json"

.EXAMPLE
    .\Backup-Arquivo.ps1 -FileName ".\dados.txt"

.NOTES
    Autor     : Script Gerado Automaticamente
    Versao    : 1.0.0
    Plataforma: Windows PowerShell 5.1+ / PowerShell Core 7+
#>

[CmdletBinding()]
param(
    [Parameter(Mandatory = $true, HelpMessage = "Informe o caminho do arquivo para backup.")]
    [ValidateNotNullOrEmpty()]
    [string]$FileName
)

BEGIN {
    $ErrorActionPreference = "Stop"
}

PROCESS {
    try {
        # (5) Validar se o arquivo existe antes de fazer backup
        if (-not (Test-Path -Path $FileName -PathType Leaf)) {
            Write-Error "Arquivo nao encontrado: $FileName"
            exit 1
        }

        # Obter informacoes do arquivo original
        $arquivoInfo = Get-Item -Path $FileName
        $diretorioBase = $arquivoInfo.DirectoryName
        $nomeArquivo = $arquivoInfo.Name

        # (2) Criar pasta backup/ se nao existir
        $pastaBackup = Join-Path -Path $diretorioBase -ChildPath "backup"
        if (-not (Test-Path -Path $pastaBackup -PathType Container)) {
            Write-Host "Criando pasta de backup: $pastaBackup"
            New-Item -Path $pastaBackup -ItemType Directory -Force | Out-Null
        }

        # (3) Gerar timestamp no formato YYYYMMDD_HHMMSS
        $timestamp = Get-Date -Format "yyyyMMdd_HHmmss"
        $nomeBackup = "{0}_{1}{2}" -f `
            [System.IO.Path]::GetFileNameWithoutExtension($nomeArquivo), `
            $timestamp, `
            $arquivoInfo.Extension

        $caminhoBackup = Join-Path -Path $pastaBackup -ChildPath $nomeBackup

        # Realizar a copia do arquivo
        Copy-Item -Path $arquivoInfo.FullName -Destination $caminhoBackup -Force

        # (4) Exibir caminho do backup criado
        Write-Host "Backup criado com sucesso: $caminhoBackup"

        # Retorna o caminho do backup para permitir uso em pipeline/scripts
        Write-Output $caminhoBackup
    }
    catch {
        Write-Error "Falha ao criar backup do arquivo '$FileName'. Detalhes: $($_.Exception.Message)"
        exit 2
    }
}

END {
    # Nenhuma acao de finalizacao necessaria
}

