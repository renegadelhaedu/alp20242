
def cadastrar_usuario(usuarios):
    print("Cadastro de Usuário")
    nome = input("Nome: ")
    email = input("E-mail: ")
    senha = input("Senha: ")
    confirma_senha = input("Confirme a Senha: ")

    if senha != confirma_senha:
        print("Senhas não conferem.")
        return usuarios

    for usuario in usuarios:
        if usuario[1] == email:
            print("E-mail já cadastrado.")
            return usuarios

    usuarios.append([nome, email, senha])
    print("Usuário cadastrado com sucesso.")
    return usuarios

def login(usuarios):
    print("Login")
    email = input("E-mail: ")
    senha = input("Senha: ")

    for usuario in usuarios:
        if usuario[1] == email and usuario[2] == senha:
            print(f"Bem-vindo, {usuario[0]}!")
            return usuario
    print("E-mail ou senha inválidos.")
    return None

def cadastrar_evento(eventos, login_usuario):
    print("Cadastro de Evento")
    titulo = input("Título do Evento: ")
    descricao = input("Descrição: ")
    data = input("Data (DD/MM/AAAA): ")
    local = input("Local: ")
    valor_inscricao = float(input("Valor de Inscrição: "))

    # Estrutura do evento: [criador, título, descrição, data, local, valor_inscricao, participantes]
    evento = [
        login_usuario[1],  # e-mail do criador
        titulo,
        descricao,
        data,
        local,
        valor_inscricao,
        []  # lista de participantes
    ]
    eventos.append(evento)
    print("Evento cadastrado com sucesso.")
    return eventos

def buscar_evento(eventos):
    nome = input("Digite o nome do evento para buscar: ")
    for evento in eventos:
        if nome.lower() in evento[1].lower():  # Título do evento está no índice 1
            print(f"Título: {evento[1]}, Data: {evento[3]}, Local: {evento[4]}, Valor: {evento[5]}")

def listar_eventos(eventos, login_usuario):
    print("Eventos Cadastrados:")
    for evento in eventos:
        if evento[0] == login_usuario[1]:  # Criador do evento está no índice 0
            print(f"Título: {evento[1]}, Data: {evento[3]}, Local: {evento[4]}, Valor: {evento[5]}")

def remover_evento(eventos, login_usuario):
    nome_evento = input("Nome do evento para remover: ")
    for evento in eventos:
        if evento[1] == nome_evento and evento[0] == login_usuario[1]:  # Índice 1 é o título, 0 é o criador
            confirmacao = input("Tem certeza que deseja remover o evento? (s/n): ")
            if confirmacao.lower() == 's':
                eventos.remove(evento)
                print("Evento removido com sucesso.")
            else:
                print("Remoção cancelada.")
            return eventos
    print("Evento não encontrado ou você não tem permissão para removê-lo.")
    return eventos

def participar_evento(eventos, login_usuario):
    nome_evento = input("Digite o nome do evento para se inscrever: ")
    for evento in eventos:
        if evento[1] == nome_evento:  # Índice 1 é o título
            evento[6].append(login_usuario[1])  # Índice 6 é a lista de participantes
            print("Inscrição realizada com sucesso.")
            return eventos
    print("Evento não encontrado.")
    return eventos

def listar_participantes(eventos, login_usuario):
    nome_evento = input("Digite o nome do evento para listar participantes: ")
    for evento in eventos:
        if evento[1] == nome_evento and evento[0] == login_usuario[1]:  # Índices 1 e 0 para título e criador
            print("Participantes do evento:")
            for participante in evento[6]:  # Índice 6 é a lista de participantes
                print(participante)
            return
    print("Evento não encontrado ou você não tem permissão para visualizar os participantes.")

def verificar_valor_arrecadado(eventos, login_usuario):
    nome_evento = input("Digite o nome do evento para verificar arrecadação: ")
    for evento in eventos:
        if evento[1] == nome_evento and evento[0] == login_usuario[1]:  # Índices 1 e 0 para título e criador
            total = len(evento[6]) * evento[5]  # Índice 6 é a lista de participantes, 5 é o valor de inscrição
            print(f"Número de inscritos: {len(evento[6])}")
            print(f"Total arrecadado: R${total:.2f}")
            return
    print("Evento não encontrado ou você não tem permissão para visualizar a arrecadação.")


