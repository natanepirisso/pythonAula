while True:
    city = input('Digite o nome completo de um brasileiro pobre: ').title()
    cityFinder = city.find('Silva')
    if cityFinder == -1:
        print('Não tem "Silva" nesse nome... Digite outro')
    else:
        print('Tem "Silva" nesse nome... brasileiro e pobre.')
        break
        