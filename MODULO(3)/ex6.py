import os
os.system('cls')

#Criar um algoritmo que leia um número que servirá para
#controlar os números pares que serão impressos a partir de dois (2)
qntd=int(input('Digite quantos números pares deseja imprimir: '))
num=2
for i in range(2,qntd*2+1,2):
    print(i)