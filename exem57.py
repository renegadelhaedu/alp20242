#criar arquivos w a r
#write w : sobrescreve arquivo existente
#append a: adiciona no final do arquivo

file = open('alunos2.txt', 'a')
for i in range(6):
    nome = input('digite seu nome ')
    file.write(nome + '\n')
file.close()