import os
os.system('cls')
#Crie uma função chamada calcular_imc que receba o peso (em kg) e a altura (em metros)
#de uma pessoa e devolva o valor do seu IMC. (Fórmula: IMC = peso / (altura * altura))

def calcular_imc(peso,altura):
    imc=peso/(altura*altura)
    return imc

peso=float(input('Digite o valor do peso (kg): '))
altura=(float(input('Digite o valor da altura (m): ')))

resultado=calcular_imc(peso,altura)
print('='*40)
print(f'Resultado do IMC: {resultado:.2f}')
print('='*40)
