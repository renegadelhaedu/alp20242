'''
o nosso amigo Wesley deseja determinar a variação de temperatura em um dispositivo de
hardware. Ele fez 5 medições de temperatura e deseja verificar se a média de temperatura
ultrapassa 90 graus. Caso ultrapasse, ele pede ao usuário para informar qual a tempratura
ambiente. O programa  deve emitir uma alerta se a média de temperatura
do hardware for menor que o dobro da temperatura ambiente. Caso não, mostre uma
mensagem que está tudo bem.
'''
t1 = float(input('digite a temperatura do dispositivo'))
t2 = float(input('digite a temperatura do dispositivo'))
t3 = float(input('digite a temperatura do dispositivo'))
t4 = float(input('digite a temperatura do dispositivo'))
t5 = float(input('digite a temperatura do dispositivo'))

media = (t1 + t2 + t3 + t4 + t5) / 5

if(media > 90):
    tAmbiente = float(input('digite a temperatura ambiente'))
    if(media < tAmbiente ** 2):
        print('Hardware em perigo')
    else:
        print('está tudo bem')
else:
    print('está tudo bem')


