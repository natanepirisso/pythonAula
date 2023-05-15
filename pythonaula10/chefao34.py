sal = float(input('Digite o seu salário: '))
salinf = sal + (sal * 0.15)
salsup = sal + (sal * 0.1)
if sal <= 1250.00:
    print(f'Houve um aumento de 15% no seu salário. Logo, passará a valer {salinf:.2f}R$.')
else:
    print(f'Houve um aumento de 10% no seu salário. Logo, passará a valer {salsup:.2f}R$.')