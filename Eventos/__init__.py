
def criar_evento(codigo, nome, login, limite, valor, eventos):
    eventos[codigo] = [nome, login, limite, valor]
    print('evento criado com sucesso')


def listar_eventos(eventos):
    for chave in eventos:
        print(f'nome: {eventos[chave][0]}')
        print(f'codigo: {chave}')
        print(f'valor: {eventos[chave][3]}')
        print(' ')
