import os
os.system('cls')
#Crie uma função chamada classificar_imc que receba o valor do IMC (calculado na questão anterior)
#e devolva uma string com a classificação: "Abaixo do peso" (menor que 18.5),"Peso normal" (18.5 a 24.9),
#"Excesso de peso" (25 a 29.9) ou "Obesidade" (30 ou mais).

def calcular_imc(peso,altura):
    imc=peso/(altura*altura)
    return imc

peso=float(input('Digite o valor do peso (kg): '))
altura=(float(input('Digite o valor da altura (m): ')))
resultado=calcular_imc(peso,altura)

if resultado<18.5:
    print('='*40)
    print('Abaixo do peso')
elif resultado>18.5 and resultado<24.9:
    print('='*40)
    print('Peso normal')
elif resultado>25 and resultado<29.9:
    print('='*40)
    print('Excesso de peso')
else:
    print('='*40)
    print('Obesidade')

print(f'Resultado do IMC: {resultado:.2f}')
print('='*40)