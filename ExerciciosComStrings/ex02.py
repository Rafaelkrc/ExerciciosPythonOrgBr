# Nome ao contrário em maiúsculas. Faça um programa que permita ao usuário digitar o seu nome e em seguida mostre o
# nome do usuário de trás para frente utilizando somente letras maiúsculas. Dica: lembre−se que ao informar o nome o
# usuário pode digitar letras maiúsculas ou minúsculas.

nome = 'Rafael Rosso Coelho'.upper()

nome_invertido_por_letras = ''.join(reversed(nome))
nome_invertido_por_palavras = ' '.join(reversed(nome.split()))

print(f'Nome com letras em maiusculo: {nome}')
print(f'Nome com letras em maiusculo invertido por letras: {nome_invertido_por_letras}')
print(f'Nome com letras em maiusculo invertido por palavras: {nome_invertido_por_palavras}')
