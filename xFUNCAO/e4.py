import os
os.system('cls')
#Crie uma função chamada retornar_maior que receba dois números
#e retorne o maior entre eles. Se forem iguais, pode retornar qualquer um dos dois.

def retornar_maior(a,b,):
    if a>b:
        print(f'{a} > {b}')
        return a
    elif b>a:
        print(f'{b} > {a}')
        return b
    else:
        print('Os números são iguais')

a=float(input('Digite o primeiro número: '))
b=float(input('Digite o segundo número: '))

resultado=retornar_maior(a,b)
print(resultado)    