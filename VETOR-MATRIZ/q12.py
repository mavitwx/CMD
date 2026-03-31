import os
os.system('cls')
#Crie um algoritmo que desloque (rotacione) todos os elementos de um array para a direita em n posições
#(onde n é um número inteiro não negativo fornecido pelo usuário).
#Exemplo: considere o vetor [1, 2, 3, 4, 5, 6, 7], se k=3,
#novo vetor [5, 6, 7, 1, 2, 3, 4]


def rotacionar_direita(lista, k):
    n=len(lista)
    if n==0:
        return lista

    k=k%n
    return lista[-k:]+lista[:-k]

numeros=[]

for i in range(4):
    n=int(input(f'Digite o {i+1}° número: '))
    numeros.append(n)

k=int(input('Digite o valor de k: '))

resultado=rotacionar_direita(numeros, k)

print('='*40)
print(f'Lista original: {numeros}')
print(f'Lista rotacionado: {resultado}')
print('='*40)