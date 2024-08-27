estado = input('informe seu estado civil')

if(estado == 'solteiro'):
    nome = 'voce nao tem conjuge'
if(estado == 'casado'):
    nome = input('informe o nome do conjuge')
if(estado == 'divorciado'):
    nome = input('informe o nome do(a) ex')
if(estado == 'viuvo'):
    nome = input('informe o nome do falecido esposo(a)')

print(f'O usuário respondeu o estado civil como: {estado}')
