base = int(input('digite a base'))
exp = int(input('digite o expoente'))

resp = 1
for i in range(exp):
    resp = resp * base

print(resp)
