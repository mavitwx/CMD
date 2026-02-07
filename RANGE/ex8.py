import os
os.system('cls')

#Criar um algoritmo que leia um número (num) e imprima a soma dos números múltiplos de 5
#no intervalo aberto entre 1 e num. Suponha que num será maior que zero.
num=int(input('Digite um número maior que zero: '))
soma=0
if num<=5:
    print('O intervalo aberto não contém nenhum múltiplo de 5')
else:
    for i in range(5,num,5):
        print(i)
        soma= soma+i
    print(f'Soma: {soma}')
