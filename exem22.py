sb = float(input('digite seu salario bruto'))
ndep = int(input('digite a qtde de dependentes'))

valorDeps = 150 * ndep
sbdep = sb - valorDeps

if(sbdep <= 2000):
    imp = 0
elif(sbdep > 2000 and sbdep <= 4000):
    imp = sbdep * 0.1
elif(sbdep > 4000 and sbdep <= 6000):
    imp = sbdep * 0.15
else:
    imp = sbdep * 0.2

sl = sbdep - imp
print(f'o salário líquido é {sl}')
print(f'o valor do import é {imp}')
print(f'o salário descontado pelos dependentes {sbdep}')
print(f'o total de dependentes somou {valorDeps}')

