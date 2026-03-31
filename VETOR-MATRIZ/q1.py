import os
os.system('cls')
#Escreva um programa que receba um array de números inteiros e
#retorne a soma de todos os seus elementos sem utilizar a função nativa.

nums1 = []
nums2 = []
somas = []

for i in range (1):
    num1= float(input(f'Digite o {i+1}º número: '))
    num2=float(input(f'Digite o {i+2}º número: '))
    nums1.append(num1)
    nums2.append(num2)
    somas.append(num1+num2)
    
for i in range(len(somas)):
    print(f'Resultado da soma: {somas[i]}')