a = input('digite algo: ')
print(f'Você digitou {a}.')
print(f'O tipo primitivo de {a}, é {type(a)}')
print(f'Ele é numéro ? {a.isnumeric()}')
print('Ele é caractére? {}'.format(a.isalpha()))
print('Ele é Alfa-Numérico ? {}'.format(a.isalnum()))
print(f'Ele é vazio ? {a.isspace()}')

