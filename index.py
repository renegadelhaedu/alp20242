from auth import *
from menuusuario import *
users = [['Rene', 'rene@', '123']]


def menu_login():
    while True:
        print('1-Cadastrar usuário')
        print('2-Login')
        print('0-Sair do programa')

        op = input('Digite a opção desejada: ')
        if op == '1':
            nome = input('Digite seu nome: ')
            email = input('Digite seu e-mail: ')
            while not verificar_email(email):
                print("Certifique-se de digitar um email válido com '@' e '.com'")
                email = input("Digite novamente seu e-mail: ")
            while verificar_user_existente(email, users):
                email = input('E-mail já cadastrado. Digite novamente seu e-mail: ')
            print("Email válido.")

            senha = input('Digite sua senha: ')
            senha2 = input('Repita sua senha: ')
            while not verificar_senha(senha, senha2):
                print('Senhas diferentes. Tente novamente.')
                senha = input('Digite sua senha: ')
                senha2 = input('Repita sua senha: ')

            print('Usuário cadastrado com sucesso')
            users.append([nome, email, senha])

        elif op == '2':
            email = input('Digite o seu email: ')
            senha = input('Digite a sua senha: ')

            usuario = verificar_login(email, senha, users)
            if usuario:
                menu_usuario(usuario)

        elif op == '0':
            print('_______________________\n'
                  'See you soon\n'
                  '_______________________')
            break
        else:
            print('INSIRA UMA OPÇÃO VÁLIDA')


if __name__ == '__main__':
    menu_login()
