import os
os.system('cls')
#Crie uma função chamada contar_vogais que receba uma palavra ou frase (string)
#e retorne a quantidade de vogais (a, e, i, o, u) presentes nela

def contar_vogais(texto):
    contador=0
    vogais='aeiouAEIOU'

    for xletra in texto:
        if xletra in vogais:
            contador += 1
            
    return contador

texto=input('Digite uma palavra ou frase: ')
print(f'Quantidade de vogais: {contar_vogais(texto)}')