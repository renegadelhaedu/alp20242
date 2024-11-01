import usuarios as usu
import eventos as ev

nome = 'aa'

users = [['rene','rene@r','123'],['samuel','s@gm','456'],['jose','jose','444']]
events = []

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

        novo_usuario = [nome, email, senha]
        usu.inserir_usuario(novo_usuario, users)




