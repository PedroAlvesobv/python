sal = float(input('Quanto recebe por mês? '))
aum10 = sal * 1.1
aum15 = sal * 1.15

if sal > 1250:
    print(f'O seu aumento é de 10% recebendo assim {aum10:.2f}.')
else: 
    print(f'O seu aumento é de 15% recebendo assim {aum15:.2f}.')