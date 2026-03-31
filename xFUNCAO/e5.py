import os
os.system('cls')
#Crie uma função chamada celsius_para_fahrenheit que receba uma temperatura em graus Celsius
#e retorne o valor convertido para Fahrenheit. (Fórmula: F = C * 1.8 + 32)

def celsius_para_fahrenheit(c):
    f=c*1.8+32
    return f

c=float(input('Digite o valor da temperatura em CELSIUS: '))

resultado=celsius_para_fahrenheit(c)
print('=============================================')
print(f'A temperatura convertida para Fahrenheit é: {resultado}')
print('=============================================')
