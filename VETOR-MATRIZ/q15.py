import os
os.system('cls')
#Crie uma matriz 3x3 onde todos os elementos sejam 0,
#exceto os elementos da diagonal principal, que devem ser 1. Imprima a matriz na tela, linha por linha.

matriz=[]
for i in range(3):
    linha=[]
    for j in range(3):
        if i==j:
            linha.append(1)
        else:
            linha.append(0)
    matriz.append(linha)


for linha in matriz:
    print(linha)
