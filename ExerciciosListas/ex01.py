# Faça um Programa que leia um vetor de 5 números inteiros e mostre-os.

lista = []
for i in range(1, 6):
    lista.append(int(input(f'Informe o {i}° numero inteiro: ')))
print(f'Os números inteiro digitados foram: {lista}!')
