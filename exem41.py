def verificar_vogais(nome):
    contar = 0
    for l in nome:
        if(l == 'a' or l == 'e' or l == 'i' or l == 'o' or l == 'u'):
            contar += 1

    print(f'o nome {nome} possui {contar} vogais')

nomes = ['henrique','kauan','keven','pedro']
nomes.append('kevin')

for pessoa in nomes:
    verificar_vogais(pessoa)



