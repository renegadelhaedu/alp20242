def aumentar_salario(nome, valor):
    final = valor * 1.3
    print(f'{nome} vai receber {final} reais')

for i in range(5):
    nome = input('digite seu nome')
    salario = float(input('digite seu salario'))
    aumentar_salario(nome, salario)