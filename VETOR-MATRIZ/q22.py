import os
os.system('cls')
#Crie uma matriz 2x2 e peça para o usuário digitar um número multiplicador (escalar).
#O programa deve multiplicar todos os elementos da matriz por esse número e imprimir a nova matriz modificada.

matriz=[]

for i in range(2):
    linha=[]
    for j in range(2):
        n=int(input(f'Digite o valor para posição [{i}][{j}]: '))
        linha.append(n)
    matriz.append(linha)
print('='*35)
escalar=int(input("Digite o número multiplicador: "))
print('='*35)
for i in range(2):
    for j in range(2):
        matriz[i][j]*=escalar

print('Matriz modificada:')
for linha in matriz:
    print(linha)
print('='*35)