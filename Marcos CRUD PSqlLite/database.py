import sqlite3
import os

DB_NAME = "app.db"

def conectar():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    return conn, cursor

def criar_tabela():
    conn, cursor = conectar()
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tarefas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            funcionario TEXT NOT NULL,
            funcao TEXT NOT NULL,
            local TEXT NOT NULL,
            tarefa TEXT NOT NULL,
            prioridade TEXT NOT NULL,
            status TEXT NOT NULL,
            inicio TEXT,
            termino TEXT,
            responsavel_registro TEXT NOT NULL,
            data_criacao TEXT NOT NULL
        )
    """)
    
    conn.commit()
    conn.close()
    print("Tabela 'tarefas' verificada/criada com sucesso.")

if __name__ == "__main__":
    criar_tabela()
