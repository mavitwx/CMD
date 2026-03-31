import os
os.system('cls')
#Crie uma função chamada somar_tres_numeros que receba três números como parâmetros
#e retorne a soma deles.


def somar_tres_numeros(n1,n2,n3):
    soma=n1+n2+n3
    return soma
n1=float(input('Digite o primeiro número: '))
n2=float(input('Digite o segundo número: '))
n3=float(input('Digite o terceiro número: '))

resultado = somar_tres_numeros(n1, n2, n3)
print('===============================================')
print(f'A soma de {n1} + {n2} + {n3} = {resultado}')
print('===============================================')
