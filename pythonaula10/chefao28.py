import random

num = random.randint(0, 5)
while True:
    numusr = int(input(f'Selecione um numero de 0 a 5 ({num}): '))
    print('Processando.......\n')
    if numusr == num:
        print('Parabens, Você acertou !!!')
        break
    else:
        print('número errado... tente novamente por favor\n')
