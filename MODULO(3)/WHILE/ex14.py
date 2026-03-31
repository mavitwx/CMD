import os
os.system('cls')

#Ler vários números e informar quantos números entre 100 e 200 foram digitados.
#Quando o valor 0 (zero) for lido, o algoritmo deverá cessar sua execução
contador=0
while True:
    num=int(input(f'Digite um número (0 para sair): '))
    if num==0:
        break
    elif 100<num<200:
        contador=contador+1
print(f'A quantidade de números entre 100 e 200 foram: {contador}')