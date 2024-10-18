#funções em python

def calcular_media(n1,n2,n3):
    media = (n1 + n2 + n3)/3
    return media

def calc_media_lista(lista_notas):
    return sum(lista_notas) / len(lista_notas)

def calc_media_lista2(lista_notas):
    soma = 0
    for num in lista_notas:
        soma += num
    return soma / 3

for i in range(5):
    nota1 = float(input('digite sua nota'))
    nota2 = float(input('digite sua nota'))
    nota3 = float(input('digite sua nota'))
    notas = [nota1, nota2, nota3]
    #print('sua média foi', calcular_media(nota1,nota2,nota3))
    print('minha média foi', calc_media_lista(notas))
