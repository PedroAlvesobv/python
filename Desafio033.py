n1 = float(input('Diga um número: '))
n2 = float(input('Diga outro: '))
n3 = float(input('Mais um: '))
#verifica quem é o menor
menor = n1

if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
print(f'O número mais piquena é {menor}.')

maior = n1

if n2 > n1 and n2 > n3:
    maior = n2

if n3 > n2 and n3 > n1:
    maior = n3

print(f'O número mais maior grande é {maior}.')