import os
os.system('cls')
#Implemente um programa que calcule a média dos valores armazenados
#em um vetor de números de ponto flutuante.

numeros = []
for i in range (2):
    n=float(input(f'Digite o {i+1}º número: '))
    numeros.append(n)

media=sum(numeros)/len(numeros)

print('=====================================================')
print(f'A média dos números é: {media} ')
print('=====================================================')