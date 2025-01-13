num = int(input('Informe um número: '))
u = num // 1 % 10     # para termos as unidades do numero e não dar erro
d = num // 10 % 10    # para termos as dezenas do numero e não dar erro
c = num // 100 % 10   # para termos as centenas do numero e não dar erro
m = num // 1000 % 10  # para termos os milhares do numero e não dar erro

print(f'A anaisar o número {num}')
print(f'Unidade: {u}')
print(f'Dezena: {d}')
print(f'Centena: {c}')
print(f'Milhar: {m}')