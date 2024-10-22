#desenvolva um menu com duas funcionalidades: cadastrar e atualizar
#cadastrar(nome, idade, rg)
#atualizar(novonome, idade)
#use lista e funções

def cadastrar_pessoa(lista, nome, idade, rg):
    lista.append([nome,idade,rg])
    print('Pessoa cadastrada com sucesso')

def atualizar_pessoa(lista,rg):
    ind = -1
    for i in range(len(lista)):
        if(lista[i][2] == rg):
            ind = i
    if(ind != -1):
        novonome = input('digite seu novo nome')
        lista[ind][0] = novonome
        print('nome atualizado com sucesso')
    else:
        print('RG nao encontrado')



pessoas = []
op = -1
while(op != 0):
    print('1-cadastrar pessoa')
    print('2-atualizar pessoa')
    print('0-sair')
    op = int(input('digite a opcao desejada'))

    if(op == 1):
        nome = input('digite seu nome')
        idade = int(input('digite sua idade'))
        rg = input('digite seu RG')
        cadastrar_pessoa(pessoas,nome,idade,rg)
    elif(op == 2):
        rg = input('digite o RG')
        atualizar_pessoa(pessoas, rg)
        print(pessoas)
