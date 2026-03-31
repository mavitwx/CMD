import os
os.system('cls')
#Crie duas matrizes A e B, ambas de tamanho 2x2, preenchidas com números inteiros.
#Crie uma terceira matriz C (inicialmente vazia ou cheia de zeros) que seja o resultado da soma de A e B.
#com valores fixos!

a=[
    [1, 2],
    [3, 4]
]

b=[
    [5, 6],
    [7, 8]
]

c=[
    [0, 0],
    [0, 0]
]

for i in range(2):
    for j in range(2):
        c[i][j] = a[i][j] + b[i][j]

print('Matriz A:')
for linha in a:
    print(linha)

print('='*35)

print('Matriz B:')
for linha in b:
    print(linha)

print('='*35)

print('Matriz C (A + B):')
for linha in c:
    print(linha)
    
print('='*35)