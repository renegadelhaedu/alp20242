'''desenvolva um algoritmo em python para receber
o valor do salário e o percentual de aumento.
exiba no final o salário reajustado
'''
salario = float(input('digite seu salário'))
perc = float(input('digite o percentual de aumento'))

final = salario * (1 + perc/100)
print(f'vc vai receber {final} reais')
