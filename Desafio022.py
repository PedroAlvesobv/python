nome = str(input('Digite o seu nome completo: ')).strip()
print(f'''A analisar o seu nome...
{nome} em:
Capslock {nome.upper()} 
Minusculas {nome.lower()} 
E tem {len(nome) - nome.count(' ')} Letras no total
O seu primeiro nome tem {nome.find(' ')} letras.
''')

#ou na penultima linha
#separa = nome.split()
#print(f'Seu primeiro nome é {separa[0]} e ele tem {len(separa[0])} letras.')