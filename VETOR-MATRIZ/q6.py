import os
os.system('cls')
#Escreva um programa que receba um array de inteiros e crie dois novos arrays:
#um contendo apenas os números pares e outro apenas os ímpares do array original.

numeros = []

for i in range(4):
    num = int(input("Digite um número inteiro: "))
    numeros.append(num)

pares = []
impares = []

for i in range(len(numeros)):
    if numeros[i] % 2 == 0:
        pares.append(numeros[i])
    else:
        impares.append(numeros[i])
print('===================================')
print(f"Valores digitados: {numeros}")
print('===================================')
print(f"Números pares: {pares}")
print(f"Números ímpares: {impares}")
print('===================================')