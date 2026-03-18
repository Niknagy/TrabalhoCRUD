from database import (
    atualizar_frete,
    buscar_frete_por_id,
    criar_frete,
    excluir_frete,
    init_db,
    listar_fretes,
)


def ler_int(texto: str) -> int:
    while True:
        try:
            return int(input(texto).strip())
        except ValueError:
            print("Digite um numero inteiro valido.")


def ler_float(texto: str) -> float:
    while True:
        valor = input(texto).strip().replace(",", ".")
        try:
            return float(valor)
        except ValueError:
            print("Digite um numero valido. Ex: 1500.75")


def inserir() -> None:
    print("\n--- Inserir Frete ---")
    caminhao = input("Caminhao: ").strip()
    motorista = input("Motorista: ").strip()
    origem = input("Origem: ").strip()
    destino = input("Destino: ").strip()
    carga = input("Carga: ").strip()
    valor = ler_float("Valor (R$): ")
    status = input("Status: ").strip()
    data_entrega = input("Data entrega (AAAA-MM-DD): ").strip()

    frete_id = criar_frete(
        caminhao,
        motorista,
        origem,
        destino,
        carga,
        valor,
        status,
        data_entrega,
    )
    print(f"Frete cadastrado. ID: {frete_id}")


def consultar() -> None:
    print("\n--- Consultar Fretes ---")
    fretes = listar_fretes()
    if not fretes:
        print("Nenhum frete cadastrado.")
        return

    for f in fretes:
        print(
            f"ID {f['id']} | {f['caminhao']} | {f['motorista']} | "
            f"{f['origem']} -> {f['destino']} | R$ {f['valor']:.2f} | "
            f"{f['status']} | {f['data_entrega']}"
        )


def excluir() -> None:
    print("\n--- Excluir Frete ---")
    frete_id = ler_int("ID do frete: ")
    frete = buscar_frete_por_id(frete_id)
    if not frete:
        print("Frete nao encontrado.")
        return

    confirma = input("Confirmar exclusao? (s/n): ").strip().lower()
    if confirma != "s":
        print("Cancelado.")
        return

    if excluir_frete(frete_id):
        print("Frete excluido com sucesso.")
    else:
        print("Nao foi possivel excluir.")


def atualizar() -> None:
    print("\n--- Atualizar Frete ---")
    frete_id = ler_int("ID do frete: ")
    frete = buscar_frete_por_id(frete_id)
    if not frete:
        print("Frete nao encontrado.")
        return

    caminhao = input(f"Caminhao [{frete['caminhao']}]: ").strip() or frete["caminhao"]
    motorista = input(f"Motorista [{frete['motorista']}]: ").strip() or frete["motorista"]
    origem = input(f"Origem [{frete['origem']}]: ").strip() or frete["origem"]
    destino = input(f"Destino [{frete['destino']}]: ").strip() or frete["destino"]
    carga = input(f"Carga [{frete['carga']}]: ").strip() or frete["carga"]

    valor_txt = input(f"Valor [{frete['valor']}]: ").strip().replace(",", ".")
    valor = float(valor_txt) if valor_txt else float(frete["valor"])

    status = input(f"Status [{frete['status']}]: ").strip() or frete["status"]
    data_entrega = input(f"Data entrega [{frete['data_entrega']}]: ").strip() or frete["data_entrega"]

    ok = atualizar_frete(
        frete_id,
        caminhao,
        motorista,
        origem,
        destino,
        carga,
        valor,
        status,
        data_entrega,
    )

    if ok:
        print("Frete atualizado com sucesso.")
    else:
        print("Nao foi possivel atualizar.")


def menu() -> None:
    while True:
        print("\n===== SISTEMINHA CRUD (TERMINAL) =====")
        print("1 - Inserir")
        print("2 - Consultar")
        print("3 - Excluir")
        print("4 - Atualizar")
        print("5 - Sair")

        opcao = input("Opcao: ").strip()

        if opcao == "1":
            inserir()
        elif opcao == "2":
            consultar()
        elif opcao == "3":
            excluir()
        elif opcao == "4":
            atualizar()
        elif opcao == "5":
            print("Encerrando.")
            break
        else:
            print("Opcao invalida.")


def main() -> None:
    init_db()
    menu()


if __name__ == "__main__":
    main()
