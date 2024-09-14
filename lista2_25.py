p1 = input("Telefonou para a vítima?")
p2 = input("Esteve no local do crime?")
p3 = input("Mora perto da vítima?")
p4 = input("Devia para a vítima?")
p5 = input("Já trabalhou com a vítima?")
contador = 0

if(p1 == 'sim'):
    contador = contador + 1
if(p2 == 'sim'):
    contador = contador + 1
if(p3 == 'sim'):
    contador = contador + 1
if(p4 == 'sim'):
    contador = contador + 1
if(p5 == 'sim'):
    contador = contador + 1

if(contador == 2):
    print('você é suspeito e matou o rapaz do comício')
elif(contador == 3 or contador == 4):
    print('você é cúmplice e ajudou a matar o rapaz do som')
elif(contador == 5):
    print('com certeza vc matou o lazarento do som')
else:
    print('inocente')

