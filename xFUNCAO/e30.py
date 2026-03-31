import os
os.system('cls')
#Crie uma função chamada buscar_elemento que receba uma lista e um número alvo.
#A função deve procurar esse número na lista e devolver a posição (índice) da sua primeira ocorrência.
#Se o número não existir na lista, a função deve devolver -1.

def buscar_elemento(numeros,alvo):

    for i in range(len(numeros)):
        if numeros[i]==alvo:
            return i
    return -1
    
numeros=[]

for i in range(5):
    n=int(input(f'Digite o {i+1}° número inteiro: '))
    numeros.append(n)
print('='*40)
alvo=int(input('Digite o número alvo (int): '))
print('='*40)

resultado=buscar_elemento(numeros,alvo)
if resultado!=-1:
    print(f'O {alvo} aparece na posição {resultado} da lista')
else:
    print(f'O número {alvo} não foi encontrado na lista')
print('='*40)