n1 = int(input("Digite um numero: "))
n2 = int(input("Digite um segundo numero: "))
n3 = int(input("Digite um terceiro numero: "))

if n1 > n2 and n1 > n3:
    if n2 < n3:
        print(f"{n1} é o maior número e {n2} é o menor.")
    else:
        print(f'{n1} é o maior número e {n3} é o menor.')
if n2 > n1 and n2 > n3:
    if n1 < n3:
        print(f"{n2} é o maior número e {n1} é o menor.")
    else:
        print(f'{n2} é o maior número e {n3} é o menor.')
if n3 > n1 and n3 > n2:
    if n2 < n1:
        print(f'{n3} é o maior número e {n2} é o menor.')
    else:
        print(f'{n3} é o maior número e {n1} é o menor.')
