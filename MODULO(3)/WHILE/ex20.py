import os
os.system('cls')

#Entrar com vários números e verificar se eles são ou não quadrados perfeitos.
#O algoritmo termina quando se digita um número menor ou igual a 0.
import math
contador=0
while True:
    num=int(input(f'Digite o {contador+1}º número (0 para sair): '))
    if num==0:
        print('                 ')
        print('Encerrando...')
        print('                 ')
        break

    raiz=math.sqrt(num)
    if raiz.is_integer():
        print(f'{num} é um quadrado perfeito.')
        print('                 ')
    else:
        print(f'{num} não é um quadrado perfeito.')
        print('                 ')
    contador+=1