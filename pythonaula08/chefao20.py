import random
a1 = input('Digite o nome de um aluno: ')
a2 = input('Digite o nome do segundo aluno: ')
a3 = input('Digite o nome do terceiro aluno: ')
a4 = input('Digite o nome do quarto aluno: ')
lista = [a1,a2,a3,a4]
random.shuffle(lista)
print(f'Ficou assim: {lista[0]} vai apresentar primeiro. {lista[1]} será o segundo, seguido por {lista[2]} e {lista[3]} respectivamente.')