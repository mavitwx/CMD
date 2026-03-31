import os
os.system('cls')

estoq=int(input('Digite quantos sacos de cimentos estão disponíveis: '))
preco=float(input('Digite o valor de cada cimento: '))
while True:
    if estoq<=100:
        break
    cod=int(input('Digite seu código do cliente: '))
    if cod==0:
        break
    saco=int(input('Digite a quantidade de sacos que deseja comprar: '))
    if estoq<saco:
        print('====================================')
        print('Estoque Insuficiente')
    elif 0.10*estoq<saco:
        print('====================================')
        print('Ultrapassado o máximo permitido')
    else:
        print('====================================')
        print(f'Código do cliente: {cod}')
        print(f'Quantidade de sacos pedidos: {saco}')
        print(f'Valor do pedido: {preco*saco}')
        print('====================================')
        estoq=estoq-saco
print(f'Estoque: {estoq}')