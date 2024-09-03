vhr = float(input('digite o valor da sua hora'))
qtde_hr = int(input('digite a quantidade de horas'))
sal = vhr * qtde_hr

if(sal <= 900):
    ir = sal
elif(sal > 900 and sal <= 1500):
    ir = sal * 0.05
elif(sal > 1500 and sal <=2500):
    ir = sal * 0.10
else:
    ir = sal * 0.20

sind = sal * 0.03
inss = sal * 0.1
fgts = sal * 0.11

total_desc = ir + inss + sind
sal_liq = sal - total_desc
print('coloquem os prints')