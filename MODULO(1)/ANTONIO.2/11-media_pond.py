import os
os.system('cls')

n1=float(input('Digite sua primeira nota: '))
n2=float(input('Digite sua segunda nota: '))
n3=float(input('Digite sua terceira nota: '))
n4=float(input('Digite sua quarta nota: '))
p1=1
p2=2
p3=3
p4=4
med=(n1*p1+n2*p2+n3*p3+n4*p4)/10
print(f'A sua média ponderada é: {med}')