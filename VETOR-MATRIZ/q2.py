import os
os.system('cls')
#Dado um array numérico, crie um algoritmo que encontre e imprima o maior
#e o menor valor presentes nele, iterando sobre o vetor apenas uma vez.

numeros=[]

for i in range(2):
    num=float(input(f'Digite o {i+1}º número: '))
    numeros.append(num)

maior=numeros[0]
menor=numeros[0]

for num in numeros:
    if num>maior:
        maior=num
    elif num<menor:
        menor=num
print('=================================')
print(f'Maior++ valor: {maior}')
print(f'Menor-- valor: {menor}')
print('=================================')
