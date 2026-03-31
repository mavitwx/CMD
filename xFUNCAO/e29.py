import os
os.system('cls')
#Crie uma função chamada remover_duplicados que receba uma lista contendo números repetidos
#e devolva uma nova lista contendo apenas valores únicos, preservando a ordem da primeira vez que aparecem.

def remover_duplicados(lista):
    novalista=[]

    for n in lista:
        if n not in novalista:
            novalista.append(n)
    return novalista

numeros=[]

for i in range(4):
    n=int(input(f'Digite o {i+1}° número inteiro: '))
    numeros.append(n)

resultado=remover_duplicados(numeros)
print(f'Nova lista sem duplicados: {resultado}')