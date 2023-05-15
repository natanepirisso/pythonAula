while True:
    num = float(input("""Bem vindo ao Serviço de Viagens Pau, um serviço do caralho!\n
Digite aqui a distância de sua viagem: """))
    if num <= 0:
        print('\nQuilometragem incorreta...')
    else:
        print("""\nLembrando que: Até 200Km, é cobrado 0,50R$ por quilometro rodado.
Caso contrário, é de 0,45R$\n""")
        if num <= 200:
            print(f'Sua viagem terá uma distancia de {num}Km. Logo, será cobrado um valor de {num*.5}R$.')
        else:
            print(f'Sua viagem terá uma distancia de {num}Km. Logo, será cobrado um valor de {num*.45}R$.')
        break
    print('\n----FIM----\n')
