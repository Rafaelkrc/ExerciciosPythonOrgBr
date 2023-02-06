# Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido
# por eles.
while True:
    try:
        num1 = int(input(f'Informe um número inteiro: '))
        num2 = int(input(f'Informe outro número inteiro: '))
        if num1 < num2:
            for c in range(num1, num2 + 1):
                print(c, end=' ')
        if num1 > num2:
            for c in range(num1, num2 - 1, -1):
                print(c, end=' ')
        break
    except ValueError:
        print('Informe apenas números inteiros!')
        continue

