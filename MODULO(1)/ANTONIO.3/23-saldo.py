import os
os.system('cls')

sal=float(input('Digite o saldo da aplicação: '))
while True:
    sal*=1.01
    print(f'Seu novo saldo é: {sal:.2f}')

    res=input('Aplicar mais uma vez? (s/n): ').lower()
    if res!='s':
        break