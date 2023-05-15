name = str(input('Digite seu nome completo: ')).strip()
n = name.split()
print(f'Seu Nome é {n[0]}')
print(f'Seu Sobrenome é {n[n.__len__() - 1]}')
