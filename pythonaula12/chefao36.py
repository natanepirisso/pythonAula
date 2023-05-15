vlr = float(input('Digite o valor da casa: '))
sal = float(input('Digite o valor do seu salário: '))
ano = float(input('Digite a quantidade de anos que deseja pagar: '))

anoMes = ano * 12
prestTest = sal * .3

if vlr/anoMes <= prestTest:
    print('Ok! Podemos fazer o emprestimo')
elif vlr/anoMes > prestTest:
    print('Infelizmente o valor excede 30% do seu salário.')
else:
    print('Erro. Tente novamente.')