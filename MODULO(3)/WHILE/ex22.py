import os
os.system('cls')

mulher=0
homem=0
outro=0

idade_homens_xp = 0
homens_xp = 0
homens_mais_45 = 0

mulheres_menos_35_xp = 0
menor_idade_mulher_exp = None

while True:
    idad=int(input('Digite sua idade (0 p/ sair): '))
    if idad==0:
         print('Parando...')
         break
    
    sex=input('Digite seu sexo (F/M/O): ').upper()
    exp=input('Você possui experiência no serviço? (S/N): ').upper()
    if sex=='F':
        mulher+=1
        if exp=='S' and idad<35:
             mulheres_menos_35_xp+=1
        if exp=='S':
             if menor_idade_mulher_exp is None or idad<menor_idade_mulher_exp:
                  menor_idade_mulher_exp=idad

    elif sex=='M':
        homem+=1
        if exp=='S':
             idade_homens_xp+=idad
             homens_xp+=1
        if idad>45:
             homens_mais_45+=1

    elif sex=='O':
        outro+=1
    else:
        print('Sexo INVÁLIDO')
        break

if homens_xp>0:
     mediahomemxp= idade_homens_xp/homens_xp
else:
     mediahomemxp=0
if homem>0:
     porc_homem45=(homens_mais_45/homem)*100
else:
     porc_homem45=0
print('====================================================')
print('RESULTADOS:')
print(f'Número de mulheres: {mulher}')
print(f'Número de homens: {homem}')
print(f'Número de candidatos de outro sexo: {outro}')
print('                                                             ')
print(f'Idade média dos homens com experiência: {mediahomemxp}')
print(f'Porcentagem dos homens com mais de 45 anos: {porc_homem45}%')
print('                                                             ')
print(f'Número de mulheres menores de 35 anos e com experiência: {mulheres_menos_35_xp}')
if menor_idade_mulher_exp is not None:
    print(f'Menor idade entre mulheres com experiência: {menor_idade_mulher_exp}')
    print('                                                             ')
else:
    print('Não há mulheres com experiência.')
    print('                                                             ')