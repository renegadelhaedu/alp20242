tipo = input('digite o tipo de carne que você deseja')
qtde = float(input('digite a quantidade de carne que vc deseja'))

cartao = input('você vai pagar com o cartao tabajara?')

if(tipo == 'file duplo' and qtde <= 5):
    valor = qtde * 4.9
elif(tipo == 'file duplo' and qtde > 5):
    valor = qtde * 5.8
elif(tipo == 'alcatra' and qtde <= 5):
    valor = qtde * 5.9
elif(tipo == 'alcatra' and qtde > 5):
    valor = qtde * 6.8
elif(tipo == 'picanha' and qtde <= 5):
    valor = qtde * 6.9
elif(tipo == 'picanha' and qtde > 5):
    valor = qtde * 7.8
else:
    print('tipo de carne inválido')
    valor = 0

if(valor != 0):

    if(cartao == 'sim'):
        desconto = valor * 0.05
    else:
        desconto = 0

    print(f'voce comprou {qtde} de {tipo}')
    final = valor - desconto

    if(desconto > 0):
        print(f'o valor final foi {final} e teve desconto de {desconto}')
    else:
        print(f'o valor final foi {final} e nao tivemos desconto')
