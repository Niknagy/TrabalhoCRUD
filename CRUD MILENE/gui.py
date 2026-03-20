import tkinter as tk
from tkinter import messagebox
import crud
import db_setup

db_setup.create_database()

def main_menu():
    root = tk.Tk()
    root.title("Sistema CRUD de Tarefas")
    root.geometry("300x300")

    tk.Label(root, text="Menu Principal", font=("Arial", 16)).pack(pady=20)

    tk.Button(root, text="Inserir Tarefa", command=insert_screen, width=20).pack(pady=5)
    tk.Button(root, text="Consultar Tarefas", command=query_screen, width=20).pack(pady=5)
    tk.Button(root, text="Atualizar Tarefa", command=update_screen, width=20).pack(pady=5)
    tk.Button(root, text="Excluir Tarefa", command=delete_screen, width=20).pack(pady=5)
    tk.Button(root, text="Sair", command=root.quit, width=20).pack(pady=5)

    root.mainloop()

def insert_screen():
    window = tk.Toplevel()
    window.title("Inserir Tarefa")
    window.geometry("400x400")

    tk.Label(window, text="Funcionário:").grid(row=0, column=0, padx=10, pady=5)
    employee_entry = tk.Entry(window, width=30)
    employee_entry.grid(row=0, column=1, padx=10, pady=5)

    tk.Label(window, text="Função:").grid(row=1, column=0, padx=10, pady=5)
    function_entry = tk.Entry(window, width=30)
    function_entry.grid(row=1, column=1, padx=10, pady=5)

    tk.Label(window, text="Local:").grid(row=2, column=0, padx=10, pady=5)
    location_entry = tk.Entry(window, width=30)
    location_entry.grid(row=2, column=1, padx=10, pady=5)

    tk.Label(window, text="Tarefa:").grid(row=3, column=0, padx=10, pady=5)
    task_entry = tk.Entry(window, width=30)
    task_entry.grid(row=3, column=1, padx=10, pady=5)

    tk.Label(window, text="Prioridade:").grid(row=4, column=0, padx=10, pady=5)
    priority_entry = tk.Entry(window, width=30)
    priority_entry.grid(row=4, column=1, padx=10, pady=5)

    tk.Label(window, text="Status:").grid(row=5, column=0, padx=10, pady=5)
    status_entry = tk.Entry(window, width=30)
    status_entry.grid(row=5, column=1, padx=10, pady=5)

    tk.Label(window, text="Data de início (YYYY-MM-DD):").grid(row=6, column=0, padx=10, pady=5)
    start_date_entry = tk.Entry(window, width=30)
    start_date_entry.grid(row=6, column=1, padx=10, pady=5)

    tk.Label(window, text="Data de término (YYYY-MM-DD):").grid(row=7, column=0, padx=10, pady=5)
    end_date_entry = tk.Entry(window, width=30)
    end_date_entry.grid(row=7, column=1, padx=10, pady=5)

    tk.Label(window, text="Responsável:").grid(row=8, column=0, padx=10, pady=5)
    responsible_entry = tk.Entry(window, width=30)
    responsible_entry.grid(row=8, column=1, padx=10, pady=5)

    def submit():
        try:
            crud.insert_task(
                employee_entry.get(),
                function_entry.get(),
                location_entry.get(),
                task_entry.get(),
                priority_entry.get(),
                status_entry.get(),
                start_date_entry.get(),
                end_date_entry.get(),
                responsible_entry.get()
            )
            messagebox.showinfo("Sucesso", "Tarefa inserida com sucesso!")
            window.destroy()
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao inserir: {str(e)}")

    tk.Button(window, text="Inserir", command=submit).grid(row=9, column=1, pady=20)

def query_screen():
    window = tk.Toplevel()
    window.title("Consultar Tarefas")
    window.geometry("600x400")

    text = tk.Text(window, wrap=tk.WORD)
    text.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)

    tasks = crud.get_all_tasks()
    if tasks:
        for t in tasks:
            text.insert(tk.END, f"ID: {t[0]}, Funcionário: {t[1]}, Função: {t[2]}, Local: {t[3]}, Tarefa: {t[4]}, Prioridade: {t[5]}, Status: {t[6]}, Início: {t[7]}, Fim: {t[8]}, Responsável: {t[9]}, Criado: {t[10]}\n\n")
    else:
        text.insert(tk.END, "Nenhuma tarefa encontrada.")

