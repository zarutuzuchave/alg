from dados_iniciais import participantes
def adicionar_novo_participante(): 
    print("\n---- Adicionar Novo Partipante---- ")
    nome = input("Digite o nome do Participante: ")
    email = input("Digite o email do participante (Ex: 'alice.s@example.com'): ")
    evento_desejado = input("Digite o ID do evento (Ex: '1'; Workshop de Python para Iniciantes): ")

    # Gerar um novo ID para o evento (simplesmente pega o maior ID existente + 1)
    novo_id = max([i['id'] for i in participantes]) + 1 if participantes else 1

    novo_participante = {
        'id': novo_id,
        'nome': nome,
        'email': email,
        'evento_desejado': evento_desejado
    }
    participantes.append(novo_participante)
    print(f"Participante '{nome}' adicionado com sucesso ID: {novo_id}, Email:'{email}', Evento desejado: '{evento_desejado}'")
