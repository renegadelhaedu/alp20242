import usuarios as usu
import Eventos as eve

nome = 'aa'
users ={'r':['rene','123'], 's@gm':['samuel','456']}
#users = [['rene','rene@r','123'],['samuel','s@gm','456'],['jose','jose','444']]
events = {'rar2024':['rock n rio 2024','s@gm', 100000, 3000]}

op = -1
while(op != 0):
    print('1-Cadastrar usuário')
    print('2-Login')
    print('0-Sair do programa')

    op = int(input('Digite a opçao desejada '))
    if(op == 1):
        nome, email, senha, senha2 = usu.ler_info_usuario()

        while(usu.verificar_user_existente(email, users)):
            email = input('digite novamente seu e-mail')

        while(not usu.verificar_senha(senha, senha2)):
            print('dessa vez digite senhas iguais')
            senha = input('digite sua senha')
            senha2 = input('Repita sua senha')

        novo_usuario = [nome, senha]
        usu.inserir_usuario(email, novo_usuario, users)

    elif op == 2:
        login = input('digite seu login/e-mail')
        senha = input('digite sua senha')

        if not usu.fazer_login(login, senha, users):
            print('Usuário ou senha inválidos')
        else:
            opmenu = -1
            while(op != 0):

                print('------- MENU--------')
                print('3-criar evento')
                print('4-buscar evento')
                print('5-listar eventos')

                opmenu = int(input('digite a opcao desejada'))
                if(opmenu == 3):
                    nome_even = input('qual o nome do evento')
                    codigo = input('qual o codigo do evento')
                    limite = int(input('qual o limite de pessoas'))
                    preco = float(input('qual o preco do ingresso'))

                    eve.criar_evento(codigo, nome_even, login, limite, preco, events)
                elif(opmenu == 5):
                    eve.listar_eventos(events)








