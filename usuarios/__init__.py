def verificar_senha(senha1, senha2):
    if(senha1 == senha2):
        return True
    else:
        return False

def verificar_user_existente(email, usuarios):
    existe = False
    for login in usuarios:
        if(login == email):
            existe = True
            break
    return existe

def inserir_usuario(login, usuario, usuarios):
    usuarios[login] = usuario

def ler_info_usuario():
    nome = input('Digite seu nome')
    email = input('digite seu e-mail')
    senha = input('digite sua senha')
    senha2 = input('Repita sua senha')

    return nome, email, senha, senha2

def fazer_login(login, senha, usuarios):
    logado = False
    for chave in usuarios:
        if(chave == login and usuarios[chave][1] == senha):
            logado = True
            break

    return logado

def adicionar_arquivo(nome, senha):
    arquivo = open('usuarios.txt','a')
    arquivo.write(f'{nome},{senha}\n')
    arquivo.close()

def login_arquivo(nome, senha):
    arquivo = open('usuarios.txt', 'r')
    linhas = arquivo.readlines()
    arquivo.close()
    for linha in linhas:
        mod = linha.replace('\n', '')
        nome_user = mod.split(',')[0]
        senha_user = mod.split(',')[1]
        if nome == nome_user and senha == senha_user:
            return True

    return False






