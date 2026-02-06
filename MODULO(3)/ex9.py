import os
os.system('cls')

#Criar um algoritmo que leia um número que servirá para controlar os primeiros números ímpares.
#Deverá ser impressa a soma desses números. Suponha que num será maior que zero.
num=int(input('Digite um número maior que zero: '))
soma=0
for i in range(1,num*2+1,2):
    print(i)
    soma+=i
print(f'Soma: {soma}')