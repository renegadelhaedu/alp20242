sal = float(input('digite seu salario'))

if(sal <= 280):
    percentual = 0.20
if(sal > 280 and sal <= 700):
    percentual = 0.15
if(sal > 700 and sal <=1500):
    percentual = 0.10
if(sal > 1500):
    percentual = 0.05

aumento = sal * percentual
final = sal + aumento
print(f'voce ganhava {sal}')
print(f'seu salário aumento {percentual * 100}%')
print(f'em termos reais, voce ganhará a mais {aumento} reais')
print(f'no final, vc passou a ganhar {final} reais')