import os
os.system('cls')

#Escreva um programa que armazene notas e informe o índice daquelas que são abaixo de 7
notas=[6,5,8,9]
for i, nota in enumerate(notas,start=1):
    if nota<7:
        print(f'O aluno da posição {i}está de recuperação.')