#ano bissexto
#ser  divisível por 4 e nao ser divisível por 100
#se ele nao for divisível por 4, tem que ser por 400

ano = int(input('digite o ano para checarmos se é bissexto'))

if(ano % 4 == 0 and ano % 100 != 0):
    print('ano bissexto')
elif(ano % 400 == 0):
    print('ano bissexto')
else:
    print('ele nao é bissexto')
