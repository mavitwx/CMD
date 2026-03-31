import os
os.system('cls')
#Crie uma matriz 2x3 (2 linhas e 3 colunas) com números inteiros de sua escolha.
#Calcule e imprima a média de todos os elementos dessa matriz.

matriz=[
    [3, 13, 8],
    [15, 27, 16]
]

soma=0
qtd=0

for linha in matriz:
    for elemento in linha:
        soma+=elemento
        qtd+=1

media=soma/qtd

print("Matriz:")
for linha in matriz:
    print(linha)
print('='*35)
print(f"Média dos elementos: {media:.2f}")
print('='*35)