import os
os.system('cls')
#Crie uma função chamada calcular_media que receba três notas de um aluno
#e retorne a média aritmética dessas notas.

def calcular_media(a,b,c):
    media=(a+b+c)/3
    return media
a=float(input('Digite a primeira nota: '))
b=float(input('Digite a segunda nota: '))
c=float(input('Digite a terceira nota: '))

resultado=calcular_media(a,b,c)
print('==========================================')
print(f'A média dessas 3 notas é: {resultado:.2f}')
print('==========================================')
