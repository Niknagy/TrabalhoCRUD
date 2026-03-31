import customtkinter as ctk
import sqlite3
from tkinter import messagebox

# --- Configuração do Banco de Dados ---
def init_db():
    conn = sqlite3.connect('usuarios.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS usuarios 
                      (id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT, email TEXT)''')
    conn.commit()
    conn.close()

# --- Classe Principal do App ---
class CRUDApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Sistema CRUD Python")
        self.geometry("700x450")
        
        init_db()

        # Configuração de Grid
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # Barra Lateral
        self.sidebar = ctk.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar.grid(row=0, column=0, sticky="nsew")
        
        self.logo_label = ctk.CTkLabel(self.sidebar, text="Menu CRUD", font=ctk.CTkFont(size=20, weight="bold"))
        self.logo_label.pack(pady=20, padx=10)

        self.btn_create = ctk.CTkButton(self.sidebar, text="Cadastrar", command=self.show_create)
        self.btn_create.pack(pady=10, padx=10)

        self.btn_read = ctk.CTkButton(self.sidebar, text="Listar Usuários", command=self.show_read)
        self.btn_read.pack(pady=10, padx=10)

        # Container Principal
        self.main_frame = ctk.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.main_frame.grid(row=0, column=1, sticky="nsew", padx=20, pady=20)
        
        self.show_create()

    def clear_frame(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()

    def show_create(self):
        self.clear_frame()
        ctk.CTkLabel(self.main_frame, text="Cadastrar Novo Usuário", font=("Arial", 20)).pack(pady=10)
        
        nome_entry = ctk.CTkEntry(self.main_frame, placeholder_text="Nome Completo", width=300)
        nome_entry.pack(pady=10)
        
        email_entry = ctk.CTkEntry(self.main_frame, placeholder_text="E-mail", width=300)
        email_entry.pack(pady=10)

        def salvar():
            nome, email = nome_entry.get(), email_entry.get()
            if nome and email:
                conn = sqlite3.connect('usuarios.db')
                conn.execute("INSERT INTO usuarios (nome, email) VALUES (?, ?)", (nome, email))
                conn.commit()
                conn.close()
                messagebox.showinfo("Sucesso", "Usuário cadastrado!")
                nome_entry.delete(0, 'end')
                email_entry.delete(0, 'end')
            else:
                messagebox.showwarning("Erro", "Preencha todos os campos")

        ctk.CTkButton(self.main_frame, text="Salvar", fg_color="green", command=salvar).pack(pady=20)

    def show_read(self):
        self.clear_frame()
        ctk.CTkLabel(self.main_frame, text="Lista de Usuários", font=("Arial", 20)).pack(pady=10)

        scroll_frame = ctk.CTkScrollableFrame(self.main_frame, width=500, height=300)
        scroll_frame.pack(fill="both", expand=True)

        conn = sqlite3.connect('usuarios.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM usuarios")
        for row in cursor.fetchall():
            f = ctk.CTkFrame(scroll_frame)
            f.pack(fill="x", pady=5, padx=5)
            
            ctk.CTkLabel(f, text=f"ID: {row[0]} | {row[1]}").pack(side="left", padx=10)
            
            ctk.CTkButton(f, text="X", width=30, fg_color="red", command=lambda r=row[0]: self.delete_user(r)).pack(side="right", padx=5)
            ctk.CTkButton(f, text="Editar", width=60, command=lambda r=row: self.show_update(r)).pack(side="right", padx=5)
        conn.close()

    def show_update(self, user_data):
        self.clear_frame()
        ctk.CTkLabel(self.main_frame, text=f"Editar ID: {user_data[0]}", font=("Arial", 20)).pack(pady=10)
        
        nome_entry = ctk.CTkEntry(self.main_frame, width=300)
        nome_entry.insert(0, user_data[1])
        nome_entry.pack(pady=10)
        
        email_entry = ctk.CTkEntry(self.main_frame, width=300)
        email_entry.insert(0, user_data[2])
        email_entry.pack(pady=10)

        def atualizar():
            conn = sqlite3.connect('usuarios.db')
            conn.execute("UPDATE usuarios SET nome=?, email=? WHERE id=?", (nome_entry.get(), email_entry.get(), user_data[0]))
            conn.commit()
            conn.close()
            self.show_read()

        ctk.CTkButton(self.main_frame, text="Atualizar", command=atualizar).pack(pady=10)
        ctk.CTkButton(self.main_frame, text="Cancelar", fg_color="gray", command=self.show_read).pack()

    def delete_user(self, user_id):
        if messagebox.askyesno("Confirmar", "Deseja excluir este usuário?"):
            conn = sqlite3.connect('usuarios.db')
            conn.execute("DELETE FROM usuarios WHERE id=?", (user_id,))
            conn.commit()
            conn.close()
            self.show_read()

if __name__ == "__main__":
    app = CRUDApp()
    app.mainloop()
