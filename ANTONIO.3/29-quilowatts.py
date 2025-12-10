import os
os.system('cls')

while True:
    gasto=float(input('Digite o valor de Kw gasto por residência: '))
    sal=float(input('Digite o valor do salário mínimo: R$ '))
    print('===================================')
    cad=sal/700
    kw=sal/700*gasto
    desc=kw*0.90
    print(f'O valor de cada Kw é {cad:.2f}')
    print(f'O valor a ser pago pela residência é: R$ {kw:.2f}')
    print(f'O valor a ser pago com um desconto de 10% é: R$ {desc:.2f}')
    print('===================================')
    res=input('Aplicar mais uma vez? (s/n): ').lower()
    if res!='s':
        break
    print('===================================')