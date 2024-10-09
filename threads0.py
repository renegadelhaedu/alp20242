import threading
import time

def thread_funcao(name):
    print(f"Thread {name} está rodando")
    time.sleep(2)
    print(f"Thread {name} terminou")


thread1 = threading.Thread(target=thread_funcao, args=("A",))
thread2 = threading.Thread(target=thread_funcao, args=("B",))


thread1.start()
thread2.start()


