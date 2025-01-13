n = int(input('Digita um número: '))
res = n % 2 # % representa o resto da divisão entre o 'n' e o '2', neste caso, então se o resto for = 0 então é par, senão é impar 

if res == 0:
    print(f'O número {n} é par.')
else:
    print(f'O número {n} é impar.')