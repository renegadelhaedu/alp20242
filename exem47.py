#desenvolva uma função em python que receba uma lista de números inteiros
#como parâmetro e dentro da função encontre os elementos da lista que são
#o maior e o menor elemento

def procurar_valores(meusnums):
    maior = 0
    menor = 999999999

    for num in meusnums:
        if(num > maior):
            maior = num
        if(num < menor):
            menor = num

    return maior, menor

#fora da função
lista_nums = [1,6,8,2,44,11,9]
maiorNum, menorNum = procurar_valores(lista_nums)

print(f'o maior valor é {maiorNum} e o menor valor é {menorNum}')





