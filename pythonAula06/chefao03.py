name = str(input('Salve! Diga teu nome aí > '))
n1 = int(input('Beleza {}, agora me dê um número aí > '.format(name)))
n2 = int(input('Nice ! Um outro número agora > '))
s = n1 + n2
print('Seguinte {}... Tu somou {} com {} e o resultado foi {}. Curtiu tua calculadora ? Se não gostou foda-se :D !!!!!'.format(name, n1, n2, s))