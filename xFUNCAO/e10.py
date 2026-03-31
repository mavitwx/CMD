import os
os.system('cls')
#Crie uma função chamada eh_primo que receba um número inteiro
#e retorne True se ele for primo (divisível apenas por 1 e por ele mesmo) e False caso contrário.

def eh_primo(n):
    if n<= 1:
        return False
    
    for i in range(2,n):
        if n%i==0:
            return False
    
    return True


n=int(input('Digite um número inteiro: '))

if eh_primo(n):
    print('É PRIMO')
else:
    print('NÃO é primo')