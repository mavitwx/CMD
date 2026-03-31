import os
os.system('cls')

saldo=0
while True:
    print('================================')
    print('CAIXA ELETRÔNICO')
    print('1 - Saque')
    print('2 - Depósito')
    print('3 - Ver saldo')
    print('4 - Sair')
    
    opcao=int(input('Digite a opção que deseja (1 a 4): '))

    if opcao==1:
        valor=int(input('Digite o valor que deseja fazer o saque: R$ '))
        if valor<=0:
            print('================================')
            print('VALOR INVÁLIDO')
        elif valor>saldo:
            print('================================')
            print('SALDO INSUFICIENTE')
        else:
            saldo=saldo-valor
            print('================================')
            print('Saque realizado com sucesso!')

    elif opcao==2:
        valor=int(input('Digite o valor que deseja depositar: R$ '))
        if valor<=0:
            print('================================')
            print('VALOR INVÁLIDO')
        else:
            saldo=saldo+valor
            print('================================')
            print('Depósito realizado com sucesso!')
    elif opcao==3:
        print('================================')
        print(f'Saldo atual R$ {saldo:.2f}')
    elif opcao==4:
        print('================================')
        print('Encerrando...')
        break
    else:
        print('================================')
        print('OPCAO INVÁLIDA')
        