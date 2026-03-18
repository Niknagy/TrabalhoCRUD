import os
from datetime import datetime
import models

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def exibir_cabecalho(titulo):
    print("=" * 60)
    print(f"{titulo:^60}")
    print("=" * 60)

def exibir_menu():
    print("\n===== SISTEMA DE CONTROLE DE TAREFAS =====")
    print("1. Adicionar tarefa")
    print("2. Listar todas as tarefas")
    print("3. Buscar tarefa por ID")
    print("4. Atualizar tarefa")
    print("5. Excluir tarefa")
    print("6. Sair")
    print("-" * 40)

def exibir_tarefa(tarefa):
    print(f"ID: {tarefa[0]}")
    print(f"Funcionário: {tarefa[1]}")
    print(f"Função: {tarefa[2]}")
    print(f"Local: {tarefa[3]}")
    print(f"Tarefa: {tarefa[4]}")
    print(f"Prioridade: {tarefa[5]}")
    print(f"Status: {tarefa[6]}")
    print(f"Início: {tarefa[7]}")
    print(f"Término: {tarefa[8]}")
    print(f"Responsável pelo registro: {tarefa[9]}")
    print(f"Data de criação: {tarefa[10]}")
    print("-" * 40)

def adicionar_tarefa():
    print("\n--- Nova Tarefa ---")
    funcionario = input("Funcionário: ").strip()
    funcao = input("Função: ").strip()
    local = input("Local: ").strip()
    tarefa = input("Tarefa: ").strip()
    prioridade = input("Prioridade (Alta/Média/Baixa): ").strip().capitalize()
    status = input("Status (Atribuída/Em andamento/Concluída/Não atribuída): ").strip()
    inicio = input("Início (AAAA-MM-DD HH:MM): ").strip()
    termino = input("Término (AAAA-MM-DD HH:MM): ").strip()
    responsavel = input("Responsável pelo registro: ").strip()
    
    data_criacao = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    if not all([funcionario, funcao, local, tarefa, prioridade, status, responsavel]):
        print("❌ Campos obrigatórios não preenchidos. Operação cancelada.")
        return
    
    dados = (funcionario, funcao, local, tarefa, prioridade, status,
             inicio, termino, responsavel, data_criacao)
    
    novo_id = models.inserir_tarefa(dados)
    print(f"✅ Tarefa adicionada com sucesso! ID: {novo_id}")

def listar_todas():
    tarefas = models.listar_tarefas()
    if not tarefas:
        print("\n📭 Nenhuma tarefa cadastrada.")
        return
    
    print(f"\n--- Total de tarefas: {len(tarefas)} ---")
    for tarefa in tarefas:
        exibir_tarefa(tarefa)

def buscar_por_id():
    try:
        id_tarefa = int(input("\nID da tarefa: ").strip())
    except ValueError:
        print("❌ ID inválido. Digite um número.")
        return
    
    tarefa = models.buscar_tarefa_por_id(id_tarefa)
    if tarefa:
        print("\n--- Tarefa encontrada ---")
        exibir_tarefa(tarefa)
    else:
        print(f"❌ Tarefa com ID {id_tarefa} não encontrada.")

def atualizar():
    try:
        id_tarefa = int(input("\nID da tarefa a ser atualizada: ").strip())
    except ValueError:
        print("❌ ID inválido.")
        return
    
    # Verifica se a tarefa existe
    tarefa = models.buscar_tarefa_por_id(id_tarefa)
    if not tarefa:
        print(f"❌ Tarefa com ID {id_tarefa} não encontrada.")
        return
    
    print("\n--- Dados atuais ---")
    exibir_tarefa(tarefa)
    
    print("\nCampos disponíveis para atualização:")
    print("1. Funcionário")
    print("2. Função")
    print("3. Local")
    print("4. Tarefa")
    print("5. Prioridade")
    print("6. Status")
    print("7. Início")
    print("8. Término")
    print("9. Responsável pelo registro")
    print("10. Data de criação")
    
    opcao = input("Escolha o número do campo que deseja alterar: ").strip()
    
    mapa_campos = {
        "1": "funcionario",
        "2": "funcao",
        "3": "local",
        "4": "tarefa",
        "5": "prioridade",
        "6": "status",
        "7": "inicio",
        "8": "termino",
        "9": "responsavel_registro",
        "10": "data_criacao"
    }
    
    if opcao not in mapa_campos:
        print("❌ Opção inválida.")
        return
    
    campo = mapa_campos[opcao]
    novo_valor = input(f"Novo valor para '{campo}': ").strip()
    
    if not novo_valor:
        print("❌ Valor não pode ser vazio.")
        return
    
    sucesso = models.atualizar_tarefa(id_tarefa, campo, novo_valor)
    if sucesso:
        print("✅ Tarefa atualizada com sucesso!")
    else:
        print("❌ Falha ao atualizar. Verifique se o campo é válido.")

def excluir():
    try:
        id_tarefa = int(input("\nID da tarefa a ser excluída: ").strip())
    except ValueError:
        print("❌ ID inválido.")
        return
    
    tarefa = models.buscar_tarefa_por_id(id_tarefa)
    if not tarefa:
        print(f"❌ Tarefa com ID {id_tarefa} não encontrada.")
        return
    
    print("\n--- Tarefa a ser excluída ---")
    exibir_tarefa(tarefa)
    
    confirmacao = input("Tem certeza que deseja excluir? (s/N): ").strip().lower()
    if confirmacao == 's':
        sucesso = models.excluir_tarefa(id_tarefa)
        if sucesso:
            print("✅ Tarefa excluída com sucesso!")
        else:
            print("❌ Falha ao excluir.")
    else:
        print("Operação cancelada.")

def main():    
    from database import criar_tabela
    criar_tabela()
    
    while True:
        limpar_tela()
        exibir_menu()
        opcao = input("Escolha uma opção: ").strip()
        
        if opcao == "1":
            adicionar_tarefa()
            input("\nPressione Enter para continuar...")
        elif opcao == "2":
            listar_todas()
            input("\nPressione Enter para continuar...")
        elif opcao == "3":
            buscar_por_id()
            input("\nPressione Enter para continuar...")
        elif opcao == "4":
            atualizar()
            input("\nPressione Enter para continuar...")
        elif opcao == "5":
            excluir()
            input("\nPressione Enter para continuar...")
        elif opcao == "6":
            print("Saindo do sistema... Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")
            input("\nPressione Enter para continuar...")

if __name__ == "__main__":
    main()
