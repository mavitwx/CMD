import os
os.system('cls')
#Crie uma função chamada contar_ocorrencias que receba uma lista de números e um número "alvo".
#A função deve devolver quantas vezes o número alvo aparece dentro da lista.

def contar_ocorrencias(numeros,alvo):
    contador=0

    for n in numeros:
        if n==alvo:
            contador+=1
    return contador
    
numeros=[]

for i in range(5):
    n=int(input(f'Digite o {i+1}° número inteiro: '))
    numeros.append(n)
print('='*40)
alvo=int(input('Digite o número alvo (int): '))
print('='*40)

resultado=contar_ocorrencias(numeros,alvo)
print(f'O alvo aparece {resultado} vezes na lista')
print('='*40)