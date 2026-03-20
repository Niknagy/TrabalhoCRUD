import crud

tasks = crud.get_all_tasks()
if tasks:
    print("Tarefas no sistema:")
    for t in tasks:
        print(f"ID: {t[0]}, Funcionário: {t[1]}, Função: {t[2]}, Local: {t[3]}, Tarefa: {t[4]}, Prioridade: {t[5]}, Status: {t[6]}, Início: {t[7]}, Fim: {t[8]}, Responsável: {t[9]}, Criado: {t[10]}")
else:
    print("Nenhuma tarefa encontrada.")