def update_screen():
    window = tk.Toplevel()
    window.title("Atualizar Tarefa")
    window.geometry("400x500")

    tk.Label(window, text="ID da tarefa:").grid(row=0, column=0, padx=10, pady=5)
    id_entry = tk.Entry(window, width=30)
    id_entry.grid(row=0, column=1, padx=10, pady=5)

    tk.Label(window, text="Novo Funcionário:").grid(row=1, column=0, padx=10, pady=5)
    employee_entry = tk.Entry(window, width=30)
    employee_entry.grid(row=1, column=1, padx=10, pady=5)

    tk.Label(window, text="Nova Função:").grid(row=2, column=0, padx=10, pady=5)
    function_entry = tk.Entry(window, width=30)
    function_entry.grid(row=2, column=1, padx=10, pady=5)

    tk.Label(window, text="Novo Local:").grid(row=3, column=0, padx=10, pady=5)
    location_entry = tk.Entry(window, width=30)
    location_entry.grid(row=3, column=1, padx=10, pady=5)

    tk.Label(window, text="Nova Tarefa:").grid(row=4, column=0, padx=10, pady=5)
    task_entry = tk.Entry(window, width=30)
    task_entry.grid(row=4, column=1, padx=10, pady=5)

    tk.Label(window, text="Nova Prioridade:").grid(row=5, column=0, padx=10, pady=5)
    priority_entry = tk.Entry(window, width=30)
    priority_entry.grid(row=5, column=1, padx=10, pady=5)

    tk.Label(window, text="Novo Status:").grid(row=6, column=0, padx=10, pady=5)
    status_entry = tk.Entry(window, width=30)
    status_entry.grid(row=6, column=1, padx=10, pady=5)

    tk.Label(window, text="Nova Data de início:").grid(row=7, column=0, padx=10, pady=5)
    start_date_entry = tk.Entry(window, width=30)
    start_date_entry.grid(row=7, column=1, padx=10, pady=5)

    tk.Label(window, text="Nova Data de término:").grid(row=8, column=0, padx=10, pady=5)
    end_date_entry = tk.Entry(window, width=30)
    end_date_entry.grid(row=8, column=1, padx=10, pady=5)

    tk.Label(window, text="Novo Responsável:").grid(row=9, column=0, padx=10, pady=5)
    responsible_entry = tk.Entry(window, width=30)
    responsible_entry.grid(row=9, column=1, padx=10, pady=5)

    def submit():
        try:
            crud.update_task(
                int(id_entry.get()),
                employee_entry.get(),
                function_entry.get(),
                location_entry.get(),
                task_entry.get(),
                priority_entry.get(),
                status_entry.get(),
                start_date_entry.get(),
                end_date_entry.get(),
                responsible_entry.get()
            )
            messagebox.showinfo("Sucesso", "Tarefa atualizada com sucesso!")
            window.destroy()
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao atualizar: {str(e)}")

    tk.Button(window, text="Atualizar", command=submit).grid(row=10, column=1, pady=20)

def delete_screen():
    window = tk.Toplevel()
    window.title("Excluir Tarefa")
    window.geometry("300x150")

    tk.Label(window, text="ID da tarefa a excluir:").grid(row=0, column=0, padx=10, pady=10)
    id_entry = tk.Entry(window, width=20)
    id_entry.grid(row=0, column=1, padx=10, pady=10)

    def submit():
        try:
            crud.delete_task(int(id_entry.get()))
            messagebox.showinfo("Sucesso", "Tarefa excluída com sucesso!")
            window.destroy()
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao excluir: {str(e)}")

    tk.Button(window, text="Excluir", command=submit).grid(row=1, column=1, pady=10)

if __name__ == "__main__":
    main_menu()