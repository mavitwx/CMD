while True:
    print('=====CALCULADORA BÁSICA=====')
    n1=int(input('Digite um número: '))
    n2=int(input('Digite outro número: '))
    print('============================')
    print('SOMA = 1')
    print('MULTIPLICAÇÃO = 2')
    print('DIVISÃO = 3')
    print('SUBTRAÇÃO = 4')
    print('=============================')
    op=int(input('DIGITE A OPERAÇÃO QUE DESEJA: '))
    if op==1:
        resul = n1+n2
    elif op==2:
        resul = n1*n2
    elif op==3:
        if n1==0:
            print('ERRO: DIVISÃO POR ZERO!')
        resul = n1/n2
    elif op==4:
        resul = n1-n2
    else:
        print('OPERAÇÃO INVÁLIDA')

    print(f'O resultado da operação é: {resul}')
    sair=input('Deseja sair? (s/n): ')
    if sair.lower()=='s':
        break