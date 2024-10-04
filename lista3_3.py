nome = input('digite seu nome')
while(len(nome) <= 3):
    nome = input('digite seu nome')

idade = int(input('digite sua idade'))
while(idade < 0 or idade > 150):
    idade = int(input('digite sua idade'))

salario = float(input('digite seu salario'))
while(salario <= 0):
    salario = float(input('digite seu salario'))

sexo = input('digite o sexo')
while(sexo != 'f' and sexo != 'm'):
    sexo = input('digite o sexo')

ec = input('digite seu estado civil')
while(ec != 's' and ec != 'c' and ec != 'd' and ec != 'v'):
    ec = input('digite seu estado civil')