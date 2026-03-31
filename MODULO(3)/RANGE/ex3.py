import os
os.system('cls')

#Entrar com 10 números e imprimir a metade de cada número.
for i in range(1,11):
    num = float(input(f"Digite o {i}º número: "))
    print(f'Metade de {num} é {num/2}')