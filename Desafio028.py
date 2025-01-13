import random
from time import sleep

n = random.randint(0, 5)

num = int(input('Tenta adivinhar o numero que pensei entre 0 e 5: '))
print('Processando a informação... ')
sleep(3)
if n == num:
    print('GANHASTE CRLH!!!!!!!!!!')
else:
    print(f'Fudeste-te, estava a pensar em {n}.')