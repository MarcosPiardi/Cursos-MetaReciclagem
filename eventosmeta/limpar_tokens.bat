@echo off
REM ============================================================
REM Arquivo: limpar_tokens.bat
REM Caminho: eventosmeta/limpar_tokens.bat
REM Alteração: Script de limpeza automática de tokens expirados
REM Data: 20/02/2026
REM ============================================================

REM Ativa o ambiente virtual
call C:\PMS\PMS2025\Inscr-Meta\prg-Meta\Eventos-MetaReciclagem\.venv\Scripts\activate.bat

REM Entra na pasta do projeto
cd /d C:\PMS\PMS2025\Inscr-Meta\prg-Meta\Eventos-MetaReciclagem\eventosmeta

REM Executa o comando de limpeza
python manage.py limpar_tokens

REM Registra no log com data e hora
echo [%date% %time%] Limpeza de tokens executada >> logs\limpar_tokens.log

