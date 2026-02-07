import os
os.system('cls')

#Entrar com vários números positivos e imprimir a média dos números digitados.
contador=0
soma=0
while True:
    num=int(input(f'Digite o {contador+1}º número (negativo para sair): '))
    if num<0:
        break
    contador=contador+1
    soma=soma+num
media=soma/contador
print(f'A média dos números é {soma}/{contador} = {media}')
