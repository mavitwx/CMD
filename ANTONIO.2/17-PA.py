while True:
    a1 =  int(input('Primeiro termo: '))
    r= int(input('Razão: '))
    n=int(input('Termo que deseja descobrir: '))
    an = a1+(n-1)*r
    print(f'O {n}° termo é: {an}')

    sair=input('Deseja sair? (s/n): ')
    if sair.lower()=='s':
        break