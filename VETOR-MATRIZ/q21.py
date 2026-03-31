import os
os.system('cls')
#Dada uma matriz 3x3, crie um programa que calcule a soma dos elementos de cada linha separadamente
#e guarde os resultados em uma lista simples. Imprima a lista resultante.
matriz=[
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

somas=[]

for linha in matriz:
    soma_linha=0
    for elemento in linha:
        soma_linha+=elemento
    somas.append(soma_linha)
print('='*35)
print('Matriz:')
for linha in matriz:
    print(linha)
print('='*35)
print('Soma de cada linha:')
print(somas)
print('='*35)