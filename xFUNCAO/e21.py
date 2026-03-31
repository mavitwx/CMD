import os
os.system('cls')
#Crie uma função chamada somar_lista que receba uma lista de números
#e devolva a soma de todos os seus elementos.
#(Tente usar um laço for para simular o processo algorítmico, em vez de usar a função pronta sum()).

def somar_lista(nums):
    soma=0

    for n in nums:
        soma+=n

    return soma

nums=[]

for i in range(5):
    n=float(input(f'Digite o {i+1}° número: '))
    nums.append(n)

resultado=somar_lista(nums)
print('='*40)
print(f'A soma dos números é = {resultado}')
print('='*40)
