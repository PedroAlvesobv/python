n1 = float(input('Digita a primeira nota: '))
n2 = float(input('Digita a segunda nota: '))
m = (n1 + n2) / 2
print(f'A sua média é {m:.1f}')

if m >= 12.0:
    print('QUE MAQNA!')
else:
    print('És uma bela merda.')