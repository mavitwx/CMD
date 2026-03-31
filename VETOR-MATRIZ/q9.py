import os
os.system('cls')
#Crie um algorítmo que determine se um array é um palíndromo, ou seja, se a sequência de elementos
#lida da esquerda para a direita é idêntica ao ser lida da direita para a esquerda.

A = [1,2,3,2,1]
print(A)

palindromo=True

for i in range(len(A)//2):
    if A[i]!=A[len(A)-1-i]:
        palindromo=False
        break

if palindromo:
    print('É um palíndromo!')
else:
    print('NÃO é um palíndromo')