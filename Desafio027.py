nome = str(input('Digite o seu nome completo: ')).strip()
n = nome.split()
print('Muito Prazer em conhecer-te')
print(f'O seu primeiro nome é {n[0]}.')
print(f'O seu último nome é {n[len(n) - 1]}.') #O n representa o numero de palavras
                                               #neste caso e vai fazer o numero de palavras -1
                                               #isso vai fazer com que meta a sua posição correta
                                               #e vai dar o último nome