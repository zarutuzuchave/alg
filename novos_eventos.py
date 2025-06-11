from eventos_iniciais import eventos 

def adicionar_novo_evento(): 
    print("\n---- Adicionar Novos Eventos ---- ")
    nome = input("Digite o nome do evento: ").strip()
    data = input("Digite a data do evento (DD/MM/AAAA): ").strip()
    local = input("Digite o local do evento (Ex: Rua Banana, 450): ").strip()

    # Gerar um novo ID para o evento (simplesmente pega o maior ID existente + 1)
    novo_id = max([i['id'] for i in eventos]) + 1 if eventos else 1

    novo_evento = {
        'id': novo_id,
        'nome': nome,
        'data': data,
        'local': local
    }
    eventos.append(novo_evento)
    print(f"Evento '{nome}' adicionado com sucesso ID: {novo_id}")
