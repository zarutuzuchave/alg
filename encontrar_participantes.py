from dados_iniciais import participantes

def encontrar_participante(id_busca):
    """Retorna um participante pelo ID, ou None se não encontrado."""
    for participante in participantes:
        if participante['id'] == id_busca:
            return participante
    return None