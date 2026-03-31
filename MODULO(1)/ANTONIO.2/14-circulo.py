import os
os.system('cls')

import math
raio=float(input('Digite o raio do círculo: '))
math.pi=3.14
peri=2*math.pi*raio
area=math.pi*raio**2
print(f'O perímetro do círculo é = {peri:.2f}')
print(f'A área do círculo é = {area}')
