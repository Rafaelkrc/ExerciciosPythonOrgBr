# Faça um programa para uma loja de tintas. O programa deverá
# pedir o tamanho em metros quadrados da área a ser pintada. Considere
# que a cobertura da tinta é de 1 litro para cada 3 metros quadrados
# e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00.
# Informe ao usuário a quantidades de latas de tinta a serem compradas
# e o preço total.
import math
area = float(input('Informe a área a ser pintada: '))
litrosNecessario = area / 3

if litrosNecessario > 18:
    totallitros = litrosNecessario / 18
    totL = math.ceil(totallitros)
    valor = totL * 80
    print(f'Para a área de {area:.2f}mt2, você precisará de {totL:.2f} latas de tinta '
          f'de 18 litros que irá custar R${valor:.2f}.')
else:
    print(f'Para a área de {area:.2f}mt2, você precisará de 1 lata de tinta '
          f'de 18 litros que vai lhe custar R$80,00.')


