import os
os.system('cls')

while True:
    valor=float(input('Digite um valor: R$ '))
    dolar=valor/5.43
    print(f'O valor em dólares é: {dolar:.2f} U$')
    print('===================================')
    res=input('Aplicar mais uma vez? (s/n): ').lower()
    if res!='s':
        break
    print('===================================')