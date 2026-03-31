import os
os.system('cls')

while True:
    hor=float(input('Digite o valor da hora atual: '))
    min=ho*60
    print(f'Foram passados {min} minutos desde o início do dia!')
    sair=input('Deseja sair? (s/n): ')
    if sair.lower()=='s':
        break