import funcoes_eventos as fe

# Menu Principal --- CODE PRINCIPAL
usuarios = []
eventos = []
login_usuario = None

while True:
    print("\nMENU PRINCIPAL")
    print("1 - Cadastro de Usuário")
    print("2 - Login")
    print("3 - Cadastro de Evento")
    print("4 - Buscar Evento")
    print("5 - Listar Eventos")
    print("6 - Remover Evento")
    print("7 - Participar de Evento")
    print("8 - Listar Participantes do Evento")
    print("9 - Verificar Valor Arrecadado")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        usuarios = fe.cadastrar_usuario(usuarios)
    elif opcao == "2":
        login_usuario = fe.login(usuarios)
    elif opcao == "3" and login_usuario:
        fe.cadastrar_evento(eventos, login_usuario)
    elif opcao == "4" and login_usuario:
        fe.buscar_evento(eventos)
    elif opcao == "5" and login_usuario:
        fe.listar_eventos(eventos, login_usuario)
    elif opcao == "6" and login_usuario:
        eventos = fe.remover_evento(eventos, login_usuario)
    elif opcao == "7" and login_usuario:
        eventos = fe.participar_evento(eventos, login_usuario)
    elif opcao == "8" and login_usuario:
        fe.listar_participantes(eventos, login_usuario)
    elif opcao == "9" and login_usuario:
        fe.verificar_valor_arrecadado(eventos, login_usuario)
    elif opcao == "0":
        print("Saindo do sistema.")
        break
    else:
        if not login_usuario and opcao in ["3", "4", "5", "6", "7", "8", "9"]:
            print("Por favor, faça login para acessar essa opção.")
        else:
            print("Opção inválida.")
