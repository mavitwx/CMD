import os
os.system('cls')

while True:
    num=int(input('Digite um número inteiro de 3 dígitos: '))
    dezen=(num//10)%10
    print(f'O algarismo da casa das dezenas é {dezen}')
    print('===================================')
    res=input('Aplicar mais uma vez? (s/n): ').lower()
    if res!='s':
        break
    print('===================================')