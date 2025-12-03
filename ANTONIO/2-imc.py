nome = input('Digite seu nome: ')
altura = float(input('Digite sua altura em metros: '))
peso = float(input('Digite seu peso em kg: '))

IMC =  peso/(altura * altura)
print(f'{nome} tem {altura} de altura e pesa {peso} kg.')
print(f'seu IMC é: {IMC:.2f}')