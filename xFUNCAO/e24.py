import os
os.system('cls')
#Crie uma função chamada filtrar_pares que receba uma lista de números
#e devolva uma nova lista contendo apenas os números pares encontrados na lista original.

def filtrar_pares(numeros):
    pares=[]

    for n in numeros:
        if n%2==0:
            pares.append(n)
    return pares

numeros=[]

for i in range(5):
    n=int(input(f'Digite o {i+1}° número inteiro: '))
    numeros.append(n)
print('='*40)

resultado=filtrar_pares(numeros)
print(f'Lista somente som os números pares: {resultado}')
print('='*40)
