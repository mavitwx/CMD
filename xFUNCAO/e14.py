import os
os.system('cls')
#Crie uma função chamada maior_da_lista que receba uma lista de números
#e devolva o maior valor encontrado nela (tente implementar a lógica com um ciclo for
#em vez de usar a função predefinida max()).

def maior_da_lista(nums):
    maior=nums[0]

    for num in nums:
        if num>maior:
            maior=num
    return maior

lista = []

for i in range(4):
    num = int(input(f'Digite o {i+1}° número: '))
    lista.append(num)

resultado = maior_da_lista(lista)
print('='*40)
print(f'Maior número da lista: {resultado}')
print('='*40)