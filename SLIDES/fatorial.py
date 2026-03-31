import os
os.system('cls')

while True:
    import math
    n=int(input('Digite um número (0) p/sair: '))
    fatorial=math.factorial(n)
    print(f'Resultado de {n} fatorial = {fatorial}')
    if n==0:
        break