import sqlite3

def conectar():
    #Conecta ao bd (cria se nâo existir)
    conn = sqlite3.connect('app.db')
    return conn

def criar_tabela():
    conn = conectar ()
    cursor = conn.cursor()
    #cria a tabela com os campos exigidos
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tarefas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            funcionario TEXT NOT NULL,
            tarefa TEXT NOT NULL,
            prioridade TEXT NOT NULL,
            status TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

if __name__ == '__main__':
    criar_tabela()
    print("Banco de dados e tabela criados com sucesso!")