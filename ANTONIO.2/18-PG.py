while True:
    a1 =  int(input('Primeiro termo: '))
    r= int(input('Razão: '))
    n=int(input('Termo que deseja descobrir: '))
    an=a1*r**(n-1)
    print(f'O {n}° termo é: {an}')
    
    sair=input('Deseja sair? (s/n): ')
    if sair.lower()=='s':
        break