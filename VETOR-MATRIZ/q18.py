import os
os.system('cls')
#Crie uma matriz 3x3 preenchida com números aleatórios (pode pedir para o usuário informá-los).
#Escreva um programa que conte quantos números pares e quantos números ímpares existem nela.

matriz = []

for i in range(3):
    linha = []
    for j in range(3):
        num = int(input(f'Digite o valor para posição [{i}][{j}]: '))
        linha.append(num)
    matriz.append(linha)

pares=0
impares=0

for linha in matriz:
    for elemento in linha:
        if elemento%2==0:
            pares+=1
        else:
            impares+=1
print('='*40)
print("Matriz:")
for linha in matriz:
    print(linha)
print('='*40)
print(f'Quantidade de números pares: {pares}')
print(f'Quantidade de números ímpares: {impares}')
print('='*40)