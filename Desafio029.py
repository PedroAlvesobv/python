v = float(input('Qual é a velocidade do seu veículo em km/h? '))
d = (v - 80) * 7

if v > 80:
    print(f'Vais ter que pagar R$ {d:.2f } de multa.')
else:
    print('Não pagas nada, oh moço')

#ou

#if v > 80:
#    print(f'Vais ter que pagar R$ {d:.2f } de multa.')
#print('Não pagas nada, oh moço')
#também funciona normalmente