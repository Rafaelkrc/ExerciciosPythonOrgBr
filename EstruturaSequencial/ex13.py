#Tendo como dado de entrada a altura (h) de uma pessoa,
# construa um algoritmo que calcule seu peso ideal,
# utilizando as seguintes fórmulas:
#a)Para homens: (72.7*h) - 58
#b)Para mulheres: (62.1*h) - 44.7


h = float(input('Informe sua altura: '))
s = str(input('Informe seu genero[M/F]: ')).strip().upper()
if s == 'M':
    ideal = (72.7 * h) - 58
elif s == 'F':
    ideal = (62.1 * h) - 44.7

print(f'Seu peso ideal é: {ideal:.2f}')
