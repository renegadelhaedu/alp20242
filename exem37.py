#desenolva um programa para realizar a eleiçao do representante da
#turma. o programa deve ir lendo o número dos candidatos e ir contando
#os votos enquanto o usuário disser que tem um próximo eleitor.

numA = input('digite o numero do candidato A')
numB = input('digite o numero do candidato B')
qtdeA =0
qtdeB =0
qtdeNulos =0
while(True):
    op = input('qual o numero do seu candidato')
    if(op == numA):
        qtdeA += 1
        #ou qtdeA = qtdeA + 1
    elif(op == numB):
        qtdeB += 1
    else:
        qtdeNulos += 1

    outro = input('tem um próximo eleitor?')
    if(outro != 'sim'):
        break

if(qtdeA > qtdeB):
    print('quem vai roubar é o candidato A')
else:
    print('quem vai roubar é o candidato B')