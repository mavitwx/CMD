import os
os.system('cls')

soma=0
while True:
    num=float(input('Digite um número (0 p/ sair): '))
    soma+=num
    if num==0:
        break
print(f'Soma: {soma:.2f}')