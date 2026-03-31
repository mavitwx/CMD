import os
os.system('cls')

nomes = []
for i in range(5):
    nome=input(f"Digite o NOME da {i+1}º pessoa : ")
    nomes.append (nome)
print('Listagem de nomes:')
for nome in nomes:
    print (nome)