r1 = float(input("Digite uma reta: "))
r2 = float(input("Digite uma segunda reta: "))
r3 = float(input("Digite uma terceira reta: "))

if abs(r2 - r3) < r1 < r2 + r3:
    if abs(r1 - r3) < r2 < r1 + r3:
        if abs(r1 - r2) < r3 < r1 + r2:
            print('é possível criar um triangulo com essas retas.')
        else:
            print(f'Não foi possível criar este triangulo por conta da reta de valor {r3:\033[1;31m}')
    else:
        print(f'Não foi possível criar este triangulo por conta da reta de valor {r2:\033[1;31m}')
else:
    print(f'Não foi possível criar este triangulo por conta da reta de valor {r1:\033[1;31m}')
