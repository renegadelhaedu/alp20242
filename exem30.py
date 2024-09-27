#estrutura de repetição
# for e while
#faça um programa que leia 5 números informados pelo usuário e
#calcule a multiplicação entre eles

rep = int(input('digite a quantidade de números'))
mult = 1
for i in range(rep):
    num = int(input('diga um número'))
    mult = num * mult

print(mult)