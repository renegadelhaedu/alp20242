ant = 0
atual = 1

n = int(input('digite o n da sequencia'))
for i in range(n):
    aux = atual
    print(f'o atual é {atual} e o anterior {ant}')
    atual = atual + ant
    ant = aux
    print(f'o novo atual é {atual} e o anterior {ant}\n')
