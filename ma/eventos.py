events = [['Devops', 'Rene', '123', '12/07/2025', 'JP', '50', 'S', 0.0]]
inscritos = []


def cadastrar_evento(usuario):
    while True:
        nome_evento = input('Digite o nome do evento: ')
        evento_repetido = False
        for evento in events:
            if evento[0] == nome_evento:
                evento_repetido = True
                break

        if evento_repetido:
            print("Já existe um evento com esse nome. Por favor, insira um nome diferente.")
        else:
            break
    descricao = input('Insira a descrição do evento: ')
    data_evento = verificar_data()
    local = input('Insira o local do evento: ')
    valor = float(input('Digite o valor da inscrição: '))
    cancelavel = input('Você deseja permitir o cancelamento de inscrições em seu evento?: (S/N) ').upper()
    while cancelavel != 'S' and cancelavel != 'N':
        print("Insira apenas 'S' ou 'N': ")
        cancelavel = input().upper()

    events.append([nome_evento, usuario[0], descricao, data_evento, local, valor, cancelavel, 0.0])
    print('Evento cadastrado com sucesso!')
    print(events)


def listar_eventos():
    if len(events) == 0:
        print('Nenhum evento cadastrado.')
    else:
        for evento in events:
            print(f'Evento: {evento[0]}, Criador: {evento[1]}, Valor: R$ {evento[5]}')


def buscar_evento():
    listar_eventos()
    if len(events) == 0:
        return
    procurar = input('Digite o nome do evento que deseja buscar: ')
    for evento in events:
        if evento[0] == procurar:
            print(f'Evento: {evento[0]}, Criador: {evento[1]}, Valor: R$ {evento[5]}')
            return
    print('Evento não encontrado!')


def participar_evento(usuario):
    listar_eventos()
    if len(events) == 0:
        return
    nome_evento = input('Digite o nome do evento que deseja participar: ')
    for evento in events:
        if evento[0] == nome_evento:
            for inscricao in inscritos:
                if inscricao[0] == nome_evento and inscricao[1] == usuario[0]:
                    print('Você já está inscrito no evento.')
                    return

            pagar = input('Deseja realizar o pagamento agora? (S/N): ').upper()
            while pagar != 'S' and pagar != 'N':
                print('Insira apenas S ou N')
                pagar = input('Deseja realizar o pagamento agora? (S/N): ')

            if pagar == 'S':
                status = 'Pago'
                inscritos.append([evento[0], usuario[0], status])
                print(f'Inscrição realizada com sucesso no evento {nome_evento}')
            elif pagar == 'N':
                status = 'Pendente'
                inscritos.append([evento[0], usuario[0], status])
                print(f'Inscrição realizada com sucesso no evento {nome_evento}')
                print('Você deverá pagar a inscrição no dia do evento')
            return
    else:
        print('Evento não encontrado')


def cancelar_inscricao(usuario):
    listar_eventos()
    if len(events) == 0:
        return
    nome_evento = input('Digite o nome do evento do qual deseja se desinscrever: ')
    evento_encontrado = ''
    for evento in events:
        if evento[0] == nome_evento:
            evento_encontrado = evento
            break

    if evento_encontrado:
        if evento_encontrado[6] == 'S':
            for inscricao in inscritos:
                if inscricao[0] == nome_evento and inscricao[1] == usuario[0]:
                    inscritos.remove(inscricao)
                    print(f"Inscrição removida com sucesso do evento '{nome_evento}'!")
                    return
            print('Você não está inscrito neste evento.')
        else:
            print('Este evento não é cancelável.')
    else:
        print("Evento não encontrado.")


def remover_evento(usuario):
    listar_eventos()
    if len(events) == 0:
        return
    nome_evento = input('Digite o nome do evento que deseja remover: ')
    evento_encontrado = False
    for evento in events:
        if evento[0] == nome_evento:
            evento_encontrado = True
            if evento[1] == usuario[0]:
                confirmacao = input(f"Tem certeza que deseja remover o evento '{nome_evento}'(S/N): ").upper()

                if confirmacao == 'S':
                    events.remove(evento)
                    print('Evento removido com sucesso!')
                    return
                else:
                    print('Evento não removido')
    if not evento_encontrado:
        print('Evento não encontrado!')


