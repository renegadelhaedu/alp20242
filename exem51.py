#estruturas de dados (list, tuple, set, dict)
#dicionário
#dict (map)
#mapeamento chave valor
#não garante ordem
#chaves são únicas
#valores podem ter duplicidade
#são mutáveis

alunos = dict()
professores = {'wacelys@gmail.com':['wacelys',25,'umari']
               ,'macelo@gmail.com':['macelo',26,'umari']
               ,'bruna@gmail.com':['bruna',21,'bernadino']}

#acessar um valor de um item do dicionário
#print(professores['a'])
login = 'wacelys@gmail.com'
senha = 25
if login in professores and professores[login][1] ==  senha:
    print('usuario logado')
    print('mostrar menu')
else:
    print('esse usuario nao está cadastrado')






