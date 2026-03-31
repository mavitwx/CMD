import os
os.system('cls')
#Crie um programa que receba um vetor e um peça um número ao usuário.
#O programa deve retornar o índice da primeira ocorrência desse número no vetor
# ou -1 se ele não estiver presente.

vetor=[10,20,30,20]
print(vetor)

num=int(input('Digite o número a ser encontrado:'))
ind=-1

for i in range(len(vetor)):
    if num==vetor[i]:
        ind=i
        break
if ind==-1:
    print('================================================')
    print('O número digitado não está presente no vetor')
    print('================================================')

else:
    print('================================================')
    print(f'O número {num} está no índice {ind}')
    print('================================================')
