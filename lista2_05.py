n1 = float(input('digite a primeira nota '))
n2 = float(input('digite a segunda nota '))

media = (n1 + n2) / 2

if(media >= 7 and media < 10):
    print('aprovado')

if(media < 7):
    print('reprovado')

if(media == 10):
    print('aprovado com distincao')

