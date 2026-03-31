import os
os.system('cls')

#Dado um país A, com 5.000.000 de habitantes e uma taxa de natalidade de 3% ao ano
#e um país B com 7.000.000 de habitantes e uma taxa de natalidade de 2% ao ano
#calcular e imprimir o tempo necessário para que a população do país A ultrapasse a do país B.
paisa=5000000
paisb=7000000
anos=0
while paisa<=paisb:
    paisa=paisa*1.03
    paisb=paisb*1.02
    anos=anos+1
    print(f'País A ultrapassará o País B em {anos} anos')