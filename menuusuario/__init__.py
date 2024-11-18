from Eventos import *

def menu_usuario(usuario):
    while True:
        print('\nMenu do Usuário')
        print('1 - Cadastrar Evento')
        print('2 - Buscar Evento')
        print('3 - Listar Eventos')
        print('4 - Remover Evento')
        print('5 - Participar de Evento')
        print('6 - Cancelar inscrição')
        print('7 - Listar Participantes do Evento')
        print('8 - Verificar valor arrecadado')
        print('9 - Doar para um evento')
        print('0 - Retornar ao Menu de acesso')
        opcao = input('Escolha uma opção: ')

        if opcao == '1':
            cadastrar_evento(usuario)
        if opcao == '2':
            buscar_evento()
        if opcao == '3':
            listar_eventos()
        if opcao == '4':
            remover_evento(usuario)
        if opcao == '5':
            participar_evento(usuario)
        if opcao == '6':
            cancelar_inscricao(usuario)
        if opcao == '7':
            listar_participantes(usuario)
        if opcao == '8':
            verificar_valor_arrecadao(usuario)
        if opcao == '9':
            doar_para_evento()
        if opcao == '0':
            break
