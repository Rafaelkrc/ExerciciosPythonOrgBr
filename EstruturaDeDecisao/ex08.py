# Faça um programa que pergunte o preço de três produtos e informe qual produto
# você deve comprar, sabendo que a decisão é sempre pelo mais barato.

for p in range(1, 4):
    preco = float(input(f'Informe o preço do {p}° produto:R$ '))
    if p == 1:
        menor = preco
    if preco < menor:
        menor = preco
print(f'O menor valor foi o produto de R${menor:.2f}')
