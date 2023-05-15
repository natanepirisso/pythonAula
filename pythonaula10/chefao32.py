year = int(input('Me diga um ano: '))
if year % 4 == 0:
    if year % 100 != 0:
        print(f"O ano de {year} é Bissexto.")
    else:
        if year % 400 == 0:
            print(f"O ano de {year} é Bissesto.")
        else:
            print("Este ano não é Bissexto.")
else:
    print("Este ano não é Bissexto.")