
def atualizar_nome_raiz(lista, nomeAtual, novoNome):
    ind = -1
    for i in range(len(lista)):
        if(lista[i] == nomeAtual):
            ind = i
    if(ind != -1):
        lista[ind] = novoNome
        print('nome atualizado')
    else:
        print('pessoa nao encontrada')

nomes = ['Wesley', 'Pedro', 'Kelvin']

nomeAtual = input('Informe o nome que deseja alterar: ')
novoNome = input('Informe o novo nome: ')
atualizar_nome_raiz(nomes, nomeAtual, novoNome)
print(nomes)