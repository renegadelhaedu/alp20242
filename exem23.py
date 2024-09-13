#desenvolva um algoritmo para ler o nome, a idade e a altura
#para verificar se você vai ser aceito na polícia.

#só aceitam candidatos se:
# 1-eles tiverem mais de 18 anos com pelo menos 1.70 de altura
# 2-se a idade for acima de 35 anos, deve ter mais de 1.85
# 3-se altura for maior que 2m, o candidato é excluído

nome = input('digite seu nome')
idade = int(input('digite sua idade'))
alt = float(input('digite sua altura'))

if(idade >= 18 and idade <= 35 and alt >= 1.7 and alt <= 2):
    print('voce pode ser policial')
elif(idade > 35 and alt > 1.85 and alt <= 2):
    print('voce pode ser policial')
else:
    print('voce nao pode ser policial')

