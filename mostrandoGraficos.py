import matplotlib.pyplot as plt

lista = [13,17,21,30,62,80,85]
#plt.plot(lista)

eventos =['rock n rio', 'cha da barbie', 'casamento de macelo']
qtde =[121,123,30]

plt.bar(eventos, qtde)

#plt.ylabel('quantidade de casos acumulados')
#plt.xlabel('dias desde a primeira infecção')
plt.show()

