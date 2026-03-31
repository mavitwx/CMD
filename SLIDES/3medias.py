import os
os.system('cls')

nomes = []
notas1 = []
notas2 = []
medias = []
for i in range (5):
    nome=input(f'Digite o NOME da {i+1}º pessoa: ')
    nota1=float(input(f'Digite a primeira nota de {nome}: '))
    nota2=float(input(f'Digite a segunda nota de {nome}: '))
    print('=====================================================')
    nomes.append(nome)
    notas1.append(nota1)
    notas2.append(nota2)
    medias.append((nota1+nota2)/2)
print('Nota de alunos e média')
for i in range(5):
    print (f'Nome: {nomes[i]} / Primeira nota: {notas1[i]} / Segunda nota: {notas2[i]} / Média = {medias[i]:.2f}')