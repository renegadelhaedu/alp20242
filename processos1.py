#pacote para lidar com múltiplos processadores da máquina
import multiprocessing
import os

def processoFilho():
    x = 2
    for i in range(999999):
        print(f"Processo filho possui o ID {os.getpid()} e x:{x}")

def processoPai():
    x = 1
    p = multiprocessing.Process(target=processoFilho)
    p.start()

    p.join()
    print(f'---- o processo pai terminou e x:{x}')

if __name__ == '__main__':
    processoPai()