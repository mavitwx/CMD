import os
os.system('cls')

while True:
    n1=float(input('Digite sua primeira nota: '))
    n2=float(input('Digite sua segunda nota: '))
    n3=float(input('Digite sua terceira nota: '))
    media=(n1+n2+n3)/3
    if media>=9:
        print('Conceito do aluno de acordo com a média: A')
    elif 7<media<8.9:
        print('Conceito do aluno de acordo com a média: B')
    elif 5<media<6.9:
        print('Conceito do aluno de acordo com a média: C')
    elif 3<media<4.9:
        print('Conceito do aluno de acordo com a média: D')
    else:
        print('Conceito do aluno de acordo com a média: E')
    print('===================================')
    res=input('Aplicar mais uma vez? (s/n): ').lower()
    if res!='s':
        break
    print('===================================')