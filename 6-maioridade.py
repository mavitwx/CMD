import os
os.system('cls')

while True:
    ida=int(input('Digite sua idade: '))
    if ida>=18:
        print(f'Você tem {ida} anos e é maior de idade')
    elif ida<18:
        print(f'Você tem {ida} anos e é menor de idade')
    print('===================================')
    res=input('Aplicar mais uma vez? (s/n): ').lower()
    if res!='s':
        break
    print('===================================')