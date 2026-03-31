import os
os.system('cls')

hora=float(input('Digite o valor da hora aula : R$ '))
aula=int(input('Digite o número de aulas dadas no mês: '))
inss=float(input('Digite o percentual de desconto do INSS (%): '))

sbruto=hora*aula
dinss=sbruto*(inss/100)
sliq=sbruto-dinss
print('===================================')
print(f'Salário bruto: R$ {sbruto:.2f}')
print(f'Desconto do INSS: R$ {dinss:.2f}')
print(f'Salário líquido: R$ {sliq:.2f}')
print('====================================')
