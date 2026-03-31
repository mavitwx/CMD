import os
os.system('cls')
#Crie uma função chamada inverter_lista que receba uma lista
#e devolva uma nova lista com os elementos na ordem inversa. (Neste exercício, crie a lógica algorítmica
#com um laço de repetição, evitando usar os atalhos prontos do Python como lista[::-1]).

def inverter_lista(lista):
    inverso=[]  
    for i in range(len(lista)-1,-1,-1):
        inverso.append(lista[i])
    return inverso

numeros = [1,2,3,4,5]
print(inverter_lista(numeros))

