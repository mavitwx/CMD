import os
os.system('cls')

vpres=float(input('Digite o valor da prestação: R$ '))
taxa=float(input('Digite o valor da taxa de juros (% ao mês): '))
tempo=int(input('Digite o tempo de atraso (em meses): '))

prest= vpres+(vpres*(taxa/100)*tempo)
print('==================================')
print(f'O valor da prestação em atraso é: R$ {prest:.2f}')
print('==================================')