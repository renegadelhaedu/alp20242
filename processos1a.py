#pacote para lidar com múltiplos processadores da máquina
import multiprocessing
import os
def processoFilho():
    print(f"FILHO-- Processo filho possui o ID {os.getpid()}")

def processoPai():
    filho = multiprocessing.Process(target=processoFilho)
    filho.start()
    print(f'PAI-- o processo pai terminou e seu ID era {os.getpid()}')

if (__name__ == '__main__'):
    processoPai()