import sqlite3
from database import conectar, criar_tabela

#Operações CRUD

#Create
def cadastrar_tarefa(funcionario, tarefa, prioridade, status):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO tarefas (funcionario, tarefa, prioridade, status)
        VALUES (?, ?, ?, ?)
        ''', (funcionario, tarefa, prioridade, status))
    conn.commit()
    conn.close()
    print ("\n Tarefa cadastrada com sucesso!")

#READ
def listar_tarefas():
    conn = conectar ()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM tarefas')
    tarefas = cursor.fetchall()
    conn.close()

    print("\n--- Lista de Tarefas ---")
    if not tarefas:
        print("Nenhuma tarefa encontrada")
    else:
        for t in tarefas:
            print(f"ID: {t[0]} | Funcionario: {t[1]} | Tarefa: {t[2]} | Prioridade: {t[3]} | Status: {t[4]}")
            print("--------------------------")
 
#UPDATE
def atualizar_status(id_tarefa, novo_status):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE tarefas SET status = ? WHERE id = ?
        ''', (novo_status, id_tarefa))
    conn.commit()
    conn.close()
    print("\n Status atualizado com sucesso!")

#DELETE
def excluir_tarefa(id_tarefa):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM tarefas WHERE id = ?', (id_tarefa,))
    conn.commit()
    conn.close()
    print("\n Tarefa excluida com sucesso!")


#MENU INTERATIVO

def menu():
    criar_tabela() #Garante que a tabela existe antes de começar.and

    while True:
        print("\n=== Sistema de Controle de Tarefas ===")
        print("1. Cadastrar nova tarefa (CREATE)")
        print("2. Listar tarefas (READ)")
        print("3. Atualizar status da tarefa (UPDATE)")
        print("4. Excluir tarefa (DELETE)")
        print("5. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            func = input("Nome do funcionario: ")
            tar = input("Descrição da tarefa: ")
            prio = input("Prioridade (Ex: Alta, Média, Baixa): ")
            stat = input("Status (Ex: Não atribuída, Em andamento, Concluída): ")
            cadastrar_tarefa(func, tar, prio, stat)
        
        elif opcao == '2':
            listar_tarefas()
        
        elif opcao == '3':
            listar_tarefas()
            id_t = int(input("Difite o ID da tarefa que deseja atualizar: "))
            novo_stat = input("Digite o novo status: ")
            atualizar_status(id_t, novo_stat)

        elif opcao == '4':
            listar_tarefas()
            id_t = int(input("Digite o ID da tarefa que deseja excluir: "))
            excluir_tarefa(id_t)

        elif opcao =='5':
            print("Saindo do sistema...")
            break
        else:  
            print("Opção inválida. Tente novamente.")

if __name__ == '__main__':
    menu()