import os
os.system('cls')

#Entrar com a idade de várias pessoas e imprimir quantas pessoas são menores de idade.
#O programa deve parar caso o usuário informe uma idade inferior a 1.
contador=0
while True:
    id=int(input(f'Digite a idade da {contador+1}º pessoa: '))
    if id<1:
        print('                            ')
        print('Parando... Idade inferior a 1')
        break
    elif id<18:
        contador=contador+1
print(f'A quantidade de pessoas menores de idade são: {contador}')