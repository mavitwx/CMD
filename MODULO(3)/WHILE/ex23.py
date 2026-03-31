import os
os.system('cls')

maior_abono=0
matric_maiorabono=None
abono_regular=0
regulares=0

while True:
    matricula=int(input('Digite sua matrícula: '))
    if matricula==0:
        print('==========================')
        print('Valor INVÁLIDO')
        print('==========================')
        break

    base=float(input('Digite seu salário base: '))
    nivel_abono=int(input('Digite seu nível de abono (1-Excelente | 2-Bom | 3-Regular): '))
    if nivel_abono==1:
        abono=base*0.8
    elif nivel_abono==2:
        abono=base*0.5
    elif nivel_abono==3:
        abono=base*0.3
    else:
        print('Nível INVÁLIDO')
        continue
    salariofinal=base+abono
    print(f'Salário a receber: {salariofinal:.2f} ')

    if abono>maior_abono:
        maior_abono=abono
        matric_maiorabono=matricula

    if nivel_abono==3:
        abono_regular+=abono
        regulares+=1

if matric_maiorabono is not None:
    print(f'Matrícula do funcionário com maior abono: {matric_maiorabono}')
else:
    print('Nenhum funcionário cadastrado')
if regulares>0:
    media_regular = abono_regular/regulares
    print(f"Média dos abonos dos funcionários Regulares: R$ {media_regular:.2f}")
else:
    print("Não houve funcionários Regulares.")