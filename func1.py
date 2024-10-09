#funções em python
#são blocos de código nomeados e que podem ser chamados durante o programa

#1-dar um nome para a função
#2-defino se vai ter ou não parâmetros
#3-coloco as instruções dentro da função

def descobrirPreferida():
    disciplina = input('qual sua disciplina preferida?')
    if(disciplina == 'algoritmos'):
        print('deixe de ser mentiroso, caba safado')
    else:
        print('parabéns!')

def saudar_alunos():
    nome = input('digite seu nome')
    print(f'seja bem-vindo {nome}')

descobrirPreferida()



