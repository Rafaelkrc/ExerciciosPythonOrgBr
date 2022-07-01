# Faça um Programa que peça um número correspondente a um determinado ano e em seguida informe se este
# ano é ou não bissexto.

ano = int(input('Informe o ano que quer consultar: '))

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano de {ano} é BISSEXTO!')
else:
    print(f'O ano de {ano} não é BISSEXTO!')
