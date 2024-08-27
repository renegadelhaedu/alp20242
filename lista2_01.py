#fazer as duas primeiras questões da lista de estrutura de decisão
num1 = int(input('digite o número'))
num2 = int(input('digite o outro número'))

#estrutura de decisão (dois caminhos possíveis)

if(num1 > num2):
    print(f'o maior deles é o número {num1} e o menor é o número {num2}')
else:
    #num2 ser maior que o num1, num1 ser igual ao num2
    print(f'o maior deles é o número {num2} informado pelo usuário')
