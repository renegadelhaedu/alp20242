#estrutura de repetição
# for e while

while(True):
    print('1-cadastrar produto')
    print('2-excluir produto')
    print('3-listar produtos')
    print('0-sair')

    op = int(input('digite a opcao desejada'))
    if(op == 1):
        print('produto cadastrado')
    elif(op == 2):
        print('remover produto')
    elif(op == 0):
        break