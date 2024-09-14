num = int(input('digite um numero'))

if(num < 1000):
    cem = num // 100
    sobrou = num - ( cem * 100)
    dez = sobrou // 10
    sobrou = sobrou - ( dez * 10)
    uni = sobrou

    if(cem == 1):
        print(f'{cem} centena,')
    elif(cem > 1):
        print(f'{cem} centenas,')

    if(dez == 1):
        print(f'{dez} dezena,')
    elif(dez > 1):
        print(f'{dez} dezenas,')

    if (uni == 1):
        print(f'{uni} unidade')
    elif (dez > 1):
        print(f'{uni} unidades')


