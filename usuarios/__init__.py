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

def inserir_usuario(usuario, lista_usuarios):
    lista_usuarios.append(usuario)

def ler_info_usuario():
    nome = input('Digite seu nome')
    email = input('digite seu e-mail')
    senha = input('digite sua senha')
    senha2 = input('Repita sua senha')

    return nome, email, senha, senha2