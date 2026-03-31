import os
os.system('cls')
#Desenvolva um algoritmo para encontrar o segundo maior valor em um array de inteiros
#em uma única passagem, sem ordenar o array previamente.

def segundo_maior(A):
    if len(A)<2:
        return None

    maior=float('-inf') #infinito
    segundo_maior=float('-inf')

    for num in A:
        if num>maior:
            segundo_maior=maior
            maior=num
        elif num>segundo_maior and num!=maior:
            segundo_maior=num

    return segundo_maior

numeros=[]

for i in range(4):
    n=int(input(f'Digite o {i+1}° número inteiro: '))
    numeros.append(n)

resultado=segundo_maior(numeros)

print('='*40)
print(f'Lista: {numeros}')
print(f'Segundo maior valor: {resultado}')
print('='*40)