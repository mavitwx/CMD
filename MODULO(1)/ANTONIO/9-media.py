import os
os.system('cls')
while True:
    n1=float(input('Digite sua primeira nota: '))
    n2=float(input('Digite sua segunda nota: '))
    n3=float(input('Digite sua terceira nota: '))
    media=(n1+n2+n3)/3
    print(f'Sua média é: {media:.2f}')
    print('===================================')
    res=input('Aplicar mais uma vez? (s/n): ').lower()
    if res!='s':
        break
    print('===================================')