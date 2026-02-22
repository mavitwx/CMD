import os
os.system('cls')

#Chico tem 1,50m e cresce 2 centímetros por ano,enquanto Juca tem 1,10m e cresce 3 centímetros por ano.
#Construir um algoritmo que calcule e imprima quantos anos serão necessários para que Juca seja maior
chico=1.5
juca=1.1
anos=0
while juca<=chico:
    chico=chico+0.02
    juca=juca+0.03
    anos=anos+1
print(f'Juca ultrapassará Chico em {anos} anos')