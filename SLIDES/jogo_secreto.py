import os
os.system('cls')

import random
n=random.randint(1,50)
tenta=0
while True:
    test=int(input('Tente adivinhar o número secreto! Digite: '))
    tenta+=1
    if test==n:
        print('Você acertou!! PARABÉNS')
        print(f'O número era {n}')
        print('                              ')
        print(f'Quantidade de tentativas: {tenta}')
        break
    elif test>n:
        print('Tente um MENOR')
    else:
        print('Tente um MAIOR')