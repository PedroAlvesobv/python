import math

ang = float(input('Escolha um angulo: '))

sen = math.sin(math.radians(ang)) #O math.sin vem em radianos por isso math.radians serve para converter radianos a graus 
cos = math.cos(math.radians(ang))
tan = math.tan(math.radians(ang))

print(f'Para o angulo {ang} o Seno é {sen:.2f}, o Cosseno é {cos:.2f} e a Tangente é {tan:.2f}.')