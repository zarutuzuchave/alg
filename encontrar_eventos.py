from eventos_iniciais import eventos


def encontrar_evento(id_busca):
    """Retorna um evento pelo ID, ou None se não encontrado."""
    for evento in eventos:
        if evento['id'] == id_busca:
            return evento
    return None