def listar_participantes(usuario):
    listar_eventos()
    if len(events) == 0:
        return
    nome_evento = input('Digite o nome do evento que deseja ver os participantes: ')
    evento_encontrado = False
    for evento in events:
        if evento[0] == nome_evento:
            evento_encontrado = True
            if evento[1] == usuario[0]:
                if len(inscritos) == 0:
                    print('Nenhum participante cadastrado')
                else:
                    for participantes in inscritos:
                        if participantes[0] == nome_evento:
                            print(f'________________________________________ \n'
                                  f'Usuário: {participantes[1]}, Status de Pagamento: {participantes[2]}')
                        else:
                            print('Nenhum participante cadastrado.')
            else:
                print('Você não é o criador desse evento.')
    if not evento_encontrado:
        print('Evento não encontrado!')


def verificar_valor_arrecadao(usuario):
    listar_eventos()
    if len(events) == 0:
        return
    nome_evento = input('Digite o nome do evento que deseja ver a arrecadação: ')
    valor_arrecadado = 0
    valor_pendente = 0
    numinscrit = 0
    for evento in events:
        if evento[0] == nome_evento:
            if evento[1] == usuario[0]:
                valor_inscricao = float(evento[5])
                doacoes = float(evento[7])
                criador = True
                if criador:
                    for participantes in inscritos:
                        if participantes[0] == nome_evento:
                            numinscrit += 1
                            if participantes[2] == 'Pago':
                                valor_arrecadado += valor_inscricao
                            elif participantes[2] == 'Pendente':
                                valor_pendente += valor_inscricao
                    print(f'________________________________________\n'
                          f'O número de inscritos foi: {numinscrit}\n'
                          f'Valor arrecadado para o evento "{nome_evento}": R$ {valor_arrecadado:.2f}\n'
                          f'Valor pendente para o evento "{nome_evento}": R$ {valor_pendente:.2f}\n'
                          f'O valor total esperado é de R$ {valor_pendente + valor_arrecadado + doacoes}\n'
                          f'O total de doações para o evento foi de {doacoes}\n'
                          f'________________________________________')
                    return
            else:
                print('Você não é o criador deste evento!')
                return
        else:
            print('Evento não encontrado')
            return




def doar_para_evento():
    listar_eventos()
    if len(events) == 0:
        return
    nome_evento = input('Digite o nome do evento para o qual deseja doar: ')
    for evento in events:
        if evento[0] == nome_evento:
            valor_doacao = float(input('Digite o valor que deseja doar: '))
            if valor_doacao > 0:
                evento[7] += valor_doacao
                print(f'Doação de R$ {valor_doacao:.2f} realizada com sucesso para o evento "{nome_evento}"!')
                print(f'Valor total arrecadado com doações: R$ {evento[7]:.2f}')
            else:
                print("O valor da doação deve ser positivo.")
            return

    print('Evento não encontrado.')


def verificar_data():
    dia_limite = 11
    mes_limite = 11
    ano_limite = 2024

    while True:
        data_evento = input('Insira a data do evento no formato: DD/MM/AAAA. ')

        if len(data_evento) == 10 and data_evento[2] == '/' and data_evento[5] == '/' and \
                data_evento[:2].isdigit() and data_evento[3:5].isdigit() and data_evento[6:].isdigit():

            dia = int(data_evento[0:2])
            mes = int(data_evento[3:5])
            ano = int(data_evento[6:10])

            if dia <= 0 or dia > 31:
                print('Insira valores de 1 a 31 para o dia.')
            elif mes <= 0 or mes > 12:
                print('Insira valores de 1 a 12 para o mês.')
            elif ano < 2024:
                print('Não tenho máquina do tempo. Insira um valor válido para o ano.')
            elif ano < ano_limite or (ano == ano_limite and mes < mes_limite) or (
                    ano == ano_limite and mes == mes_limite and dia < dia_limite):
                print("O evento não pode ser no passado!")
            else:
                print("Data válida para o evento!")
                return data_evento
        else:
            print("Formato inválido. Certifique-se de usar o formato DD/MM/AAAA.")
