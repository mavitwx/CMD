print('Calculadora TOP')

n1= float(input('Digite o primeiro número: '))
n2= float(input('Digite o segundo número: '))

print('Escolha a operação')
print('1 SOMA')
print('2 MULTIPLICAR')
print('3 SUBTRAÇÃO')
print('4 DIVISÃO')

op= input('Opção: ')
if op == '1':
    resultado = n1+n2
elif op == '2':
    resultado = n1*n2
elif op == '3':
    resultado = n1-n2
elif op == '4':
    resultado = n1/n2
else: print('OPÇÃO INVÁLIDA!!') and exit()

print('Resultado:',resultado)