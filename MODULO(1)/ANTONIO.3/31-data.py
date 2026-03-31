import os
os.system('cls')
while True:

    n=int(input('Digite uma data (ddmmaaaa): '))
    dia=n//1000000
    mes=n%1000000//10000
    ano=n%10000
    print(f'Dia: {dia:02d}')
    print(f'Mês: {mes:02d}')
    print(f'Ano: {ano:04d}')
    print('===================================')
    res=input('Aplicar mais uma vez? (s/n): ').lower()
    if res!='s':
        break
    print('===================================')