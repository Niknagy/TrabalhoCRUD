import sqlite3
from database import conectar

def inserir_tarefa(dados):
    conn, cursor = conectar()
    cursor.execute("""
        INSERT INTO tarefas (
            funcionario, funcao, local, tarefa, prioridade, status,
            inicio, termino, responsavel_registro, data_criacao
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, dados)
    
    conn.commit()
    novo_id = cursor.lastrowid
    conn.close()
    return novo_id

def listar_tarefas():
    conn, cursor = conectar()
    cursor.execute("SELECT * FROM tarefas ORDER BY id")
    tarefas = cursor.fetchall()
    conn.close()
    return tarefas

def buscar_tarefa_por_id(id_tarefa):
    conn, cursor = conectar()
    cursor.execute("SELECT * FROM tarefas WHERE id = ?", (id_tarefa,))
    tarefa = cursor.fetchone()
    conn.close()
    return tarefa

def atualizar_tarefa(id_tarefa, campo, novo_valor):
    conn, cursor = conectar()
    
    colunas_permitidas = [
        "funcionario", "funcao", "local", "tarefa", "prioridade",
        "status", "inicio", "termino", "responsavel_registro", "data_criacao"
    ]
    
    if campo not in colunas_permitidas:
        print("Campo inválido para atualização.")
        conn.close()
        return False
    
    query = f"UPDATE tarefas SET {campo} = ? WHERE id = ?"
    cursor.execute(query, (novo_valor, id_tarefa))
    conn.commit()
    
    linhas_afetadas = cursor.rowcount
    conn.close()
    return linhas_afetadas > 0

def excluir_tarefa(id_tarefa):
    conn, cursor = conectar()
    cursor.execute("DELETE FROM tarefas WHERE id = ?", (id_tarefa,))
    conn.commit()
    linhas_afetadas = cursor.rowcount
    conn.close()
    return linhas_afetadas > 0
