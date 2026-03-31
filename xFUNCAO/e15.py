import os
os.system('cls')
#Crie uma função chamada calcular_juros_simples que receba três parâmetros:
#o capital inicial, a taxa de juro (em percentagem) e o tempo (em meses).
#A função deve devolver o valor dos juros acumulados no final do período.
#(Fórmula: J = (C * i * t) / 100).

def calcular_juros_simples(c,i,t):
    j=(c*i*t)/100
    m=c+j
    return j,m
c=float(input('Digite o valor da capital inicial: '))
i=float(input('Digite o valor da porcetagem %: '))
t=int(input('Digite o tempo (em meses): '))

resultado=calcular_juros_simples(c,i,t)
print('='*45)
print(f'Valor dos juros acumulados, montante final: {resultado:.2f}')
print('='*45)
