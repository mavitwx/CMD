import os
os.system('cls')
#Escreva um programa que inverta a ordem dos elementos de um array no próprio array
#(sem criar um array auxiliar na memória), trocando os elementos das extremidades em direção ao centro.
#Exemplo: o vetor [10,20, 25, 27,30,40] ficaria desta forma [40,30, 27,25, 20,10]

A = [10,20,30,40,50]
print(A)

trocas=len(A)//2

for i in range(trocas):
    A[i],A[len(A)-1-i] = A[len(A)-1-i],A[i]

print(f"Vetor trocado: {A}")