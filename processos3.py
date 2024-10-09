import multiprocessing
import os

def processoFilho():
    x = 2 + os.getpid()
    for i in range(999999):
        print(f"Processo filho possui o ID {os.getpid()} e x:{x}")

def processoPai():
    x = 1
    for i in range(5):
        multiprocessing.Process(target=processoFilho).start()
    print(f'---- o processo pai terminou e x:{x}')

if __name__ == '__main__':
    processoPai()