#funções em python
#são blocos de código nomeados e que podem ser chamados durante o programa

#criar funçoes com parâmetros

def saudar_pessoa(nome):
    if(nome == 'keven'):
        print('cuidado para nao cair de motor, meu amigo')
    else:
        print('vc anda devagar. Parabéns, meu amigo')
    print(f'seja bem-vindo {nome}')

def saudar_formalmente(nome, sobrenome):
    print(f'seja bem-vindo {nome} da família {sobrenome}')

def calc_media(n1, n2, n3):
    media = (n1 + n2 + n3)/3
    media = round(media, 2)#definir a quantidade de casas decimais
    print(f'sua média foi {media}')

calc_media(4,9,7)