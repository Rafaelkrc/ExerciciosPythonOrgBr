# Faça um Programa que leia três números e mostre o maior e o menor deles.
maior = 0
menor = 0
for i in range(1, 4):
    n1 = float(input(f'Digite o {i}° número: '))
    if i == 1:
        maior = n1
        menor = n1
    else:
        if n1 > maior:
            maior = n1
        if n1 < menor:
            menor = n1

print(f'O maior número digitado foi {maior} e o menor número digitado foi {menor}')
