import os
os.system('cls')

paisa=5000000
paisb=7000000
anos=0
while paisa<=paisb:
    paisa=paisa*1.03
    paisb=paisb*1.02
    anos=anos+1
    print(f'País A ultrapassará o País B em {anos} anos')