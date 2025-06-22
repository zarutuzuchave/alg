import os

def criar_arquivo(caminho, conteudo):
    """Cria um arquivo com o conteúdo especificado."""
    os.makedirs(os.path.dirname(caminho), exist_ok=True)
    with open(caminho, 'w', encoding='utf-8') as f:
        f.write(conteudo)

def criar_estrutura_projeto():
    """Cria a estrutura de pastas e arquivos do projeto."""
    diretorio_base = "Filipe Silva"

    print(f"Criando a estrutura do projeto em '{diretorio_base}/'...")

    # Conteúdo dos arquivos (string pura)
    main_py_conteudo = """
from menus.menu_principal import executar_menu_principal

if __name__ == "__main__":
    executar_menu_principal()
"""

    dados_eventos_py_conteudo = """
eventos = [
    {
        'nome': 'Workshop de Fundamentos de Python',
        'data': '2025-07-10',
        'tema': 'Web',
        'participantes': ['P001', 'P002', 'P003', 'P005']
    },
    {
        'nome': 'Seminário de IA na Saúde',
        'data': '2025-07-15',
        'tema': 'Inteligência Artificial',
        'participantes': ['P001', 'P004', 'P006']
    },
    {
        'nome': 'Fundamentos de Cibersegurança',
        'data': '2025-07-20',
        'tema': 'Segurança',
        'participantes': ['P002', 'P005']
    },
    {
        'nome': 'Bootcamp de Desenvolvimento Web',
        'data': '2025-08-01',
        'tema': 'Web',
        'participantes': ['P001', 'P003', 'P004', 'P007']
    },
    {
        'nome': 'Meetup de Ciência de Dados',
        'data': '2025-08-05',
        'tema': 'Inteligência Artificial',
        'participantes': ['P002', 'P006', 'P008']
    },
    {
        'nome': 'Essenciais de Redes',
        'data': '2025-08-10',
        'tema': 'Segurança',
        'participantes': ['P009']
    }
]
"""

    dados_participantes_py_conteudo = """
participantes = [
    {
        'codigo': 'P001',
        'nome_completo': 'Alice Silva',
        'email': 'alice.s@example.com',
        'preferencias_tematicas': ['Web', 'Inteligência Artificial']
    },
    {
        'codigo': 'P002',
        'nome_completo': 'Bruno Costa',
        'email': 'bruno.c@example.com',
        'preferencias_tematicas': ['Segurança', 'Web']
    },
    {
        'codigo': 'P003',
        'nome_completo': 'Carlos Oliveira',
        'email': 'carlos.o@example.com',
        'preferencias_tematicas': ['Web']
    },
    {
        'codigo': 'P004',
        'nome_completo': 'Diana Santos',
        'email': 'diana.s@example.com',
        'preferencias_tematicas': ['Inteligência Artificial', 'Web']
    },
    {
        'codigo': 'P005',
        'nome_completo': 'Eduarda Almeida',
        'email': 'eduarda.a@example.com',
        'preferencias_tematicas': ['Segurança', 'Web']
    },
    {
        'codigo': 'P006',
        'nome_completo': 'Felipe Rocha',
        'email': 'felipe.r@example.com',
        'preferencias_tematicas': ['Inteligência Artificial']
    },
    {
        'codigo': 'P007',
        'nome_completo': 'Giovana Souza',
        'email': 'giovana.s@example.com',
        'preferencias_tematicas': ['Web']
    },
    {
        'codigo': 'P008',
        'nome_completo': 'Hugo Fernandes',
        'email': 'hugo.f@example.com',
        'preferencias_tematicas': ['Inteligência Artificial']
    },
    {
        'codigo': 'P009',
        'nome_completo': 'Isabela Gomes',
        'email': 'isabela.g@example.com',
        'preferencias_tematicas': ['Segurança']
    },
    {
        'codigo': 'P001',
        'nome_completo': 'Alice Silva Duplicada',
        'email': 'alice.dup@example.com',
        'preferencias_tematicas': ['Web']
    }
]
"""

    init_py_conteudo = "" # Conteúdo vazio para __init__.py

    menu_principal_py_conteudo = """
import dados_eventos
import dados_participantes
from menus.menu_eventos import executar_menu_gerenciar_eventos
from menus.menu_participantes import executar_menu_gerenciar_participantes
from menus.menu_relatorios import executar_menu_relatorios
import gerenciador_eventos.funcoes_eventos as GerenciadorEventos

def executar_menu_principal():

    opcoes_menu = {
        '1': ("Ver Eventos", lambda: GerenciadorEventos.mostrar_eventos(dados_eventos.eventos)),
        '2': ("Gerenciar Eventos", lambda: executar_menu_gerenciar_eventos(dados_eventos.eventos, dados_participantes.participantes)),
        '3': ("Gerenciar Participantes", lambda: executar_menu_gerenciar_participantes(dados_eventos.eventos, dados_participantes.participantes)),
        '4': ("Relatórios e Estatísticas", lambda: executar_menu_relatorios(dados_eventos.eventos, dados_participantes.participantes)),
        '5': ("Sair", None)
    }

    while True:
        print("\\n--- Sistema de Gerenciamento de Eventos ---")
        for chave, (descricao, _) in opcoes_menu.items():
            print(f"{chave}. {descricao}")

        escolha = input("Digite sua escolha: ")

        acao = opcoes_menu.get(escolha)
        if acao:
            descricao, funcao = acao
            if funcao:
                funcao()
            else:
                print("Saindo do sistema. Até logo!")
                break
        else:
            print("Escolha inválida. Por favor, tente novamente.")
"""

    menu_eventos_py_conteudo = """
import gerenciador_eventos.funcoes_eventos as GerenciadorEventos

def executar_menu_gerenciar_eventos(eventos, dados_participantes):

    def _adicionar_evento():
        nome = input("Nome do evento: ")
        data = input("Data do evento (AAAA-MM-DD): ")
        tema = input("Tema do evento: ")
        GerenciadorEventos.adicionar_evento(eventos, nome, data, tema)

    def _remover_evento():
        nome_evento = input("Nome do evento para remover: ")
        GerenciadorEventos.remover_evento(eventos, nome_evento)

    def _atualizar_tema():
        nome_evento = input("Nome do evento para atualizar o tema: ")
        novo_tema = input("Novo tema: ")
        GerenciadorEventos.atualizar_tema_evento(eventos, nome_evento, novo_tema)

    def _agrupar():
        agrupados = GerenciadorEventos.agrupar_eventos_por_tema(eventos)
        for tema, lista_eventos in agrupados.items():
            print(f"\\nTema: {tema}")
            for evento in lista_eventos:
                print(f"  - {evento['nome']} em {evento['data']}")

    def _listar_por_participante():
        codigo_participante = input("Digite o código do participante: ")
        eventos_inscritos = GerenciadorEventos.listar_eventos_por_participante(eventos, codigo_participante)
        if eventos_inscritos:
            print(f"\\nEventos em que {codigo_participante} está inscrito:")
            for nome_evento in eventos_inscritos:
                print(f"- {nome_evento}")
        else:
            print(f"O participante {codigo_participante} não está inscrito em nenhum evento ou não existe.")

    def _identificar_baixa_participacao():
        eventos_com_pouca_participacao = GerenciadorEventos.identificar_eventos_baixa_participacao(eventos)
        if eventos_com_pouca_participacao:
            print("\\nEventos com baixa participação (menos de 2 participantes):")
            for nome_evento in eventos_com_pouca_participacao:
                print(f"- {nome_evento}")
        else:
            print("Nenhum evento com baixa participação encontrado.")

    opcoes_menu = {
        '1': ("Adicionar Novo Evento", _adicionar_evento),
        '2': ("Remover Evento", _remover_evento),
        '3': ("Atualizar Tema do Evento", _atualizar_tema),
        '4': ("Agrupar Eventos por Tema", _agrupar),
        '5': ("Listar Eventos por Participante", _listar_por_participante),
        '6': ("Identificar Eventos com Baixa Participação", _identificar_baixa_participacao),
        '7': ("Voltar ao Menu Principal", None)
    }

    while True:
        print("\\n--- Gerenciar Eventos ---")
        for chave, (descricao, _) in opcoes_menu.items():
            print(f"{chave}. {descricao}")

        escolha = input("Digite sua escolha: ")

        acao = opcoes_menu.get(escolha)
        if acao:
            _descricao, funcao = acao
            if funcao:
                funcao()
            else:
                break
        else:
            print("Escolha inválida. Por favor, tente novamente.")
"""

    menu_participantes_py_conteudo = """
import gerenciador_participantes.funcoes_participantes as GerenciadorParticipantes

def executar_menu_gerenciar_participantes(eventos, dados_participantes):

    def _listar_em_evento():
        nome_evento = input("Digite o nome do evento: ")
        GerenciadorParticipantes.mostrar_participantes_em_evento(eventos, dados_participantes, nome_evento)

    def _buscar_participante():
        codigo_participante = input("Digite o código do participante: ")
        GerenciadorParticipantes.buscar_participante(dados_participantes, codigo_participante)

    def _atualizar_email():
        codigo_participante = input("Digite o código do participante: ")
        novo_email = input("Digite o novo e-mail: ")
        GerenciadorParticipantes.atualizar_email_participante(dados_participantes, codigo_participante, novo_email)

    def _remover_duplicados():
        dados_participantes[:] = GerenciadorParticipantes.remover_participantes_duplicados(dados_participantes)

    opcoes_menu = {
        '1': ("Listar Participantes em um Evento", _listar_em_evento),
        '2': ("Buscar Participante por Código", _buscar_participante),
        '3': ("Atualizar E-mail do Participante", _atualizar_email),
        '4': ("Remover Participantes Duplicados", _remover_duplicados),
        '5': ("Voltar ao Menu Principal", None)
    }

    while True:
        print("\\n--- Gerenciar Participantes ---")
        for chave, (descricao, _) in opcoes_menu.items():
            print(f"{chave}. {descricao}")

        escolha = input("Digite sua escolha: ")

        acao = opcoes_menu.get(escolha)
        if acao:
            _descricao, funcao = acao
            if funcao:
                funcao()
            else:
                break
        else:
            print("Escolha inválida. Por favor, tente novamente.")
"""

    menu_relatorios_py_conteudo = """
import relatorios.funcoes_relatorios as FuncoesRelatorios

def executar_menu_relatorios(eventos, dados_participantes):

    def _participantes_ativos():
        FuncoesRelatorios.obter_participantes_mais_ativos(eventos, dados_participantes)

    def _temas_frequentes():
        FuncoesRelatorios.obter_temas_mais_frequentes(eventos)

    def _contar_eventos_por_tema():
        contagem_temas = FuncoesRelatorios.contar_eventos_por_tema(eventos)
        print("\\nEventos por Tema:")
        for tema, contagem in contagem_temas.items():
            print(f"- {tema}: {contagem} eventos")

    def _media_participacao():
        taxas_medias = FuncoesRelatorios.calcular_media_participacao_por_tema(eventos)
        print("\\nTaxa Média de Participação por Tema:")
        for tema, taxa in taxas_medias.items():
            print(f"- {tema}: {taxa:.2f} participantes por evento")

    def _relatorio_baixa_participacao():
        eventos_com_pouca_participacao = FuncoesRelatorios.relatorio_eventos_baixa_participacao(eventos)
        if eventos_com_pouca_participacao:
            print("\\nRelatório de Eventos com Baixa Participação:")
            for nome_evento in eventos_com_pouca_participacao:
                print(f"- {nome_evento}")
        else:
            print("Nenhum evento com baixa participação para relatar.")

    opcoes_menu = {
        '1': ("Participantes Mais Ativos", _participantes_ativos),
        '2': ("Temas Mais Frequentes", _temas_frequentes),
        '3': ("Contar Eventos por Tema", _contar_eventos_por_tema),
        '4': ("Taxa Média de Participação por Tema", _media_participacao),
        '5': ("Eventos com Baixa Participação (Relatório)", _relatorio_baixa_participacao),
        '6': ("Voltar ao Menu Principal", None)
    }

    while True:
        print("\\n--- Relatórios e Estatísticas ---")
        for chave, (descricao, _) in opcoes_menu.items():
            print(f"{chave}. {descricao}")

        escolha = input("Digite sua escolha: ")

        acao = opcoes_menu.get(escolha)
        if acao:
            _descricao, funcao = acao
            if funcao:
                funcao()
            else:
                break
        else:
            print("Escolha inválida. Por favor, tente novamente.")
"""

    funcoes_eventos_py_conteudo = """
from collections import defaultdict

def mostrar_eventos(eventos):
    if not eventos:
        print("Nenhum evento para exibir.")
        return

    print("\\n--- Todos os Eventos ---")
    for evento in eventos:
        print(f"Nome: {evento['nome']}")
        print(f"Data: {evento['data']}")
        print(f"Tema: {evento['tema']}")
        print("-" * 20)

def adicionar_evento(eventos, nome, data, tema, participantes=None):
    if any(evento['nome'] == nome for evento in eventos):
        print(f"Erro: Um evento com o nome '{nome}' já existe.")
        return

    novo_evento = {
        'nome': nome,
        'data': data,
        'tema': tema,
        'participantes': participantes if participantes is not None else []
    }
    eventos.append(novo_evento)
    print(f"Evento '{nome}' adicionado com sucesso.")

def remover_evento(eventos, nome_evento):
    tamanho_original = len(eventos)
    eventos[:] = list(filter(lambda evento: evento['nome'] != nome_evento, eventos))
    if len(eventos) < tamanho_original:
        print(f"Evento '{nome_evento}' removido com sucesso.")
        return True
    else:
        print(f"Evento '{nome_evento}' não encontrado.")
        return False

def atualizar_tema_evento(eventos, nome_evento, novo_tema):
    for evento in eventos:
        if evento['nome'] == nome_evento:
            evento['tema'] = novo_tema
            print(f"Tema para o evento '{nome_evento}' atualizado para '{novo_tema}'.")
            return True
    print(f"Evento '{nome_evento}' não encontrado.")
    return False

def agrupar_eventos_por_tema(eventos):
    agrupados = defaultdict(list)
    for evento in eventos:
        agrupados[evento['tema']].append(evento)
    return dict(agrupados)

def listar_eventos_por_participante(eventos, codigo_participante):
    eventos_inscritos = [
        evento['nome'] for evento in eventos
        if 'participantes' in evento and codigo_participante in evento['participantes']
    ]
    return eventos_inscritos

def identificar_eventos_baixa_participacao(eventos, min_participantes=2):
    eventos_com_pouca_participacao = [
        evento['nome'] for evento in eventos
        if 'participantes' in evento and len(evento['participantes']) < min_participantes
    ]
    return eventos_com_pouca_participacao
"""

    funcoes_participantes_py_conteudo = """
def mostrar_participantes_em_evento(eventos, dados_participantes, nome_evento):
    evento_encontrado = False
    for evento in eventos:
        if evento['nome'] == nome_evento:
            evento_encontrado = True
            print(f"\\n--- Participantes em {nome_evento} ---")
            if 'participantes' in evento and evento['participantes']:
                codigos_participantes_evento = set(evento['participantes'])
                participantes_do_evento = list(filter(
                    lambda p: p['codigo'] in codigos_participantes_evento,
                    dados_participantes
                ))
                if participantes_do_evento:
                    for participante in participantes_do_evento:
                        print(f"Código: {participante['codigo']}, Nome: {participante['nome_completo']}, E-mail: {participante['email']}")
                else:
                    print("Nenhum participante registrado para este evento.")
            else:
                print("Nenhum participante registrado para este evento.")
            break
    if not evento_encontrado:
        print(f"Evento '{nome_evento}' não encontrado.")

def buscar_participante(participantes, codigo_participante):
    encontrado = next(filter(lambda p: p['codigo'] == codigo_participante, participantes), None)
    if encontrado:
        print(f"\\n--- Participante Encontrado ---")
        print(f"Código: {encontrado['codigo']}")
        print(f"Nome: {encontrado['nome_completo']}")
        print(f"E-mail: {encontrado['email']}")
        print(f"Preferências: {encontrado['preferencias_tematicas']}")
    else:
        print(f"Participante com o código '{codigo_participante}' não encontrado.")
    return encontrado

def atualizar_email_participante(participantes, codigo_participante, novo_email):
    for participante in participantes:
        if participante['codigo'] == codigo_participante:
            participante['email'] = novo_email
            print(f"E-mail do participante '{codigo_participante}' atualizado para '{novo_email}'.")
            return True
    print(f"Participante com o código '{codigo_participante}' não encontrado.")
    return False

def remover_participantes_duplicados(participantes):
    codigos_vistos = set()
    participantes_unicos = []
    contador_removidos = 0

    for participante in participantes:
        if participante['codigo'] not in codigos_vistos:
            participantes_unicos.append(participante)
            codigos_vistos.add(participante['codigo'])
        else:
            contador_removidos += 1
            print(f"Participante duplicado encontrado e removido: Código {participante['codigo']}")

    if contador_removidos > 0:
        print(f"Removido(s) {contador_removidos} registro(s) duplicado(s) de participante.")
    else:
        print("Nenhum participante duplicado encontrado.")
    return participantes_unicos
"""

    funcoes_relatorios_py_conteudo = """
from collections import Counter, defaultdict
from functools import reduce

def obter_participantes_mais_ativos(eventos, dados_participantes, top_n=5):
    todos_codigos_participantes = []
    for evento in eventos:
        if 'participantes' in evento:
            todos_codigos_participantes.extend(evento['participantes'])

    contagem_participantes = Counter(todos_codigos_participantes)
    mapa_nomes_participantes = {p['codigo']: p['nome_completo'] for p in dados_participantes}

    participantes_ativos = [
        (mapa_nomes_participantes.get(codigo, f"Desconhecido ({codigo})"), contagem)
        for codigo, contagem in contagem_participantes.items()
    ]
    participantes_ativos.sort(key=lambda x: x[1], reverse=True)

    print("\\n--- Participantes Mais Ativos ---")
    for nome, contagem in participantes_ativos[:top_n]:
        print(f"- {nome}: {contagem} eventos")

    return participantes_ativos[:top_n]

def obter_temas_mais_frequentes(eventos, top_n=5):
    todos_temas = [evento['tema'] for evento in eventos if 'tema' in evento]
    contagem_temas = Counter(todos_temas)
    temas_frequentes = sorted(contagem_temas.items(), key=lambda item: item[1], reverse=True)

    print("\\n--- Temas Mais Frequentes ---")
    for tema, contagem in temas_frequentes[:top_n]:
        print(f"- {tema}: {contagem} eventos")

    return temas_frequentes[:top_n]

def contar_eventos_por_tema(eventos):
    contagem_temas = reduce(
        lambda acumulador, evento: {**acumulador, evento['tema']: acumulador.get(evento['tema'], 0) + 1},
        eventos,
        {}
    )
    return contagem_temas

def calcular_media_participacao_por_tema(eventos):
    somas_participacao_tema = defaultdict(int)
    contagem_eventos_tema = defaultdict(int)

    for evento in eventos:
        tema = evento.get('tema')
        participantes = evento.get('participantes', [])
        if tema:
            somas_participacao_tema[tema] += len(participantes)
            contagem_eventos_tema[tema] += 1

    media_taxas_participacao = {
        tema: somas_participacao_tema[tema] / contagem_eventos_tema[tema]
        for tema in contagem_eventos_tema
    }
    return media_taxas_participacao

def relatorio_eventos_baixa_participacao(eventos, min_participantes=2):
    eventos_com_pouca_participacao = []
    for evento in eventos:
        if 'participantes' in evento and len(evento['participantes']) < min_participantes:
            eventos_com_pouca_participacao.append(evento['nome'])
    return eventos_com_pouca_participacao
"""

    # Mapeamento de caminhos e conteúdos
    arquivos_e_conteudos = {
        f"{diretorio_base}/main.py": main_py_conteudo,
        f"{diretorio_base}/dados_eventos.py": dados_eventos_py_conteudo,
        f"{diretorio_base}/dados_participantes.py": dados_participantes_py_conteudo,

        f"{diretorio_base}/menus/__init__.py": init_py_conteudo,
        f"{diretorio_base}/menus/menu_principal.py": menu_principal_py_conteudo,
        f"{diretorio_base}/menus/menu_eventos.py": menu_eventos_py_conteudo,
        f"{diretorio_base}/menus/menu_participantes.py": menu_participantes_py_conteudo,
        f"{diretorio_base}/menus/menu_relatorios.py": menu_relatorios_py_conteudo,

        f"{diretorio_base}/gerenciador_eventos/__init__.py": init_py_conteudo,
        f"{diretorio_base}/gerenciador_eventos/funcoes_eventos.py": funcoes_eventos_py_conteudo,

        f"{diretorio_base}/gerenciador_participantes/__init__.py": init_py_conteudo,
        f"{diretorio_base}/gerenciador_participantes/funcoes_participantes.py": funcoes_participantes_py_conteudo,

        f"{diretorio_base}/relatorios/__init__.py": init_py_conteudo,
        f"{diretorio_base}/relatorios/funcoes_relatorios.py": funcoes_relatorios_py_conteudo,
    }

    for caminho, conteudo in arquivos_e_conteudos.items():
        criar_arquivo(caminho, conteudo)
        print(f"  Criado: {caminho}")

    print("\nEstrutura do projeto criada com sucesso!")

if __name__ == "__main__":
    criar_estrutura_projeto()
