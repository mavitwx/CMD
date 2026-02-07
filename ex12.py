import os
os.system('cls')

#Entrar com números enquanto forem positivos e imprimir quantos números foram digitados.
contador = 0
while True:
    num=int(input(f'Digite o {contador+1}º número (negativo para sair): '))
    if num<0:
        print('Você digitou um número negativo!')
        break
    contador = contador+1
print(f'Quantidade de números positivos digitados: {contador}')
