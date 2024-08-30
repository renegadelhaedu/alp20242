turno = input('digite M ou V ou N')
invalido = True
if(turno == 'm' or turno == 'M'):
    print('bom dia')
    invalido = False
if(turno == 'v' or turno == 'V'):
    print('boa tarde')
    invalido = False
if(turno == 'n' or turno == 'N'):
    print('boa noite')
    invalido = False
if(invalido):
    print('valor inválido')
