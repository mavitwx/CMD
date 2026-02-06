import os
os.system('cls')

while True:
    n=float(input('Digite um número: '))
    if n>0:
        print(f'O número {n:+} é positivo!')
    elif n<0:
        print(f'O número {n:+} é negativo!')
    else:
        print(f'O número {n} é nulo!')
    print('===================================')
    res=input('Aplicar mais uma vez? (s/n): ').lower()
    if res!='s':
        break
    print('===================================')