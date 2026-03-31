import os
os.system('cls')
#Crie uma função chamada eh_par que receba um número inteiro.
#A função deve retornar True se o número for par e False se for ímpar.

def eh_par(num):
    if num%2==0:
        print('é PAR')
        return True
    else:
        print('é ÍMPAR')
        return False
    
num=int(input('Digite um número inteiro: '))
resultado=eh_par(num)
print(resultado)