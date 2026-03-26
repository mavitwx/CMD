import os
os.system('cls')

def calcular_desconto(num,porcent):
    desconto = num*(porcent/100)
    precodescont = num-desconto
    return precodescont

n=float(input('Digite o preço : R$ '))
desc=int(input('Digite o valor do desconto: '))
resultado = calcular_desconto(n, desc)
print(f'O preço de {n} com desconto é: {resultado}')