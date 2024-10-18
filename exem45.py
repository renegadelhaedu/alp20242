pessoas = list()
rene = ['rene de sousa', 36, 1.70]
wacelys = ['wacelys aguiar', 25, 1.78]
pedro = ['pedro silva', 20, 1.72]
pessoas.append(rene)
pessoas.append(wacelys)
pessoas.append(pedro)
soma = 0
for p in pessoas:
    soma = soma + p[2]

media = soma / len(pessoas)
print(f'a média de altura é {media}')







