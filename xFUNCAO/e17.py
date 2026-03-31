import os
os.system('cls')
#Diferente do exercício anterior que apenas imprimia no ecrã, crie uma função chamada gerar_tabuada
#que receba um número inteiro e devolva uma lista contendo os resultados da sua tabuada do 1 ao 10.

def gerar_tabuada(n):
    resultados = []
    
    for i in range(1, 11):
        resultados.append(n*i)
    return resultados
n=int(input('Digite um número inteiro: '))

resultado=gerar_tabuada(n)
print(f'Tabuada de {n} de 1 a 10: {resultado}')