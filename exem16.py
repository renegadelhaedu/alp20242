#operadores lógicos (and or not)
#and E lógico

#tabela verdade do E
# True and True => True
# True and False => False
# False and True => False
# False and False => False

sal = float(input('digite seu salario'))

if(sal < 2259.21):
    sal_liq = sal
if(sal >= 2259.21 and sal <= 2826.65):
    sal_liq = sal * 0.925
if(sal >= 2826.66 and sal <= 3751.05):
    sal_liq = sal * 0.85
if(sal >= 3751.06 and sal <= 4664.68):
    sal_liq = sal * 0.775
if(sal > 4664.68):
    sal_liq = sal * 0.725

print(f'o valor final do salario será {sal_liq}')


        




