import os
os.system('cls')

nums1 = []
nums2 = []
somas = []

for i in range (5):
    num1= float(input(f'Digite o {i+1}º número do vetor1: '))
    num2=float(input(f'Digite o {i+1}º número do vetor2: '))
    nums1.append(num1)
    nums2.append(num2)
    somas.append(num1+num2)
    
for i in range(len(somas)):
    print(f'{i+1}ª Soma: {somas[i]}')