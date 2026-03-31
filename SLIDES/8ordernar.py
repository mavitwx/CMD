import os
os.system('cls')

vetor = [64, 34, 25, 12, 22, 11, 90]
for i in range(len(vetor)):
    ind_menor = i

    for j in range(i + 1, len(vetor)):
        if vetor[j] < vetor[ind_menor]:
            ind_menor = j

    if ind_menor != i:
        aux = vetor[i]
        vetor[i] = vetor[ind_menor]
        vetor[ind_menor] = aux

print("Vetor ordenado:", vetor)