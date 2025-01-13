n1 = int(input('Um número: '))
n2 = int(input('Outro número: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2

print('A soma vale {}, a multiplicação é {} a divisão é {:.3f}, a divisão inteira é {} e o seu exponencial é {} '.format(s, m, d, di, e)) 

#,end=' ') se quiser por tudo na mesma linha se tiver 2 prints no codigo 
#'\n    ....      \n'      onde quiser passar para baixo no mesmo print
#{:.3f}   para 3 casas decimais