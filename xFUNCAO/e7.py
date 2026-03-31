import os
os.system('cls')
#Crie uma função chamada calcular_desconto que receba o preço de um produto e o percentual de desconto.
#A função deve retornar o novo preço final do produto com o desconto aplicado.

def calcular_desconto(num,porcent):
    desconto = num*(porcent/100)
    precodescont = num-desconto
    return precodescont

n=float(input('Digite o preço : R$ '))
desc=int(input('Digite o valor do desconto: '))
resultado = calcular_desconto(n, desc)
print('='*45)
print(f'O preço de {n} com desconto é: {resultado}')
print('='*45)
