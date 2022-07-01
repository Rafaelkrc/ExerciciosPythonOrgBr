# Faça um Programa que leia três números e mostre o maior deles.
maior = 0
for i in range(3):
    num = float(input(f'Informe o {i + 1}° número: '))
    if num > maior:
        maior = num
print(f'O maior numero digitado foi o {maior:.2f}')

