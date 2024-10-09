import threading

acertos = 0

def incrementarValor():
    global acertos
    acertos = acertos + 1
    print(f'a quantidade de acertos é {acertos}')


thread1 = threading.Thread(target=incrementarValor)
thread2 = threading.Thread(target=incrementarValor)

thread1.start()
thread2.start()
