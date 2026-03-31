import os
os.system('cls')
#Crie uma matriz quadrada 4x4 preenchida com números aleatórios (ou fixos de sua escolha).
#Imprima apenas os elementos da diagonal principal
#(aqueles onde o índice da linha é igual ao índice da coluna, ex: [0][0], [1][1]...).

matriz = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 27, 15, 8],
    [10, 13, 16, 46]
]

print('Elementos da diagonal principal:')

print('='*35)
for i in range(4):
    print(matriz[i][i])
print('='*35)