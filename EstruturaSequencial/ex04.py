#Faça um Programa que peça as 4 notas bimestrais e mostre a média.

soma = 0
cont = 0
for i in range(4):
    notas = float(input(f'Digite a {i+1}° nota: '))
    soma += notas
    cont += 1
    media = soma / cont
print(f'A média das notas foi de: {media:.2f}')

