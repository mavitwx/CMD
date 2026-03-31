import os
os.system('cls')

#Entrar com um nome, idade e sexo de 10 pessoas. Imprimir o nome se for do sexo F e tiver mais de 21 anos
for i in range(1,11):
    nome=input(f"Digite o NOME da {i}º pessoa : ")
    id=int(input(f"Digite a IDADE da {i}º pessoa : "))
    sexo=input(f"Digite o sexo (F/M) da {i}º pessoa : ").upper()
    if sexo=='F' and id>21:
        print(f'Nome: {nome}')

