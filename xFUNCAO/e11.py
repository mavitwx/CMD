import os
os.system('cls')
#Crie uma função chamada eh_palindromo que receba uma palavra (string)
#e devolva True se a palavra for um palíndromo e False caso contrário.

def eh_palindromo(texto):
    if texto==texto[::-1]:
        print('É UM PALÍNDROMO')
        return True
    else:
        print('NÃO é um palíndromo')
        return False
    
texto=input('Digite uma palavra: ')
resultado=eh_palindromo(texto)
print(resultado)