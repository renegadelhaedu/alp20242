#3 números

n1 = int(input('digite o número'))
n2 = int(input('digite o número'))
n3 = int(input('digite o número'))

if(n1 > n2 and n2 > n3):
    print(f'p maior de todos é {n1}')
if(n1 > n3 and n3 > n2):
    print(f'p maior de todos é {n1}')

if(n2 > n1 and n1 > n3):
    print(f'p maior de todos é {n2}')
if(n2 > n3 and n3 > n1):
    print(f'p maior de todos é {n2}')

if (n3 > n2 and n2 > n1):
    print(f'p maior de todos é {n3}')
if (n3 > n1 and n1 > n2):
    print(f'p maior de todos é {n3}')