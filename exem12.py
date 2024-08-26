#faça um algoritmo em python para ler a idade e o valor recebido do usuário
# e calcule se ele deve pagar imposto de renda com base na idade

idade = int(input('digite sua idade'))
valor = float(input('digite o valor recebido'))

if(idade >= 18):
    valor_liq = valor * 0.85 #retirando 15% do valor
    print(f'voce ficará com o valor líquido de {valor_liq} reais')
else:
    print(f'voce nao terá imposto atribuído e ficou com {valor} reais')


