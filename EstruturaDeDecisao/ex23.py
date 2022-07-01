# Faça um Programa que peça um número e informe se o número é inteiro ou decimal. Dica: utilize uma função
# de arredondamento.

num = float(input('Digite um número: '))

if int(num) == num:
    print(f'O {num:.0f} é INTEIRO!')
else:
    print(f'O {num} é DECIMAL!')
