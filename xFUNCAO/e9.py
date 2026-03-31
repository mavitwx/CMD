import os
os.system('cls')
#Crie uma função chamada calcular_fatorial que receba um número inteiro positivo
#e retorne o seu fatorial.

def calcular_fatorial(n):
    fatorial = 1
    
    for i in range(1,n+1):
        fatorial *= i
        
    return fatorial

n= int(input('Digite um número: '))
print(f'Fatorial de {n}: {calcular_fatorial(n)}')