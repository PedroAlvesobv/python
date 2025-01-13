r1 = float(input('Diga o comprimento da primeira reta: '))
r2 = float(input('Diga o comprimento da segunda reta: '))
r3 = float(input('Diga o comprimento da terceira reta: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r2 + r1:
    print('Os segmentos podem criar um triangulo.')
else:
    print('Os segmentos não podem criar um triangulo.')

# Os lados têm que ser menores do que a soma dos outros lados para ser um triangulo.