import os
os.system('cls')

vetor=[25,48,55,10,16,7,13,64]
print(vetor)
num=int(input('Digite o número para buscar: '))
ind=-1

for i in range(len(vetor)):
    if num==vetor[i]:
        ind=i
        break
if ind !=-1:
    print(f'Número encontrado no índice {ind}')
else:
    print('O número não está no vetor')