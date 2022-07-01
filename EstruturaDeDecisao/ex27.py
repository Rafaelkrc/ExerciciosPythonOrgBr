# Uma fruteira está vendendo frutas com a seguinte tabela de preços:
#                       Até 5 Kg           Acima de 5 Kg
# Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
# Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg
# Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, receberá ainda um
# desconto de 10% sobre este total. Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade
# (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente.

morango = float(input('Informe a quantidade em Kg de Morango: '))
maca = float(input('Informe a quantidade em Kg de Maçãs: '))

if morango <= 5:
    totalmo = morango * 2.5
else:
    totalmo = morango * 2.2
if maca <= 5:
    totalma = maca * 1.8
else:
    totalma = maca * 1.5

totalkg = morango + maca
totalcomp = totalmo + totalma

if totalkg > 8 or totalcomp > 25:
    totalcomp = totalcomp - (totalcomp * 0.10)

print(f'O total da compra foi R${totalcomp:.2f}')
