import os
os.system('cls')

while True:
    n=int(input('Digite um número inteiro de 3 dígitos: '))
    c=n//100
    d=(n//10)%10
    u=n%10
    print(f'O número ao contrário é: {u}{d}{c}')
    print('===================================')
    res=input('Aplicar mais uma vez? (s/n): ').lower()
    if res!='s':
        break
    print('===================================')