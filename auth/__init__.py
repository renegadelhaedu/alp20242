def verificar_senha(senha1, senha2):
    if senha1 == senha2:
        return True
    else:
        return False


def verificar_user_existente(email, usuarios):
    existe = False
    for user in usuarios:
        if user[1] == email:
            existe = True
            break
    return existe


def verificar_email(email):
    return '@' in email and '.com' in email


def verificar_login(email, senha, users):
    for usuario in users:
        if usuario[1] == email and usuario[2] == senha:
            print(f'Login realizado com sucesso\n'
                  f'___________________________\n'
                  f'Seja bem-vindo {usuario[0]}!')
            return usuario
    print('Verifique o login')
    return False
