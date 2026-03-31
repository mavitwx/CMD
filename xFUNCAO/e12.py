import os
os.system('cls')
#Crie uma função chamada inverter_texto que receba uma string e devolva essa mesma string invertida.
#(Exemplo: ao receber "Python", deve devolver "nohtyP").

def inverter_texto(texto):
        return texto[::-1]

texto=input('Digite uma palavra: ')
resultado=inverter_texto(texto)
print(resultado)