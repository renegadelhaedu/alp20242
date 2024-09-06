dia = int(input('digite o dia'))
mes = int(input('digite o mes'))
ano = int(input('digite o ano'))

if(dia > 0 and dia <= 31 and mes >= 1 and mes <= 12 and ano > 0):
    print('data válida')
else:
    print('data inválida')
