s0 = float(input('digite o deslocamento inicial '))
v0 = float(input('digite a velocidade inicial '))
t = float(input('digite o tempo gasto'))
a = float(input('digite a aceleração'))

s = s0 + v0 * t + (a * (t*t))/2

print(str(s))