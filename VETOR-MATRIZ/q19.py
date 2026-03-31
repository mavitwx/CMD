import os
os.system('cls')
#Peça ao usuário para digitar 9 números para preencher uma matriz 3x3.
#Em seguida, mostre qual foi o maior e o menor número digitado
#e em quais posições (linha e coluna) eles estão.

matriz=[]

for i in range(3):
    linha=[]
    for j in range(3):
        num=int(input(f'Digite o valor para posição [{i}][{j}]: '))
        linha.append(num)
    matriz.append(linha)

maior=matriz[0][0]
menor=matriz[0][0]

posimaior=(0, 0)
posimenor=(0, 0)

for i in range(3):
    for j in range(3):
        if matriz[i][j]>maior:
            maior=matriz[i][j]
            posimaior=(i, j)
        
        if matriz[i][j]<menor:
            menor=matriz[i][j]
            posimenor=(i, j)
print('='*50)
print('Matriz:')
for linha in matriz:
    print(linha)
print('='*50)
print(f'Maior número: {maior} na posição {posimaior}')
print(f'Menor número: {menor} na posição {posimenor}')
