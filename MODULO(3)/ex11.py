import os
os.system('cls')

#Criar um algoritmo que deixe escolher qual a tabuada de multiplicar que se deseja imprimir.
num=int(input('Digite um número: '))
for i in range(1,11):
    prod=num*i
    print(f'{num}x{i}={prod}')
