# Faça um programa que leia 5 números e informe o maior número.
maior = 0
for c in range(1, 6):
    numero = float(input(f'Informe o {c}° número: '))
    if c == 1:
        maior = numero
    else:
        if numero > maior:
            maior = numero

print(f'O maior numero digitado foi {maior:.0f}!')

