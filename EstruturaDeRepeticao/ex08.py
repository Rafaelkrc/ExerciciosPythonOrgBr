# Faça um programa que leia 5 números e informe a soma e a média dos números.

soma = 0

for c in range(1, 6):
    numero = float(input(f'Digite o {c}° número: '))
    soma += numero
media = soma / c
print(f'A soma dos números digitas foi de {soma:.2f}!')
print(f'A média dos números digitados foi de {media:.2f}!')
