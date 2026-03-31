import os
os.system('cls')

#Criar um algoritmo que leia um número e imprima todos os números de 1 até o número lido e o seu produto
n=int(input('Digite um número: '))
produto=n
for i in range(1,n+1):
    produto*=i
    print(f'Número: {i} | {i}x{n}: {produto}')