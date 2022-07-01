# Faça um Programa que leia três números e mostre-os em ordem decrescente.

lista = []

for p in range(1, 4):
    num = int(input(f'Digite o {p}° número: '))
    lista.append(num)

lista.sort()
print(lista[::-1])
