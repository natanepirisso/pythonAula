name = input('Digite seu nome: ').lower()
nameSplited = name.split()
print(f'\nAnalisando o nome...\n{nameSplited[0].title()} KKKKKKK.... que merda de nome é esse...\n ')
print(f'seu nome possui {name.count("a")} letras "a" {nameSplited[0].title()}.')
print(f'Além disso, a primeira letra "a" se encontra na posição {name.find("a")-name.count(" ")} de seu nome.')
print(f'A ultima vez que essa letra aparece, seria na posição {name.rfind("a") - name.count(" ")} de seu nome.')
