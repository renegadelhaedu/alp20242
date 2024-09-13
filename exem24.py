
# desenvolva um algoritmo em python para ler um nome e verifique
# se as primeiras duas letras do nome são iguais as últimas 2
nome = input('digite seu nome ')

t = len(nome)
if(t >= 4):

    if(nome[0:2] == nome[t-2:t]):
        print('sao iguais')
    else:
        print('nao sao iguais')

