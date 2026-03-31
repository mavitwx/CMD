import os
os.system('cls')
#Crie uma função chamada contar_pares_lista que receba uma lista de números inteiros como parâmetro
#e devolva a quantidade de números pares que existem dentro dessa lista.

def contar_pares_lista(nums):
    contador=0

    for num in nums:
        if num%2==0:
            contador+=1
    return contador

lista=[]

for i in range(5):
    num=float(input(f'Digite o {i+1}° número: '))
    lista.append(num)

resultado=contar_pares_lista(lista)
print('='*40)
print(f'Números pares: {resultado}')
print('='*40)