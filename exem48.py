
def atualizar_nome(lista, nomeAtual, novoNome):
    if(nomeAtual in lista):
        ind = lista.index(nomeAtual)
        lista[ind] = novoNome

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



