# Faça um Programa que peça dois números e imprima o maior deles.

num1 = float(input('Informe o primeiro número: '))
num2 = float(input('Informe o segundo número: '))

if num1 > num2:
    print(f'O Maior número é o {num1:.2f}')
else:
    print(f'O Maior número é o {num2:.2f}')
