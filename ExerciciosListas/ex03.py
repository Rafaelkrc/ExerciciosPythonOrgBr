# Faça um Programa que leia 4 notas, mostre as notas e a média na tela.
notas = []
soma = 0
for i in range(0, 4):
    nota = (float(input(f'Digite a {i + 1}° nota: ')))
    notas.append(nota)
    soma += nota
media = soma / len(notas)

print(f'As notas informadas foram: ')
print('; '.join([str(nota) for nota in notas]))
print(f'A média das notas foi de {media}')



