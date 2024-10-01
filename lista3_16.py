ant = 0
atual = 1
for i in range(9999):
    aux = atual
    print(f'o atual é {atual} e o anterior {ant}')
    atual = atual + ant
    ant = aux
    print(f'o novo atual é {atual} e o anterior {ant}\n')
    if(atual >= 500):
        break
