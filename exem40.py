alunos = []

alunos.append('ricardo')
alunos.append('gabriel')
alunos.append('rhafael')
alunos.append('diogo')

remover = []
for i in range(4):
    if(alunos[i] == 'gabriel'):
        remover.append(alunos[i])

for r in remover:
    alunos.remove(r)

print(alunos)