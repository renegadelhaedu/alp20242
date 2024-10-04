popA = 80000
popB = 200000
contador = 0
while(popB > popA):
    popA = popA * 1.03
    popB = popB * 1.015
    contador = contador + 1

print(popA)
print(popB)
print(f'durou {contador} anos para A superar B')