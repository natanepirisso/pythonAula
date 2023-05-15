import math
catop = float(input('Digite o cateto oposto: '))
catad = float(input('Digite o cateto adjascente: '))
hyp = math.hypot(catop,catad)
print(f'A hipotenusa desse triangulo retangulo, é {hyp:.3}')