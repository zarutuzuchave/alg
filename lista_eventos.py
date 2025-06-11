from eventos_iniciais import eventos

def listar_todos_eventos():
    evento = print("\n--- TODOS OS EVENTOS ---")
    if not eventos:
        print("Nenhum evento cadastrado.")
        return evento

    for evento in eventos:
        print(f"ID: {evento['id']} | Nome: {evento['nome']} | Data: {evento['data']} | Local: {evento['local']}")
    print("------------------------")
    return evento
