import os
os.system('cls')
#Crie uma função chamada eh_ano_bissexto que receba um ano (inteiro)
#e devolva True se o ano for bissexto e False caso não seja.
#Um ano é bissexto se for divisível por 4, mas não por 100, exceto se for também divisível por 400).

def eh_ano_bissexto(ano):
    if (ano%4==0 and ano%100 != 0) or (ano % 400 == 0):
        return True
    else:
        return False

ano=int(input('Digite o ano: '))
resultado=eh_ano_bissexto(ano)
print(resultado)

if resultado:
    print('É BISSEXTO')
else:
    print('NÃO é bissexto')