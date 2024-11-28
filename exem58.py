#criar arquivos w a r
# read r : leitura de arquivo

file = open('alunos.txt', 'r')

linhas = file.readlines()
for linha in linhas:
    modificada = linha.replace('/n','')
    print(modificada)

file.close()