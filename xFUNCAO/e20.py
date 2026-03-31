import os
os.system('cls')
#Crie uma função chamada remover_vogais que receba uma string
#e devolva uma nova string sem nenhuma das vogais (a, e, i, o, u).

def remover_vogais(texto):
    vogais='aeiouAEIOU'
    resultado = ""

    for xletra in texto:
        if xletra not in vogais:
            resultado+=xletra
    return resultado

texto=input("Escreva algo: ")
resultado=remover_vogais(texto)

print(f"O seu texto sem vogais ficou assim: "{resultado}"")