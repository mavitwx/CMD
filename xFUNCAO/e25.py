import os
os.system('cls')
#Crie uma função chamada multiplicar_lista que receba uma lista de números e um valor multiplicador(fator)
#A função deve devolver uma nova lista onde cada elemento da original foi multiplicado por esse fator.

def multiplicar_lista(numeros,fator):
    novalista=[]

    for n in numeros:
        novalista.append(n*fator)

    return novalista

numeros=[]

for i in range(3):
    n=int(input(f'Digite o {i+1}° número inteiro: '))
    numeros.append(n)
print('='*40)
fator=float(input('Digite o valor multiplicador: '))
print('='*80)

resultado=multiplicar_lista(numeros,fator)
print(f'Nova lista com cada elemento multiplicado pelo fator: {resultado}')
print('='*80)
