import os
os.system('cls')
#Crie uma função chamada unir_listas que receba duas listas distintas
#e devolva uma terceira lista que seja a junção (concatenação) das duas primeiras.

def unir_listar(l1,l2):
    novalista=[]

    for item in l1:
        novalista.append(item)

    for item in l2:
        novalista.append(item)

    return novalista

l1=[]
for i in range(3):
    txt=input(f'Digite a {i+1}° palavra da lista 1: ')
    l1.append(txt)
print('='*55)
l2=[]
for i in range(3):
    txt=input(f'Digite a {i+1}° palavra da lista 2: ')
    l2.append(txt)
print('='*55)
resultado=unir_listar(l1,l2)
print(f'Listas unidas: {resultado}')
print('='*55)