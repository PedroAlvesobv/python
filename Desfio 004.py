p = input('Diz alguma coisa: ')

print('Qual é o tipo primitivo? ', type(p))
print('é um numero?' , (p.isnumeric()))
print('é uma palavra ou letra?' , (p.isalpha()))
print('é uma letra, numero ou palavra?' , (p.isalnum()))
print('está em capslock?' , (p.isupper()))
print('é printavel?' , (p.isprintable()))
print('é um digito?', (p.isdigit()))
print('é um decimal?', (p.isdecimal()))
print('é identificavel?', (p.isidentifier()))
print('está com minusculas?', (p.islower()))
print('é composto por espaços?', (p.isspace()))
print('é um titulo?', (p.istitle())) #está com a primeira letra em maiúscula e o resto minúsculas