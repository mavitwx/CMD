import os
os.system('cls')
#Crie um algoritmo que copie os elementos de um vetor A para um vetor B,
#mas armazenando-os na ordem inversa.

A = [1, 2, 3, 4, 5]
B = []

for i in range(len(A)-1, -1, -1):
    B.append(A[i])

print(f"Vetor A: {A}")
print(f"Vetor B: {B}")