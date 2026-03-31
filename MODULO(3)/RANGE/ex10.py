import os
os.system('cls')

#Criar um algoritmo que imprima os 10 primeiros termos da série de Fibonacci.
a=0
b=1
posicao=int(input('Digite a posição da sequência que deseja: '))
print(0)
print(1)
for i in range(posicao-2):
    c=a
    a=b
    b=c+b
    print(b)