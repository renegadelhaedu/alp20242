# faça um algoritmo na linguagem python que possa receber as
# notas dos 4 alunos da sala e possa informar quais deles
# possuem nota menor que a média dos 4 alunos, assim como os que
# possuem nota maior que a média dos 4 alunos

n1 = float(input('digite sua nota'))
n2 = float(input('digite sua nota'))
n3 = float(input('digite sua nota'))
n4 = float(input('digite sua nota'))

media = (n1 + n2 + n3 + n4) / 4

if(n1 > media):
    print('o primeiro aluno está acima da média')
elif(n1 < media):
    print('o primeiro aluno está abaixo da média')

if(n2 > media):
    print('o segundo aluno está acima da média')
elif(n2 < media):
    print('o segundo aluno está abaixo da média')

if(n3 > media):
    print('o terceiro aluno está acima da média')
elif(n3 < media):
    print('o terceiro aluno está abaixo da média')

if(n4 > media):
    print('o quarto aluno está acima da média')
elif(n4 < media):
    print('o quarto aluno está abaixo da média')