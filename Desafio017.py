CatO = float(input('Quanto mede o comprimento do cateto oposto? '))
CatA = float(input('Quanto mede o comprimento do cateto adjacente? '))

hip = (CatA**2 + CatO**2)**(1/2)

print(f'A hipotenusa do triangulo retangulo é {hip:.2f}')

#OU

#import math
#CatO = float(input('Quanto mede o comprimento do cateto oposto? '))
#CatA = float(input('Quanto mede o comprimento do cateto adjacente? '))
#hip = math.hypot(CatO, CatA)
