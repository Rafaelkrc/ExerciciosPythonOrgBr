#Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
#a)o produto do dobro do primeiro com metade do segundo .
#b)a soma do triplo do primeiro com o terceiro.
#c)o terceiro elevado ao cubo.

num1 = int(input('Digite o 1° número: '))
num2 = int(input('Digite o 2° número: '))
num3 = float(input('Digite um número Real: '))
print(f'A) {(num1 * 2) * (num2 / 2):.0f}')
print(f'B) {(num1 * 3) + num3:.0f}')
print(f'C) {num3 ** 3:.0f}')
