import os
os.system('cls')

#Criar um algoritmo que leia um número que será o limite superior de um intervalo e o incremento.
#Imprimir todos os números naturais no intervalo de 0 até esse número.
#Suponha que os dois números lidos são maiores do que zero.
stop=int(input(f'Digite o limite superior: '))
step = int(input('Digite o incremento: '))
for i in range(0,stop,step):
    print(i)