#crie um algoritmo que o usuário informe 2 números e exiba na tela o quadrado do
# menor número e a raiz quadrada do maior número.

num1 = int(input('digite um número'))
num2 = int(input('digite outro número'))

if(num1 > num2):
    raizMaior = num1 ** (1/2)
    quadMenor = num2 ** 2
    print(f'o maior foi o primeiro {raizMaior} e o menor foi o segundo {quadMenor}')
else:
    raizMaior = num2 ** (1 / 2)
    quadMenor = num1 ** 2
    print(f'o maior foi o segundo {raizMaior} e o menor foi o primeiro {quadMenor}')

