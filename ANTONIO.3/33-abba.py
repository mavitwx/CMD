import os
os.system('cls')
while True:
    va=float(input('Digite um valor para A: '))
    vb=float(input('Digite um valor para B: '))
    print('===============================')
    print('Os valores estão sendo trocados...')
    print('                                ')
    print(f'O valor de A é: {vb:.2f}')
    print(f'O valor de B é: {va:.2f}')
    print('===================================')
    res=input('Aplicar mais uma vez? (s/n): ').lower()
    if res!='s':
        break
    print('===================================')