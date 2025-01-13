d = float(input('Qual é a distancia da sua viagem? '))

if d <= 200:
    print(f'Oh moço, vais pagar {d * 0.5:.2f} Euros!')
else:
    print(f'Oh moço, vais pagar {d * 0.45:.2f} Euros!')

