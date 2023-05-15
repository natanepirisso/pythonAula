while True:
    city = input('Digite uma cidade: ').title()
    cityFinder = city.find('Santo')
    if cityFinder == -1:
        print('Essa cidade não começa com a palavra "Santo"... Digite outra')
    else:
        print('Essa cidade tem a palavra "Santo" nela... interessante')
        break
