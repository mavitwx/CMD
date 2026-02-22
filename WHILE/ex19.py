import os
os.system('cls')

#Entrar com a idade de várias pessoas e imprimir:
#total de pessoas com menos de 21 anos.
#total de pessoas com mais de 50 anos.
#O programa deve parar se uma das idades não estiverem no intervalo de 0 a 120 anos.
menor=0
maior=0
contador=0
while True:
    id=int(input(f'Digite a idade da {contador+1}º pessoa: '))
    if id<0 or id>120:
        print('                            ')
        print('Parando... Idade não está presente no intervalo (0 a 120)')
        print('                            ')
        break
    elif id<21:
        menor=+1
    elif id>50:
        maior+=1
    contador=+1
print(f'A quantidade de pessoas menores de idade são: {menor}')
print(f'A quantidade de pessoas com mais de 50 anos são: {maior}')
print('                            ')