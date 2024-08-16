'''faça um programa em python para receber do usuário
o salário final e o salário inicial. o programa deve
calcular e exibir qual o percentual de aumento '''
sal_ini = float(input('quanto vc recebia?'))
sal_fim = float(input('quanto vai receber?'))

perc = ((sal_fim - sal_ini) / sal_ini) * 100
print(f'voce teve um aumento de {perc}%')
