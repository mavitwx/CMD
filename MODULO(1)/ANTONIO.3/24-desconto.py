import os
os.system('cls')

val=float(input('Digite o valor de um produto: '))
while True:
    val*=0.81
    print(f'O valor do produto com desconto é: {val:.2f}')
    res=input('Aplicar mais uma vez? (s/n): ').lower()
    if res!='s':
        break