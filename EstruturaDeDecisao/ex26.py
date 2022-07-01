# Um posto está vendendo combustíveis com a seguinte tabela de descontos:
# Álcool:
# até 20 litros, desconto de 3% por litro
# acima de 20 litros, desconto de 5% por litro
# Gasolina:
# até 20 litros, desconto de 4% por litro
# acima de 20 litros, desconto de 6% por litro Escreva um algoritmo que leia o número de litros vendidos,
# o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina), calcule e imprima o valor a
# ser pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.
print('-' * 30)
print('NOSSO POSTO')
print('-' * 30)
print('''Qual Combustível?
A - Alcool
G - Gasolina''')
print('-' * 30)
tipo = str(input('Infomre o tipo de combustível:[A/G] ')).upper()
litros = float(input('Quantos litros foi abastecidos? '))

if tipo == 'A' and litros <= 20:
    valor = (litros * 1.9) - (litros * 1.9 * 0.03)
    print(f'O Total foi de R${valor:.2f}')
elif tipo == 'A' and litros > 20:
    valor = (litros * 1.9) - (litros * 1.9 * 0.05)
    print(f'O Total foi de R${valor:.2f}')
elif tipo == 'G' and litros <= 20:
    valor = (litros * 2.5) - (litros * 2.5 * 0.04)
    print(f'O Total foi de R${valor:.2f}')
else:
    valor = (litros * 2.5) - (litros * 2.5 * 0.06)
    print(f'O Total foi de R${valor:.2f}')
