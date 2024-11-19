'''
crie um dicionário vazio e construa uma estrutura de repetição para ir adicionando 3 informações do usuário (rg, nome e salario).
Após ler todas essas informaçoes, percorra o dicionário somando os salários.
Exiba a soma dos salários na tela
'''
pessoas = dict()
for i in range(4):
    rg = input('digite seu rg')
    nome = input('qual seu nome')
    salario = float(input('digite seu salário'))
    pessoas[rg] = [nome, salario]

soma = 0
for chave in pessoas:
    soma = soma + pessoas[chave][1]
    #soma = soma + pessoas.get(chave)[1]

print('a soma de salários foi ', soma)

