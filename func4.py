minic = [['dev', 50.0, 'eu eue u', []], ['bd', 40.0, 'kakakaka', []]]

for i in range(2):
    nome = input('digite nome')
    email = input('digite seu email')

    ind = int(input('digite o indice do mmininucr'))
    minic[ind][3].append(email)

print(minic)
