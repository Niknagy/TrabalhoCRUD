#!/bin/bash
# Script para executar o Sistema de Gerenciamento de Fretes
# Para Linux/Mac/GitHub Codespaces

echo ""
echo "============================================"
echo "    Sistema CRUD de Fretes - Deploy Local"
echo "============================================"
echo ""

# Verificar se Python está instalado
if ! command -v python3 &> /dev/null; then
    echo "[ERRO] Python não está instalado."
    echo "Instale com: sudo apt-get install python3 python3-pip"
    exit 1
fi

# Criar ambiente virtual se não existir
if [ ! -f ".venv/bin/python" ]; then
    echo "[INFO] Criando ambiente virtual local..."
    python3 -m venv .venv
    if [ $? -ne 0 ]; then
        echo "[ERRO] Falha ao criar ambiente virtual."
        exit 1
    fi
fi

PY=".venv/bin/python"

# Instalar dependências
echo "[1/3] Verificando dependências..."
"$PY" -m pip install -q -r requirements.txt

if [ $? -ne 0 ]; then
    echo "[ERRO] Falha ao instalar dependências."
    exit 1
fi

# Inicializar banco de dados com exemplos
echo "[2/3] Preparando banco de dados..."
"$PY" dados_exemplo.py

# Iniciar a aplicação
echo ""
echo "[3/3] Iniciando servidor..."
echo ""
echo "============================================"
echo "    Servidor rodando em:"
echo "    http://127.0.0.1:5000"
echo "============================================"
echo ""
echo "Pressione Ctrl+C para parar o servidor."
echo ""

"$PY" app.py
