from datetime import date

ano = int(input('Em que ano estamos, moço? '))

if ano ==0:
    ano = date.today().year

bisexto = ano // 4

if ano / 4 == bisexto and ano % 100 != 0 or ano % 400 == 0:  # != significa diferente e não igual
    print(f'Estamos no ano {ano} e é um ano bisexto moço!!!')
else:
    print(f'Estamos no ano {ano} e não é um ano bisexto. :( ')

#O ano bisexto tem que ser divisivel por quatro não pode ser divisivel por 100 e tem que ser divisivel por 400.