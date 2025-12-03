import os
os.system('cls')

prim = float(input('Digite um número: '))
seg = float(input('Digite outro número: '))

if prim < seg:
    print(f'A ordem é: {prim} ; {seg}')
elif prim > seg:
    print(f'A ordem é: {seg} ; {prim}')
else:
    print(f'{prim} e {seg} são número iguais!')



