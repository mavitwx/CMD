import os
os.system('cls')
#Crie uma função chamada calcular_media_lista que receba uma lista de números
#e devolva a média aritmética dos seus elementos. Se a lista estiver vazia, a função deve retornar 0.

def calcular_media_lista(numeros):
    if len(numeros)==0:
        print('A lista está vazia')
        return 0
    
    soma=0
    for n in numeros:
        soma+=n

    media=soma/len(numeros)
    return media

numeros=[]

for i in range(5):
    n=float((input(f'Digite o {i+1}° número: ')))
    numeros.append(n)

resultado=calcular_media_lista(numeros)
print('='*40)
print(f'A média dos números é = {resultado}')
print('='*40)