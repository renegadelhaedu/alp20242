#estrutura de repetição
# for e while
#você investiu em uma aplicação no banco do brasil que rende 0,34%
#ao mês. faça um programa que leia do usuário o valor inicial
#investido e a quantidade de meses. o programa deve no final exibir
#o montante gerado.

inicial = float(input('quanto vc quer investir?'))
meses = int(input('quantos meses quer deixar o dinheiro investido'))

for x in range(meses):
    inicial = inicial + inicial * 0.0034
    # ou inicial = inicial * 1.0034

print(inicial)