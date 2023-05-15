name = input('Digite seu nome completo: ').strip()
splitedName = name.split()


print(f'Seu nome possui as seguintes possibilidades de escrita: \nUpper: {name.upper()}\nLower: {name.lower()}\n ')
print(f'Além disso, seu nome possui um total de {name.__len__()-name.count(" ") } letras, com seu seu primeiro nome contendo apenas {splitedName[0].__len__()}')
