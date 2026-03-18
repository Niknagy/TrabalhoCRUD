import sqlite3
import tkinter as tk
from tkinter import messagebox, ttk


# 1. CONFIGURAÇÃO DO BANCO DE DADOS

def conectar():

    return sqlite3.connect('app.db')

def criar_tabela():
    conn = conectar()
    cursor = conn.cursor()
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

# 2. TELAS DO SISTEMA

# Tela de Inserir Dados (Create)
def abrir_tela_inserir():
    janela_inserir = tk.Toplevel()
    janela_inserir.title("Inserir Dados")
    janela_inserir.geometry("300x350")
    
    tk.Label(janela_inserir, text="Funcionário:").pack(pady=2)
    entrada_func = tk.Entry(janela_inserir, width=30)
    entrada_func.pack(pady=2)
    
    tk.Label(janela_inserir, text="Tarefa:").pack(pady=2)
    entrada_tar = tk.Entry(janela_inserir, width=30)
    entrada_tar.pack(pady=2)
    
    tk.Label(janela_inserir, text="Prioridade (Alta/Média/Baixa):").pack(pady=2)
    entrada_prio = tk.Entry(janela_inserir, width=30)
    entrada_prio.pack(pady=2)
    
    tk.Label(janela_inserir, text="Status (Pendente/Concluída):").pack(pady=2)
    entrada_stat = tk.Entry(janela_inserir, width=30)
    entrada_stat.pack(pady=2)
    
    def salvar_no_banco():
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO tarefas (funcionario, tarefa, prioridade, status)
            VALUES (?, ?, ?, ?)
        ''', (entrada_func.get(), entrada_tar.get(), entrada_prio.get(), entrada_stat.get()))
        conn.commit()
        conn.close()
        
        messagebox.showinfo("Sucesso", "Tarefa inserida com sucesso!")
        janela_inserir.destroy()
        
    tk.Button(janela_inserir, text="Guardar Dados", command=salvar_no_banco, bg="lightgreen").pack(pady=15)

# Tela de Consultar Dados (Read) 
def abrir_tela_consultar():
    janela_consultar = tk.Toplevel()
    janela_consultar.title("Consultar Dados")
    janela_consultar.geometry("600x300")
    
    # Criação de uma tabela visual
    colunas = ("ID", "Funcionário", "Tarefa", "Prioridade", "Status")
    tabela = ttk.Treeview(janela_consultar, columns=colunas, show="headings")
    
    # Define os cabeçalhos
    for col in colunas:
        tabela.heading(col, text=col)
        tabela.column(col, width=110)
    
    tabela.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
    
    # Busca os dados no banco
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM tarefas')
    linhas = cursor.fetchall()
    conn.close()
    
    # Insere os dados na tabela visual
    for linha in linhas:
        tabela.insert("", tk.END, values=linha)

# Tela de Atualizar Dados (Update) 
def abrir_tela_atualizar():
    janela_atualizar = tk.Toplevel()
    janela_atualizar.title("Atualizar Dados")
    janela_atualizar.geometry("300x200")
    
    tk.Label(janela_atualizar, text="ID da Tarefa a atualizar:").pack(pady=2)
    entrada_id = tk.Entry(janela_atualizar, width=10)
    entrada_id.pack(pady=2)
    
    tk.Label(janela_atualizar, text="Novo Status:").pack(pady=2)
    entrada_stat = tk.Entry(janela_atualizar, width=30)
    entrada_stat.pack(pady=2)
    
    def atualizar_no_banco():
        conn = conectar()
        cursor = conn.cursor()
        
        cursor.execute('''
            UPDATE tarefas SET status = ? WHERE id = ?
        ''', (entrada_stat.get(), entrada_id.get()))
        conn.commit()
        conn.close()
        
        messagebox.showinfo("Sucesso", "Status da tarefa atualizado!")
        janela_atualizar.destroy()
        
    tk.Button(janela_atualizar, text="Atualizar", command=atualizar_no_banco, bg="lightblue").pack(pady=15)

# Tela de Excluir Dados (Delete)
def abrir_tela_excluir():
    janela_excluir = tk.Toplevel()
    janela_excluir.title("Excluir Dados")
    janela_excluir.geometry("300x150")
    
    tk.Label(janela_excluir, text="ID da Tarefa a Excluir:").pack(pady=10)
    entrada_id = tk.Entry(janela_excluir, width=10)
    entrada_id.pack(pady=5)
    
    def excluir_no_banco():
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute('DELETE FROM tarefas WHERE id = ?', (entrada_id.get(),))
        conn.commit()
        conn.close()
        
        messagebox.showwarning("Aviso", "Tarefa excluída com sucesso!")
        janela_excluir.destroy()
        
    tk.Button(janela_excluir, text="Excluir", command=excluir_no_banco, bg="salmon").pack(pady=10)


# 3. TELA DE MENU

def iniciar_menu():
    criar_tabela()
    
    janela = tk.Tk()
    janela.title("Gestão de Tarefas - FATEC")
    janela.geometry("350x350")
    
    tk.Label(janela, text="Menu Principal", font=("Arial", 16, "bold")).pack(pady=20)
    
    tk.Button(janela, text="Inserir Dados", width=25, height=2, command=abrir_tela_inserir).pack(pady=5)
    tk.Button(janela, text="Consultar Dados", width=25, height=2, command=abrir_tela_consultar).pack(pady=5)
    tk.Button(janela, text="Atualizar Dados", width=25, height=2, command=abrir_tela_atualizar).pack(pady=5)
    tk.Button(janela, text="Excluir Dados", width=25, height=2, command=abrir_tela_excluir).pack(pady=5)
    
    janela.mainloop()

# Inicia o programa
if __name__ == '__main__':
    iniciar_menu()