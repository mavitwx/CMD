import os
os.system('cls')
#Dado um array numérico, mova todos os valores zero para o final do array,
#mantendo a ordem relativa dos elementos não nulos. Faça isso in-place, otimizando o uso de memória.
#Exemplo: [0, 1, 0, 3, 12, 0, 5] ficaria [1, 3, 12, 5, 0, 0, 0]

numeros=[]

for i in range(5):
    n=int(input(f'Digite o {i+1}° número: '))
    numeros.append(n)

posicao=0

for i in range(len(numeros)):
    if numeros[i] != 0:
        numeros[posicao] = numeros[i]
        posicao+=1

for i in range(posicao, len(numeros)):
    numeros[i]=0

print('='*40)
print(f'Array modificado: {numeros}')
print('='*40)