import os
os.system('cls')
while True:
    x=int(input('Digite um número: '))
    if x%2==0:
        print('O número é PAR!')
    else:
        print('O número é ÍMPAR!')
        print('===================================')
    res=input('Aplicar mais uma vez? (s/n): ').lower()
    if res!='s':
        break
    print('===================================')
