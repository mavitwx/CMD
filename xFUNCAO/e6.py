import os
os.system('cls')
#Crie um procedimento (função void) chamado imprimir_tabuada que receba um número inteiro
#e imprima na tela a tabuada desse número (de 1 a 10). 

def imprimir_tabuada(n):
    for i in range(1,11):
        print(f'{n}x{i} = {n*i}')

n=int(input('Digite um número inteiro: '))
print(imprimir_tabuada(n))