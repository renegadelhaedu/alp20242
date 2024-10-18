def verificar_dados(nome, idade, cpf):
    valido = True
    nums = ['0','1','2','3','4','5','6','7','8','9']
    for num in nums:
        if(num in nome):
            valido = False
            break

    if(idade <= 0 or idade >= 150):
        valido = False

    if(len(cpf) != 11):
        valido = False

    return valido

pessoas = []

for i in range(5):
    nome = input('digite seu nome')
    idade = int(input('digite sua idade'))
    cpf = input('digite o cpf')

    if(verificar_dados(nome, idade, cpf) == True):
        pessoas.append([nome, idade, cpf])
        print('usuario adicionado com sucesso')
    else:
        print('erro nos dados do usuário')

