@echo off
REM Script para executar o Sistema de Gerenciamento de Fretes
REM Coloque este arquivo na raiz do projeto

echo.
echo ============================================
echo    Sistema CRUD de Fretes - Deploy Local
echo ============================================
echo.

REM Verificar se Python está instalado
python --version >nul 2>&1
if errorlevel 1 (
    echo [ERRO] Python não está instalado ou não está no PATH.
    echo Baixe em: https://www.python.org/downloads/
    pause
    exit /b 1
)

REM Criar ambiente virtual se não existir
if not exist ".venv\Scripts\python.exe" (
    echo [INFO] Criando ambiente virtual local...
    python -m venv .venv
    if errorlevel 1 (
        echo [ERRO] Falha ao criar ambiente virtual.
        pause
        exit /b 1
    )
)

set "PY=.venv\Scripts\python.exe"

REM Instalar dependências se necessário
echo [1/3] Verificando dependências...
%PY% -m pip install -q -r requirements.txt
if errorlevel 1 (
    echo [ERRO] Falha ao instalar dependências.
    pause
    exit /b 1
)

REM Inicializar banco de dados com exemplos
echo [2/3] Preparando banco de dados...
%PY% dados_exemplo.py

REM Iniciar a aplicação
echo.
echo [3/3] Iniciando servidor...
echo.
echo ============================================
echo    Servidor rodando em:
echo    http://127.0.0.1:5000
echo ============================================
echo.
echo Pressione Ctrl+C para parar o servidor.
echo.

%PY% app.py
