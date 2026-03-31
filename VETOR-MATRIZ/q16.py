import os
os.system('cls')
#Dada a matriz M = [[5, 8, 2], [12, 90, 3], [7, 4, 11]],
#escreva um programa que peça ao usuário para digitar um número
#e verifique se esse número existe dentro da matriz.

M=[[5, 8, 2], [12, 90, 3], [7, 4, 11]]
print(f'Matriz: {M}')

numero = int(input("Digite um número: "))
print('='*40)
encontrado = False

for linha in M:
    for elemento in linha:
        if elemento==numero:
            encontrado=True

if encontrado:
    print(f"O número {numero} está na matriz")
else:
    print(f"O número {numero} NÃO está na matriz")
print('='*40)