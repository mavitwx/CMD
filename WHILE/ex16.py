import os
os.system('cls')

#Elabore um algoritmo que leia vários números inteiros, encerrando a leitura quando for digitado o valor -999.
#Para cada número informado o programa deve calcular e imprimir todos os seus divisores
contador=0
while True:
    num=int(input(f'Digite o {contador+1}º número (-999 p/ sair): '))
    if num==-999:
        break
    print(f'Divisores de {num}: ')
    
