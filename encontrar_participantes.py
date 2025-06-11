from dados_iniciais import participantes
import main

def encontrar_participante(id_busca, lista_participantes):
    
    for participante in lista_participantes:
        if participante['id'] == id_busca:
            return participante
     #se a func terminar sem encontrar nada ele vai retornar None
    return None



# 1. pedir o ID pro usuário
try:
    id_desejado_str = input("Digite o ID do participante desejado: ")
    id_desejado = int(id_desejado_str) 
except ValueError:
    print("ID inválido. Por favor, digite um número inteiro.")
    id_desejado = None # se ele digitar um id nao correspondente ele retorna none 

# se o id for valido ele vai chamar a funcao 
if id_desejado is not None:
    participante_encontrado = encontrar_participante(id_desejado, participantes)

    # 3. printar o resultado 
    if participante_encontrado:
        print(f"\nParticipante encontrado:")
        for key, value in participante_encontrado.items():
            print(f"  {key.capitalize()}: {value}") #captalize ele aumenta a primeira letra do id
    else:
        print(f"\nParticipante com ID {id_desejado} não encontrado.")
