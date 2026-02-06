import os
os.system('cls')

#Criar um algoritmo que imprima os 10 primeiros termos da série de Fibonacci.
a=0
b=1
print(0)
print(1)
for i in range(8):
    c=a
    a=b
    b=c+b
    print(b)