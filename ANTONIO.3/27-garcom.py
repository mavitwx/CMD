import os
os.system('cls')

comida=float(input('Digite o valor total da conta: R$ '))
taxa= comida*1.10
perg=input('Deseja pagar os 10% do garçom? (s/n) ').lower()
if perg== 's':
    print(f'O valor com a gorjeta ficou: R$ {taxa:.2f}')
else:
    print(f'O valor total da conta ficou: R$ {comida:.2f}')