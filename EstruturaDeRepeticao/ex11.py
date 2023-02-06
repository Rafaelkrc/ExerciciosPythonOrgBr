# Altere o programa anterior para mostrar no final a soma dos números.

while True:
    try:
        num1 = int(input(f'Informe um número inteiro: '))
        num2 = int(input(f'Informe outro número inteiro: '))
        soma = 0
        if num1 < num2:
            for c in range(num1, num2 + 1):
                soma += c
                print(c, end=' ')
        if num1 > num2:
            for c in range(num1, num2 - 1, -1):
                print(c, end=' ')
                soma += c
        break
    except ValueError:
        print('Informe apenas números inteiros!')
        continue
print()
print(f'A soma dos valores foi de {soma}')
