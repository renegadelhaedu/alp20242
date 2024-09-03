#faça um programa para ler o dia e o mês de nascimento
#do usuário. o programa deve informar se ele é ou não do
#signo de câncer

dia = int(input('digite o dia que vc nasceu'))

if(dia < 1 or dia > 31):
    print('dia inválido')
else:
    mes = int(input('digite o mês que vc nasceu'))
    if(mes < 1 or mes > 12):
        print('mês inválido')
    elif((dia >= 21 and dia <=30 and mes == 6)
        or (dia >= 1 and dia <= 22 and mes ==7)):
        print('vc é canceriano')
    else:
        print('vc nao é canceriano')
