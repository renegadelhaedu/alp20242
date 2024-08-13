#desenvolva um algoritmo em python para ler o nome e a idade do
# usuário. O programa deve exibir na tela o nome do usuário e o ano
# que ele nasceu

nome = input('digite seu nome ')
idade = int(input('digite sua idade '))

ano_nasc = 2024 - idade

print(nome + ' voce nasceu em ')
print(ano_nasc)