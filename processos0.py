#processos uma instância do programa sendo executada pelo SO
#pacote para acessar funcionalidades do seu Sistema operacional
import os
nome = 'wacelys'
#get = pegar e pid = process id

while(True):
    print(f"Este processo possui ID {os.getpid()} e o nome é {nome}")

