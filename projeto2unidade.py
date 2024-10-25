users = [['rene','rene@r','123'],['samuel','s@gm','456'],['jose','jose','444']]
events = []

def verificar_senha(senha1, senha2):
    if(senha1 == senha2):
        return True
    else:
        return False

def verificar_user_existente(email, usuarios):
    existe = False
    for user in usuarios:
        if(user[1] == email):
            existe = True
            break
    return existe

op = -1
while(op != 0):
    print('1-Cadastrar usuário')
    print('2-Login')
    print('0-Sair do programa')

    op = int(input('Digite a opçao desejada '))
    if(op == 1):
        nome = input('Digite seu nome')
        email = input('digite seu e-mail')
        senha = input('digite sua senha')
        senha2 = input('Repita sua senha')
        #verificar se este email já consta na lista de usuarios(def)
        #verificar se a senha1 é igual a senha2
        #inserir o novo usuário na lista

        while(verificar_user_existente(email, users)):
            email = input('digite novamente seu e-mail')

        while(not verificar_senha(senha, senha2)):
            print('dessa vez digite senhas iguais')
            senha = input('digite sua senha')
            senha2 = input('Repita sua senha')

        users.append([nome, email, senha])




