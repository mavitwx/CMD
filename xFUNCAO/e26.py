import os
os.system('cls')
#Crie uma função chamada esta_ordenada que receba uma lista de números
#e devolva True se a lista estiver estritamente ordenada de forma crescente e False caso contrário.

def esta_ordenada(numeros):
    comparacoes=len(numeros)-1

    for i in range(comparacoes):
        print(i)
        if numeros[i]>=numeros[i+1]:
            return False
        
    return True

numeros=[]
for i in range(5):
    n=float(input(f'Digite o {i+1}° número: '))
    numeros.append(n)
    
print(esta_ordenada(numeros))