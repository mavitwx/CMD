import os
os.system('cls')
#Dado um array e peça ao usuário que informe um número,
#desenvolva um algoritmo que conte quantas vezes esse número aparece no array.

vetor=[16,3,3,7,8,2,]
print(vetor)
num=int(input('Digite um número: '))

cont = 0

for i in range(len(vetor)):
    if num==vetor[i]:
        cont += 1
print('===============================================')
print(f'O número {num} aparece {cont} vezes no vetor')
print('===============================================')