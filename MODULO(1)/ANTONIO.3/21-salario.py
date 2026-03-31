import os
os.system('cls')

while True:
    salmi=float(input('Digite o valor do salário mínimo: '))
    sal1=float(input('Digite o valor do salário da pessoa: '))
    op=sal1/salmi
    print(f'Essa pessoa ganha aproximadamente {op:.2f} salário(s) mínimo(s)')
    sair=input('Deseja sair? (s/n): ')
    if sair.lower()=='s':
        break
