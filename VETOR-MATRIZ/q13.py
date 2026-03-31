import os
os.system('cls')
#Escreva um programa que verifique se um dado array está estritamente ordenado em ordem crescente,
#retornando uma mensagem se verdadeiro ou falso

numeros=[]
for i in range(5):
    n=float(input(f'Digite o {i+1}° número: '))
    numeros.append(n)
    
ordenado=True

for i in range(len(numeros)-1):
    if numeros[i]>=numeros[i+1]:
        ordenado = False
        break

print('='*40)
print(f'Array: {numeros}')

if ordenado:
    print('A lista está estritamente ordenado em ordem crescente')
else:
    print('A lista NÃO está estritamente ordenado em ordem crescente')
print('='*40)