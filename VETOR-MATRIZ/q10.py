import os
os.system('cls')
#Escreva um programa que dado um array ordenado, remova os elementos duplicados
#de forma que cada elemento apareça apenas uma vez e retorne o novo comprimento do array modificado.

numeros=[]
for i in range(5):
    n=int(input(f'Digite o {i+1}° número: '))
    numeros.append(n)
print('='*40)

def remover_duplicados_ordenado(array):
    if len(array) == 0:
        return 0
    
    j=0
    for i in range(1, len(array)):
        if array[i]!=array[j]:
            j+=1
            array[j]=array[i]  
    return j+1  

comprimentonv=remover_duplicados_ordenado(numeros)

print(f'Novo comprimento do array: {comprimentonv}')
print(f'Array modificado: {numeros[:comprimentonv]} ')
print('='*40)