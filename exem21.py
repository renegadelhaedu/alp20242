valor = input('digite seu nome')

# isnumeric é uma função que verifica se dentro da variável possui
# apenas números. se for, ela retorna True

if( not valor.isnumeric()):
    print('Nao possui apenas números')
else:
    print('valor composto apenas de números')

