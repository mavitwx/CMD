import os
os.system('cls')

while True:
    x=float(input('Digite um número: '))
    y=float(input('Digite outro número: '))
    print('                               ')
    if x>y:
        print(f'O número {x} é maior que {y}')
    elif x<y:
        print(f'O número {y} é maior que {x}')
    elif x==y:
        print(f'Os números são iguais!')
    print('===================================')
    res=input('Aplicar mais uma vez? (s/n): ').lower()
    if res!='s':
        break
    print('===================================')