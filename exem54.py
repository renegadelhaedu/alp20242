alunos = dict()
alunos[1] = 'rene'
alunos[2] = 'josemar jr'
alunos[3] = 'kauan'
remover = []
for chave in alunos:
    if 'e' in alunos[chave]:
        remover.append(chave)

for chave in remover:
    alunos.pop(chave)
print(alunos)
