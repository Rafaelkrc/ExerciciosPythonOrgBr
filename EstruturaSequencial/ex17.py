# Faça um Programa para uma loja de tintas. O programa deverá
# pedir o tamanho em metros quadrados da área a ser pintada.
# Considere que a cobertura da tinta é de 1 litro para cada 6 metros
# quadrados e que a tinta é vendida em latas de 18 litros, que custam
# R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
# Informe ao usuário as quantidades de tinta a serem compradas e os
# respectivos preços em 3 situações:
# comprar apenas latas de 18 litros;
# comprar apenas galões de 3,6 litros;
# misturar latas e galões, de forma que o desperdício de tinta seja menor.
# Acrescente 10% de folga e sempre arredonde os valores para cima, isto é,
# considere latas cheias.

import math
area = float(input('Informe a área a ser pintada em mt2: '))
litro = (area / 6) * 1.1
latas18 = math.ceil(litro / 18)
valor18 = latas18 * 80
latas3 = math.ceil(litro / 3.6)
valor3 = latas3 * 25
mixlatas18 = math.trunc(litro / 18)
mixlata3 = math.ceil((litro - (mixlatas18 * 18)) / 3.6)

total_mix = (mixlatas18 * 80) + (mixlata3 * 25)

print(f'Na área de {area:.2f}mt2, você vai precisar de {latas18} lata(s) de 18 litros que custará R${valor18:.2f}.')
print(f'Na área de {area:.2f}mt2, você vai precisar de {latas3} lata(s) de 3.6 litros que custará R${valor3:.2f}.')
print(f'Mesclando as latas de 18 e 3,6 litros você ira precisar de {mixlatas18} latas de 18 litros'
      f' e {mixlata3} lata(s) de 3,6 litros, dando um total de R${total_mix:.2f}')
