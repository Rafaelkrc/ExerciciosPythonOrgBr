# Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3% e que
# a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%. Faça um programa que calcule e escreva
# o número de anos necessários para que a população do país A ultrapasse ou iguale a população do país B, mantidas as
# taxas de crescimento.


populaçao_a = 80_000
populaçao_b = 200_000
taxa_de_crescimento_a = 1.03
taxa_de_crescimento_b = 1.015
anos = 0

while populaçao_a < populaçao_b:
    anos += 1
    populaçao_a = int(populaçao_a * taxa_de_crescimento_a)
    populaçao_b *= taxa_de_crescimento_b
    populaçao_b = int(populaçao_b)

print(f'População de A ultrapassará a população de B em {anos} anos.')
print(f'População de A será de {populaçao_a} habitantes.')
print(f'População de B será de {populaçao_b} habitantes!')
